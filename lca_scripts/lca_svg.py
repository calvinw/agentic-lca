#!/usr/bin/env python3
"""
lca_svg.py  —  Generate an LCA product-system SVG from a recipe_card.md file.

This script produces two types of supply chain diagrams:
  • Scaled graph    — shows flow amounts and scaling factors (default)
  • Structure graph — shows flow names only (use --structure)

It is also called automatically by lca_analysis.py after the LCA calculation
step (Step 14 in the report). No separate command is needed during a normal
analysis workflow.

┌─────────────────────────────────────────────────────────────────────┐
│ USAGE                                                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   # Scaled graph (with amounts + scaling factors)                   │
│   python3 lca_svg.py lca_analysis/coffee/recipe_card.md             │
│                                                                     │
│   # Structure graph (flow names only)                               │
│   python3 lca_svg.py lca_analysis/coffee/recipe_card.md --structure │
│                                                                     │
│   # Specify output path                                             │
│   python3 lca_svg.py recipe_card.md my_graph.svg                    │
│                                                                     │
│   # Or the default — just pass the recipe card path:                │
│   #   python3 lca_svg.py lca_analysis/coffee/recipe_card.md         │
│   #   →  writes lca_analysis/coffee/recipe_card.svg                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Prerequisites:
  • Python 3 with numpy, pyyaml, olca-schema (no olca-ipc needed for SVG)
  • graphviz (dot command) — installed in the devcontainer base image

Layout engine: graphviz dot (left-to-right DAG ranking)
Rendering:     pure SVG built from dot -Tplain node positions
"""

import sys
import re
import subprocess
import numpy as np
import yaml
from pathlib import Path


# ── Style constants ────────────────────────────────────────────────────────────
COL_PROCESS   = '#3a7ebf'
COL_FU        = '#7b4ea6'
COL_TECH_EDGE = '#555555'
COL_GREEN     = '#2d7a45'
COL_RED       = '#c0392b'
FONT          = 'Helvetica,Arial,sans-serif'

BOX_W, BOX_H  = 165, 54
FU_W,  FU_H   = 165, 66
MARGIN        = 60          # px around the graphviz bounding box
ELEM_ARM      = 60          # length of elementary flow arrows
EMIT_OFFSET   = 45          # ±px horizontal offset for multiple emissions
TITLE_HEIGHT  = 38          # px reserved for title above the graph

DPI           = 96          # graphviz uses 72 pt; we scale to 96px


# ── YAML parsing ──────────────────────────────────────────────────────────────
def load_recipe(path: str) -> dict:
    text = Path(path).read_text()
    # strip markdown fences if present
    m = re.search(r'^---\n(.*?)^---', text, re.DOTALL | re.MULTILINE)
    if m:
        return yaml.safe_load(m.group(1))
    return yaml.safe_load(text)


# ── Graphviz plain layout ──────────────────────────────────────────────────────
def run_dot_plain(recipe: dict) -> str:
    """Build a dot graph and return dot -Tplain output."""
    lines = ['digraph G {']
    lines.append('  rankdir=LR;')
    lines.append('  nodesep=1.2;')
    lines.append('  ranksep=0.6;')
    lines.append('  node [shape=rectangle, width=1.8, height=0.6, fixedsize=true];')
    lines.append('  edge [fontsize=11];')

    # process nodes
    for p in recipe['processes']:
        name = p['name']
        lines.append(f'  "{name}" [];')

    # functional unit node
    fu = recipe['functional_unit']
    lines.append(f'  "Functional Unit" [width=1.8, height=0.75];')

    # technosphere edges (process → process)
    ref = recipe['reference_process']
    for p in recipe['processes']:
        for inp in p.get('inputs', []):
            # find which process produces this flow
            src = _producer(recipe, inp['flow'])
            if src:
                label = inp["flow"]
                lines.append(f'  "{src}" -> "{p["name"]}" [label="{label}"];')

    # edge from reference process to functional unit
    ref = recipe['reference_process']
    ref_out = _ref_process(recipe, ref)
    fu_label = ref_out["reference_output"]["flow"]
    lines.append(f'  "{ref}" -> "Functional Unit" [label="{fu_label}"];')

    lines.append('}')
    dot_src = '\n'.join(lines)

    result = subprocess.run(
        ['dot', '-Tplain'],
        input=dot_src.encode(),
        capture_output=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"dot failed: {result.stderr.decode()}")
    return result.stdout.decode()


