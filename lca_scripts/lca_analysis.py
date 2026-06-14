#!/usr/bin/env python3
"""
lca_analysis.py

Reads an LCA specification from a recipe_card.md file (YAML frontmatter), builds
the model in openLCA via the gdt-server REST API, walks through each step of the
LCI methodology, writes lca_results.md, and generates product system graphs
(product_graph_scaled.svg and product_graph_structure.svg).

Usage:
    python3 lca_scripts/lca_analysis.py lca_analysis/coffee/recipe_card.md
"""

import sys
import pathlib
import datetime
import yaml
import numpy as np
from olca_ipc.rest import RestClient
import olca_schema as o
from lca_svg import generate as generate_svg

ANALYSIS_FILE = sys.argv[1] if len(sys.argv) > 1 else "recipe_card.md"
RESULTS_FILE  = str(pathlib.Path(ANALYSIS_FILE).parent / "lca_results.md")
SERVER_URL    = "http://localhost:8080/"

# ── Formatting helpers ────────────────────────────────────────────────────────

W = 64

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

# ── Parse recipe_card.md ──────────────────────────────────────────────────────

def load_spec(path: str) -> dict:
    text = pathlib.Path(path).read_text()
    if not text.startswith("---"):
        raise ValueError(f"{path} must begin with YAML frontmatter (---)")
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)

# ── Unit lookup helper ────────────────────────────────────────────────────────

def get_ef_unit(spec: dict, flow_name: str) -> str:
    for ef in spec.get("elementary_flows", {}).get("emissions", []):
        if ef["name"] == flow_name:
            return ef["unit"]
    for ef in spec.get("elementary_flows", {}).get("resources", []):
        if ef["name"] == flow_name:
            return ef["unit"]
    return "?"

# ── Build openLCA entities ────────────────────────────────────────────────────

def resolve_flow(client: RestClient, name: str, flow_property) -> o.Flow:
    """Look up flow by FEDEFL name in DB; create new only as fallback."""
    try:
        for d in client.get_descriptors(o.Flow):
            if d.name and d.name.strip().lower() == name.strip().lower():
                existing = client.get(o.Flow, d.id)
                if existing is not None:
                    print(f"      ✓ resolved '{name}' → DB flow ({d.id[:8]})")
                    return existing
    except Exception:
        pass
    flow = o.new_elementary_flow(name, flow_property)
    client.put(flow)
    print(f"      + created new flow '{name}'")
    return flow

def build_model(client: RestClient, spec: dict) -> tuple[dict, o.Ref]:
    reg = {}

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
        flow = resolve_flow(client, ef["name"], reg[ef["unit"]])
        reg[ef["name"]] = flow
        print(f"    {ef['name']}  [{ef['unit']}]  → emission to nature")
    for ef in spec.get("elementary_flows", {}).get("resources", []):
        flow = resolve_flow(client, ef["name"], reg[ef["unit"]])
        reg[ef["name"]] = flow
        print(f"    {ef['name']}  [{ef['unit']}]  ← extraction from nature")

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
        for res in ps.get("resources", []):
            o.new_input(p, reg[res["flow"]], res["amount"])
        client.put(p)
        reg[ps["name"]] = p
        print(f"    {ps['name']}")
        print(f"      output:  {ro['amount']} {ro['flow']}")
        for inp in ps.get("inputs", []):
            print(f"      input:   {inp['amount']} {inp['flow']}")
        for em in ps.get("emissions", []):
            print(f"      emits:   {em['amount']} {em['flow']} → biosphere")
        for res in ps.get("resources", []):
            print(f"      uses:    {res['amount']} {res['flow']} ← from nature")

    step(7, "Product System  (auto-link by matching flows)")
    ref_proc   = reg[spec["reference_process"]]
    system_ref = client.create_product_system(ref_proc)
    if system_ref is None:
        raise RuntimeError("create_product_system returned None — check docker logs")
    print(f"    System: {system_ref.name}")
    print(f"    ID    : {system_ref.id}")
    return reg, system_ref

def get_impact_method_ref(client: RestClient, method_name: str):
    """Look up an impact method in the database by name. Returns Ref or None."""
    try:
        for d in client.get_descriptors(o.ImpactMethod):
            if d.name and method_name.strip().lower() in d.name.strip().lower():
                print(f"    ✓ found impact method in DB: {d.name}")
                return d.to_ref()
    except Exception:
        pass
    print(f"    ✗ method '{method_name}' not found in database — LCIA skipped")
    return None

