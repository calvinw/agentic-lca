# Plan: Production LCIA with ReCiPe 2016 as an Alternative to TRACI 2.2

## What is ReCiPe?

**ReCiPe 2016** is a widely used life cycle impact assessment method developed
jointly by RIVM (Netherlands National Institute for Public Health), Radboud
University, and PRé Consultants. The name is a play on the word "recipe"
because it combines several earlier European methods (CML, Eco-indicator 99)
into one.

ReCiPe is the most common LCIA method used in European and global LCA studies.
TRACI 2.2 (the method currently used in this project) is the US EPA's method
and is calibrated for North American conditions. For fashion and textile studies
that span global supply chains — farms in India, mills in China, factories in
Bangladesh — ReCiPe is often a better fit because its characterization factors
are derived from global rather than US-only models.

---

## ReCiPe vs TRACI 2.2 — Key Differences

| Feature | TRACI 2.2 | ReCiPe 2016 |
|---|---|---|
| Origin | US EPA | Dutch / European consortium |
| Geographic scope | North America | Global |
| Number of midpoint categories | 9 | 18 |
| Endpoint aggregation | No | Yes (3 damage areas) |
| Common in fashion LCA? | Yes (US studies) | Yes (European + global) |
| Available in LCA Commons? | Yes (built in) | No — not included |
| Available via LCIA methods pack? | Yes | Yes (free download) |
| Available in ecoinvent? | Yes | Yes (built in) |

### ReCiPe's two levels

ReCiPe operates at two levels that work together:

**Midpoint (problem-oriented)** — 18 categories, similar in concept to
TRACI's categories. Each midpoint score is in its own unit and measures a
specific type of environmental stress (e.g. global warming in kg CO₂ eq,
freshwater use in m³, land use in m² per year).

**Endpoint (damage-oriented)** — 3 aggregated scores that translate midpoint
impacts into damage to three "areas of protection":
- Human Health (DALY — disability-adjusted life years)
- Ecosystems (species·year — local species loss over time)
- Resource Scarcity (USD2013 — extra cost of future resource extraction)

For teaching, **midpoints are easier to explain** — each one corresponds to
a recognisable environmental problem. Endpoints are more powerful for
decision-making because they reduce 18 numbers to 3, but the aggregation
involves value judgements that are harder to teach at introductory level.

### ReCiPe cultural perspectives

ReCiPe comes in three versions reflecting different assumptions about
time horizon and risk:

| Perspective | Abbreviation | Time horizon | Use when |
|---|---|---|---|
| Individualist | (I) | Short (20 yr) | Optimistic / near-term |
| Hierarchist | (H) | Medium (100 yr) | Scientific consensus — **recommended default** |
| Egalitarian | (E) | Long (500 yr) | Precautionary / worst-case |

**Use ReCiPe 2016 Midpoint (H)** as the default. The "(H)" stands for
Hierarchist — it uses 100-year time horizons consistent with IPCC GWP100
and is the most commonly cited perspective in published LCA studies.

---

## ReCiPe 2016 Midpoint (H) — Categories and Units

These are the 18 midpoint categories. The ones most relevant to textile
and fashion supply chains are marked with ★.

| # | Category | Unit | Relevant to textiles? |
|---|---|---|---|
| 1 | ★ Global Warming | kg CO₂ eq | Yes — energy, farming, transport |
| 2 | ★ Stratospheric Ozone Depletion | kg CFC-11 eq | Minor |
| 3 | ★ Ionizing Radiation | kBq Co-60 eq | Minor |
| 4 | ★ Ozone Formation (Human Health) | kg NOₓ eq | Yes — dyes, energy |
| 5 | ★ Fine Particle Formation | kg PM2.5 eq | Yes — combustion |
| 6 | Ozone Formation (Ecosystems) | kg NOₓ eq | Yes |
| 7 | ★ Terrestrial Acidification | kg SO₂ eq | Yes — coal energy |
| 8 | ★ Freshwater Eutrophication | kg P eq | Yes — fertiliser runoff |
| 9 | Marine Eutrophication | kg N eq | Yes — fertiliser |
| 10 | ★ Terrestrial Ecotoxicity | kg 1,4-DCB | Yes — pesticides |
| 11 | Freshwater Ecotoxicity | kg 1,4-DCB | Yes — dyes, chemicals |
| 12 | Marine Ecotoxicity | kg 1,4-DCB | Yes |
| 13 | ★ Human Carcinogenic Toxicity | kg 1,4-DCB | Yes — chemicals |
| 14 | Human Non-Carcinogenic Toxicity | kg 1,4-DCB | Yes |
| 15 | ★ Land Use | m² per year | Yes — cotton farming |
| 16 | ★ Mineral Resource Scarcity | kg Cu eq | Minor for textiles |
| 17 | Fossil Resource Scarcity | kg oil eq | Yes — polyester |
| 18 | ★ Water Consumption | m³ | Yes — cotton irrigation |

