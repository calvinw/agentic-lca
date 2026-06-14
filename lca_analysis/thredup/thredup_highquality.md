---
# ─────────────────────────────────────────────────────────────────────────────
# LCA Analysis Specification — thredUP Comparative LCA (2019)
# SCENARIO: Secondhand garment — premium quality items (85% life remaining)
# Run with: python3 lca_scripts/lca_analysis.py lca_analysis/thredup/thredup_highquality.md
# ─────────────────────────────────────────────────────────────────────────────

name: thredUP Comparative LCA — Secondhand, High Quality (85% life remaining)
goal: >
  Model the environmental savings when thredUP sells higher-quality or
  lightly-used garments that still have 85% of their useful life remaining,
  rather than the study's base assumption of 70%.

functional_unit:
  description: One average secondhand garment (0.4 kg) purchased via thredUP, 85% of useful life remaining
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

  - name: P2 — Sort, list online, and ship to buyer
    reference_output: { flow: Sorted garment, amount: 1.0 }
    inputs:
      - { flow: Donated garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 1.0 }

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

**What changed:** The base study assumes that secondhand garments have
**70% of their useful life remaining** when thredUP sells them. This scenario
tests what happens if thredUP focuses on sourcing and reselling **higher-quality,
lightly-used items** that still have **85% of their useful life remaining** —
meaning the original owner wore them even less before selling.

The only thing that changes in the model is P3 (end of life). Because the
garment has only used 15% of its life (instead of 30%), the end-of-life disposal
burden attributed to this purchase shrinks from 0.2 kg CO₂ to 0.12 kg CO₂.

**Why this matters:** The end-of-life impact is small — but the real value is
in the comparison with the new garment. If the secondhand garment has 85% of
its life left (not 70%), you're getting **even more value** out of the same
manufacturing emissions. The effective savings per "wear" increase.

---

### CO₂ comparison

| Scenario | thredUP ops CO₂ | Life remaining | CO₂ saving vs. new (per equivalent life) |
|---|---|---|---|
| New garment | 15.8 kg | 100% | — |
| Secondhand base (70% life) | 1.9 kg | 70% | 58% less per equivalent life |
| **Secondhand high quality (85% life)** | **1.82 kg** | **85%** | **~67% less per equivalent life** |

The higher the garment quality and remaining life, the greater the environmental
savings per wear — which is a strong argument for quality curation in resale.
