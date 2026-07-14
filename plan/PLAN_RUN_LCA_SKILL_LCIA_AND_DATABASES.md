# Plan: Adding LCIA Methods and Database Support to the run-lca Skill

## Background — What the Skill Can Do Today

The current `run-lca` skill and `lca_analysis.py` script build a complete
product system in openLCA and run a calculation. However the calculation only
returns **raw inventory results** — e.g. "0.1 kg CO₂ per cup". It does not
produce **impact scores** (GWP in kg CO₂-eq, DALYs, species-years, etc.)
because no LCIA method is passed to the `CalculationSetup`.

In other words, the skill currently stops at **Step 2 (Characterisation)** of
the LCIA chain. Steps 3 and 4 (damage modelling, endpoint scores) are not
reached.

---

## Step 0 — Audit the Product Graph Against the olca-schema (DO THIS FIRST)

### Why this must come first

The product graph format was designed from scratch to be readable for students.
That was the right goal — but it was written without systematically checking
every field against the olca-schema (the actual data format openLCA uses
internally). Before extending the product graph with new fields, we need to
confirm that every existing field maps cleanly onto a real olca-schema concept,
and identify any gaps or mismatches.

The olca-schema example files live at:
**https://github.com/GreenDelta/olca-schema/tree/master/examples**

### What the olca-schema looks like

Every object in openLCA is a JSON file with a `@type` field, a UUID `@id`,
and typed fields. Here are the key types relevant to the product graph:

**`Process`** — one production step in the supply chain:
```json
{
  "@type": "Process",
  "@id": "59963026-...",
  "name": "Steel production",
  "processType": "UNIT_PROCESS",
  "location": { "@type": "Location", "name": "Germany" },
  "exchanges": [ ... ]
}
```

**`Exchange`** — one input or output of a process:
```json
{
  "@type": "Exchange",
  "internalId": 1,
  "amount": 1.0,
  "isInput": false,
  "isQuantitativeReference": true,
  "isAvoidedProduct": false,
  "flow": { "@type": "Flow", "name": "Steel" },
  "unit": { "@type": "Unit", "name": "kg" },
  "flowProperty": { "@type": "FlowProperty", "name": "Mass" }
}
```

**`Flow`** — a material, product, energy, or emission that moves between processes:
```json
{
  "@type": "Flow",
  "name": "electricity, high voltage, at grid",
  "flowType": "PRODUCT_FLOW",
  "location": { "name": "Poland" },
  "flowProperties": [
    {
      "isRefFlowProperty": true,
      "flowProperty": { "name": "Energy" }
    }
  ]
}
```
Flow types are: `PRODUCT_FLOW` (technosphere), `ELEMENTARY_FLOW` (biosphere),
or `WASTE_FLOW`.

**`UnitGroup`** — a family of related units with conversion factors:
```json
{
  "@type": "UnitGroup",
  "name": "Units of energy",
  "units": [
    { "name": "MJ",  "isRefUnit": true,  "conversionFactor": 1.0 },
    { "name": "kWh", "isRefUnit": false, "conversionFactor": 3.6 }
  ]
}
```

**`ProductSystem`** — the full supply chain model:
```json
{
  "@type": "ProductSystem",
  "name": "Ingot casting",
  "refProcess": { "name": "Ingot casting" },
  "refExchange": { "internalId": 1 },
  "targetAmount": 1.0,
  "targetUnit": { "name": "kg" },
  "processes": [ ... ],
  "processLinks": [ ... ]
}
```

**`ImpactCategory`** — one impact category with its characterisation factors:
```json
{
  "@type": "ImpactCategory",
  "name": "Depletion of abiotic resources",
  "referenceUnitName": "kg antimony eq.",
  "impactFactors": [
    {
      "value": 1.09e-9,
      "flow": { "name": "Aluminium" },
      "unit": { "name": "kg" }
    }
  ]
}
```

### Mapping: product graph fields → olca-schema

