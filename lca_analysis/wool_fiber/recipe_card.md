---
# ─────────────────────────────────────────────────────────────
# LCA Analysis Specification
# Run with:  python3 lca_scripts/lca_analysis.py lca_analysis/wool_fiber/recipe_card.md
# ─────────────────────────────────────────────────────────────

name: Wool Fiber LCA — 1 kg of yarn (expanded)
goal: >
  Calculate the climate and air-quality impact of producing 1 kg of wool yarn,
  tracing the full supply chain from sheep farming through scouring, spinning,
  and the electricity that powers the mill. This expanded version separates
  electricity into its own process to show which impacts come from the farm
  vs. the mill energy supply.

functional_unit:
  description: 1 kg of wool yarn, ready for knitting or weaving
  amount: 1.0
  unit: kg

units:
  kg:  Mass
  L:   Volume
  kWh: Energy

products:
  - { name: Raw wool,    unit: kg  }
  - { name: Wool yarn,   unit: kg  }
  - { name: Electricity, unit: kWh }

elementary_flows:
  emissions:
    - { name: Carbon dioxide,  compartment: air, unit: kg }
    - { name: Methane,         compartment: air, unit: kg }
    - { name: Sulfur dioxide,  compartment: air, unit: kg }
    - { name: Nitrogen oxides, compartment: air, unit: kg }
  resources:
    - { name: Water, compartment: water, unit: L }

processes:
  - name: P1 — Sheep farming
    reference_output: { flow: Raw wool, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.5 }
      - { flow: Methane,        amount: 0.4 }

  - name: P2 — Scour and spin
    reference_output: { flow: Wool yarn, amount: 1.0 }
    inputs:
      - { flow: Raw wool,    amount: 1.1 }
      - { flow: Electricity, amount: 4.0 }
    resources:
      - { flow: Water, amount: 30 }

  - name: P3 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.5    }
      - { flow: Sulfur dioxide,  amount: 0.0006 }
      - { flow: Nitrogen oxides, amount: 0.0009 }

reference_process: "P2 — Scour and spin"

lcia:
  method_name: "TRACI 2.2"
---

## About this analysis

An expanded cradle-to-gate LCA for 1 kg of wool yarn.

Compared to the skills_references/wool_yarn version, this version adds:
- Electricity as a separate process (P3), using the same coal-grid factors as the cotton shirt
- Sulfur dioxide and nitrogen oxides from electricity generation, which contribute to acidification and smog

Supply chain: sheep farm → scouring & spinning mill → electricity grid

Key assumptions:
- P2 requires 1.1 kg raw wool per 1 kg yarn (10% fibre loss during scouring and carding)
- P2 requires 4.0 kWh electricity per kg yarn (hot water for scouring + spinning motors)
- P1 emits 0.5 kg CO₂ and 0.4 kg CH₄ per kg raw wool (farm energy + enteric fermentation)
- Electricity grid: 0.5 kg CO₂, 0.0006 kg SO₂, 0.0009 kg NOₓ per kWh (coal-heavy grid)
- 30 L of water consumed per kg yarn at the scouring stage
