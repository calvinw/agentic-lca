---
name: "Experiment 2 — 4 emissions + 3 extractions"
goal: "3-node linear chain with emissions on all nodes and extractions on two nodes."

functional_unit:
  description: One finished Widget
  amount: 1.0
  unit: widget

units:
  widget: Widget count
  part:   Part count
  kg:     Mass
  L:      Volume
  kWh:    Energy

products:
  - { name: Widget,   unit: widget }
  - { name: Part,     unit: part   }
  - { name: Material, unit: kg    }

elementary_flows:
  emissions:
    - { name: CO2 to air,  unit: kg }
    - { name: CH4 to air,  unit: kg }
    - { name: SO2 to air,  unit: kg }
    - { name: NOx to air,  unit: kg }
  resources:
    - { name: Water,      unit: L   }
    - { name: Ore,        unit: kg  }
    - { name: Crude oil,  unit: L   }

processes:
  - name: "P1 — Assemble Widget"
    reference_output: { flow: Widget, amount: 1.0 }
    inputs:
      - { flow: Part, amount: 2.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.5 }
      - { flow: SO2 to air, amount: 0.1 }

  - name: "P2 — Make Part"
    reference_output: { flow: Part, amount: 1.0 }
    inputs:
      - { flow: Material, amount: 0.5 }
    emissions:
      - { flow: NOx to air, amount: 0.3 }
    resources:
      - { flow: Water,     amount: 3.0 }
      - { flow: Crude oil, amount: 0.8 }

  - name: "P3 — Extract Material"
    reference_output: { flow: Material, amount: 1.0 }
    emissions:
      - { flow: CH4 to air, amount: 1.2 }
    resources:
      - { flow: Ore, amount: 4.0 }

reference_process: "P1 — Assemble Widget"
---
