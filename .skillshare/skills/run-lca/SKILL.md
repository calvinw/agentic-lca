---
name: run-lca
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

The standard workflow produces three files:

| File | Purpose |
|---|---|
| `recipe_card.md` | YAML spec: defines the system (edit this) |
| `lca_results.md` | Generated report: matrices, scaling vector, results |
| `product_graph.png` | Visual diagram of the supply chain |

Run the analysis with:
```bash
python3 lca_scripts/lca_analysis.py lca_analysis/<name>/recipe_card.md
```

---

## Prerequisites

The openLCA `gdt-server` must be running on port 8080 (starts automatically
via `postStartCommand`). Verify:

```bash
curl -s http://localhost:8080/api/version
```

If it is not running:
```bash
bash .devcontainer/start_olca.sh
```

Python packages required:
```bash
pip install olca-ipc olca-schema pyyaml numpy --break-system-packages
```

**Critical**: always use `RestClient`, NOT `ipc.Client`. The gdt-server speaks
REST, not JSON-RPC:

```python
from olca_ipc.rest import RestClient   # ← correct for gdt-server
import olca_schema as o

client = RestClient("http://localhost:8080/")
```

---

## recipe_card.md format

`recipe_card.md` is a markdown file whose YAML frontmatter fully specifies the
LCA model. The markdown body is free text (ignored by the runner).

```yaml
---
name: <human name for this analysis>
goal: <one sentence describing the purpose>

functional_unit:
  description: <what is being analysed, in plain English>
  amount: 1.0
  unit: <unit symbol, must appear in 'units' below>

# Unit symbols used anywhere in this file.
# Each entry creates a UnitGroup + FlowProperty in openLCA.
# key   = symbol referenced in flows and processes
# value = human-readable description
units:
  cup: Cup count
  L:   Volume
  kWh: Energy
  kg:  Mass

# Intermediate product flows (technosphere).
# These move between processes inside the system.
products:
  - { name: <flow name>, unit: <symbol> }

# Elementary flows crossing the biosphere boundary.
elementary_flows:
  emissions:
    - { name: <flow name>, unit: <symbol> }

# Unit processes.
# reference_output  → the product this process "sells" (diagonal of A)
# inputs            → product flows consumed (negative off-diagonal of A)
# emissions         → biosphere outputs (entries of B)
processes:
  - name: <process name>
    reference_output: { flow: <product name>, amount: <number> }
    inputs:
      - { flow: <product name>, amount: <number> }
    emissions:
      - { flow: <emission name>, amount: <number> }

# Must match one of the process names above.
reference_process: <process name that delivers the functional unit>
---
```

### Minimal working example (coffee)

```yaml
---
name: Coffee LCA — one cup
goal: Calculate CO₂ for one cup of coffee
functional_unit:
  description: One cup of coffee
  amount: 1.0
  unit: cup

units:
  cup: Cup count
  L:   Volume
  kWh: Energy
  kg:  Mass

products:
  - { name: Coffee,        unit: cup }
  - { name: Boiled water,  unit: L   }
  - { name: Electricity,   unit: kWh }

elementary_flows:
  emissions:
    - { name: CO2 to air, unit: kg }

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
      - { flow: CO2 to air,   amount: 1.0 }

reference_process: P1 — Make coffee
---
```

---

## What the runner prints (13 steps)

`lca_analysis.py` mirrors the LCA methodology exactly:

| Step | What |
|---|---|
| 1 | Goal and scope — functional unit, reference flow vector f |
| 2 | Product graph — processes, products, emissions summary |
| 3 | Creates unit groups and flow properties in openLCA |
| 4 | Creates product flows (technosphere) |
| 5 | Creates elementary flows (biosphere) |
| 6 | Creates unit processes with exchanges |
| 7 | Builds product system (auto-link by flow matching) |
| 8 | Displays technology matrix **A** |
| 9 | Solves **s = A⁻¹ · f** and shows scaling vector with bar chart |
| 10 | Displays intervention matrix **B** |
| 11 | Submits calculation to gdt-server, waits for result |
| 12 | Compares B·s (numpy) vs openLCA result — shows ✓ MATCH or ✗ DIFF |
| 13 | Contribution analysis — which process drives the impact |

Output is written to `lca_results.md` with all matrices and results as
markdown tables.

---

## What to specify when setting up a new analysis

Ask the user for:

1. **Name and goal** — what system, why are they studying it?

2. **Functional unit** — what, how much, which unit?
   - Never silently default geography for real ecoinvent processes.

3. **Units** — list every unit symbol used (cup, kg, kWh, L, m², MJ, …).

4. **Products** (technosphere flows) — one entry per intermediate good or
   service that flows between processes.

5. **Emissions** (biosphere flows) — CO₂, CH₄, NOₓ, freshwater, etc.
   For a real database, these must match ecoinvent elementary flow names exactly.

6. **Processes** — for each process:
   - What is the reference output (the "product" it sells)?
   - What does it consume from other processes (inputs)?
   - What does it emit to nature (emissions)?

7. **Reference process** — which process delivers the functional unit?
   This is the root of the product system.

---

## Low-level API (for custom scripts)

```python
from olca_ipc.rest import RestClient
import olca_schema as o

client = RestClient("http://localhost:8080/")

# Create entities
ug   = o.new_unit_group("Mass units", "kg")
fp   = o.new_flow_property("Mass", ug)
flow = o.new_product("My product", fp)
client.put_all(ug, fp, flow)

# Build product system (auto-links processes)
system_ref = client.create_product_system(ref_process)

# Calculate
setup  = o.CalculationSetup(target=o.Ref(id=system_ref.id), amount=1.0)
result = client.calculate(setup)
result.wait_until_ready()

# Inventory results
for f in result.get_total_flows():
    print(f.envi_flow.flow.name, f.amount)

# LCIA results (requires an impact method in the database)
for r in result.get_total_impacts():
    print(r.impact_category.name, r.amount, r.impact_category.ref_unit)

result.dispose()  # always dispose
```

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `Connection refused` | gdt-server not running | `bash .devcontainer/start_olca.sh` |
| `AttributeError: module 'olca_ipc' has no attribute 'RestClient'` | Using wrong import | `from olca_ipc.rest import RestClient` |
| `create_product_system returned None` | Process exchanges not linked | Check flow names match exactly between processes |
| `get_total_impacts()` empty | No LCIA method in database | Load a method (ReCiPe, CML, etc.) via ecoinvent import first |
| `wait_until_ready()` hangs | Solver error | `docker logs olca-server` for stack trace |
