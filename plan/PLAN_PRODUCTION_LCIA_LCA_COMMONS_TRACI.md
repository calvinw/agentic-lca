# Plan: Production-Level LCIA with LCA Commons + TRACI 2.2 (Ecoinvent-Ready)

## Background — What the System Does Today

`lca_analysis.py` builds a complete product system in openLCA from a product graph,
solves the technology matrix A, computes the scaling vector s = A⁻¹·f, and
produces the LCI result B·s. It then does one of two things:

- If the product graph has an `lcia:` block with hand-typed `characterization_factors`,
  it multiplies B·s by those CFs in Python and reports impact scores.
- If there is no `lcia:` block, it reports only raw CO₂.

Neither path uses openLCA's own LCIA engine. No real LCIA method is attached to
`CalculationSetup`. The database (`paper_cup_lca`) is empty — every flow, process,
and unit is created from scratch on each run with fresh UUIDs.

This plan upgrades to a production-level system while keeping the matrix pedagogy
fully intact.

---

## Goal

1. Replace the empty database with **LCA Commons 2025.1** (free US government data)
2. Use **TRACI 2.2** from that database as the LCIA method (what Schiros uses)
3. Update product graphs to use **FEDEFL flow names** so TRACI can characterize them
4. Wire `CalculationSetup` to pass the method and call `get_total_impacts()`
5. Structure everything so switching to **ecoinvent** later is a one-line change

The matrix steps (A, B, s, B·s) stay exactly as they are — students still see
every calculation. What changes is that Step 7 (LCIA) uses the real engine and
real published characterization factors instead of hand-typed estimates.

---

## Why LCA Commons + TRACI 2.2

**LCA Commons 2025.1** (nexus.openlca.org, free):
- Built and maintained by US government agencies (USDA, NREL, EPA)
- Uses FEDEFL (Federal Elementary Flow List) — the same flow standard TRACI is built on
- TRACI 2.2 is already embedded — no separate methods download needed
- Includes USLCI background processes (US electricity, transport, materials)

**TRACI 2.2** covers:
- Global Warming Potential (kg CO₂-eq)
- Acidification (kg SO₂-eq)
- Eutrophication, freshwater (kg N-eq)
- Smog Formation (kg O₃-eq)
- Human Health — Cancer (CTUh)
- Human Health — Non-cancer (CTUh)
- Ecotoxicity (CTUe)
- Ozone Depletion (kg CFC-11-eq)
- Fossil Fuel Depletion (MJ surplus)

