---
name: Levi's 501 Jeans — organic cotton farm (Custom Scenario B)
goal: >
  Model the impact of switching from conventional cotton to organic cotton.
  Organic cotton avoids synthetic nitrogen fertilisers, which are a major
  source of CO₂ and N₂O emissions on conventional cotton farms. The farm
  emission factor drops from 2.9 kg to 1.5 kg CO₂ per kg of raw cotton.
  Everything else is identical to the baseline.
  Question: is the "organic cotton" label actually meaningful for climate impact?

functional_unit:
  description: One pair of Levi's 501 jeans — full lifecycle, organic cotton
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
      - { flow: Carbon dioxide, amount: 1.5 }

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

## About this scenario

Custom Scenario B — organic cotton farm.

The only change from the baseline is P1's emission factor: 2.9 → 1.5 kg CO₂/kg cotton.
This represents a roughly 48% reduction in farm-level CO₂, reflecting the removal of
synthetic nitrogen fertilisers and reduction in machinery use.

Saving = 2.9 - 1.5 = 1.4 kg CO₂ per kg cotton × 1.0 kg cotton per pair = 1.4 kg saved.
Expected total: 33.4 - 1.4 = ~32.0 kg CO₂.
