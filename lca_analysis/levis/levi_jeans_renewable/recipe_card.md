---
name: Levi's 501 Jeans — renewable energy supply chain (Custom Scenario A)
goal: >
  Model the impact of switching the entire textile supply chain — fabric mills
  and garment factory — from a coal-heavy electricity grid to renewable energy
  (solar or wind). The electricity emission factor drops from 0.5 kg CO₂/kWh
  down to 0.05 kg CO₂/kWh. Everything else is identical to the baseline.
  Question: what is the value of a brand moving its supply chain to green energy?

functional_unit:
  description: One pair of Levi's 501 jeans — full lifecycle, renewable energy supply chain
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
      - { flow: Carbon dioxide,  amount: 0.05     }
      - { flow: Nitrogen oxides, amount: 0.00009  }
      - { flow: Sulfur dioxide,  amount: 0.00006  }

reference_process: P4 — Distribute, wash, dry, and dispose of jeans

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

Custom Scenario A — renewable energy supply chain.

The only change from the baseline is P5's emission factor: 0.5 → 0.05 kg CO₂/kWh.
This represents a grid powered by solar or wind (a ~90% reduction in electricity
carbon intensity).

The baseline uses 48.2 kWh total electricity per pair of jeans.
At 0.05 kg CO₂/kWh that produces 48.2 × 0.05 = 2.41 kg CO₂ via electricity.
The remaining direct emissions are: P1 (2.9 kg) + P4 direct (6.4 kg) = 9.3 kg.
Expected total: 9.3 + 2.41 = ~11.7 kg CO₂.