def _producer(recipe: dict, flow_name: str) -> str | None:
    for p in recipe['processes']:
        if p['reference_output']['flow'] == flow_name:
            return p['name']
    return None


def _ref_process(recipe: dict, name: str) -> dict:
    for p in recipe['processes']:
        if p['name'] == name:
            return p
    raise KeyError(name)


def _flow_unit(recipe: dict, flow_name: str) -> str:
    for f in recipe.get('products', []):
        if f['name'] == flow_name:
            return f['unit']
    return ''


# ── Scaling vector solver ─────────────────────────────────────────────────────
def compute_scaling(recipe: dict) -> dict:
    """Solve A·s = f and return {process_name: scaling_factor}."""
    order = [p['name'] for p in recipe['processes']]
    proc_map = {p['name']: p for p in recipe['processes']}
    products = [p['name'] for p in recipe['products']]

    n = len(order)
    m = len(products)
    A = np.zeros((m, n))

    for j, pname in enumerate(order):
        ps = proc_map[pname]
        ro = ps['reference_output']
        if ro['flow'] in products:
            A[products.index(ro['flow']), j] = ro['amount']
        for inp in ps.get('inputs', []):
            if inp['flow'] in products:
                A[products.index(inp['flow']), j] -= inp['amount']

    ref_ro = proc_map[recipe['reference_process']]['reference_output']
    f = np.zeros(m)
    if ref_ro['flow'] in products:
        f[products.index(ref_ro['flow'])] = recipe['functional_unit']['amount']

    s_vec = np.linalg.solve(A, f)
    return {pname: float(s_vec[j]) for j, pname in enumerate(order)}


# ── Parse dot -Tplain ──────────────────────────────────────────────────────────
def tokenize_plain(line: str) -> list[str]:
    """Split a dot -Tplain line respecting double-quoted tokens."""
    tokens = []
    i = 0
    while i < len(line):
        if line[i].isspace():
            i += 1
        elif line[i] == '"':
            j = i + 1
            while j < len(line) and line[j] != '"':
                j += 1
            tokens.append(line[i+1:j])
            i = j + 1
        else:
            j = i
            while j < len(line) and not line[j].isspace():
                j += 1
            tokens.append(line[i:j])
            i = j
    return tokens


def parse_plain(plain: str, scale: float):
    """
    Returns:
        graph_w, graph_h  — canvas size in px
        nodes   — {name: (cx, cy, w, h)}
        edges   — [(src, dst, points, label, lx, ly)]
    """
    nodes = {}
    edges = []
    graph_w = graph_h = 0

    for line in plain.splitlines():
        parts = tokenize_plain(line)
        if not parts:
            continue

        if parts[0] == 'graph':
            graph_w = float(parts[2]) * scale
            graph_h = float(parts[3]) * scale

        elif parts[0] == 'node':
            # node name cx cy w h label style shape color fillcolor
            name  = parts[1]
            cx    = float(parts[2]) * scale
            cy    = float(parts[3]) * scale
            w     = float(parts[4]) * scale
            h     = float(parts[5]) * scale
            nodes[name] = (cx, cy, w, h)

        elif parts[0] == 'edge':
            src   = parts[1]
            dst   = parts[2]
            n_pts = int(parts[3])
            pts   = []
            idx   = 4
            for _ in range(n_pts):
                px = float(parts[idx])   * scale
                py = float(parts[idx+1]) * scale
                pts.append((px, py))
                idx += 2
            # label may follow (quoted string, not a style keyword)
            label = lx = ly = None
            style_keywords = {'solid','dashed','bold','invis','dotted'}
            if idx < len(parts) and parts[idx] not in style_keywords:
                label = parts[idx].replace('\\n', '\n')
                lx    = float(parts[idx+1]) * scale
                ly    = float(parts[idx+2]) * scale
            edges.append((src, dst, pts, label, lx, ly))

    return graph_w, graph_h, nodes, edges


# ── SVG helpers ────────────────────────────────────────────────────────────────
def x(v):   return f'{v:.1f}'
def esc(s): return s.replace('&', '&amp;')