---

## ReCiPe 2016 Midpoint (H) — Key Characterization Factors

These are the CFs for the flows used in current recipe cards.

### Global Warming (GWP100) — kg CO₂ eq per kg

| Flow | CF |
|---|---|
| Carbon dioxide | 1.0 |
| Methane | 29.8 (fossil) / 27.9 (biogenic) |
| Nitrous oxide | 273.0 |

### Terrestrial Acidification — kg SO₂ eq per kg

| Flow | CF |
|---|---|
| Sulfur dioxide | 1.0 |
| Nitrogen oxides | 0.56 |
| Ammonia | 2.45 |

### Freshwater Eutrophication — kg P eq per kg

| Flow | CF |
|---|---|
| Phosphorus | 1.0 |
| Phosphate | 0.33 |

### Marine Eutrophication — kg N eq per kg

| Flow | CF |
|---|---|
| Ammonia | 0.8 |
| Nitrous oxide | 0.27 |
| Nitrogen oxides | 0.21 |

### Fine Particle Formation — kg PM2.5 eq per kg

| Flow | CF |
|---|---|
| Sulfur dioxide | 0.058 |
| Nitrogen oxides | 0.12 |
| Ammonia | 0.36 |

### Water Consumption — m³ per L

| Flow | CF |
|---|---|
| Water | 0.001 (L → m³ conversion, CF = 1.0 per m³) |

---

## How to Use ReCiPe in This System

### Recommended approach — Import the free openLCA LCIA methods pack

The cleanest path is to import the **openLCA LCIA methods pack** on top of
the `lca_commons` database that is already running. This is a small free file
(methods only, no background processes) that adds ReCiPe 2016, CML, EF, ILCD,
and about a dozen other methods alongside TRACI 2.2.

**Step 1 — Download the methods pack (one time only)**

1. Go to https://nexus.openlca.org (free account required)
2. Search for **"openLCA LCIA methods"**
3. Download the latest `.zip` file (~few MB)
4. Place it anywhere accessible — e.g. `$HOME/olca-data/`

**Step 2 — Import into the running database**

Make sure the openLCA server is running (`bash start_olca.sh`), then import
via the openLCA desktop app:

> File → Import → Linked Data (JSON-LD) → select the `.zip` file → OK

Or try the API import endpoint:
```bash
curl -X POST http://localhost:8080/api/import \
  -H "Content-Type: application/octet-stream" \
  --data-binary @"$HOME/olca-data/openLCA_LCIA_methods_2_2.zip"
```

**Step 3 — Verify ReCiPe is now in the database**

```python
python3 -c "
from olca_ipc.rest import RestClient
import olca_schema as o
client = RestClient('http://localhost:8080')
for m in client.get_descriptors(o.ImpactMethod):
    print(m.name)
"
```

You should see ReCiPe 2016 Midpoint (H), (I), and (E) listed alongside
TRACI 2.2. No restart needed.

**Step 4 — Change one line in a recipe card**

```yaml
# Before (TRACI):
lcia:
  method_name: "TRACI 2.2"

# After (ReCiPe):
lcia:
  method_name: "ReCiPe 2016 Midpoint (H)"
```

