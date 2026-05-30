#!/usr/bin/env python3
"""
lca_analysis.py

Reads an LCA specification from a recipe_card.md file (YAML frontmatter), builds
the model in openLCA via the gdt-server REST API, walks through each step of the
LCI methodology, writes lca_results.md, and generates product_graph.png.

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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ANALYSIS_FILE = sys.argv[1] if len(sys.argv) > 1 else "recipe_card.md"
RESULTS_FILE  = str(pathlib.Path(ANALYSIS_FILE).parent / "lca_results.md")
GRAPH_FILE    = str(pathlib.Path(ANALYSIS_FILE).parent / "product_graph.png")
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

# ── Build openLCA entities ────────────────────────────────────────────────────

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

    step(5, "Elementary Flows  (biosphere — emissions & extractions)")
    ef = spec.get("elementary_flows", {})
    for em in ef.get("emissions", []):
        flow = o.new_elementary_flow(em["name"], reg[em["unit"]])
        client.put(flow)
        reg[em["name"]] = flow
        print(f"    {em['name']}  [{em['unit']}]  ↑ emission to nature")
    for res in ef.get("resources", []):
        flow = o.new_elementary_flow(res["name"], reg[res["unit"]])
        client.put(flow)
        reg[res["name"]] = flow
        print(f"    {res['name']}  [{res['unit']}]  ↓ extraction from nature")

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
        print(f"      output:    {ro['amount']} {ro['flow']}")
        for inp in ps.get("inputs", []):
            print(f"      input:     {inp['amount']} {inp['flow']}")
        for em in ps.get("emissions", []):
            print(f"      emits:     {em['amount']} {em['flow']} → biosphere")
        for res in ps.get("resources", []):
            print(f"      extracts:  {res['amount']} {res['flow']} ← nature")

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

    ef = spec.get("elementary_flows", {})
    emissions_list = ef.get("emissions", [])
    resources_list = ef.get("resources", [])

    # env_flows: all biosphere flows with type info for display and sign logic
    env_flows = (
        [{"name": e["name"], "unit": e["unit"], "type": "emission"} for e in emissions_list] +
        [{"name": r["name"], "unit": r["unit"], "type": "resource"} for r in resources_list]
    )
    env_names = [f["name"] for f in env_flows]

    prod_idx = {n: i for i, n in enumerate(prod_names)}
    proc_idx = {n: i for i, n in enumerate(proc_names)}
    env_idx  = {n: i for i, n in enumerate(env_names)}

    n_prod = len(prod_names)
    n_proc = len(proc_names)
    n_env  = len(env_names)

    A = np.zeros((n_prod, n_proc))
    B = np.zeros((n_env,  n_proc))

    for ps in spec["processes"]:
        j = proc_idx[ps["name"]]
        ro = ps["reference_output"]
        if ro["flow"] in prod_idx:
            A[prod_idx[ro["flow"]], j] = ro["amount"]
        for inp in ps.get("inputs", []):
            if inp["flow"] in prod_idx:
                A[prod_idx[inp["flow"]], j] = -inp["amount"]
        for em in ps.get("emissions", []):
            if em["flow"] in env_idx:
                B[env_idx[em["flow"]], j] = +em["amount"]    # positive: output to nature
        for res in ps.get("resources", []):
            if res["flow"] in env_idx:
                B[env_idx[res["flow"]], j] = -res["amount"]  # negative: input from nature

    return A, B, prod_names, proc_names, env_names, env_flows

# ── Generate product_graph.png ────────────────────────────────────────────────

def topo_sort(processes):
    produces = {ps["reference_output"]["flow"]: ps["name"] for ps in processes}
    deps = {ps["name"]: [] for ps in processes}
    for ps in processes:
        for inp in ps.get("inputs", []):
            if inp["flow"] in produces:
                deps[ps["name"]].append(produces[inp["flow"]])
    ordered = []
    remaining = [ps["name"] for ps in processes]
    while remaining:
        for name_p in remaining:
            if all(d in ordered for d in deps[name_p]):
                ordered.append(name_p)
                remaining.remove(name_p)
                break
    return ordered

def generate_graph(spec: dict, output_path: str):
    processes = spec["processes"]
    ref_name  = spec["reference_process"]
    fu        = spec["functional_unit"]
    name      = spec["name"]

    order    = topo_sort(processes)
    proc_map = {ps["name"]: ps for ps in processes}
    produces = {ps["reference_output"]["flow"]: ps["name"] for ps in processes}

    n     = len(processes)
    COL_W = 3.2
    ROW_H = 6.5
    fig_w = (n + 1) * COL_W + 1.0

    fig, ax = plt.subplots(figsize=(fig_w, ROW_H))
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, ROW_H)
    ax.axis("off")
    fig.patch.set_facecolor("#f5f5f5")

    Y_NATURE_IN  = 5.8
    Y_PROCESS    = 3.2
    Y_BUS        = 4.3
    Y_NATURE_OUT = 1.0
    C_PROC = "#3a7ebf"; C_FU = "#7b4ea6"; C_IN = "#3a9957"
    C_OUT  = "#c45c1a"; C_ARROW = "#444444"; C_EM_ARR = "#c0392b"
    BOX_W  = 2.2;  BOX_H = 0.8;  EM_W = 2.0;  EM_H = 0.5

    LABEL_PROPS = dict(fontsize=7.5, zorder=6,
                       bbox=dict(boxstyle="round,pad=0.15",
                                 facecolor="white", edgecolor="none", alpha=0.85))

    def col_x(i):
        return 0.9 + i * COL_W + COL_W / 2

    proc_col = {pname: col_x(i) for i, pname in enumerate(order)}

    def box(cx, cy, text, color, w=BOX_W, h=BOX_H, fs=8):
        ax.add_patch(mpatches.FancyBboxPatch(
            (cx - w/2, cy - h/2), w, h,
            boxstyle="round,pad=0.06",
            facecolor=color, edgecolor="white", linewidth=1.5, zorder=3))
        ax.text(cx, cy, text, ha="center", va="center",
                fontsize=fs, color="white", fontweight="bold",
                zorder=4, multialignment="center", linespacing=1.3)

    def labelled_arrow(x1, y1, x2, y2, label="", color=C_ARROW):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.6), zorder=2)
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            if abs(x2-x1) >= abs(y2-y1):
                ax.text(mx, my + 0.16, label, ha="center", va="bottom",
                        color=color, **LABEL_PROPS)
            else:
                ax.text(mx + 0.12, my, label, ha="left", va="center",
                        color=color, **LABEL_PROPS)

    # ── Title
    ax.text(fig_w/2, ROW_H - 0.28, name, ha="center", fontsize=12,
            fontweight="bold", color="#222", zorder=5)
    ax.text(fig_w/2, ROW_H - 0.65, "Product Graph", ha="center",
            fontsize=9, color="#666", zorder=5)

    # ── Zone bands
    for label, color, y_bot, y_top in [
        ("From Nature",  "#e8f5ec", 5.1, 6.4),
        ("Supply Chain", "#e8f0f8", 2.4, 5.0),
        ("To Nature",    "#fdeede", 0.2, 1.7),
    ]:
        h = y_top - y_bot
        ax.add_patch(mpatches.FancyBboxPatch(
            (0.2, y_bot), fig_w - 0.4, h,
            boxstyle="round,pad=0.05", facecolor=color, edgecolor="none", zorder=0))
        ax.text(0.45, (y_bot + y_top) / 2, label, ha="center", va="center",
                fontsize=7.5, color="#555", fontstyle="italic", rotation=90, zorder=1)

    # ── Process boxes
    for pname in order:
        ps = proc_map[pname]
        ro = ps["reference_output"]
        box(proc_col[pname], Y_PROCESS,
            f"{pname}\n→ {ro['amount']} {ro['flow']}", C_PROC)

    # ── Group flows: (src, flow_name, unit) → [(dst, amount)]
    flow_groups = {}
    for pname in order:
        for inp in proc_map[pname].get("inputs", []):
            if inp["flow"] in produces:
                src      = produces[inp["flow"]]
                unit_sym = next((p["unit"] for p in spec["products"]
                                 if p["name"] == inp["flow"]), "")
                key = (src, inp["flow"], unit_sym)
                flow_groups.setdefault(key, []).append((pname, inp["amount"]))

    # ── Draw technosphere arrows
    for (src, flow, unit_sym), dsts in flow_groups.items():
        src_cx = proc_col[src]

        if len(dsts) == 1:
            dst, amount = dsts[0]
            labelled_arrow(src_cx + BOX_W/2, Y_PROCESS,
                           proc_col[dst] - BOX_W/2, Y_PROCESS,
                           label=f"{amount} {unit_sym}")
        else:
            dst_cxs     = [proc_col[d] for d, _ in dsts]
            x_bus_start = src_cx
            x_bus_end   = max(dst_cxs)
            ax.plot([src_cx, src_cx], [Y_PROCESS + BOX_H/2, Y_BUS],
                    color=C_ARROW, lw=1.5, zorder=2)
            ax.plot([x_bus_start, x_bus_end], [Y_BUS, Y_BUS],
                    color=C_ARROW, lw=1.5, ls="--", zorder=2)
            ax.text((x_bus_start + x_bus_end)/2, Y_BUS + 0.1, flow,
                    ha="center", va="bottom", color=C_ARROW, **LABEL_PROPS)
            for dst, amount in dsts:
                dcx = proc_col[dst]
                labelled_arrow(dcx, Y_BUS, dcx, Y_PROCESS + BOX_H/2,
                               label=f"{amount} {unit_sym}")

    # ── From Nature boxes (named resources if defined, generic fallback otherwise)
    for pname in order:
        ps  = proc_map[pname]
        cx  = proc_col[pname]
        resources     = ps.get("resources", [])
        has_tech_inputs = any(inp["flow"] in produces for inp in ps.get("inputs", []))

        if resources:
            label = "\n".join(f"{r['amount']} {r['flow']}" for r in resources)
            box(cx, Y_NATURE_IN, label, C_IN, w=EM_W, h=EM_H, fs=7.5)
            labelled_arrow(cx, Y_NATURE_IN - EM_H/2,
                           cx, Y_PROCESS + BOX_H/2, color=C_IN)
        elif not has_tech_inputs:
            box(cx, Y_NATURE_IN, "Raw materials\n(from nature)", C_IN,
                w=EM_W, h=EM_H, fs=7.5)
            labelled_arrow(cx, Y_NATURE_IN - EM_H/2,
                           cx, Y_PROCESS + BOX_H/2, color=C_IN)

    # ── Emission arrows + boxes
    em_positions = {}
    for pname in order:
        cx = proc_col[pname]
        for em in proc_map[pname].get("emissions", []):
            labelled_arrow(cx, Y_PROCESS - BOX_H/2, cx, Y_NATURE_OUT + EM_H/2,
                           label=f"{em['amount']} {em['flow']}", color=C_EM_ARR)
            em_positions[em["flow"]] = cx
    for em_flow, cx in em_positions.items():
        box(cx, Y_NATURE_OUT, em_flow, C_OUT, w=EM_W, h=EM_H, fs=7.5)

    # ── Functional unit box
    fu_cx  = proc_col[ref_name] + COL_W
    ref_ro = proc_map[ref_name]["reference_output"]
    box(fu_cx, Y_PROCESS,
        f"Functional Unit\n{fu['amount']} {fu['unit']}\n{fu['description']}",
        C_FU, w=BOX_W, h=BOX_H + 0.2, fs=7.5)
    labelled_arrow(proc_col[ref_name] + BOX_W/2, Y_PROCESS,
                   fu_cx - BOX_W/2, Y_PROCESS,
                   label=f"{ref_ro['amount']} {ref_ro['flow']}")

    # ── Legend
    ax.legend(handles=[
        mpatches.Patch(facecolor=C_PROC, label="Supply chain process"),
        mpatches.Patch(facecolor=C_FU,   label="Functional unit"),
        mpatches.Patch(facecolor=C_IN,   label="Extraction from nature"),
        mpatches.Patch(facecolor=C_OUT,  label="Emission to nature"),
    ], loc="lower right", fontsize=7.5, framealpha=0.9, edgecolor="#ccc")

    plt.tight_layout(pad=0.3)
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="#f5f5f5")
    plt.close()

# ── Generate lca_results.md ───────────────────────────────────────────────────

def write_results_md(spec, A, B, s, Bs, olca_by_name,
                     proc_names, prod_names, env_names, env_flows, system_id):
    fu   = spec["functional_unit"]
    name = spec["name"]
    now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

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
    ln("Columns = processes, rows = elementary flows.  "
       "`+` = emission to nature, `−` = extraction from nature.")
    ln()
    ln(header); ln(sep)
    for i, ef in enumerate(env_flows):
        tag = "↑" if ef["type"] == "emission" else "↓"
        row = f"| **{tag} {ef['name']}** |"
        for j in range(len(proc_names)):
            v = B[i, j]
            row += f" {v:+.2f} |" if v != 0 else "  0   |"
        ln(row)
    ln()

    ln("## Step 5 — LCI Results  B · s")
    ln()
    ln("| Flow | Type | Numpy result | openLCA result | Unit | Match |")
    ln("|---|---|---:|---:|---|:---:|")
    for i, ef in enumerate(env_flows):
        olca_val = olca_by_name.get(ef["name"])
        np_val   = Bs[i]
        unit     = ef["unit"]
        match    = "✓" if olca_val is not None and abs(olca_val - np_val) < 1e-4 else "✗"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        ftype    = "emission ↑" if ef["type"] == "emission" else "extraction ↓"
        ln(f"| **{ef['name']}** | {ftype} | {np_val:.4f} | {olca_str} | {unit} | {match} |")
    ln()

    ln("## Step 6 — Contribution Analysis")
    ln()
    ln("Which process is responsible for each elementary flow?")
    ln()
    for i, ef in enumerate(env_flows):
        flow_total = Bs[i]
        if abs(flow_total) < 1e-10:
            continue
        ftype = "emission ↑" if ef["type"] == "emission" else "extraction ↓"
        ln(f"### {ef['name']}  ({ftype})")
        ln()
        ln("| Process | Scale (s) | Direct amount | % of total |")
        ln("|---|---:|---:|---:|")
        for j, pn in enumerate(proc_names):
            direct = B[i, j] * s[j]
            pct    = direct / flow_total * 100 if flow_total != 0 else 0
            ln(f"| {pn} | {s[j]:.4f} | {direct:.4f} {ef['unit']} | {pct:.0f}% |")
        ln()

    ln("## Summary")
    ln()
    ln("$$")
    ln(r"\text{Total inventory} = B \cdot A^{-1} \cdot f")
    ln("$$")
    ln()
    for i, ef in enumerate(env_flows):
        sign = "released" if ef["type"] == "emission" else "extracted"
        ln(f"> **{ef['name']}: {abs(Bs[i]):.4f} {ef['unit']} {sign}** "
           f"per {fu['amount']} {fu['unit']} of {fu['description']}")
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
        print(f"\n  Start it with:  bash start_olca.sh")
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
    ef = spec.get("elementary_flows", {})
    print(f"\n  Processes   : {len(spec['processes'])}")
    print(f"  Products    : {len(spec['products'])}")
    print(f"  Emissions   : {len(ef.get('emissions', []))}")
    print(f"  Extractions : {len(ef.get('resources', []))}")
    print()
    for ps in spec["processes"]:
        ro  = ps["reference_output"]
        ins = ", ".join(f"{i['amount']} {i['flow']}" for i in ps.get("inputs", []))
        ems = ", ".join(f"{e['amount']} {e['flow']}" for e in ps.get("emissions", []))
        res = ", ".join(f"{r['amount']} {r['flow']}" for r in ps.get("resources", []))
        print(f"  {ps['name']}")
        print(f"    → outputs  {ro['amount']} {ro['flow']}")
        if ins:  print(f"    ← needs    {ins}")
        if ems:  print(f"    ↑ emits    {ems}")
        if res:  print(f"    ↓ extracts {res}")

    client = RestClient(SERVER_URL)
    reg, system_ref = build_model(client, spec)

    A, B, prod_names, proc_names, env_names, env_flows = build_matrices(spec)

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
    if env_names:
        print("  + = emission to nature   − = extraction from nature")
        print()
        print_matrix(env_names, proc_names, B.tolist(),
                     row_label="elementary flows", col_label="processes")
    else:
        print("  (no elementary flows defined)")

    step(11, "LCA Calculation via openLCA gdt-server")
    print(f"\n  Submitting product system {system_ref.id[:8]}…")
    setup  = o.CalculationSetup(target=o.Ref(id=system_ref.id), amount=fu["amount"])
    result = client.calculate(setup)
    result.wait_until_ready()
    print(f"  Calculation complete.")

    flows = result.get_total_flows()
    # Signed to match B matrix convention: positive = emission, negative = extraction
    olca_by_name = {
        f.envi_flow.flow.name: (-f.amount if f.envi_flow.is_input else f.amount)
        for f in flows
    }
    result.dispose()

    step(12, "LCI Results  B · s")
    Bs = B @ s
    print()
    print(f"  {'Flow':<32} {'Type':<12} {'Numpy':>10}  {'openLCA':>10}  Unit")
    rule()
    for i, ef in enumerate(env_flows):
        olca_val = olca_by_name.get(ef["name"])
        ftype    = "emission ↑" if ef["type"] == "emission" else "extract ↓"
        match    = "✓ MATCH" if olca_val is not None and abs(olca_val - Bs[i]) < 1e-4 else "✗ DIFF"
        olca_str = f"{olca_val:.4f}" if olca_val is not None else "—"
        print(f"  {ef['name']:<32} {ftype:<12} {Bs[i]:>10.4f}  {olca_str:>10}  {ef['unit']}  {match}")
    print()

    step(13, "Contribution Analysis (Hotspot Identification)")
    print()
    for i, ef in enumerate(env_flows):
        flow_total = Bs[i]
        if abs(flow_total) < 1e-10:
            continue
        ftype = "emission ↑" if ef["type"] == "emission" else "extraction ↓"
        print(f"  {ef['name']}  ({ftype})  total = {flow_total:.4f} {ef['unit']}")
        print()
        print(f"  {'Process':<30} {'Scale':>8}  {'Direct amount':>14}  % of total")
        rule()
        for j, pn in enumerate(proc_names):
            direct = B[i, j] * s[j]
            pct    = direct / flow_total * 100 if flow_total != 0 else 0
            bar    = "█" * int(abs(pct) / 5)
            print(f"  {pn:<30} {s[j]:>8.4f}  {direct:>10.4f} {ef['unit']}  {pct:5.1f}%  {bar}")
        print()

    write_results_md(spec, A, B, s, Bs, olca_by_name,
                     proc_names, prod_names, env_names, env_flows, system_ref.id)

    step(14, "Product Graph")
    generate_graph(spec, GRAPH_FILE)
    print(f"  Graph saved  → {GRAPH_FILE}")

    banner("Done")
    print(f"  Results written to → {RESULTS_FILE}")
    print(f"  Graph saved    to → {GRAPH_FILE}")
    print()

if __name__ == "__main__":
    main()