def svg_defs():
    return '''<defs>
  <marker id="arr"       viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="5" markerHeight="5" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="#555555"/>
  </marker>
  <marker id="arr-green" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="5" markerHeight="5" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="#2d7a45"/>
  </marker>
  <marker id="arr-red"   viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="5" markerHeight="5" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="#c0392b"/>
  </marker>
</defs>'''


def svg_text(tx, ty, text, anchor='middle', size=11, weight='normal',
             fill='#222', baseline='auto'):
    lines = text.split('\n')
    if len(lines) == 1:
        return (f'<text x="{x(tx)}" y="{x(ty)}" text-anchor="{anchor}" '
                f'dominant-baseline="{baseline}" '
                f'font-family="{FONT}" font-size="{size}" '
                f'font-weight="{weight}" fill="{fill}">{esc(text)}</text>')
    dy = size * 1.3
    start_y = ty - (len(lines) - 1) * dy / 2
    parts = [f'<text text-anchor="{anchor}" font-family="{FONT}" '
             f'font-size="{size}" font-weight="{weight}" fill="{fill}">']
    for i, ln in enumerate(lines):
        parts.append(f'<tspan x="{x(tx)}" y="{x(start_y + i*dy)}"'
                     f' dominant-baseline="{baseline}">{esc(ln)}</tspan>')
    parts.append('</text>')
    return '\n'.join(parts)


def svg_line(x1, y1, x2, y2, color, marker='arr', width=1.6):
    return (f'<line x1="{x(x1)}" y1="{x(y1)}" x2="{x(x2)}" y2="{x(y2)}" '
            f'stroke="{color}" stroke-width="{width}" '
            f'marker-end="url(#{marker})"/>')


def svg_rect(rx, ry, rw, rh, fill, corner=8):
    return (f'<rect x="{x(rx)}" y="{x(ry)}" width="{rw}" height="{rh}" '
            f'rx="{corner}" fill="{fill}"/>')


# ── Elementary flow injection ──────────────────────────────────────────────────
def elementary_flows(recipe: dict, nodes: dict, flip_y: float,
                     show_quantities: bool = True) -> list[str]:
    """
    Generate SVG elements for biosphere inputs (green, top) and
    emissions (red, bottom) for every process node.
    flip_y: canvas height used to flip graphviz y-axis (dot origin is bottom-left)
    """
    els = []

    for p in recipe['processes']:
        name = p['name']
        if name not in nodes:
            continue
        cx, cy, nw, nh = nodes[name]
        # flip y: graphviz origin is bottom-left, SVG is top-left
        cy = flip_y - cy
        box_top = cy - nh / 2
        box_bot = cy + nh / 2

        # ── Resources / biosphere inputs (green arrows, from above into top of box) ──
        resources = p.get('resources', [])
        n_res = len(resources)
        for i, res in enumerate(resources):
            offset = (i - (n_res - 1) / 2) * EMIT_OFFSET
            rx = cx + offset
            start_y = box_top - ELEM_ARM      # arrow starts above box
            from_nature_y = start_y - 10      # "from Nature" label above arrow start

            lx, anchor = rx + 5, 'start'

            els.append(svg_text(rx, from_nature_y, 'from Nature',
                                anchor='start', size=9, fill=COL_GREEN, baseline='auto',
                                weight='bold'))
            els.append(svg_line(rx, start_y, rx, box_top,
                                COL_GREEN, marker='arr-green'))
            shaft_mid = start_y + ELEM_ARM * 0.38
            els.append(svg_text(lx, shaft_mid,
                                res['flow'], anchor=anchor, size=11, fill=COL_GREEN,
                                weight='bold'))
            if show_quantities:
                els.append(svg_text(lx, shaft_mid + 14,
                                    f"{res['amount']} {_res_unit(recipe, res['flow'])}",
                                    anchor=anchor, size=11, fill=COL_GREEN,
                                    weight='bold'))

        # ── Emissions (red arrows, exit bottom downward) ──
        emissions = p.get('emissions', [])
        n_em = len(emissions)
        for i, em in enumerate(emissions):
            offset = (i - (n_em - 1) / 2) * EMIT_OFFSET
            ex = cx + offset
            end_y = box_bot + ELEM_ARM
            to_air_y = end_y + 12

            lx, anchor = ex + 5, 'start'

            els.append(svg_line(ex, box_bot, ex, end_y,
                                COL_RED, marker='arr-red'))
            mid_y = box_bot + ELEM_ARM * 0.38
            unit = _em_unit(recipe, em['flow'])
            els.append(svg_text(lx, mid_y,
                                em['flow'].replace(' to air', ''), anchor=anchor, size=11, fill=COL_RED,
                                weight='bold'))
            if show_quantities:
                els.append(svg_text(lx, mid_y + 14,
                                    f"{em['amount']} {unit}", anchor=anchor, size=11, fill=COL_RED,
                                    weight='bold'))
            els.append(svg_text(ex, to_air_y, 'to Air',
                                anchor='start', size=9, fill=COL_RED, baseline='auto',
                                weight='bold'))

    return els


