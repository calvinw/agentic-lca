---
name: product-graph-svg
description: >
  Use this skill whenever the user wants to generate a supply chain diagram
  (SVG image) from an LCA recipe card. Triggers include: "generate SVG",
  "draw supply chain", "product graph", "supply chain diagram",
  "visualise the processes", "recipe card SVG", "product graph SVG",
  "structure diagram", "scaled diagram", "run lca_svg.py".
  Also triggers when the user asks to experiment with or modify recipe
  cards in the product_graphs/ folder and regenerate the diagrams.
---

## How this skill works

This skill uses `lca_scripts/lca_svg.py` to turn a **recipe card** (a YAML
description of a supply chain) into a **supply chain diagram** as an SVG image.

The script produces two types of diagrams:

| Type | Flag | What it shows |
|---|---|---|
| **Scaled graph** | (default) | Each process box, its scaling factor, and the amounts flowing between processes. Emissions and resource arrows also show calculated quantities. |
| **Structure graph** | `--structure` | Flow names only — no numbers. Clean, simple overview of how processes connect. |

These use the `dot` engine from graphviz to do the layout, then draw the SVG
from scratch using the positions dot gives back.

---

## Prerequisites

The script needs these tools. They should already be available in the dev
container, but if they are not:

```bash
pip install pyyaml numpy --break-system-packages   # Python packages
sudo apt-get install -y graphviz                   # dot command
```

You do **not** need the openLCA server running for this script — it works
entirely from the recipe card YAML with no database connection.

---

## Naming convention

Each recipe card produces two SVG files:

| Output file | Contents |
|---|---|
| `<product>_product_graph_scaled.svg` | Scaled diagram — amounts + scaling factors |
| `<product>_product_graph_structure.svg` | Structure diagram — flow names only |

Always pass the output path explicitly so the name comes out right.

## Usage (terminal commands)

### Scaled diagram (amounts + scaling factors shown) — default
```bash
python3 lca_scripts/lca_svg.py product_graphs/coffee_recipe_card.md \
    product_graphs/coffee_product_graph_scaled.svg
```
This creates `coffee_product_graph_scaled.svg` — each process box shows its
scaling factor `sₙ` and the amounts flowing between processes.

### Structure diagram (flow names only)
```bash
python3 lca_scripts/lca_svg.py product_graphs/coffee_recipe_card.md \
    product_graphs/coffee_product_graph_structure.svg --structure
```
This creates `coffee_product_graph_structure.svg` — flow names only, no
quantities.

---

## Recipe cards available in `product_graphs/`

There are 9 recipe cards ready to use for experimenting:

| File | Product |
|---|---|
| `coffee_recipe_card.md` | Coffee — one cup |
| `cotton_shirt_recipe_card.md` | Cotton shirt — cradle to gate |
| `paper_cup_recipe_card.md` | Paper cup — one cup |
| `light_bulb_recipe_card.md` | Incandescent light bulb — 800 lm for 5000 h |
| `hand_dryer_recipe_card.md` | Warm air hand dryer — one drying event |
| `plastic_broom_recipe_card.md` | Plastic broom — cradle to gate |
| `blorp_recipe_card.md` | Blorp (fictional teaching example) — 10 Blorps |
| `electricity_recipe_card.md` | Electricity — 200 kWh from crude oil |
| `coffee_exercise_recipe_card.md` | Coffee exercise — process tree (student version) |

---

## Experimenting with recipe cards

You can open any recipe card (in `product_graphs/`) and edit it — change
amounts, add new processes, add emissions — then regenerate the SVG to see
how the diagram changes. No server needed.

### Common experiments to try

1. **Change an amount** — edit the amount in an input or output line, then
   re-run `lca_svg.py`. The scaling factors and all arrow labels
   recalculate automatically.

2. **Add a new process** — add a new entry under `processes:`, add its
   product to `products:`, and connect it via `inputs:`. The diagram will
   grow to include it.

3. **Switch to structure view** — add `--structure` to see just the
   process connections without numbers.

---

## What the script prints

When you run the script, it prints one line like this:

```
Written: product_graphs/coffee_product_graph_scaled.svg  (800×600px)
```

This confirms the SVG file was saved. Open it in VS Code's built-in image
viewer (click the filename in the Explorer panel) to see the diagram.

---

## Related skills

- **`run-lca`** — For running the full LCA calculation (needs the openLCA
  server) which also generates SVGs as part of the analysis output.