| Product graph field | olca-schema equivalent | Status | Notes |
|---|---|---|---|
| `name` | `Process.name` (ref process) and `ProductSystem.name` | ✓ Clean | — |
| `goal` | `Process.description` or doc field | ✓ Clean | Used for human docs only |
| `functional_unit.description` | `ProductSystem` description | ✓ Clean | — |
| `functional_unit.amount` | `ProductSystem.targetAmount` | ✓ Clean | — |
| `functional_unit.unit` | `ProductSystem.targetUnit` | ✓ Clean | Must match a unit in `units` |
| `units` (dict of symbol → description) | `UnitGroup` + `FlowProperty` pairs | ⚠ Partial | The script creates one UnitGroup per unit symbol. The schema expects a UnitGroup to contain a *family* of related units (e.g. kg, g, t all in one group). Currently each unit gets its own group — this works but is not how real databases organise units. |
| `products` list | `Flow` with `flowType: PRODUCT_FLOW` | ✓ Clean | — |
| `elementary_flows.emissions` | `Flow` with `flowType: ELEMENTARY_FLOW` | ✓ Clean | — |
| `elementary_flows.resources` | `Flow` with `flowType: ELEMENTARY_FLOW` | ✓ Clean | Resources are elementary flows extracted from nature — same type, direction differs |
| `processes[].name` | `Process.name` | ✓ Clean | — |
| `processes[].reference_output` | `Exchange` where `isQuantitativeReference: true`, `isInput: false` | ✓ Clean | — |
| `processes[].inputs` | `Exchange` where `isInput: true`, flow is a `PRODUCT_FLOW` | ✓ Clean | — |
| `processes[].emissions` | `Exchange` where `isInput: false`, flow is an `ELEMENTARY_FLOW` | ✓ Clean | — |
| `processes[].resources` | `Exchange` where `isInput: true`, flow is an `ELEMENTARY_FLOW` | ✓ Clean | Resources are inputs *from* nature — `isInput: true` on an elementary flow |
| `reference_process` | `ProductSystem.refProcess` | ✓ Clean | — |
| `lcia_method` *(not yet in product graph)* | `ImpactMethod.name` — looked up by name at runtime | To add | — |
| `database` *(not yet in product graph)* | No direct schema equivalent — documentary only | To add | Records which data package was loaded; not used by the script |
| `source: background` *(not yet in product graph)* | `Process` looked up by name/ID in the database — a `Ref` rather than a full object | To add | Needed for real-world LCA using background databases |

### Issues found in the audit

**Issue 1 — Unit groups are incorrectly structured**

The product graph has a flat `units` dict:
```yaml
units:
  kWh: Energy
  kg:  Mass
  L:   Volume
```

The script currently creates one `UnitGroup` per symbol. But in the
olca-schema, a `UnitGroup` is a *family* of interconvertible units — for
example, `{kg, g, t, lb}` all belong to one "Units of mass" group with
conversion factors. The current approach creates orphaned single-unit groups
that don't match any real database's unit structure.

This matters because when linking foreground processes to background processes,
unit names must match exactly. If the background database uses a "Units of
mass" group containing `kg` with a standard UUID, and our script creates a
separate "Mass units" group also containing `kg`, openLCA may treat them as
different units.

**Recommended fix**: replace the flat `units` dict with a reference to
standard unit groups. Either hard-code the standard openLCA unit group UUIDs
in the script, or look them up from the database at runtime before creating
any flows.

**Issue 2 — No `flowType` distinction for resources vs emissions**

Both resources and emissions are `ELEMENTARY_FLOW` in the schema. The
difference is directionality: emissions are outputs from the technosphere to
the biosphere (`isInput: false`), resources are inputs from the biosphere to
the technosphere (`isInput: true`). The product graph already captures this
correctly via the `emissions` vs `resources` keys. No change needed — just
confirming the mapping is right.

**Issue 3 — No location field on flows or processes**

Real background databases tag every process and product flow with a location
(country or region). The product graph has no `location` field. For toy models
this does not matter. For real-world LCA it will matter because ecoinvent
process names include the location (e.g. `"market for electricity, low voltage
| DE"`). The `source: background` field (to be added) should handle this by
using the full database process name, which includes the location.

---

## Step 1 — Fix Unit Group Structure

Before adding any new features, fix the way the script creates unit groups so
they match the standard openLCA structure. The script should:

1. Check whether the required unit groups already exist in the database (by
   looking up standard names like "Units of mass", "Units of energy", etc.).
2. If they exist (because a real database has been loaded), use them by
   reference — do not recreate them.
