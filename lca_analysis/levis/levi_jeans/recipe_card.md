---
# ─────────────────────────────────────────────────────────────
# LCA Analysis Specification
# Run with:  python3 lca_scripts/lca_analysis.py lca_analysis/levi_jeans/recipe_card.md
# ─────────────────────────────────────────────────────────────

name: Levi's 501 Jeans LCA — cradle to grave
goal: >
  Calculate the total CO₂ emitted over the full lifecycle of one pair of
  Levi's® 501® jeans (medium stone wash), tracing the supply chain from
  cotton farming through fabric production, garment manufacturing,
  distribution, consumer washing and drying, and end-of-life disposal.
  Based on Levi Strauss & Co.'s 2015 LCA study (US consumer use profile).

functional_unit:
  description: One pair of Levi's 501 jeans (medium stone wash) — full lifecycle, cradle to grave
  amount: 1.0
  unit: pair

units:
  pair: Pair of jeans
  kg:   Mass in kilograms
  kWh:  Electrical energy in kilowatt-hours

products:
  - { name: Raw cotton,                      unit: kg   }
  - { name: Denim fabric,                    unit: kg   }
  - { name: Finished jeans,                  unit: pair }
  - { name: Levis 501 jeans full lifecycle,  unit: pair }
  - { name: Electricity,                     unit: kWh  }

elementary_flows:
  emissions:
    - { name: Carbon dioxide,  compartment: air, unit: kg }
    - { name: Nitrogen oxides, compartment: air, unit: kg }
    - { name: Sulfur dioxide,  compartment: air, unit: kg }

processes:
  - name: P1 — Grow and harvest cotton
    reference_output: { flow: Raw cotton, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 2.9 }

  - name: P2 — Spin, dye, and weave denim fabric
    reference_output: { flow: Denim fabric, amount: 1.0 }
    inputs:
      - { flow: Raw cotton,  amount: 1.25 }
      - { flow: Electricity, amount: 22.5 }

  - name: P3 — Cut, sew, and finish jeans
    reference_output: { flow: Finished jeans, amount: 1.0 }
    inputs:
      - { flow: Denim fabric, amount: 0.8  }
      - { flow: Electricity,  amount: 5.2  }

  - name: P4 — Distribute, wash, dry, and dispose of jeans
    reference_output: { flow: Levis 501 jeans full lifecycle, amount: 1.0 }
    inputs:
      - { flow: Finished jeans, amount: 1.0  }
      - { flow: Electricity,    amount: 25.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 6.4 }

  - name: P5 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.5    }
      - { flow: Nitrogen oxides, amount: 0.0009 }
      - { flow: Sulfur dioxide,  amount: 0.0006 }

reference_process: P4 — Distribute, wash, dry, and dispose of jeans

lcia:
  method_name: "TRACI 2.2"
---

## About this analysis

Cradle-to-grave LCA for one pair of Levi's® 501® jeans (medium stone wash),
based on the 2015 Levi Strauss & Co. lifecycle assessment study. This is a
full lifecycle model — it covers every stage from the cotton farm all the way
through to the customer washing and disposing of the jeans.

Supply chain:
  Cotton farm → Fabric mill (spinning + dyeing + weaving) → Garment factory
  → Distribution & retail → Consumer use (washing & drying) → End of life

### Physical quantities

A finished pair of 501 jeans weighs approximately 0.8 kg.
- Making 0.8 kg of denim fabric requires 1.0 kg of raw cotton
  (1.25 kg cotton per kg fabric, accounting for spinning and weaving losses)
- The garment factory uses 0.8 kg of denim fabric to cut and sew one pair
- The consumer washes and dries the jeans over the product's lifetime

### CO₂ accounting by phase (must total 33.4 kg)

| Process | Source of CO₂ | Amount |
|---|---|---|
| P1 Cotton farm | Direct (fertilisers, irrigation, machinery) | 2.9 kg |
| P2 Fabric mill | Electricity (18 kWh × 0.5 kg/kWh) | 9.0 kg |
| P3 Garment factory | Electricity (5.2 kWh × 0.5 kg/kWh) | 2.6 kg |
| P4 Distribute + use | Direct (sundries 1.7 + transport 3.8 + end-of-life 0.9) | 6.4 kg |
| P4 Consumer washing | Electricity (25 kWh × 0.5 kg/kWh) | 12.5 kg |
| **Total** | | **33.4 kg** |

### Key assumptions

- One pair of jeans weighs 0.8 kg and requires 1.0 kg raw cotton.
- Spinning and weaving lose 20% of material (1.25 kg cotton → 1 kg fabric).
- Grid electricity emits 0.5 kg CO₂ per kWh (average grid, 2012 data).
- Consumer care figures use the US average washing frequency (~2.3 wears
  per wash), conventional washing machine, mixed cold/warm water, tumble dry.
- Transport, sundries, packaging, and end-of-life are modelled as direct CO₂
  in P4 because they do not produce a distinct intermediate product.
- The study scope is global cotton cultivation and US consumer use.

### Key finding

Consumer care (washing and drying) is the single largest source of CO₂ in
the entire lifecycle, at 12.5 kg (37% of total). Washing every 10 wears
instead of every 2.3 could reduce the jeans' total climate impact by
roughly 25–30%. The fabric mill is the second largest contributor at
9.0 kg (27%), driven by energy-intensive dyeing and finishing processes.
