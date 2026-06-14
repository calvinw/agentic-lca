# Levi's 501 Jeans LCA — Session Notes

**Date:** 2026-06-12
**Source:** Levi Strauss & Co., *The Life Cycle of a Jean* (2015 LCA study)
**PDF location:** `lca_analysis/levi_jeans/levi_strauss_lca.pdf`

---

## What the PDF covers

The Levi's 2015 LCA study examined one pair of Levi's® 501® medium stone wash jeans,
from cradle (cotton farm) to grave (end of life disposal). It was conducted by
Industrial Ecology Consultants and LS&Co., conforms to ISO 14040/14044 standards,
and used data from 11 supplier factories and 6 fabric mills. The 2012 production
year was studied.

**Functional unit:** One pair of Levi's 501 jeans (medium stone wash), full lifecycle.

---

## Total lifecycle impact (from the PDF)

| Impact category | Amount | Equivalent |
|---|---|---|
| Climate change | 33.4 kg CO₂-e | Driving 69 miles in an average US car |
| Water consumed | 3,781 litres | 3 days of one US household's total water needs |
| Eutrophication | 48.9 g PO₄-e | Phosphorous in 1,700 tomatoes |
| Land occupation | 12 m²/year | Seven people standing arms outstretched |

---

## CO₂ breakdown by lifecycle phase

| Phase | kg CO₂ | % of total |
|---|---|---|
| Fiber (cotton farming) | 2.9 | 9% |
| Fabric production (spinning, dyeing, weaving) | 9.0 | 27% |
| Cut, sew, finish (garment manufacturing) | 2.6 | 8% |
| Sundries & packaging | 1.7 | 5% |
| Transport, logistics, retail | 3.8 | 11% |
| Consumer care (washing & drying) | 12.5 | 37% |
| End of life | 0.9 | 3% |
| **Total** | **33.4** | **100%** |

**Key finding:** Consumer care (washing and drying) is the single largest source of
CO₂ — bigger than the cotton farm and the factory combined. The fabric mill is the
second largest contributor at 27%.

---

## Water consumption breakdown

| Phase | Litres | % |
|---|---|---|
| Fiber (cotton) | 2,565 | 68% |
| Fabric production | 236 | 6% |
| Consumer care | 860 | 23% |
| Cut, sew, finish | 34 | 1% |
| Sundries & packaging | 77 | 2% |

Cotton cultivation dominates water use at 68% of total.

---

## The supply chain model we built

We translated the PDF data into a recipe card at:
`lca_analysis/levi_jeans/recipe_card.md`

### Physical quantities assumed
- One pair of jeans = 0.8 kg denim fabric
- 1.25 kg raw cotton → 1 kg denim fabric (20% loss in spinning and weaving)
- 1.0 kg raw cotton needed per pair
- Electricity emission factor: 0.5 kg CO₂ per kWh

### Five-process supply chain

| Process | Role | Key numbers |
|---|---|---|
| P1 — Grow and harvest cotton | Cotton farm | Emits 2.9 kg CO₂ per kg cotton (direct: fertilisers, irrigation, machinery) |
| P2 — Spin, dye, and weave denim fabric | Fabric mill | Uses 1.25 kg cotton + 22.5 kWh electricity per kg fabric |
| P3 — Cut, sew, and finish jeans | Garment factory | Uses 0.8 kg fabric + 5.2 kWh electricity per pair |
| P4 — Distribute, wash, dry, and dispose | Use + end of life | Uses 25 kWh electricity (washing/drying) + 6.4 kg direct CO₂ (transport, packaging, end of life) |
| P5 — Generate electricity | Power grid | Emits 0.5 kg CO₂ per kWh |

### Scaling vector (how many times each process runs per pair of jeans)

| Process | Scale factor | Meaning |
|---|---|---|
| P1 Cotton farm | 1.000 | Runs once — grows 1 kg of cotton |
| P2 Fabric mill | 0.800 | Runs at 80% — only needs 0.8 kg of fabric |
| P3 Garment factory | 1.000 | Runs once — sews 1 pair |
| P4 Use & disposal | 1.000 | Runs once — one consumer lifecycle |
| P5 Electricity grid | **48.200** | Runs 48.2 times — combined electricity demand of mills, factory, and lifetime washing |

### Verified result