3. If they do not exist (fresh empty database, toy model), create them with
   the correct multi-unit structure including standard conversion factors.

Standard unit groups to support:

| Symbol used in product graph | Standard UnitGroup name | Ref unit | Common others |
|---|---|---|---|
| `kg` | Units of mass | kg | g, t, lb, mg |
| `kWh` | Units of energy | MJ | kWh (×3.6), GJ, Wh |
| `L` | Units of volume | m³ | L (×0.001), mL |
| `m²` | Units of area | m² | cm², ha |
| `m` | Units of length | m | km, cm |
| `item` / `unit` / `cup` | Units of items | Item(s) | — |

---

## Step 2 — Add LCIA Method Support to the Product Graph and Script

### New product graph fields

```yaml
lcia_method: "ReCiPe 2016 Midpoint (H)"   # name of the method in the database
database:    "openlca-lcia-methods-2.1.2"  # documentary — which package was loaded
```

- `lcia_method` is **functional** — the script looks up this method by name
  and passes it to `CalculationSetup`.
- `database` is **documentary** — records which version of which data package
  was loaded, for reproducibility. Does not affect how the script runs.
- Both fields are **optional**. If absent, the script runs inventory-only as
  today (backwards compatible).

### Script changes

```python
# Look up method by name
methods = client.get_descriptors(o.ImpactMethod)
method  = next((m for m in methods if m.name == lcia_method_name), None)
if method is None:
    print(f"Warning: LCIA method '{lcia_method_name}' not found in database.")
    print("Running inventory-only. Load the LCIA methods package to enable impact scores.")

# Pass to calculation
setup = o.CalculationSetup(
    target=o.Ref(id=system_ref.id),
    amount=1.0,
    impact_method=method,   # None is safe — openLCA ignores it
)

# Retrieve impact results (Step 14)
if method:
    for impact in result.get_total_impacts():
        print(impact.impact_category.name,
              impact.amount,
              impact.impact_category.ref_unit)
```

### New Step 14 output in `lca_results.md`

```markdown
## LCIA Results  (ReCiPe 2016 Midpoint H)

| Impact category        | Score    | Unit          |
|------------------------|----------|---------------|
| Climate change         | 6.40     | kg CO₂-eq     |
| Acidification          | 0.025    | kg SO₂-eq     |
| Eutrophication         | 0.0023   | kg PO₄-eq     |
```

---

## Step 3 — Add Background Process Support

Extend the product graph to allow processes to be declared as coming from a
loaded background database rather than defined locally:

```yaml
processes:
  - name: P1 — Cut and sew shirt
    source: local                    # defined in this product graph (default)
    reference_output: { flow: Shirt, amount: 1.0 }
    inputs:
      - { flow: Electricity, amount: 2.5 }

  - name: market for electricity, low voltage | DE
    source: background               # look up in the database by name
```

The script looks up background processes using:
```python
provider = client.find(o.Process, "market for electricity, low voltage | DE")
```
and references them in the product system rather than creating them.

This requires a background process database to be loaded (US LCI, ELCD, etc.)
— see Database Setup below.

---

## Conceptual Background — Flow Types, Unit Process Tables, and the LCI Result

### The flow type taxonomy (from academic LCA teaching)

The standard LCA teaching vocabulary (as used in the *Constructing Inventories* lecture
slides) classifies every input and output of a unit process by a **Type** field:

| Type | Direction | What it is | Example |
|---|---|---|---|
| `Intermediate` | Input | A product flow received from another process **inside** the same foreground model | Apple arriving at Transport from Production |
| `Technosphere` | Input | A product flow bought from the **background economy** — not modelled locally | Electricity from the grid, Fertilizer, Diesel |
| `Resource` | Input | A flow extracted directly from **nature** | Water drawn from a river |
| `Product` | Output | The main product of a process (reference output) | Apple leaving Production |
| `Co-product` | Output | A second joint product of the same process | Pear leaving Production alongside Apple |
| `Emission` | Output | A release to the environment | CO₂ to air, CH₄ to air |
| `Waste treatment` | Output | Waste handed off to a downstream waste-handling process | Waste cardboard leaving Transport |