# ── Derive matrices from spec ─────────────────────────────────────────────────

def build_matrices(spec: dict):
    prod_names = [p["name"] for p in spec["products"]]
    proc_names = [p["name"] for p in spec["processes"]]
    em_names   = [e["name"] for e in
                  spec.get("elementary_flows", {}).get("emissions", [])]
    res_names  = [r["name"] for r in
                  spec.get("elementary_flows", {}).get("resources", [])]
    ef_names   = em_names + res_names  # emissions first, then resources

    prod_idx = {n: i for i, n in enumerate(prod_names)}
    proc_idx = {n: i for i, n in enumerate(proc_names)}
    ef_idx   = {n: i for i, n in enumerate(ef_names)}

    n_prod = len(prod_names)
    n_proc = len(proc_names)
    n_ef   = len(ef_names)

    A = np.zeros((n_prod, n_proc))
    B = np.zeros((n_ef,   n_proc))

    for ps in spec["processes"]:
        j = proc_idx[ps["name"]]
        ro = ps["reference_output"]
        if ro["flow"] in prod_idx:
            A[prod_idx[ro["flow"]], j] = ro["amount"]
        for inp in ps.get("inputs", []):
            if inp["flow"] in prod_idx:
                A[prod_idx[inp["flow"]], j] = -inp["amount"]
        for em in ps.get("emissions", []):
            if em["flow"] in ef_idx:
                B[ef_idx[em["flow"]], j] = +em["amount"]  # positive: exits to environment
        for res in ps.get("resources", []):
            if res["flow"] in ef_idx:
                B[ef_idx[res["flow"]], j] = -res["amount"]  # negative: enters from environment

    return A, B, prod_names, proc_names, em_names, res_names


# ── Generate lca_results.md ───────────────────────────────────────────────────