def _res_unit(recipe, flow_name):
    for f in recipe.get('elementary_flows', {}).get('resources', []):
        if f['name'] == flow_name:
            return f['unit']
    return ''


def _em_unit(recipe, flow_name):
    for f in recipe.get('elementary_flows', {}).get('emissions', []):
        if f['name'] == flow_name:
            return f['unit']
    return ''


# ── Process & FU box rendering ─────────────────────────────────────────────────
def process_boxes(recipe: dict, nodes: dict, flip_y: float,
                  scaling: dict = {},
                  show_quantities: bool = True) -> list[str]:
    els = []
    process_names = {p['name'] for p in recipe['processes']}

    for name, (cx, cy, nw, nh) in nodes.items():
        cy = flip_y - cy
        is_fu = name == 'Functional Unit'
        fill  = COL_FU if is_fu else COL_PROCESS
        bx    = cx - nw / 2
        by    = cy - nh / 2

        els.append(svg_rect(bx, by, nw, nh, fill))

        if is_fu:
            fu = recipe['functional_unit']
            els.append(svg_text(cx, cy - nh * 0.18, 'Functional Unit',
                                size=11, fill='white'))
            els.append(svg_text(cx, cy + nh * 0.15,
                                fu['description'], size=10, fill='white'))
        else:
            idx = next((i+1 for i, p in enumerate(recipe['processes'])
                        if p['name'] == name), '?')
            els.append(svg_text(cx, cy - 8,
                                name, size=11, fill='white'))
            if show_quantities:
                sc = scaling.get(name, 1.0)
                els.append(svg_text(cx, cy + 8,
                                    f"s{idx} = {sc:.4g}", size=11, fill='white'))

    return els


# ── Technosphere edge rendering ────────────────────────────────────────────────
def tech_edges(edges: list, flip_y: float, recipe: dict,
               nodes: dict, show_quantities: bool = True) -> list[str]:
    """
    Draw edges from source box right-edge to dest box left-edge.
    We ignore dot spline control points (they don't clip to box boundaries
    in -Tplain) and compute the endpoints directly from node positions.
    For diagonal edges (different y), we draw straight lines.
    Label is placed at the midpoint of the line.
    """
    els = []
    for src, dst, pts, label, lx, ly in edges:
        if not pts:
            continue
        if src not in nodes or dst not in nodes:
            continue

        scx, scy, snw, snh = nodes[src]
        dcx, dcy, dnw, dnh = nodes[dst]
        scy = flip_y - scy
        dcy = flip_y - dcy

        # start: right edge midpoint of source box
        x1 = scx + snw / 2
        y1 = scy
        # end: left edge midpoint of dest box
        x2 = dcx - dnw / 2
        y2 = dcy

        els.append(svg_line(x1, y1, x2, y2, COL_TECH_EDGE))

        if label:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            if show_quantities:
                amount = _edge_amount(recipe, src, dst, label)
                unit   = _flow_unit(recipe, label)
                if amount is not None:
                    lbl = f"{label}\n{amount} {unit}"
                    els.append(svg_text(mx, my - 14, lbl,
                                        size=11, fill='#444', baseline='auto',
                                        weight='bold'))
                else:
                    els.append(svg_text(mx, my - 5, label,
                                        size=11, fill='#444', baseline='auto',
                                        weight='bold'))
            else:
                els.append(svg_text(mx, my - 5, label,
                                    size=11, fill='#444', baseline='auto',
                                    weight='bold'))
    return els


def _edge_amount(recipe: dict, src: str, dst: str, flow: str):
    """Return the amount for a technosphere flow between src and dst."""
    # check inputs of dst process
    for p in recipe['processes']:
        if p['name'] == dst:
            for inp in p.get('inputs', []):
                if inp['flow'] == flow:
                    return inp['amount']
    # check functional unit edge (amount for the reference product only)
    if dst == 'Functional Unit':
        return recipe['functional_unit']['amount']
    return None