**Key insight:** the unit process data tables shown in teaching slides (one table per process,
with Name / Amount / Units / Type / Comments columns) are **not** the LCI result.
They are the raw input data — equivalent to our product graph. The LCI result is produced
only after solving the technology matrix (A × s = f) and multiplying by the intervention
matrix (g = B × s). The LCI result contains only elementary flows (Emissions + Resources);
all Intermediate and Technosphere flows cancel out algebraically and disappear.

### How our product graph maps to these types today

| PDF Type | Our product graph field | Status |
|---|---|---|
| `Intermediate` input | `inputs` (when a matching `reference_output` exists in the product graph) | ✓ Supported — draws an arrow between process boxes |
| `Technosphere` input | `inputs` (when no matching `reference_output` exists) | ⚠ Partially supported — number recorded but no arrow drawn, no database lookup |
| `Resource` input | `resources` | ✓ Supported |
| `Product` output | `reference_output` | ✓ Supported (one per process only) |
| `Co-product` output | — | ✗ Not supported |
| `Emission` output | `emissions` | ✓ Supported |
| `Waste treatment` output | — | ✗ Not supported |

### Why our current product graphs have no true Technosphere inputs

All existing product graphs (coffee, cotton shirt, hand dryer, light bulb) explicitly model
every upstream step — electricity generation is always its own process box. This means
every entry in `inputs` has a matching `reference_output` somewhere in the same product graph and therefore counts as **Intermediate**, not Technosphere. No inputs are silently
dropped from the diagram.

This is a deliberate pedagogical choice: making every step visible helps students
understand the full supply chain. It is also why the diagram always draws correctly —
every arrow has both a source and a destination within the product graph.

The Technosphere input distinction only becomes meaningful when background database
support is added (see Step 3 below).

---

## How `create_product_system` Auto-Linking Works

### What the API does

The `olca-ipc` Python client provides a method called `create_product_system`:

```python
system_ref = client.create_product_system(
    process_ref,
    config=o.LinkingConfig(
        prefer_unit_processes=False,
        provider_linking=o.ProviderLinking.PREFER_DEFAULTS,
    )
)
```

This is openLCA's auto-linking engine. When called, it:

1. Takes the reference (foreground) process as the starting point.
2. Scans every input of every foreground process for flows that have no supplier
   already defined within the foreground model.
3. Searches the entire database for any process whose reference output matches
   that flow (by flow name and unit).
4. If a match is found, links the background process into the product system.
5. Repeats recursively — the background process's own inputs are also searched,
   pulling in further upstream processes until all inputs are satisfied or no
   more matches exist.

The result is a fully-linked `ProductSystem` object containing both the foreground
processes (from the product graph) and any background processes found in the database.

### The scaling vector covers all processes

The technology matrix A and the subsequent scaling vector s cover **every** process
in the product system — foreground and background alike. If ecoinvent has 20,000
processes and auto-linking pulls in 5,000 of them to satisfy the apple supply chain,
then A is a 5,000×5,000 matrix and s has 5,000 entries. openLCA handles this
internally; the student only sees the final aggregated LCI and LCIA results.

### What happens when no background database is loaded

If `create_product_system` finds no supplier for a Technosphere input (because no
background database is loaded), that input is left **unlinked**. The product system
is incomplete. The calculation still runs but the results are partial — the
upstream emissions from electricity, fertilizer, diesel etc. are missing. The script
should warn the user in this case.

### The `get_providers` method — looking before linking

Before auto-linking, you can ask openLCA what is available:

```python
# Find every process in the database that produces a given flow
flow_ref = o.Ref(name="Electricity, low voltage")
providers = client.get_providers(flow_ref)
for p in providers:
    print(p.process.name)
    # e.g. "market for electricity, low voltage | DE"
    #      "electricity production, wind, <1MW turbine, onshore | DE"
```

This is useful for verifying that a background database is loaded and for letting
the student choose which provider to use when multiple options exist.

### Example: apple supply chain with background database inputs

The apple supply chain from the *Constructing Inventories* slides has 4 foreground
processes (Production, Transport, Use, Disposal). Electricity, Fertilizer, Cardboard,
Facility, and Diesel are Technosphere inputs to Production — they are NOT modelled
as explicit process boxes in the product graph. The product graph would look like:

