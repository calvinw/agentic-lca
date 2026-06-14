---
# ─────────────────────────────────────────────────────────────────────────────
# LCA Analysis Specification — thredUP Comparative LCA (2019)
# SCENARIO: Best case — renewable warehouse + high quality items + 100% displacement
# Run with: python3 lca_scripts/lca_analysis.py lca_analysis/thredup/thredup_bestcase.md
# ─────────────────────────────────────────────────────────────────────────────

name: thredUP Comparative LCA — Secondhand, Best Case
goal: >
  Model the lowest possible CO₂ footprint for a thredUP secondhand purchase:
  renewable-powered warehouse, high-quality items with 85% useful life
  remaining, and 100% buyer displacement from new purchases.

functional_unit:
  description: One premium secondhand garment (0.4 kg) via thredUP, renewable warehouse, 85% life remaining
  amount: 1.0
  unit: garment

units:
  garment: One average garment item
  kg:      Mass in kilograms

products:
  - { name: Donated garment,      unit: garment }
  - { name: Sorted garment,       unit: garment }
  - { name: thredUP purchase,     unit: garment }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }

processes:
  - name: P1 — Collect and receive used clothing
    reference_output: { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.7 }

  - name: P2 — Sort, list online, and ship to buyer (renewable warehouse)
    reference_output: { flow: Sorted garment, amount: 1.0 }
    inputs:
      - { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.15 }

  - name: P3 — End of life (remaining 15% of garment life)
    reference_output: { flow: thredUP purchase, amount: 1.0 }
    inputs:
      - { flow: Sorted garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.12 }

reference_process: P3 — End of life (remaining 15% of garment life)

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

**What changed:** This is the "everything goes right" version. Three improvements
are stacked together:

1. **Renewable warehouse** — thredUP's sorting and distribution centers run on
   solar or wind power, cutting warehouse CO₂ from 1.0 kg to 0.15 kg per garment.

2. **High-quality items** — thredUP curates only lightly-used garments with
   85% of useful life remaining (not 70%), reducing the end-of-life burden from
   0.2 kg to 0.12 kg per garment.

3. **100% displacement** — every buyer truly switches from new (the study's
   base assumption, kept here as the most optimistic case).

---

### Full scenario comparison

| Scenario | CO₂ per garment | vs. new garment (15.8 kg) |
|---|---|---|
| New garment | 15.8 kg | — |
| Secondhand base case | 1.9 kg | −88% |
| Renewable warehouse only | 1.05 kg | −93% |
| High quality only (85% life) | 1.82 kg | −88% |
| **Best case (all combined)** | **0.97 kg** | **−94%** |
| Partial displacement (50%) | 9.8 kg | −38% |

The single most powerful lever is **renewable warehouse energy**, which cuts
thredUP's own emissions nearly in half. The quality curation improvement is
smaller in absolute CO₂ terms but has a larger effect on the business case —
higher-quality items sell at higher prices, generating more revenue while
delivering more environmental value per transaction.

**Business takeaway:** A resale platform that combines renewable-powered
operations with a curated, high-quality inventory can achieve a carbon footprint
approximately **16 times lower** than buying new — but only if buyers are truly
switching from new purchases. The displacement assumption is where sustainability
claims in resale are most vulnerable to challenge.
