---
# ─────────────────────────────────────────────────────────────────────────────
# LCA Analysis Specification — thredUP Comparative LCA (2019)
# SCENARIO: thredUP secondhand garment (base displacement assumption)
# Run with: python3 lca_scripts/lca_analysis.py lca_analysis/thredup/thredup_secondhand.md
# ─────────────────────────────────────────────────────────────────────────────

name: thredUP Comparative LCA — Secondhand Garment (100% displacement)
goal: >
  Calculate the total CO₂ emitted by thredUP's operations to collect, sort,
  relist, and deliver one average secondhand garment to a US consumer.
  The study assumes 100% displacement — every thredUP buyer would have bought
  a brand-new garment if thredUP did not exist.

functional_unit:
  description: One average secondhand garment (0.4 kg) purchased via thredUP, 70% of useful life remaining
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

  - name: P3 — End of life (remaining 30% of garment life)
    reference_output: { flow: thredUP purchase, amount: 1.0 }
    inputs:
      - { flow: Sorted garment, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.2 }

reference_process: P3 — End of life (remaining 30% of garment life)

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

## About this scenario

**What this models:** The actual CO₂ emitted by thredUP's own operations to
collect, process, and resell one average secondhand garment. The upstream
manufacturing emissions (making the garment in the first place) are NOT counted
here — they are allocated entirely to the original first owner who wore it.

**Key assumption — displacement:** The study assumes **100% displacement**:
every single thredUP customer in 2018 was a first-time secondhand buyer who
would have bought new if thredUP did not exist. This is the most optimistic
possible assumption. Compare with `thredup_partial_displacement.md` to see
what happens when this assumption is relaxed.

**Key assumption — remaining useful life:** The study assumes the secondhand
garment has **70% of its useful life remaining** when thredUP sells it. A
typical garment lasts about 50 washes. Most people donate clothes after around
15 washes, leaving 35 washes (70%) for the next owner.

---

### How to read the comparison

Run this file and `product_graph.yaml` (the new garment), then compare:

| Model | CO₂ per garment | Meaning |
|---|---|---|
| New garment (`product_graph.yaml`) | ~15.8 kg CO₂ | What making a new garment costs |
| thredUP secondhand (this file) | ~1.9 kg CO₂ | What thredUP's operations cost |
| **Savings** | **~13.9 kg CO₂** | **88% less CO₂ per garment lifecycle** |

But on a **fair "per wear" basis** (adjusting for the fact that the secondhand
garment only has 70% of its life left):
- Equivalent new garment for 70% of life: 15.8 × 0.70 = 11.1 kg CO₂
- thredUP secondhand: 1.9 kg CO₂
- **Net saving: 9.2 kg CO₂ — about 58% less**

This 58% figure is what the study reports as the headline saving.

---

### CO₂ by stage

| Stage | Process | CO₂ source | CO₂ |
|---|---|---|---|
| P1 | Collection | Cleanout kit bag shipped to seller; return postage | 0.7 kg |
| P2 | Sort + ship to buyer | Warehouse electricity; USPS delivery packaging | 1.0 kg |
| P3 | End of life | Remaining 30% of garment's landfill/incineration burden | 0.2 kg |
| **Total** | | | **~1.9 kg CO₂** |