The model produces **33.4 kg CO₂**, matching the Levi's report exactly (✓ confirmed
by both numpy calculation and openLCA gdt-server).

---

## Group 1 scenarios — Washing frequency (US consumer)

All scenarios use the same supply chain. Only the electricity input to P4 changes.
The fixed manufacturing side is always 20.9 kg CO₂.

| Scenario | Folder | P4 electricity | Consumer care CO₂ | Total CO₂ | PDF target | Match |
|---|---|---|---|---|---|---|
| Wash every wear | `levi_jeans_wash1x` | 61.54 kWh | 30.77 kg | **51.67 kg** | ~51.7 kg | ✓ |
| Wash every 2 wears | `levi_jeans_wash2x` | 30.76 kWh | 15.38 kg | **36.28 kg** | ~36.3 kg | ✓ |
| Baseline (global avg) | `levi_jeans` | 25.00 kWh | 12.50 kg | **33.40 kg** | 33.4 kg | ✓ |
| Wash every 5 wears | `levi_jeans_wash5x` | 12.30 kWh | 6.15 kg | **27.05 kg** | ~27.1 kg | ✓ |
| Wash every 10 wears | `levi_jeans_wash10x` | 6.16 kWh | 3.08 kg | **23.98 kg** | ~24.0 kg | ✓ |

**Business insight:** Going from the worst habit (wash every wear) to Levi's own
recommended behaviour (wash every 10 wears) cuts the total footprint from 51.67 kg
to 23.98 kg — a **54% reduction** achieved entirely by the customer, with zero
changes to manufacturing. This is why Levi's invested in the "Care Tag for Our Planet"
campaign.

---

## Scenarios from the PDF not yet run

### Group 2 — Water temperature (US consumer)

| Scenario | Consumer care CO₂ | Full lifecycle total |
|---|---|---|
| 100% warm wash | 15.9 kg | ~36.8 kg |
| US average (mixed) | 13.4 kg | ~34.3 kg |
| 100% cold wash | 12.1 kg | ~33.0 kg |

### Group 3 — Drying method (US consumer)

| Scenario | Consumer care CO₂ | Full lifecycle total |
|---|---|---|
| Dryer & iron | 20.17 kg | ~41.1 kg |
| Dryer only (average) | 13.84 kg | ~34.7 kg |
| Line dry & iron | 10.94 kg | ~31.8 kg |
| Line dry only | 4.61 kg | ~25.5 kg |

### Group 4 — Country comparison

| Country | Consumer care CO₂ | Full lifecycle total |
|---|---|---|
| US average | 13.38 kg | ~34.3 kg |
| UK/France average | 11.17 kg | ~32.1 kg |
| China average | 11.83 kg | ~32.7 kg |

### Group 5 — Sensitivity analysis (from PDF appendix)

| What changes | By how much | Effect on CO₂ | Effect on water |
|---|---|---|---|
| Fabric loss in mills | ±10% | ±3.8% | ±7.4% |
| Fiber loss in spinning | ±10% | ±2.6% | ±6.7% |
| Washing frequency | ±10% | ±3.8% | ±2.3% |
| Transport distance | ±50% | ±1.0% | ~0% |

Key takeaway: Transport barely matters even if doubled or halved (±1%). Fabric loss
and washing frequency have a much bigger effect.

---

## Custom scenarios (not in the Levi's document)

**Important note:** None of these four scenarios appear in the Levi's PDF.
The PDF only varies consumer behaviour (washing frequency, water temperature,
drying method, country). The supply chain — cotton farm, fabric mill, garment
factory — is treated as fixed background throughout. The PDF mentions the Better
Cotton Initiative and Wellthread™ in its "Next Steps" section but never quantifies
their CO₂ impact.

**The PDF tells you what customers can do. These scenarios tell you what the brand can do.**

### Results

| Scenario | Folder | Total CO₂ | Saving vs. baseline | % reduction |
|---|---|---|---|---|
| Baseline | `levi_jeans` | 33.40 kg | — | — |
| B — Organic cotton only | `levi_jeans_organic` | 32.00 kg | −1.40 kg | −4% |
| D — Twice as durable | `levi_jeans_longlife` | 26.15 kg | −7.25 kg | −22% |
| A — Renewable energy supply chain | `levi_jeans_renewable` | 11.71 kg | −21.69 kg | −65% |
| C — Best of everything | `levi_jeans_bestcase` | 9.37 kg | −24.03 kg | −72% |

