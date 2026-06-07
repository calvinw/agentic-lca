---
# ─────────────────────────────────────────────────────────────
# LCA Analysis Specification
# Run with:  python3 lca_scripts/lca_analysis.py lca_analysis/apple/recipe_card.md
# ─────────────────────────────────────────────────────────────

name: Apple LCA — 100 kcal consumed
goal: >
  Calculate the total CO₂ and CH₄ emitted to provide 100 kcal of fresh apple
  (0.19 kg), tracing the supply chain from farm through transport to consumption.
  Based on the apple example from the Constructing Inventories lecture slides.
  Simplified version: no cardboard, no packaging, no co-products, no waste.

functional_unit:
  description: 100 kcal of apple consumed (0.19 kg)
  amount: 1.0
  unit: serving

units:
  serving: Serving count (100 kcal apple)
  kg:      Mass
  kWh:     Energy
  L:       Volume

products:
  - { name: Apple,           unit: kg      }
  - { name: Apple delivered, unit: kg      }
  - { name: Electricity,     unit: kWh     }
  - { name: Fertilizer,      unit: kg      }
  - { name: Apple service,   unit: serving }

elementary_flows:
  emissions:
    - { name: CO2 to air, unit: kg }
    - { name: CH4 to air, unit: kg }
  resources:
    - { name: Water, unit: L }

processes:
  # ── Technosphere supply processes (modelled explicitly) ────────────────
  - name: P1 — Electricity supply
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.4 }

  - name: P2 — Fertilizer supply
    reference_output: { flow: Fertilizer, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 2.5 }

  # ── Foreground processes ───────────────────────────────────────────────
  - name: P3 — Production
    reference_output: { flow: Apple, amount: 1.0 }
    inputs:
      - { flow: Electricity, amount: 0.2 }
      - { flow: Fertilizer,  amount: 1.0 }
    resources:
      - { flow: Water, amount: 0.2 }
    emissions:
      - { flow: CO2 to air, amount: 0.2   }
      - { flow: CH4 to air, amount: 0.006 }

  - name: P4 — Transport
    reference_output: { flow: Apple delivered, amount: 1.0 }
    inputs:
      - { flow: Apple, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.063 }

  - name: P5 — Use
    reference_output: { flow: Apple service, amount: 1.0 }
    inputs:
      - { flow: Apple delivered, amount: 0.19 }

reference_process: P5 — Use
---

## About this analysis

Cradle-to-use LCA for 100 kcal of fresh apple (0.19 kg), based on the apple
example from the *Constructing Inventories* lecture slides.

Supply chain: farm → transport (1,000 km by truck) → consumption.

### Simplifications in this version

- **Cardboard / packaging omitted** — only electricity and fertilizer as farm inputs.
- **Co-product Pear omitted** — requires allocation (to be added later).
- **End-of-life disposal omitted** — waste flows to be added later.
- **Transport modelled as flow transformation** — P4 receives "Apple" (farm gate)
  and outputs "Apple delivered" (at consumer).

### Key assumptions

| Parameter | Value | Source |
|---|---|---|
| Functional unit | 0.19 kg apple = 100 kcal | PDF slide data |
| Electricity per kg apple | 0.2 kWh | 100,000 kWh / 500,000 kg |
| Fertilizer per kg apple | 1.0 kg | 500,000 kg / 500,000 kg |
| Water per kg apple | 0.2 L | 100,000 L / 500,000 kg |
| Direct CO₂ per kg apple | 0.2 kg | 100,000 kg CO₂ / 500,000 kg apple |
| Direct CH₄ per kg apple | 0.006 kg | 3,000 kg CH₄ / 500,000 kg apple |
| Transport emissions | 0.063 kg CO₂/kg | 1.02 tkm × 0.062 kg CO₂/tkm |
| Electricity emission factor | 0.4 kg CO₂/kWh | European average |
| Fertilizer emission factor | 2.5 kg CO₂/kg | Ammonium nitrate, typical |
