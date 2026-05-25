# Paper Cup LCA — openLCA Python Scripts

A minimal example of building and calculating an LCA model programmatically
using the openLCA IPC API. Mirrors the paper cup example from the LCA walkthrough.

## Files

| File | Purpose |
|---|---|
| `setup_olca.sh` | Pull and start the gdt-server Docker container (standalone use) |
| `start_olca.sh` | Same, but called automatically by devcontainer on Codespaces start |
| `devcontainer_snippet.json` | Additions to merge into your `.devcontainer/devcontainer.json` |
| `01_build_model.py` | Build all flows, processes, and the product system in openLCA |
| `02_calculate.py` | Run the inventory calculation and print GWP + water results |

## Workflow

### In Codespaces (recommended)

1. Merge `devcontainer_snippet.json` into your `.devcontainer/devcontainer.json`
2. Copy `start_olca.sh` into `.devcontainer/`
3. Rebuild the container — the gdt-server starts automatically on port 8080

Then run:
```bash
pip install olca-ipc olca-schema
python 01_build_model.py
python 02_calculate.py
```

### Standalone (local Docker)

```bash
bash setup_olca.sh          # start the server
pip install olca-ipc olca-schema
python 01_build_model.py    # build the model
python 02_calculate.py      # run the calculation
```

## What the scripts do

### 01_build_model.py

Creates the full product system from scratch using the three standard LCI categories:

**Processes** (intermediate product flows between unit processes)
- Wood pulp, PE resin, electricity, heat/steam, transport, landfill service

**Inputs from nature** (elementary flows drawn from the environment)
- Freshwater (pulping), freshwater (cooling), land use, crude oil

**Outputs to nature** (elementary flows emitted to the environment)
- CO₂ to air, CH₄ to air, NOₓ to air, BOD to water, solid waste to land

Five unit processes are created and linked:
1. Forestry & pulp production
2. Cup manufacturing
3. Distribution (truck transport)
4. Use — one beverage served  ← functional unit reference
5. Landfill disposal

### 02_calculate.py

- Loads the product system ID from `model_ids.json`
- Runs `SIMPLE_CALCULATION` via `client.calculate()`
- Retrieves `get_total_flows()` and splits into Inputs / Outputs
- Applies GWP100 characterization factors to outputs
- Prints inventory table + GWP + freshwater totals

## Extending this example

To add the PS foam cup comparison, create a second set of processes
in `01_build_model.py` with PS-specific inventory values, then run
`02_calculate.py` for both systems and compare totals.

To use a real background database (ecoinvent), link your processes to
background processes from the database instead of hardcoding elementary flows.
The `client.get(o.Process, name="...")` call lets you look up existing processes.
