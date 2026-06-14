---
name: "Plastic Broom LCA — cradle to gate"
goal: >
  Calculate the total CO₂ emitted to produce one plastic broom
  with a PLA handle and nylon 6 bristles, tracing through raw
  material production and transport to the factory gate.

functional_unit:
  description: One plastic broom (cradle to gate)
  amount: 1
  unit: broom

units:
  broom:  Broom count
  kg:     Mass
  1000 km-kg: Transport (thousands of kg·km)

products:
  - { name: Nylon 6,       unit: kg           }
  - { name: PLA,           unit: kg           }
  - { name: Transport service, unit: 1000 km-kg }
  - { name: Plastic broom, unit: broom        }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }

processes:
  - name: "P1 — Produce nylon 6"
    reference_output: { flow: Nylon 6, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 9.07 }

  - name: "P2 — Produce PLA"
    reference_output: { flow: PLA, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 2.68 }

  - name: "P3 — Transport by lorry"
    reference_output: { flow: Transport service, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.15 }

  - name: "P4 — Assemble broom"
    reference_output: { flow: Plastic broom, amount: 1.0 }
    inputs:
      - { flow: Nylon 6,          amount: 0.03   }
      - { flow: PLA,              amount: 0.52   }
      - { flow: Transport service, amount: 0.1055 }

reference_process: "P4 — Assemble broom"

lcia:
  method_name: "TRACI 2.2"
---

## About this analysis

Based on the openLCA tutorial video for a plastic broom case study.

The broom has two components:
- **Handle** — PLA (polylactic acid, a bioplastic from corn): 0.52 kg
- **Bristles** — Nylon 6 (a petroleum-based plastic): 0.03 kg

Both materials are transported by 16–32 ton lorry to the German factory:
- Nylon travels 50 km → 0.03 × 50 = 1.5 kg·km
- PLA travels 200 km → 0.52 × 200 = 104 kg·km
- Total: 105.5 kg·km = 0.1055 thousand kg·km

Expected total: 1.7 kg CO₂ per broom, with ~82% from PLA, ~16% from nylon, ~1.4% from transport.