`get_impact_method_ref()` in `lca_analysis.py` does a case-insensitive
substring search, so it will find the method automatically. No code changes
needed. Run the analysis exactly as before.

---

### Fallback option — Embedded CFs in recipe card (no database needed)

Embed the CFs directly using the `impact_categories` block (same as the
existing hand-typed CF path already in `lca_analysis.py`):

```yaml
lcia:
  method: "ReCiPe 2016 Midpoint (H)"
  impact_categories:

    - name: Global Warming
      indicator: GWP100
      unit: kg CO2 eq
      characterization_factors:
        Carbon dioxide: 1.0
        Methane: 29.8
        Nitrous oxide: 273.0

    - name: Terrestrial Acidification
      indicator: TAP
      unit: kg SO2 eq
      characterization_factors:
        Sulfur dioxide: 1.0
        Nitrogen oxides: 0.56
        Ammonia: 2.45

    - name: Freshwater Eutrophication
      indicator: FEP
      unit: kg P eq
      characterization_factors:
        Phosphorus: 1.0

    - name: Fine Particle Formation
      indicator: PMFP
      unit: kg PM2.5 eq
      characterization_factors:
        Sulfur dioxide: 0.058
        Nitrogen oxides: 0.12
        Ammonia: 0.36

    - name: Water Consumption
      indicator: WCP
      unit: m3
      characterization_factors:
        Water: 0.001
```

This path requires no server and no database — pure Python multiplication
using the existing `impact_categories` code path in `lca_analysis.py`.

---

## Which Approach to Use

| Situation | Recommendation |
|---|---|
| lca_commons running, LCIA methods pack imported | Recommended — `method_name: "ReCiPe 2016 Midpoint (H)"` |
| No methods pack yet, want to test immediately | Fallback — embed CFs in recipe card |
| ecoinvent connected | `method_name: "ReCiPe 2016 Midpoint (H)"` — built into ecoinvent |
| Comparing ReCiPe vs TRACI on same product | Change `method_name` and rerun — no other changes needed |

---

## Comparing ReCiPe and TRACI on the Same Product

Because `method_name` is just a string in the recipe card, you can compare
both methods by running the analysis twice with different values:

```bash
# Run with TRACI 2.2
python3 lca_scripts/lca_analysis.py lca_analysis/cotton_shirt/recipe_card.md

# Edit recipe card: change method_name to "ReCiPe 2016 Midpoint (H)"
# Run again
python3 lca_scripts/lca_analysis.py lca_analysis/cotton_shirt/recipe_card.md
```

The GWP100 numbers should be very similar (both use IPCC AR6 GWP100 factors).
Differences will appear in categories where the methods diverge — for example,
TRACI uses North American spatial factors for acidification, while ReCiPe uses
global average factors.

---

## Pedagogical Value of Showing Both Methods

Comparing TRACI and ReCiPe results for the same product teaches students that:

1. **The inventory (B·s) is fixed** — the raw kg of CO₂, CH₄, etc. do not
   change. What changes is how those flows are weighted into impact scores.

2. **The method is a value judgement** — ReCiPe's global factors vs TRACI's
   North American factors reflects a choice about whose environment matters
   most in the assessment.

3. **GWP is stable across methods** — because both use IPCC GWP100. Students
   can trust the climate number regardless of which method is used.

4. **Other categories diverge** — acidification, eutrophication, and toxicity
   scores can differ significantly between TRACI and ReCiPe for the same
   product, especially for supply chains that span both US and non-US processes.

---

## References

- ReCiPe 2016 report: Huijbregts et al. (2017), _ReCiPe 2016: A harmonized
  life cycle impact assessment method at midpoint and endpoint level_.
  RIVM Report 2016-0104.
- openLCA LCIA methods pack (free): https://nexus.openlca.org/database/openLCA%20LCIA%20methods
- ReCiPe in openLCA: available via the methods pack or built into ecoinvent
- FEDEFL flow mapping to ReCiPe: https://github.com/USEPA/fedelemflowlist
  (the same FEDEFL names work for both TRACI and ReCiPe lookups)
