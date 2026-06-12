---
name: Levi's 501 Jeans — wash every 5 wears (Group 1, Scenario C)
goal: >
  Reproduce the Levi's 2015 LCA consumer care scenario where the consumer
  washes their jeans once every 5 times they wear them — roughly twice as
  infrequently as the US average. US consumer, conventional washing machine,
  average mix of cold/warm water and tumble dry.
  Based on Levi Strauss & Co.'s 2015 LCA study.

functional_unit:
  description: One pair of Levi's 501 jeans — full lifecycle, wash every 5 wears
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
    - { name: CO2 to air, unit: kg }

processes:
  - name: P1 — Grow and harvest cotton
    reference_output: { flow: Raw cotton, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 2.9 }

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
      - { flow: Electricity,    amount: 12.30 }
    emissions:
      - { flow: CO2 to air, amount: 6.4 }

  - name: P5 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.5 }

reference_process: P4 — Distribute, wash, dry, and dispose of jeans
---

## About this scenario

Group 1, Scenario C — wash every 5 wears.

Consumer care CO₂ from the Levi's PDF: 6.15 kg.
P4 electricity = 6.15 / 0.5 = 12.30 kWh.
Expected full lifecycle total: ~27.1 kg CO₂.
