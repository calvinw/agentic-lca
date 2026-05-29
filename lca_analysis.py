#!/usr/bin/env python3
"""
lca_analysis.py

Reads an LCA specification from analysis.md (YAML frontmatter), builds the
model in openLCA via the gdt-server REST API, walks through each step of the
LCI methodology, and writes lca_results.md.

Usage:
    python3 lca_analysis.py [analysis_file.md]   (default: analysis.md)
"""

import sys
import pathlib
import datetime
import yaml
import numpy as np
from olca_ipc.rest import RestClient
import olca_schema as o

ANALYSIS_FILE = sys.argv[1] if len(sys.argv) > 1 else "analysis.md"
RESULTS_FILE  = str(pathlib.Path(ANALYSIS_FILE).parent / "lca_results.md")
SERVER_URL    = "http://localhost:8080/"

# ── Formatting helpers ────────────────────────────────────────────────────────

W = 64  # banner width

def banner(title: str):
    print(f"\n{'═'*W}")
    print(f"  {title}")
    print(f"{'═'*W}")

def step(n: int, title: str):
    fill = W - len(title) - 12
    print(f"\n── Step {n}: {title} {'─'*max(fill,2)}")

def rule():
    print(f"  {'─'*(W-2)}")

def fmt_val(v: float) -> str:
    if v == 0:
        return "    0   "
    return f"{v:+.3f}"

def print_matrix(row_names, col_names, data, row_label="", col_label=""):
    rw = max(len(r) for r in row_names) + 2
    cw = max(max(len(c) for c in col_names), 8) + 2
    header = " " * (rw + 2) + "".join(c[:cw-1].center(cw) for c in col_names)
    if col_label:
        print(f"  columns = {col_label}")
    if row_label:
        print(f"  rows    = {row_label}")
    print()
    print(f"  {header}")
    print(f"  {'─'*(rw+2+cw*len(col_names))}")
    for r, row in zip(row_names, data):
        cells = "".join(fmt_val(v).center(cw) for v in row)
        print(f"  {r:<{rw+2}}{cells}")
    print()

# ── Parse analysis.md ─────────────────────────────────────────────────────────

def load_spec(path: str) -> dict:
    text = pathlib.Path(path).read_text()
    if not text.startswith("---"):
        raise ValueError(f"{path} must begin with YAML frontmatter (---)")
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)

# ── Build openLCA entities ────────────────────────────────────────────────────

def build_model(client: RestClient, spec: dict) -> tuple[dict, o.Ref]:
    reg = {}  # name → olca_schema object (flow or process)

    step(3, "Unit Groups and Flow Properties")
    for symbol, description in spec["units"].items():
        ug = o.new_unit_group(f"{description} units [{symbol}]", symbol)
        fp = o.new_flow_property(description, ug)
        client.put_all(ug, fp)
        reg[symbol] = fp
        print(f"    {symbol:<6} → {description}")

    step(4, "Product Flows  (technosphere — intermediate)")
    for p in spec["products"]:
        flow = o.new_product(p["name"], reg[p["unit"]])
        client.put(flow)
        reg[p["name"]] = flow
        print(f"    {p['name']}  [{p['unit']}]")

    step(5, "Elementary Flows  (biosphere — emissions / extractions)")
    for ef in spec.get("elementary_flows", {}).get("emissions", []):
        flow = o.new_elementary_flow(ef["name"], reg[ef["unit"]])
        client.put(flow)
        reg[ef["name"]] = flow
        print(f"    {ef['name']}  [{ef['unit']}]  → emission to nature")

    step(6, "Unit Processes")
    for ps in spec["processes"]:
        p = o.new_process(ps["name"])
        ro = ps["reference_output"]
        ref_ex = o.new_output(p, reg[ro["flow"]], ro["amount"])
        ref_ex.is_quantitative_reference = True
        for inp in ps.get("inputs", []):
            o.new_input(p, reg[inp["flow"]], inp["amount"])
        for em in ps.get("emissions", []):
            o.new_output(p, reg[em["flow"]], em["amount"])
        client.put(p)
        reg[ps["name"]] = p
        print(f"    {ps['name']}")
        print(f"      output:  {ro['amount']} {ro['flow']}")
        for inp in ps.get("inputs", []):
            print(f"      input:   {inp['amount']} {inp['flow']}")
        for em in ps.get("emissions", []):
            print(f"      emits:   {em['amount']} {em['flow']} → biosphere")

    step(7, "Product System  (auto-link by matching flows)")
    ref_proc   = reg[spec["reference_process"]]
    system_ref = client.create_product_system(ref_proc)
    if system_ref is None:
        raise RuntimeError("create_product_system returned None — check docker logs")
    print(f"    System: {system_ref.name}")
    print(f"    ID    : {system_ref.id}")
    return reg, system_ref