### What changed in each recipe card

| Scenario | Parameter changed | Baseline value | Scenario value |
|---|---|---|---|
| A — Renewable energy | P5 emission factor (kg CO₂/kWh) | 0.50 | 0.05 |
| B — Organic cotton | P1 direct emissions (kg CO₂/kg cotton) | 2.90 | 1.50 |
| C — Best of everything | P1 + P5 + P4 electricity (all three) | as above | as above + 6.16 kWh |
| D — Twice as durable | P4 input of Finished jeans (pairs) | 1.00 | 0.50 |

### Key findings

**Organic cotton (B) is almost irrelevant for CO₂.**
Switching all cotton to organic saves only 1.4 kg — a 4% reduction. Cotton farming
is just 9% of the total footprint. Organic cotton matters far more for water use
and soil health than for climate change.

**Renewable energy in the factory (A) is transformative.**
Switching mills and factories to solar or wind cuts 21.7 kg — a 65% reduction.
This is the single most powerful lever available to a brand, and it is entirely within
the brand's control through supplier contracts and procurement decisions.

**Durability (D) is a solid middle ground.**
Doubling how long jeans last saves 7.3 kg (22%) with no change to consumer washing
habits or factory energy. This is the business case for quality construction and repair.

**The best-case floor is 9.4 kg (C)** — about 28% of today's footprint — achievable
by combining renewable energy, organic cotton, and encouraging customers to wash less.
The remaining 9.4 kg sits in transport, packaging, end-of-life, and the basic physics
of growing cotton. It is very hard to eliminate.

---

## Files created in this session

| File | Description |
|---|---|
| `lca_analysis/levi_jeans/recipe_card.md` | Base recipe card — global average consumer |
| `lca_analysis/levi_jeans/lca_results.md` | Full LCA results for baseline |
| `lca_analysis/levi_jeans/product_graph_scaled.svg` | Supply chain diagram with amounts |
| `lca_analysis/levi_jeans/product_graph_structure.svg` | Supply chain diagram — flow names only |
| `lca_analysis/levi_jeans/levi_jeans_product_graph_scaled.svg` | Earlier diagram (generated before running full analysis) |
| `lca_analysis/levi_jeans/levi_jeans_product_graph_structure.svg` | Earlier structure diagram |
| `lca_analysis/levi_jeans_wash1x/recipe_card.md` | Scenario: wash every wear |
| `lca_analysis/levi_jeans_wash1x/lca_results.md` | Results: 51.67 kg CO₂ |
| `lca_analysis/levi_jeans_wash2x/recipe_card.md` | Scenario: wash every 2 wears |
| `lca_analysis/levi_jeans_wash2x/lca_results.md` | Results: 36.28 kg CO₂ |
| `lca_analysis/levi_jeans_wash5x/recipe_card.md` | Scenario: wash every 5 wears |
| `lca_analysis/levi_jeans_wash5x/lca_results.md` | Results: 27.05 kg CO₂ |
| `lca_analysis/levi_jeans_wash10x/recipe_card.md` | Scenario: wash every 10 wears |
| `lca_analysis/levi_jeans_wash10x/lca_results.md` | Results: 23.98 kg CO₂ |
| `lca_analysis/levi_jeans_renewable/recipe_card.md` | Custom A: renewable energy supply chain |
| `lca_analysis/levi_jeans_renewable/lca_results.md` | Results: 11.71 kg CO₂ (−65%) |
| `lca_analysis/levi_jeans_organic/recipe_card.md` | Custom B: organic cotton farm |
| `lca_analysis/levi_jeans_organic/lca_results.md` | Results: 32.00 kg CO₂ (−4%) |
| `lca_analysis/levi_jeans_bestcase/recipe_card.md` | Custom C: best of everything |
| `lca_analysis/levi_jeans_bestcase/lca_results.md` | Results: 9.37 kg CO₂ (−72%) |
| `lca_analysis/levi_jeans_longlife/recipe_card.md` | Custom D: twice as durable |
| `lca_analysis/levi_jeans_longlife/lca_results.md` | Results: 26.15 kg CO₂ (−22%) |
