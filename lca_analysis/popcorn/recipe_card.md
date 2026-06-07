---
# ─────────────────────────────────────────────────────────────
# LCA Analysis Specification — ILLUSTRATIVE NUMBERS
# Based on: Jolliet et al. (1994) Agriculture, Ecosystems and Environment 49, 253–266
# and Jolliet et al. (2016) Environmental Life Cycle Assessment textbook, Chapter 3
# ─────────────────────────────────────────────────────────────

name: Popcorn Packing Material — 1 kg
goal: >
  Illustrative supply chain for 1 kg of popcorn used as loose-fill packing material
  (an alternative to polystyrene packing peanuts). The corn is grown, dried, then
  blown with hot air to expand it into packaging fill.
  Numbers are illustrative approximations based on Jolliet et al. (1994).

functional_unit:
  description: 1 kg of popcorn packing material
  amount: 1.0
  unit: kg

units:
  kg: Mass
  L:  Volume

products:
  - { name: Fertilizer,      unit: kg }
  - { name: Corn,            unit: kg }
  - { name: Dried corn,      unit: kg }
  - { name: Packing popcorn, unit: kg }

elementary_flows:
  emissions:
    - { name: CO2 to air, unit: kg }
    - { name: N2O to air, unit: kg }
    - { name: NH3 to air, unit: kg }
  resources:
    - { name: Water, unit: L }

processes:
  - name: P1 — Fertilizer supply
    reference_output: { flow: Fertilizer, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 2.5 }

  - name: P2 — Corn farming
    reference_output: { flow: Corn, amount: 1.0 }
    inputs:
      - { flow: Fertilizer, amount: 0.05 }
    resources:
      - { flow: Water, amount: 0.5 }
    emissions:
      - { flow: CO2 to air, amount: 0.2  }
      - { flow: N2O to air, amount: 0.003 }
      - { flow: NH3 to air, amount: 0.002 }

  - name: P3 — Drying
    reference_output: { flow: Dried corn, amount: 1.0 }
    inputs:
      - { flow: Corn, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.25 }

  - name: P4 — Popping
    reference_output: { flow: Packing popcorn, amount: 1.0 }
    inputs:
      - { flow: Dried corn, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.15 }

reference_process: "P4 — Popping"
---

## About this analysis

Illustrative supply chain for popcorn used as loose-fill packing material,
based on the Jolliet et al. (1994) popcorn-vs-polystyrene case study.

Supply chain: fertilizer supply → corn farming → drying → hot-air popping.

### Key insights

- The corn field is essentially a solar panel: it captures sunlight to grow the corn,
  so most of the energy input is renewable.
- The main environmental downside is **agriculture**: fertilizer production and
  field application release CO₂, N₂O (a potent greenhouse gas), and NH₃ (which
  contributes to eutrophication — excess nutrients in water bodies).
- N₂O has a global warming potential ~298× that of CO₂, so even small amounts matter.

### The density twist

Per kg, popcorn has ~3.4× lower CO₂ than polystyrene. This looks like a clear win.

But popcorn is **4.6× denser** than polystyrene peanuts. To fill the same volume
of a package, you need 4.6 times as much popcorn by mass. When you recalculate
**per m³** (the correct functional unit for filling a package), polystyrene wins.

This is why functional unit choice is one of the most critical decisions in LCA.

### Numbers are illustrative

The per-process emission factors are approximate, chosen to reproduce the
3–4× ratio reported by Jolliet et al. (1994) when compared to polystyrene per kg.