**Ecoinvent migration path:** The EPA publishes an official FEDEFL↔ecoinvent flow
mapping (https://github.com/USEPA/fedelemflowlist). When ecoinvent is loaded,
change `-db lca_methods` to `-db ecoinvent` in the startup script. Product graphs
need no changes.

---

## Step 0 — One-Time Database Setup (instructor/admin, not students)

### 0a. Download LCA Commons 2025.1

1. Create a free account at https://nexus.openlca.org
2. Search for "LCA Commons" and download the `.zolca` file (~200 MB)
3. Place it in `$HOME/olca-data/` on the Codespace machine

### 0b. Import into the running database

First try via the gdt-server REST API (automated):
```bash
curl -X POST http://localhost:8080/api/import \
  -H "Content-Type: application/octet-stream" \
  --data-binary @"$HOME/olca-data/lca_methods_2025.1.zolca"
```

If that endpoint is not exposed, use the openLCA desktop app:
- File → Import → Linked Data (JSON-LD) → select the .zolca file

### 0c. Update the startup scripts

In `start_olca.sh` and `setup_olca.sh`, change line 41:
```bash
# Before:
-db paper_cup_lca

# After:
-db lca_methods
```

### 0d. (Future) Ecoinvent startup script

Create `start_olca_ecoinvent.sh` as a copy of `start_olca.sh` with:
```bash
-db ecoinvent
```
Students use `start_olca.sh` (LCA Commons, free). Researchers use
`start_olca_ecoinvent.sh` (ecoinvent, licensed).

---

## Step 1 — Update Product Graphs to Use FEDEFL Flow Names

FEDEFL names are the bridge between our foreground processes and TRACI 2.2.
The FEDEFL name for CO₂ is simply `Carbon dioxide`; compartment is `air`.

### FEDEFL name reference for textile/food LCA

| Current name in product graphs | FEDEFL name      | Compartment |
|------------------------------|------------------|-------------|
| CO2 to air                   | Carbon dioxide   | air         |
| CH4 to air                   | Methane          | air         |
| NOx to air                   | Nitrogen oxides  | air         |
| SOx to air / SO2 to air      | Sulfur dioxide   | air         |
| Water                        | Water            | water       |
| Phosphate                    | Phosphorus       | water       |

### New elementary flow format in product graphs

```yaml
elementary_flows:
  emissions:
    - { name: Carbon dioxide,  compartment: air,   unit: kg }
    - { name: Nitrogen oxides, compartment: air,   unit: kg }
    - { name: Sulfur dioxide,  compartment: air,   unit: kg }
    - { name: Methane,         compartment: air,   unit: kg }
  resources:
    - { name: Water,           compartment: water, unit: L  }
```

### New LCIA block in product graphs (no hand-typed CFs)

```yaml
lcia:
  method_name: "TRACI 2.2"
```

That is all. No characterization factors to type. The engine provides them.

### Product graphs to update

- `lca_analysis/cotton_shirt/product_graph.yaml`
  - Rename `CO2 to air` → `Carbon dioxide` (compartment: air)
  - Add `Nitrogen oxides` and `Sulfur dioxide` to P5 (Generate electricity)
    with realistic coal-grid values: NOₓ ≈ 0.0009 kg/kWh, SOₓ ≈ 0.0006 kg/kWh
  - Add `lcia: { method_name: "TRACI 2.2" }`

- `lca_analysis/levi_jeans/product_graph.yaml` and all 7 variants
  - Same pattern as cotton shirt

- `skills_references/wool_yarn/product_graph.yaml`
  - Rename `CO2 to air` → `Carbon dioxide`, `CH4 to air` → `Methane`
  - Remove hand-typed `characterization_factors` dict
  - Add `lcia: { method_name: "TRACI 2.2" }`

- `skills_references/cotton_fiber/product_graph.yaml`
- `skills_references/polyester_tshirt/product_graph.yaml`
- `lca_analysis/coffee/product_graph.yaml`
- `lca_analysis/paper_cup/product_graph.yaml`
- All other product graphs with elementary flows

---

## Step 2 — Code Changes to `lca_scripts/lca_analysis.py`

### 2a. New `resolve_flow()` helper

Add just before `build_model()`. Replaces `o.new_elementary_flow()` for biosphere
flows. Looks up the flow in the loaded database by FEDEFL name first; creates new
only as a fallback (for use before LCA Commons is loaded).

```python
def resolve_flow(client: RestClient, name: str, flow_property) -> o.Flow:
    """Use existing DB flow if name matches; otherwise create new."""
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
```

### 2b. Update Step 5 in `build_model()`

Replace both `o.new_elementary_flow()` loops with `resolve_flow()` calls:

```python
step(5, "Elementary Flows  (biosphere — emissions / extractions)")
for ef in spec.get("elementary_flows", {}).get("emissions", []):
    flow = resolve_flow(client, ef["name"], reg[ef["unit"]])
    reg[ef["name"]] = flow
    print(f"    {ef['name']}  [{ef['unit']}]  → emission to nature")
for ef in spec.get("elementary_flows", {}).get("resources", []):
    flow = resolve_flow(client, ef["name"], reg[ef["unit"]])
    reg[ef["name"]] = flow
    print(f"    {ef['name']}  [{ef['unit']}]  ← extraction from nature")
```

### 2c. New `get_impact_method_ref()` helper

Add after `build_model()`:

```python
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
```

### 2d. Update `CalculationSetup` in `main()`

Replace the existing CalculationSetup block (lines ~497-509):

```python
step(11, "LCA Calculation via openLCA gdt-server")

# Look up LCIA method if product graph requests one
method_ref  = None
lcia_spec   = spec.get("lcia", {})
method_name = lcia_spec.get("method_name", "")
if method_name:
    method_ref = get_impact_method_ref(client, method_name)

print(f"\n  Submitting product system {system_ref.id[:8]}…")
setup = o.CalculationSetup(
    target=o.Ref(id=system_ref.id),
    amount=fu["amount"],
    impact_method=method_ref          # None → inventory only (unchanged behaviour)
)
result = client.calculate(setup)
result.wait_until_ready()
print(f"  Calculation complete.")

# Collect flow totals (always)
flows = result.get_total_flows()
olca_outputs = {f.envi_flow.flow.name: f.amount
                for f in flows if not f.envi_flow.is_input}
olca_inputs  = {f.envi_flow.flow.name: f.amount
                for f in flows if f.envi_flow.is_input}

# Collect impact totals (only if a method was found)
olca_impacts = {}   # { category_name: (amount, unit) }
if method_ref:
    for iv in result.get_total_impacts():
        olca_impacts[iv.impact_category.name] = (iv.amount, iv.ref_unit or "")

result.dispose()
```

### 2e. Update Step 14 in `main()`

Replace the existing hand-multiplication block with:

```python
if olca_impacts:
    step(14, f"LCIA Results  ({method_name})")
    print()
    for cat_name, (val, unit) in olca_impacts.items():
        print(f"  {cat_name:<45} {val:>12.6f}  {unit}")
elif lcia_spec.get("impact_categories"):
    # Legacy fallback: hand-typed CFs (existing code block — keep as-is)
    ...
```

### 2f. Pass `olca_impacts` and `method_name` to `write_results_md()`

Update function signature:
```python
def write_results_md(spec, A, B, s, Bs, olca_outputs, olca_inputs,
                     proc_names, prod_names, em_names, res_names,
                     system_id, olca_impacts=None, method_name=""):
```

In the Step 7 section of `write_results_md()`, add engine-result path:

```python
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
elif lcia_spec.get("impact_categories"):
    # existing hand-typed CF table (keep as-is for legacy product graphs)
    ...
```

In the Summary section, replace the single CO₂ line with all TRACI categories:

```python
if olca_impacts:
    ln(f"**LCIA Method:** {method_name}")
    ln()
    for cat_name, (val, unit) in olca_impacts.items():
        ln(f"> **{cat_name}: {val:.6f} {unit}** "
           f"per {fu['amount']} {fu['unit']} of {fu['description']}")
```

---

## Step 3 — New `setup_database.sh` Script

Create `setup_database.sh` in the project root:

```bash
#!/usr/bin/env bash
# setup_database.sh
# One-time setup: imports LCA Commons 2025.1 into the openLCA database.
# Run once per Codespace after start_olca.sh has started the server.
#
# Before running:
#   1. Download LCA Commons 2025.1 .zolca from https://nexus.openlca.org
#   2. Place the file in $HOME/olca-data/
#   3. Update ZOLCA_FILE below with the exact filename

ZOLCA_FILE="$HOME/olca-data/lca_methods_2025.1.zolca"

if [ ! -f "$ZOLCA_FILE" ]; then
    echo "ERROR: $ZOLCA_FILE not found."
    echo "Download LCA Commons 2025.1 from https://nexus.openlca.org (free account required)"
    exit 1
fi

echo "[setup] Importing LCA Commons into openLCA database..."
HTTP_STATUS=$(curl -s -o /tmp/import_response.json -w "%{http_code}" \
    -X POST http://localhost:8080/api/import \
    -H "Content-Type: application/octet-stream" \
    --data-binary @"$ZOLCA_FILE")

if [ "$HTTP_STATUS" = "200" ]; then
    echo "[setup] Import successful."
    echo "[setup] Update start_olca.sh line 41: change '-db paper_cup_lca' to '-db lca_methods'"
    echo "[setup] Then restart: bash stop_olca.sh && bash start_olca.sh"
else
    echo "[setup] API import returned HTTP $HTTP_STATUS"
    echo "[setup] If /api/import is not available, import manually:"
    echo "        openLCA desktop → File → Import → Linked Data → $ZOLCA_FILE"
    cat /tmp/import_response.json 2>/dev/null
fi
```

---

## Step 4 — New `start_olca_ecoinvent.sh` Script

Create `start_olca_ecoinvent.sh` as a copy of `start_olca.sh` with one change:

```bash
# Line 41 — only difference from start_olca.sh:
-db ecoinvent
```

When the ecoinvent license is ready:
1. Import ecoinvent 3.12 (cut-off) .zolca into `$HOME/olca-data/databases/`
2. Run `bash start_olca_ecoinvent.sh` instead of `bash start_olca.sh`
3. Product graphs stay identical — `resolve_flow()` finds ecoinvent flows by FEDEFL name
4. `get_impact_method_ref()` finds EF 3.1 or TRACI in ecoinvent's embedded methods

---

## Files to Create / Modify

| File | Action | Notes |
|---|---|---|
| `lca_scripts/lca_analysis.py` | Modify | Add `resolve_flow()`, `get_impact_method_ref()`, update CalculationSetup, Step 14, write_results_md |
| `start_olca.sh` | Modify | Change `-db paper_cup_lca` → `-db lca_methods` (do after import) |
| `setup_olca.sh` | Modify | Same db name change |
| `setup_database.sh` | Create | One-time LCA Commons import script |
| `start_olca_ecoinvent.sh` | Create | Future ecoinvent startup script |
| `lca_analysis/cotton_shirt/product_graph.yaml` | Modify | FEDEFL names + NOₓ/SOₓ + `method_name: "TRACI 2.2"` |
| `lca_analysis/levi_jeans/product_graph.yaml` | Modify | Same pattern |
| `lca_analysis/levi_jeans_*/product_graph.yaml` | Modify | Same pattern (7 variant product graphs) |
| `skills_references/wool_yarn/product_graph.yaml` | Modify | FEDEFL names, remove hand-typed CFs, add method_name |
| `skills_references/cotton_fiber/product_graph.yaml` | Modify | Same pattern |
| `skills_references/polyester_tshirt/product_graph.yaml` | Modify | Same pattern |
| `lca_analysis/coffee/product_graph.yaml` | Modify | FEDEFL names + method_name |
| `lca_analysis/paper_cup/product_graph.yaml` | Modify | Same pattern |

---

## Verification Sequence

Run these in order after setup:

```bash
# 1. Check server is running with LCA Commons
curl -s http://localhost:8080/api/version

# 2. Check TRACI 2.2 is present in the database
curl -s http://localhost:8080/api/descriptors/ImpactMethod | python3 -m json.tool | grep -i traci

# 3. Run cotton shirt — watch for resolve_flow and method lookup in console
python3 lca_scripts/lca_analysis.py lca_analysis/cotton_shirt/product_graph.yaml

# Expected console output:
#   ✓ resolved 'Carbon dioxide' → DB flow (xxxxxxxx)
#   ✓ resolved 'Nitrogen oxides' → DB flow (xxxxxxxx)
#   ✓ found impact method in DB: TRACI 2.2
#
# Expected in lca_results.md Step 7:
#   | Global Warming Potential | 2.320000 | kg CO₂-eq |
#   | Acidification            | 0.004100 | kg SO₂-eq |
#   | Eutrophication           | ...      | kg N-eq   |

# 4. Confirm GWP matches the old CO2 number (should be ~2.32 kg CO₂-eq)
# 5. Run levi_jeans base vs organic — confirm burden-shift visible across categories
python3 lca_scripts/lca_analysis.py lca_analysis/levi_jeans/product_graph.yaml
python3 lca_scripts/lca_analysis.py lca_analysis/levi_jeans_organic/product_graph.yaml
```

---

## Pedagogical Notes for Claude Code in the Codespace

When running this for students, explain:

- **`resolve_flow()`** is like looking up a word in a dictionary. If "Carbon dioxide"
  is already in the database dictionary with an official ID number, we use that.
  If it is not there yet, we write a new entry. The whole point is that TRACI knows
  the official ID number, so it can find our flow and apply the right CF.

- **FEDEFL names** are like ISBN numbers for elementary flows — every copy of
  "Carbon dioxide" in every database has the same identifier, so TRACI always
  knows what to multiply by, regardless of which database is loaded.

- **The matrix steps A, B, s, B·s are unchanged.** LCIA is still Step 7, still
  shows a table. The difference is the table now comes from a published,
  peer-reviewed method rather than numbers typed by hand.

- **When ecoinvent is connected:** tell students "we have switched to a more
  detailed dictionary — the product graph is the same, but the background
  measurements are now from a professionally-measured industrial database."

---

## References

- LCA Commons download: https://nexus.openlca.org/databases
- FEDEFL GitHub (flow list + ecoinvent mapping): https://github.com/USEPA/fedelemflowlist
- FEDEFL in openLCA (import guide): https://github.com/FLCAC-admin/fedelemflowlist/wiki/FEDEFL-in-openLCA
- TRACI 2.2 documentation PDF: https://nexus.openlca.org/ws/files/36003
- gdt-server REST API: https://greendelta.github.io/openLCA-ApiDoc/
- olca-ipc Python docs: https://greendelta.github.io/olca-ipc.py/olca/ipc.html
- Ecoinvent in openLCA: https://www.openlca.org/ecoinvent-3-12-available-for-openlca/