# ── Derive matrices from spec ─────────────────────────────────────────────────

def build_matrices(spec: dict):
    prod_names = [p["name"] for p in spec["products"]]
    proc_names = [p["name"] for p in spec["processes"]]
    em_names   = [e["name"] for e in
                  spec.get("elementary_flows", {}).get("emissions", [])]

    prod_idx = {n: i for i, n in enumerate(prod_names)}
    proc_idx = {n: i for i, n in enumerate(proc_names)}
    em_idx   = {n: i for i, n in enumerate(em_names)}

    n_prod = len(prod_names)
    n_proc = len(proc_names)
    n_em   = len(em_names)

    A = np.zeros((n_prod, n_proc))
    B = np.zeros((n_em,   n_proc))

    for ps in spec["processes"]:
        j = proc_idx[ps["name"]]
        ro = ps["reference_output"]
        if ro["flow"] in prod_idx:
            A[prod_idx[ro["flow"]], j] = ro["amount"]
        for inp in ps.get("inputs", []):
            if inp["flow"] in prod_idx:
                A[prod_idx[inp["flow"]], j] = -inp["amount"]
        for em in ps.get("emissions", []):
            if em["flow"] in em_idx:
                B[em_idx[em["flow"]], j] = em["amount"]

    return A, B, prod_names, proc_names, em_names

# ── Generate lca_results.md ───────────────────────────────────────────────────