def write_results_md(spec, A, B, s, Bs, olca_outputs, olca_inputs,
                     proc_names, prod_names, em_names, res_names,
                     system_id, olca_impacts=None, method_name=""):
    fu   = spec["functional_unit"]
    name = spec["name"]
    now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    n_em  = len(em_names)
    n_res = len(res_names)

    lines = []
    def ln(x=""):  lines.append(x)

    ln(f"# LCA Results: {name}")
    ln()
    ln(f"Generated: {now}  |  openLCA system ID: `{system_id}`")
    ln()

    ln("## Step 1 — Goal and Scope")
    ln()
    ln(f"**Goal:** {spec.get('goal','').strip()}")
    ln()
    ln(f"**Functional unit:** {fu['amount']} {fu['unit']} — {fu['description']}")
    ln()
    ln("**Reference flow vector f:**")
    ln()
    ref_ps       = next(ps for ps in spec["processes"]
                        if ps["name"] == spec["reference_process"])
    ref_flow     = ref_ps["reference_output"]["flow"]
    prod_idx_md  = {p["name"]: i for i, p in enumerate(spec["products"])}
    f_vec        = [0.0] * len(prod_names)
    f_vec[prod_idx_md[ref_flow]] = fu["amount"]
    ln("```")
    for i, (pn, fv) in enumerate(zip(prod_names, f_vec)):
        ln(f"  f[{i+1}] = {fv}   ({pn})")
    ln("```")
    ln()

    ln("## Step 2 — Technology Matrix A")
    ln()
    ln("Columns = processes, rows = products.  `+` = produced, `−` = consumed.")
    ln()
    header = "| |" + "|".join(f" {p} " for p in proc_names) + "|"
    sep    = "|---|" + "|".join("---:" for _ in proc_names) + "|"
    ln(header); ln(sep)
    for i, rn in enumerate(prod_names):
        row = "| **" + rn + "** |"
        for j in range(len(proc_names)):
            v = A[i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    ln()

    ln("## Step 3 — Scaling Vector  s = A⁻¹ · f")
    ln()
    ln("How many times each process must run to deliver exactly f:")
    ln()
    ln("| Process | Scale factor |")
    ln("|---|---:|")
    for pn, sv in zip(proc_names, s):
        ln(f"| {pn} | **{sv:.4f}** |")
    ln()

    ln("## Step 4 — Intervention Matrix B")
    ln()
    ln("Columns = processes, rows = elementary flows (biosphere).")
    ln("`+` = emission (exits to environment)  `−` = resource extraction (enters from environment).")
    ln()
    ln(header); ln(sep)
    for i, en in enumerate(em_names):
        row = "| **" + en + "** |"
        for j in range(len(proc_names)):
            v = B[i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    for i, rn in enumerate(res_names):
        row = "| **" + rn + "** |"
        for j in range(len(proc_names)):
            v = B[n_em + i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    ln()

    ln("## Step 5 — LCI Results  B · s")
    ln()
    if n_em > 0:
        ln("**Emissions to environment:**")
        ln()
        ln("| Flow | Numpy result | openLCA result | Unit | Match |")
        ln("|---|---:|---:|---|:---:|")
        for i, en in enumerate(em_names):
            olca_val = olca_outputs.get(en)
            np_val   = Bs[i]
            unit     = get_ef_unit(spec, en)
            match    = "✓" if olca_val is not None and abs(olca_val - np_val) < 1e-4 else "✗"
            olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
            ln(f"| **{en}** | {np_val:.4f} | {olca_str} | {unit} | {match} |")
        ln()
    if n_res > 0:
        ln("**Resources from environment (amounts consumed):**")
        ln()
        ln("| Flow | Numpy result | openLCA result | Unit | Match |")
        ln("|---|---:|---:|---|:---:|")
        for i, rn in enumerate(res_names):
            olca_val = olca_inputs.get(rn)
            np_val   = abs(Bs[n_em + i])  # stored negative; report as positive
            unit     = get_ef_unit(spec, rn)
            match    = "✓" if olca_val is not None and abs(olca_val - np_val) < 1e-4 else "✗"
            olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
            ln(f"| **{rn}** | {np_val:.4f} | {olca_str} | {unit} | {match} |")
        ln()

    ln("## Step 6 — Scaled Emissions by Process  (B · diag(s))")
    ln()
    ln("Each cell = emission rate × scaling factor.  "
       "Columns sum to the LCI totals in Step 5.")
    ln()
    if n_em > 0:
        em_hdr = "| Process | s |" + "".join(f" {en} |" for en in em_names)
        em_sep = "|---|---:|" + "".join("---:|" for _ in em_names)
        ln(em_hdr); ln(em_sep)
        for j, pn in enumerate(proc_names):
            row = f"| {pn} | {s[j]:.4f} |"
            for k in range(n_em):
                v = B[k, j] * s[j]
                row += f" {v:.4f} |" if v != 0 else " 0 |"
            ln(row)
        tot_row = "| **Total** | |" + "".join(f" **{Bs[k]:.4f}** |" for k in range(n_em))
        ln(tot_row)
        ln()

    if n_res > 0:
        ln("**Resource extractions by process:**")
        ln()
        res_hdr = "| Process | s |" + "".join(f" {rn} |" for rn in res_names)
        res_sep = "|---|---:|" + "".join("---:|" for _ in res_names)
        ln(res_hdr); ln(res_sep)
        for j, pn in enumerate(proc_names):
            row = f"| {pn} | {s[j]:.4f} |"
            for k in range(n_res):
                v = abs(B[n_em + k, j] * s[j])
                row += f" {v:.4f} |" if v != 0 else " 0 |"
            ln(row)
        res_tot = "| **Total** | |" + "".join(
            f" **{abs(Bs[n_em + k]):.4f}** |" for k in range(n_res))
        ln(res_tot)
        ln()

    lcia = spec.get("lcia")
    if olca_impacts:
        ln(f"## Step 7 — LCIA Results  ({method_name})")
        ln()
        ln("Characterization factors from the database. "
           "Each impact category score is the sum of all "
           "elementary flow contributions as computed by the openLCA engine.")
        ln()
        ln("| Impact Category | Score | Unit |")
        ln("|---|---:|---|")
        for cat_name, (val, unit) in olca_impacts.items():
            ln(f"| {cat_name} | **{val:.6f}** | {unit} |")
        ln()
    elif lcia and lcia.get("impact_categories"):
        all_ef_names = em_names + res_names
        all_ef_idx   = {n: i for i, n in enumerate(all_ef_names)}
        ln(f"## Step 7 — LCIA Characterization  ({lcia['method']})")
        ln()
        ln("Characterization factors (CFs) convert raw inventory flows into a "
           "common impact score.  Each flow's LCI total is multiplied by its CF.")
        ln()
        for cat in lcia["impact_categories"]:
            cat_name  = cat["name"]
            indicator = cat.get("indicator", "")
            cat_unit  = cat.get("unit", "")
            cfs       = cat.get("characterization_factors", {})
            ln(f"### {cat_name}  ({indicator})  [{cat_unit}]")
            ln()
            ln(f"| Flow | LCI total | CF | Impact ({cat_unit}) |")
            ln("|---|---:|---:|---:|")
            cat_total = 0.0
            for en_name, cf in cfs.items():
                if en_name in all_ef_idx:
                    idx     = all_ef_idx[en_name]
                    lci_val = abs(Bs[idx])  # abs handles both emissions (+) and resources (-)
                    ef_unit = get_ef_unit(spec, en_name)
                    impact  = lci_val * cf
                    cat_total += impact
                    ln(f"| {en_name} | {lci_val:.4f} {ef_unit} | {cf} | {impact:.4f} |")
            ln(f"| **Total** | | | **{cat_total:.4f}** |")
            ln()

    ln("## Summary")
    ln()
    if olca_impacts:
        ln(f"**LCIA Method:** {method_name}")
        ln()
        for cat_name, (val, unit) in olca_impacts.items():
            ln(f"> **{cat_name}: {val:.6f} {unit}** "
               f"per {fu['amount']} {fu['unit']} of {fu['description']}")
    elif lcia and lcia.get("impact_categories"):
        all_ef_names = em_names + res_names
        all_ef_idx   = {n: i for i, n in enumerate(all_ef_names)}
        ln(f"**Method:** {lcia['method']}")
        ln()
        for cat in lcia["impact_categories"]:
            cfs       = cat.get("characterization_factors", {})
            cat_total = sum(
                abs(Bs[all_ef_idx[en]]) * cf
                for en, cf in cfs.items() if en in all_ef_idx
            )
            ln(f"> **{cat['name']} ({cat.get('indicator','')}): "
               f"{cat_total:.4f} {cat.get('unit','')}** "
               f"per {fu['amount']} {fu['unit']} of {fu['description']}")
    else:
        ln("$$")
        ln(r"\text{Total emissions} = B \cdot A^{-1} \cdot f")
        ln("$$")
        ln()
        for i, en in enumerate(em_names):
            ln(f"> **{en}: {Bs[i]:.4f} kg** per {fu['amount']} {fu['unit']} "
               f"of {fu['description']}")
    ln()
    ln("## Product System Graphs")
    ln()
    ln("### Scaled (with amounts)")
    ln()
    ln("![Scaled](product_graph_scaled.svg)")
    ln()
    ln("### Structure (flow names only)")
    ln()
    ln("![Structure](product_graph_structure.svg)")
    ln()
    ln("---")
    ln(f"*Generated by `lca_scripts/lca_analysis.py` using openLCA gdt-server v2*")

    pathlib.Path(RESULTS_FILE).write_text("\n".join(lines))

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    banner(f"LCA Analysis Runner  —  {ANALYSIS_FILE}")

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

    step(1, "Goal and Scope")
    print(f"\n  Functional unit : {fu['amount']} {fu['unit']} of '{fu['description']}'")
    prod_names_preview = [p["name"] for p in spec["products"]]
    ref_ps       = next(ps for ps in spec["processes"]
                        if ps["name"] == spec["reference_process"])
    ref_flow     = ref_ps["reference_output"]["flow"]
    prod_idx_pre = {p["name"]: i for i, p in enumerate(spec["products"])}
    f_vec        = [0.0] * len(prod_names_preview)
    f_vec[prod_idx_pre[ref_flow]] = fu["amount"]
    print(f"\n  Reference flow vector f:")
    for i, (pn, fv) in enumerate(zip(prod_names_preview, f_vec)):
        print(f"    f[{i+1}] = {fv}  ({pn})")

    step(2, "Product Graph")
    print(f"\n  Processes : {len(spec['processes'])}")
    print(f"  Products  : {len(spec['products'])}")
    n_em_preview  = len(spec.get("elementary_flows", {}).get("emissions", []))
    n_res_preview = len(spec.get("elementary_flows", {}).get("resources", []))
    print(f"  Emissions : {n_em_preview}")
    if n_res_preview > 0:
        print(f"  Resources : {n_res_preview}")
    print()
    for ps in spec["processes"]:
        ro  = ps["reference_output"]
        ins = ", ".join(f"{i['amount']} {i['flow']}" for i in ps.get("inputs", []))
        ems = ", ".join(f"{e['amount']} {e['flow']}" for e in ps.get("emissions", []))
        res = ", ".join(f"{r['amount']} {r['flow']}" for r in ps.get("resources", []))
        print(f"  {ps['name']}")
        print(f"    → outputs {ro['amount']} {ro['flow']}")
        if ins:  print(f"    ← needs   {ins}")
        if ems:  print(f"    ↑ emits   {ems}")
        if res:  print(f"    ↓ uses    {res} [from nature]")

    client = RestClient(SERVER_URL)
    reg, system_ref = build_model(client, spec)

    A, B, prod_names, proc_names, em_names, res_names = build_matrices(spec)
    n_em  = len(em_names)
    n_res = len(res_names)
    ef_names = em_names + res_names

    step(8, "Technology Matrix A")
    print()
    print_matrix(prod_names, proc_names, A.tolist(),
                 row_label="products", col_label="processes")

    step(9, "Scaling Vector  s = A⁻¹ · f")
    prod_idx_map = {n: i for i, n in enumerate(prod_names)}
    f = np.zeros(len(prod_names))
    f[prod_idx_map[ref_flow]] = fu["amount"]
    s = np.linalg.solve(A, f)
    print(f"\n  f = {list(f)}")
    print(f"\n  s = A⁻¹ · f")
    for i, (pn, sv) in enumerate(zip(proc_names, s)):
        bar = "█" * int(sv * 20)
        print(f"    s[{i+1}] = {sv:.4f}  {bar}  {pn}")

    step(10, "Intervention Matrix B")
    print()
    if len(ef_names) > 0:
        print_matrix(ef_names, proc_names, B.tolist(),
                     row_label="elementary flows (+ emission, − resource)",
                     col_label="processes")
    else:
        print("  (no elementary flows defined)")

    step(11, "LCA Calculation via openLCA gdt-server")

    lcia_spec   = spec.get("lcia", {})
    method_name = lcia_spec.get("method_name", "")
    method_ref  = None
    if method_name:
        method_ref = get_impact_method_ref(client, method_name)

    print(f"\n  Submitting product system {system_ref.id[:8]}…")
    setup = o.CalculationSetup(
        target=o.Ref(id=system_ref.id),
        amount=fu["amount"],
        impact_method=method_ref
    )
    result = client.calculate(setup)
    result.wait_until_ready()
    print(f"  Calculation complete.")

    flows = result.get_total_flows()
    olca_outputs = {f.envi_flow.flow.name: f.amount
                    for f in flows if not f.envi_flow.is_input}
    olca_inputs  = {f.envi_flow.flow.name: f.amount
                    for f in flows if f.envi_flow.is_input}

    olca_impacts = {}
    if method_ref:
        for iv in result.get_total_impacts():
            olca_impacts[iv.impact_category.name] = (iv.amount, iv.impact_category.ref_unit or "")

    result.dispose()

    step(12, "LCI Results  B · s")
    Bs = B @ s
    print()
    print(f"  {'Flow':<32} {'Numpy':>10}  {'openLCA':>10}  Unit")
    rule()
    for i, en in enumerate(em_names):
        olca_val = olca_outputs.get(en)
        unit_sym = get_ef_unit(spec, en)
        match    = "✓ MATCH" if olca_val is not None and abs(olca_val - Bs[i]) < 1e-4 else "✗ DIFF"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        print(f"  {en:<32} {Bs[i]:>10.4f}  {olca_str:>10}  {unit_sym}  {match}")
    for i, rn in enumerate(res_names):
        olca_val = olca_inputs.get(rn)
        np_val   = abs(Bs[n_em + i])
        unit_sym = get_ef_unit(spec, rn)
        match    = "✓ MATCH" if olca_val is not None and abs(olca_val - np_val) < 1e-4 else "✗ DIFF"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        print(f"  {rn:<32} {np_val:>10.4f}  {olca_str:>10}  {unit_sym}  [from nature]  {match}")
    print()
    print(f"  LCI emissions: " + "  ".join(f"{en}={Bs[i]:.4f}" for i, en in enumerate(em_names)))
    if res_names:
        print(f"  LCI resources: " + "  ".join(
            f"{rn}={abs(Bs[n_em+i]):.4f}" for i, rn in enumerate(res_names)))

    step(13, "Scaled Emissions by Process  (B · diag(s))")
    print()
    col_w = 10
    if em_names:
        header_e = f"  {'Process':<30} {'s':>8}  " + "  ".join(
            f"{en[:col_w]:>{col_w}}" for en in em_names)
        print(header_e)
        rule()
        for j, pn in enumerate(proc_names):
            cols = "  ".join(f"{B[k,j]*s[j]:>{col_w}.4f}" for k in range(n_em))
            print(f"  {pn:<30} {s[j]:>8.4f}  {cols}")
        totals = "  ".join(f"{Bs[k]:>{col_w}.4f}" for k in range(n_em))
        print(f"  {'Total':<30} {'':>8}  {totals}")

    if res_names:
        print()
        header_r = f"  {'Process':<30} {'s':>8}  " + "  ".join(
            f"{rn[:col_w]:>{col_w}}" for rn in res_names)
        print(header_r)
        rule()
        for j, pn in enumerate(proc_names):
            cols_r = "  ".join(
                f"{abs(B[n_em+k,j]*s[j]):>{col_w}.4f}" for k in range(n_res))
            print(f"  {pn:<30} {s[j]:>8.4f}  {cols_r}")
        totals_r = "  ".join(f"{abs(Bs[n_em+k]):>{col_w}.4f}" for k in range(n_res))
        print(f"  {'Total':<30} {'':>8}  {totals_r}")

    if olca_impacts:
        step(14, f"LCIA Results  ({method_name})")
        print()
        for cat_name, (val, unit) in olca_impacts.items():
            print(f"  {cat_name:<45} {val:>12.6f}  {unit}")
    elif lcia_spec.get("impact_categories"):
        all_ef_idx = {n: i for i, n in enumerate(em_names + res_names)}
        step(14, f"LCIA Characterization  ({lcia_spec['method']})")
        for cat in lcia_spec["impact_categories"]:
            cfs       = cat.get("characterization_factors", {})
            cat_total = sum(
                abs(Bs[all_ef_idx[en]]) * cf
                for en, cf in cfs.items() if en in all_ef_idx
            )
            indicator = cat.get("indicator", cat["name"])
            cat_unit  = cat.get("unit", "")
            print(f"\n  {indicator}: {cat_total:.4f} {cat_unit}")
            for en, cf in cfs.items():
                if en in all_ef_idx:
                    lci_val  = abs(Bs[all_ef_idx[en]])
                    ef_unit  = get_ef_unit(spec, en)
                    print(f"    {en:<28} {lci_val:.4f} {ef_unit} × {cf} = {lci_val*cf:.4f} {cat_unit}")

    write_results_md(spec, A, B, s, Bs, olca_outputs, olca_inputs,
                     proc_names, prod_names, em_names, res_names,
                     system_ref.id, olca_impacts=olca_impacts, method_name=method_name)

    step(15, "Product Graphs")
    graph_dir = str(pathlib.Path(ANALYSIS_FILE).parent)
    scaled_file    = f"{graph_dir}/product_graph_scaled.svg"
    structure_file = f"{graph_dir}/product_graph_structure.svg"
    generate_svg(ANALYSIS_FILE, scaled_file, show_quantities=True)
    generate_svg(ANALYSIS_FILE, structure_file, show_quantities=False)
    print(f"  Scaled graph    → {scaled_file}")
    print(f"  Structure graph → {structure_file}")

    banner("Done")
    print(f"  Results written to → {RESULTS_FILE}")
    print(f"  Scaled graph    to → {scaled_file}")
    print(f"  Structure graph to → {structure_file}")
    print()

if __name__ == "__main__":
    main()
