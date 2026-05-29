---
# ─────────────────────────────────────────────────────────────
# LCA Analysis Specification
# Run with:  python3 lca_analysis.py [this_file.md]
# ─────────────────────────────────────────────────────────────

name: Cotton Shirt LCA — cradle to gate
goal: >
  Calculate the total CO₂ emitted to produce one cotton shirt,
  tracing the full supply chain from cotton farming through
  yarn spinning, fabric weaving, and garment assembly.

functional_unit:
  description: One cotton shirt (cradle to gate)
  amount: 1.0
  unit: shirt

units:
  shirt: Shirt count
  kg:   Mass
  kWh:  Energy

products:
  - { name: Raw cotton,   unit: kg    }
  - { name: Yarn,         unit: kg    }
  - { name: Fabric,       unit: kg    }
  - { name: Cotton shirt, unit: shirt }
  - { name: Electricity,  unit: kWh   }

elementary_flows:
  emissions:
    - { name: CO2 to air, unit: kg }

processes:
  - name: P1 — Grow cotton
    reference_output: { flow: Raw cotton, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 3.0 }

  - name: P2 — Spin yarn
    reference_output: { flow: Yarn, amount: 1.0 }
    inputs:
      - { flow: Raw cotton,  amount: 1.1 }
      - { flow: Electricity, amount: 3.0 }

  - name: P3 — Weave fabric
    reference_output: { flow: Fabric, amount: 1.0 }
    inputs:
      - { flow: Yarn,        amount: 1.1 }
      - { flow: Electricity, amount: 4.0 }

  - name: P4 — Cut and sew shirt
    reference_output: { flow: Cotton shirt, amount: 1.0 }
    inputs:
      - { flow: Fabric,      amount: 0.25 }
      - { flow: Electricity, amount: 1.0  }

  - name: P5 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.5 }

reference_process: P4 — Cut and sew shirt
---

## About this analysis

Cradle-to-gate LCA for one cotton shirt.

Supply chain: cotton farm → spinning mill → weaving mill → garment factory.
Electricity is supplied to the spinning, weaving, and sewing steps by a
coal-powered grid (0.5 kg CO₂ per kWh).

Key assumptions:
- A finished shirt uses 0.25 kg of fabric.
- Spinning requires 1.1 kg raw cotton per 1 kg yarn (10% fibre loss).
- Weaving requires 1.1 kg yarn per 1 kg fabric (10% yarn loss).
- Cotton farming emits 3.0 kg CO₂ per kg raw cotton (fertilisers, machinery, irrigation).
- Grid electricity emits 0.5 kg CO₂ per kWh (average coal-heavy grid).
