---
name: Levi's 501 Jeans — twice as durable (Custom Scenario D)
goal: >
  Model the impact of jeans that last twice as long as average. If the product
  lifetime doubles, only half a manufacturing cycle is needed to cover the same
  period of use — so P4 only demands 0.5 pairs of finished jeans instead of 1.0.
  Consumer care washing stays the same (you still wash the same number of times
  per wear over the period). Question: how much does product durability reduce
  the lifecycle footprint compared to buying a replacement pair?

functional_unit:
  description: One pair of Levi's 501 jeans — full lifecycle, twice standard durability
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
      - { flow: Finished jeans, amount: 0.5  }
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

## About this scenario

Custom Scenario D — twice as durable.

The only change from the baseline is P4's input of Finished jeans: 1.0 → 0.5.
This halves the manufacturing burden (P1, P2, P3 all scale to 0.5) while keeping
consumer care identical (same washing electricity, same direct CO₂ for transport
and end of life).

Expected scaling:
  P1 = 0.5, P2 = 0.4, P3 = 0.5, P4 = 1.0
  P5 electricity = (22.5×0.4) + (5.2×0.5) + 25.0 = 9.0 + 2.6 + 25.0 = 36.6 kWh

CO₂: P1 (1.45) + electricity (18.3) + P4 direct (6.4) = ~26.2 kg CO₂.