```yaml
processes:
  - name: Production
    reference_output: { flow: Apple, amount: 500000, unit: kg }
    inputs:
      - { flow: Electricity, amount: 100000, unit: kWh }  # Technosphere — no local process
      - { flow: Fertilizer,  amount: 500000, unit: kg  }  # Technosphere — no local process
      - { flow: Diesel,      amount: 30000,  unit: kg  }  # Technosphere — no local process
    resources:
      - { flow: Water, amount: 100000, unit: L }
    emissions:
      - { flow: CO2 to air, amount: 100000, unit: kg }

  - name: Transport
    reference_output: { flow: Apple, amount: 5000, unit: kg }
    inputs:
      - { flow: Apple, amount: 5000, unit: kg }            # Intermediate — from Production

  - name: Use
    reference_output: { flow: Waste, amount: 0.1, unit: kg }
    inputs:
      - { flow: Apple, amount: 1.0, unit: kg }             # Intermediate — from Transport

  - name: Disposal
    reference_output: { flow: Disposed waste, amount: 0.1, unit: kg }
    inputs:
      - { flow: Waste, amount: 0.1, unit: kg }             # Intermediate — from Use
```

With a background database loaded, `create_product_system` would automatically
find and link processes for Electricity, Fertilizer, and Diesel. Without one,
those inputs would be unlinked and the results would be incomplete.

---

## Database Setup — How to Get Free LCIA Methods and Process Data

### The constraint

The gdt-server API has **no bulk import endpoint**. You cannot import a zip
file via Python. The only write operation is `PUT`, which adds one entity at a
time. To load a full database you need the **openLCA desktop app** at least
once.

### Step-by-step: loading the free LCIA methods package

1. Download the **openLCA desktop app** from openlca.org (free).
2. Download the **openLCA LCIA methods pack** from nexus.openlca.org (free —
   43 methods including ReCiPe 2016, CML-IA, TRACI, EF 3.0). Do not unzip it.
3. In the desktop app: File → Import → Others → Linked Data (JSON-LD) →
   select the ZIP → Overwrite all → Finish. Takes a few minutes.
4. Point the gdt-server at the same database folder. Methods are now available
   via the API.

### Free background process databases

| Database | Coverage | Source | Format |
|---|---|---|---|
| **US LCI** | ~1,000 US processes — energy, transport, materials | lcacommons.gov | JSON-LD (free) |
| **ELCD** | ~500 European processes — energy, chemicals, transport | EU JRC | ILCD (free) |
| **Agribalyse** | ~2,500 French food and agriculture processes | ADEME | openLCA format (free) |

Import any of these into the same database alongside the LCIA methods package.

---

## Summary of Work Items

| # | Item | Status |
|---|---|---|
| 0 | Audit product graph fields against olca-schema *(this document)* | **Done** |
| 1 | Fix unit group structure in `lca_analysis.py` to match standard openLCA groups | Not started |
| 2 | Add `lcia_method` and `database` fields to product graph format | Not started |
| 3 | Update `lca_analysis.py` to look up and apply LCIA method | Not started |
| 4 | Add LCIA results table (Step 14) to script output and `lca_results.md` | Not started |
| 5 | Document database setup and new fields in `SKILL.md` | Not started |
| 6 | Load LCIA methods package into the Codespace database (one-time manual step) | Not started |
| 7 | Test end-to-end: coffee product graph with ReCiPe 2016, confirm LCIA scores | Not started |
| 8 | Add `source: background` field to product graph and script lookup | Not started |
| 9 | Load a background process database (US LCI or ELCD) | Not started |
| 10 | Test a product graph that mixes local and background processes | Not started |

Items 1–5 are pure code — no database setup needed.
Item 6 requires the openLCA desktop app once.
Items 8–10 depend on item 6 and a loaded background database.

---

## Suggested Order of Work

1. **Item 0** *(done)* — audit complete, issues documented above.
2. **Item 1** — fix unit groups. Low risk, no user-visible change, unblocks correct background linking later.
3. **Items 2–4** — add LCIA method support to product graph and script. Test with coffee; expect empty impact results until item 6 is done — handle gracefully.
4. **Item 6** — load LCIA methods package via desktop app (one-time manual step).
5. **Item 7** — test end-to-end with ReCiPe 2016.
6. **Item 5** — update skill documentation.
7. **Items 8–10** — background process support, once a process database is loaded.