def generate(recipe_path: str, out_path: str, show_quantities: bool = True):
    recipe = load_recipe(recipe_path)

    plain = run_dot_plain(recipe)
    scale = BOX_W / 1.8
    gw, gh, nodes, edges = parse_plain(plain, scale)

    ELEM_PAD = ELEM_ARM + 30

    canvas_w = gw + MARGIN * 2
    offset_x = MARGIN
    offset_y = ELEM_PAD + MARGIN

    shifted_nodes = {
        name: (cx + offset_x, cy + offset_y, nw, nh)
        for name, (cx, cy, nw, nh) in nodes.items()
    }

    flip_y = gh + offset_y

    scaling = compute_scaling(recipe) if show_quantities else {}

    svg_parts = []
    svg_parts.append('<!--HEADER-->')
    svg_parts.append('<!--BG-->')
    svg_parts.append(svg_defs())
    svg_parts.append('<!--TITLE-->')

    svg_parts.extend(elementary_flows(recipe, shifted_nodes, flip_y,
                                      show_quantities))

    shifted_edges = []
    for src, dst, pts, label, lx, ly in edges:
        spts = [(px + offset_x, py + offset_y) for px, py in pts]
        slx  = (lx + offset_x) if lx is not None else None
        sly  = (ly + offset_y) if ly is not None else None
        shifted_edges.append((src, dst, spts, label, slx, sly))

    svg_parts.extend(tech_edges(shifted_edges, flip_y, recipe, shifted_nodes,
                                show_quantities))
    svg_parts.extend(process_boxes(recipe, shifted_nodes, flip_y, scaling,
                                   show_quantities))
    svg_parts.append('</svg>')

    # compute content bounding box in SVG coordinates (post-flip)
    svg_y0 = float('inf')
    svg_y1 = float('-inf')
    for _, (cx, cy, nw, nh) in shifted_nodes.items():
        sc = flip_y - cy
        svg_y0 = min(svg_y0, sc - nh / 2)
        svg_y1 = max(svg_y1, sc + nh / 2)

    for p in recipe['processes']:
        n = shifted_nodes.get(p['name'])
        if not n: continue
        cx, cy, nw, nh = n
        sc = flip_y - cy
        if p.get('resources'):
            svg_y0 = min(svg_y0, sc - nh / 2 - ELEM_ARM - 24)
        if p.get('emissions'):
            svg_y1 = max(svg_y1, sc + nh / 2 + ELEM_ARM + 22)

    # extend bounding box to include title
    title = recipe.get('name', '')
    if title:
        svg_y0 -= TITLE_HEIGHT

    content_h = svg_y1 - svg_y0

    if title:
        title_y = svg_y0 + TITLE_HEIGHT * 0.7
        svg_parts[3] = svg_text(canvas_w / 2, title_y, title,
                                size=14, fill='#222', weight='bold')

    svg_parts[0] = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{canvas_w:.1f}" height="{content_h:.1f}" '
        f'viewBox="0 {svg_y0:.1f} {canvas_w:.1f} {content_h:.1f}">'
    )
    svg_parts[1] = (
        f'<rect x="0" y="{svg_y0:.1f}" width="{canvas_w:.1f}" '
        f'height="{content_h:.1f}" fill="#f8f8f8"/>'
    )

    out = '\n'.join(svg_parts)
    Path(out_path).write_text(out)
    print(f"Written: {out_path}  ({canvas_w:.0f}×{content_h:.0f}px)")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Generate an LCA product-system SVG from a recipe card.")
    parser.add_argument('recipe', help='Path to recipe_card.md')
    parser.add_argument('output', nargs='?', default=None,
                        help='Output SVG path (default: same dir as recipe)')
    parser.add_argument('--structure', action='store_true',
                        help='Show structure only (no amounts or scaling factors)')
    parser.add_argument('--scaled', action='store_true',
                        help='Show amounts and scaling factors (default)')
    args = parser.parse_args()
    out_path = args.output or args.recipe.replace('.md', '.svg')
    show_quantities = not args.structure  # default to quantities
    generate(args.recipe, out_path, show_quantities=show_quantities)