def write_results_md(spec, A, B, s, Bs, olca_outputs,
                     proc_names, prod_names, em_names, system_id):

    fu   = spec["functional_unit"]
    name = spec["name"]
    now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    def ln(x=""):  lines.append(x)

    ln(f"# LCA Results: {name}")
    ln()
    ln(f"Generated: {now}  |  openLCA system ID: `{system_id}`")
    ln()

    # ── Goal and scope
    ln("## Step 1 — Goal and Scope")
    ln()
    ln(f"**Goal:** {spec.get('goal','').strip()}")
    ln()
    ln(f"**Functional unit:** {fu['amount']} {fu['unit']} — {fu['description']}")
    ln()
    ln("**Reference flow vector f:**")
    ln()
    ref_proc_spec_md = next(ps for ps in spec["processes"]
                            if ps["name"] == spec["reference_process"])
    ref_flow_name_md = ref_proc_spec_md["reference_output"]["flow"]
    prod_idx_md = {p["name"]: i for i, p in enumerate(spec["products"])}
    f_vec = [0.0] * len(prod_names)
    f_vec[prod_idx_md[ref_flow_name_md]] = fu["amount"]
    ln("```")
    for i, (pn, fv) in enumerate(zip(prod_names, f_vec)):
        ln(f"  f[{i+1}] = {fv}   ({pn})")
    ln("```")
    ln()

    # ── Technology matrix A
    ln("## Step 2 — Technology Matrix A")
    ln()
    ln("Columns = processes, rows = products.  `+` = produced, `−` = consumed.")
    ln()
    # markdown table
    header = "| |" + "|".join(f" {p} " for p in proc_names) + "|"
    sep    = "|---|" + "|".join("---:" for _ in proc_names) + "|"
    ln(header)
    ln(sep)
    for i, rn in enumerate(prod_names):
        row = "| **" + rn + "** |"
        for j in range(len(proc_names)):
            v = A[i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    ln()

    # ── Scaling vector
    ln("## Step 3 — Scaling Vector  s = A⁻¹ · f")
    ln()
    ln("How many times each process must run to deliver exactly f:")
    ln()
    ln("| Process | Scale factor |")
    ln("|---|---:|")
    for pn, sv in zip(proc_names, s):
        ln(f"| {pn} | **{sv:.4f}** |")
    ln()

    # ── Intervention matrix B
    ln("## Step 4 — Intervention Matrix B")
    ln()
    ln("Columns = processes, rows = elementary flows (biosphere).")
    ln()
    header = "| |" + "|".join(f" {p} " for p in proc_names) + "|"
    ln(header)
    ln(sep)
    for i, en in enumerate(em_names):
        row = "| **" + en + "** |"
        for j in range(len(proc_names)):
            v = B[i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    ln()

    # ── LCI results
    ln("## Step 5 — LCI Results  B · s")
    ln()
    ln("| Flow | Numpy result | openLCA result | Unit | Match |")
    ln("|---|---:|---:|---|:---:|")
    for i, en in enumerate(em_names):
        olca_val = olca_outputs.get(en)
        np_val   = Bs[i]
        unit     = spec["units"].get(
            next(e["unit"] for e in
                 spec["elementary_flows"]["emissions"] if e["name"] == en), "kg")
        match    = "✓" if olca_val is not None and abs(olca_val - np_val) < 1e-4 else "✗"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        ln(f"| **{en}** | {np_val:.4f} | {olca_str} | {unit} | {match} |")
    ln()

    # ── Contribution analysis
    ln("## Step 6 — Contribution Analysis")
    ln()
    ln("Which process is responsible for each emission?")
    ln()
    ln("| Process | Scale (s) | Direct emissions | % of total |")
    ln("|---|---:|---:|---:|")
    total = Bs[0] if len(Bs) > 0 else 1
    for j, pn in enumerate(proc_names):
        direct = sum(B[k, j] * s[j] for k in range(len(em_names)))
        pct    = direct / total * 100 if total != 0 else 0
        ln(f"| {pn} | {s[j]:.4f} | {direct:.4f} kg | {pct:.0f}% |")
    ln()

    # ── Summary
    ln("## Summary")
    ln()
    ln("$$")
    ln(r"\text{Total emissions} = B \cdot A^{-1} \cdot f")
    ln("$$")
    ln()
    for i, en in enumerate(em_names):
        ln(f"> **{en}: {Bs[i]:.4f} kg** per {fu['amount']} {fu['unit']} "
           f"of {fu['description']}")
    ln()
    ln("---")
    ln(f"*Generated by `lca_analysis.py` using openLCA gdt-server v2*")

    pathlib.Path(RESULTS_FILE).write_text("\n".join(lines))

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    banner(f"LCA Analysis Runner  —  {ANALYSIS_FILE}")

    # ── Verify server
    import requests
    try:
        r = requests.get(f"{SERVER_URL}api/version", timeout=5)
        ver = r.json().get("version", "?")
        print(f"\n  Server  : {SERVER_URL}  (gdt-server v{ver})")
    except Exception as e:
        print(f"\n  ERROR: Cannot reach openLCA server at {SERVER_URL}")
        print(f"  {e}")
        print(f"\n  Start it with:  bash .devcontainer/start_olca.sh")
        sys.exit(1)

    spec = load_spec(ANALYSIS_FILE)
    fu   = spec["functional_unit"]
    name = spec["name"]
    goal = spec.get("goal", "").replace("\n", " ").strip()

    print(f"  Analysis: {name}")
    print(f"  Goal    : {goal[:70]}{'…' if len(goal)>70 else ''}")

    # ── Step 1: Goal and scope
    step(1, "Goal and Scope")
    print(f"\n  Functional unit : {fu['amount']} {fu['unit']} of '{fu['description']}'")
    prod_names_preview = [p["name"] for p in spec["products"]]
    ref_proc_spec = next(ps for ps in spec["processes"]
                         if ps["name"] == spec["reference_process"])
    ref_flow_name = ref_proc_spec["reference_output"]["flow"]
    prod_idx_preview = {p["name"]: i for i, p in enumerate(spec["products"])}
    f_vec = [0.0] * len(prod_names_preview)
    f_vec[prod_idx_preview[ref_flow_name]] = fu["amount"]
    print(f"\n  Reference flow vector f:")
    for i, (pn, fv) in enumerate(zip(prod_names_preview, f_vec)):
        print(f"    f[{i+1}] = {fv}  ({pn})")

    # ── Step 2: Product graph summary
    step(2, "Product Graph")
    print(f"\n  Processes : {len(spec['processes'])}")
    print(f"  Products  : {len(spec['products'])}")
    n_em = len(spec.get("elementary_flows", {}).get("emissions", []))
    print(f"  Emissions : {n_em}")
    print()
    for ps in spec["processes"]:
        ro = ps["reference_output"]
        ins  = ", ".join(f"{i['amount']} {i['flow']}" for i in ps.get("inputs", []))
        ems  = ", ".join(f"{e['amount']} {e['flow']}" for e in ps.get("emissions", []))
        print(f"  {ps['name']}")
        print(f"    → outputs {ro['amount']} {ro['flow']}")
        if ins:  print(f"    ← needs   {ins}")
        if ems:  print(f"    ↑ emits   {ems}")

    # ── Build model in openLCA (Steps 3–7)
    client = RestClient(SERVER_URL)
    reg, system_ref = build_model(client, spec)

    # ── Derive matrices from spec
    A, B, prod_names, proc_names, em_names = build_matrices(spec)

    # ── Step 8: Show technology matrix A
    step(8, "Technology Matrix A")
    print()
    print_matrix(prod_names, proc_names, A.tolist(),
                 row_label="products", col_label="processes")

    # ── Step 9: Solve for scaling vector s
    step(9, "Scaling Vector  s = A⁻¹ · f")
    ref_proc_spec = next(ps for ps in spec["processes"]
                         if ps["name"] == spec["reference_process"])
    ref_flow_name = ref_proc_spec["reference_output"]["flow"]
    prod_idx_map  = {n: i for i, n in enumerate(prod_names)}
    f = np.zeros(len(prod_names))
    f[prod_idx_map[ref_flow_name]] = fu["amount"]
    s = np.linalg.solve(A, f)
    print(f"\n  f = {list(f)}")
    print(f"\n  s = A⁻¹ · f")
    for i, (pn, sv) in enumerate(zip(proc_names, s)):
        bar = "█" * int(sv * 20)
        print(f"    s[{i+1}] = {sv:.4f}  {bar}  {pn}")

    # ── Step 10: Show intervention matrix B
    step(10, "Intervention Matrix B")
    print()
    if len(em_names) > 0:
        print_matrix(em_names, proc_names, B.tolist(),
                     row_label="emissions", col_label="processes")
    else:
        print("  (no elementary flows defined)")

    # ── Step 11: Run calculation in openLCA
    step(11, "LCA Calculation via openLCA gdt-server")
    print(f"\n  Submitting product system {system_ref.id[:8]}…")
    setup  = o.CalculationSetup(
        target=o.Ref(id=system_ref.id),
        amount=fu["amount"],
    )
    result = client.calculate(setup)
    result.wait_until_ready()
    print(f"  Calculation complete.")

    flows = result.get_total_flows()
    olca_outputs = {
        f.envi_flow.flow.name: f.amount
        for f in flows if not f.envi_flow.is_input
    }
    result.dispose()

    # ── Step 12: LCI results — B · s
    step(12, "LCI Results  B · s")
    Bs = B @ s
    print()
    print(f"  {'Flow':<32} {'Numpy':>10}  {'openLCA':>10}  Unit")
    rule()
    for i, en in enumerate(em_names):
        olca_val = olca_outputs.get(en)
        unit_sym = next(
            (e["unit"] for e in spec["elementary_flows"]["emissions"]
             if e["name"] == en), "?")
        match    = "✓ MATCH" if olca_val is not None and abs(olca_val - Bs[i]) < 1e-4 else "✗ DIFF"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        print(f"  {en:<32} {Bs[i]:>10.4f}  {olca_str:>10}  {unit_sym}  {match}")
    print()
    print(f"  Core equation:  CO₂ = B · A⁻¹ · f = {Bs[0]:.4f} kg")

    # ── Step 13: Contribution analysis
    step(13, "Contribution Analysis (Hotspot Identification)")
    total = Bs[0] if len(Bs) > 0 else 1
    print()
    print(f"  {'Process':<30} {'Scale':>8}  {'Direct emiss.':>14}  % of total")
    rule()
    for j, pn in enumerate(proc_names):
        direct = float(sum(B[k, j] * s[j] for k in range(len(em_names))))
        pct    = direct / total * 100 if total != 0 else 0
        bar    = "█" * int(pct / 5)
        print(f"  {pn:<30} {s[j]:>8.4f}  {direct:>10.4f} kg  {pct:5.1f}%  {bar}")

    # ── Write results
    write_results_md(spec, A, B, s, Bs, olca_outputs,
                     proc_names, prod_names, em_names, system_ref.id)

    banner("Done")
    print(f"  Results written to → {RESULTS_FILE}")
    print()

if __name__ == "__main__":
    main()
