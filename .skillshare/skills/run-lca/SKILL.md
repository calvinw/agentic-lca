---
version: 0.2
name: run-lca
author: Calvin Williamson (calvinw)
description: >
  Use this skill whenever the user wants to perform a Life Cycle Assessment
  (LCA) using openLCA. Triggers include: "carbon footprint of", "compare
  environmental impact", "LCA for", "which material has lower impact",
  "run an LCA", "ecoinvent dataset for", "GWP of", "calculate impact",
  "environmental footprint", "lifecycle analysis", "hotspot analysis",
  "sensitivity analysis", "scenario analysis", "cradle to gate".
  Also triggers when the user asks to make a spreadsheet, slides, or report
  FROM an LCA result.
---

## How this skill works

Call the `run_lca` MCP tool with the product graph YAML as a string. The tool
returns LCI totals, LCIA impact scores, scaling vector, and two SVG supply
chain diagrams — all in one call. No bash commands needed.

```
run_lca(product_graph="<yaml string>")
```

The tool returns:
```json
{
  "name": "...",
  "method": "TRACI 2.2",
  "functional_unit": "1 shirt — One cotton t-shirt",
  "system_id": "...",
  "lci": {
    "Carbon dioxide": { "amount": 0.38, "unit": "kg", "type": "emission" },
    "Water":          { "amount": 2125, "unit": "L",  "type": "resource" }
  },
  "lcia": {
    "Global warming": { "score": 0.396, "unit": "kg CO2 eq" },
    "Acidification":  { "score": 0.0,   "unit": "kg SO2 eq" }
  },
  "scaling_vector": {
    "P1 — Cotton farming": 0.266,
    "P2 — Yarn spinning":  0.231
  },
  "svg_scaled":    "<svg>...</svg>",
  "svg_structure": "<svg>...</svg>"
}
```

Display both SVGs inline so the student can see the supply chain diagram.
Explain the results in plain English — never show the raw JSON to the student.

---

## Prerequisites

Check that the Life Cycle Assessment MCP server is running using the
`check_server` tool before calling `run_lca`. If it returns `{"running": false}`,
tell the student:

> "The calculation engine isn't running right now. Start it by running
> `cd mcp-lca && uv run python sse_server.py` in the terminal, then try again."

---

## product_graph.yaml format

The product graph is a YAML string (the frontmatter of a `product_graph.yaml` file).
Pass it directly to `run_lca` — no file path needed.

```yaml
name: <human name for this analysis>
goal: <one sentence describing the purpose>

functional_unit:
  description: <what is being analysed, in plain English>
  amount: 1.0
  unit: <unit symbol, must appear in 'units' below>

units:
  cup: Cup count
  L:   Volume
  MJ:  Energy
  kg:  Mass

products:
  - { name: <flow name>, unit: <symbol> }

elementary_flows:
  emissions:
    - { name: <flow name>, unit: <symbol> }
  resources:
    - { name: <flow name>, unit: <symbol> }

processes:
  - name: <process name>
    reference_output: { flow: <product name>, amount: <number> }
    inputs:
      - { flow: <product name>, amount: <number> }
    emissions:
      - { flow: <emission name>, amount: <number> }
    resources:
      - { flow: <resource name>, amount: <number> }

reference_process: <process name that delivers the functional unit>

lcia:
  method_name: "TRACI 2.2"
```

### Minimal working example (coffee)

```yaml
name: Coffee LCA — one cup
goal: Calculate CO₂ for one cup of coffee
functional_unit:
  description: One cup of coffee
  amount: 1.0
  unit: cup

units:
  cup: Cup count
  L:   Volume
  MJ:  Energy
  kg:  Mass

products:
  - { name: Coffee,       unit: cup }
  - { name: Boiled water, unit: L   }
  - { name: Electricity,  unit: MJ  }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, unit: kg }

processes:
  - name: P1 — Make coffee
    reference_output: { flow: Coffee,       amount: 1.0 }
    inputs:
      - { flow: Boiled water, amount: 0.2 }

  - name: P2 — Boil water
    reference_output: { flow: Boiled water, amount: 1.0 }
    inputs:
      - { flow: Electricity,  amount: 0.5 }

  - name: P3 — Burn coal
    reference_output: { flow: Electricity,  amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 1.0 }

reference_process: P1 — Make coffee

lcia:
  method_name: "TRACI 2.2"
```

---

## FEDEFL flow names

Always use exact EPA FEDEFL names for elementary flows:

| Use this | Not this |
|---|---|
| `Carbon dioxide` | `CO2`, `CO2 to air` |
| `Methane` | `CH4` |
| `Nitrous oxide` | `N2O` |
| `Nitrogen oxides` | `NOx` |
| `Sulfur dioxide` | `SO2` |
| `Water` | `H2O` |

---

## What to ask the user when setting up a new analysis

1. **Name and goal** — what system, why are they studying it?
2. **Functional unit** — what, how much, which unit?
3. **Units** — list every unit symbol used.
4. **Products** — intermediate goods flowing between processes.
5. **Emissions** — CO₂, CH₄, NOₓ, freshwater, etc.
6. **Processes** — for each: what does it produce, consume, and emit?
7. **Reference process** — which process delivers the functional unit?

---

## After getting results

Explain everything in plain English. Never show raw JSON. Always:

1. Show both SVG diagrams (scaled and structure)
2. Call out the **global warming** score first — it's the number students
   understand most easily
3. Explain the **scaling vector** — which processes ran how much?
4. Identify the **hotspot** — which process contributed most to GWP?
5. Connect the result to a real business decision

Example:
> "To produce one cotton t-shirt, the cotton farm only needs to run at 27%
> capacity — but it still accounts for most of the water use (2,125 litres).
> The total climate impact is 0.40 kg of CO₂-equivalent, roughly the same as
> driving a car for 3 kilometres."
