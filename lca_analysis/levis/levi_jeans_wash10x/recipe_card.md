---
name: Levi's 501 Jeans — wash every 10 wears (Group 1, Scenario D)
goal: >
  Reproduce the Levi's 2015 LCA best-practice consumer care scenario:
  the consumer washes their jeans only once every 10 times they wear them —
  the recommendation from Levi's "Care Tag for Our Planet" campaign.
  US consumer, conventional washing machine, average mix of cold/warm water
  and tumble dry. Based on Levi Strauss & Co.'s 2015 LCA study.

functional_unit:
  description: One pair of Levi's 501 jeans — full lifecycle, wash every 10 wears
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
      - { flow: Electricity,    amount: 6.16 }
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

Group 1, Scenario D — best-practice washing frequency (wash every 10 wears).

This is the behaviour Levi's actively encourages through their "Care Tag for
Our Planet" campaign. Consumer care CO₂ from the Levi's PDF: 3.08 kg.
P4 electricity = 3.08 / 0.5 = 6.16 kWh.
Expected full lifecycle total: ~24.0 kg CO₂.
