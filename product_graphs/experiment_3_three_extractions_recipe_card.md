---
name: "Experiment 3 — 8 extractions + 2 emissions"
goal: "3-node linear chain with 8 extractions across all nodes plus 2 emissions on P1."

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
  m3:     Volume cubic
  MJ:     Energy

products:
  - { name: Widget,   unit: widget }
  - { name: Part,     unit: part   }
  - { name: Material, unit: kg    }

elementary_flows:
  emissions:
    - { name: CO2 to air,  unit: kg }
    - { name: SO2 to air,  unit: kg }
  resources:
    - { name: Water,       unit: L  }
    - { name: Crude oil,   unit: L  }
    - { name: Ore,         unit: kg }
    - { name: Natural gas, unit: m3 }
    - { name: Coal,        unit: kg }
    - { name: Limestone,   unit: kg }
    - { name: Bauxite,     unit: kg }
    - { name: Silica sand, unit: kg }

processes:
  - name: "P1 — Assemble Widget"
    reference_output: { flow: Widget, amount: 1.0 }
    inputs:
      - { flow: Part, amount: 2.0 }
    emissions:
      - { flow: CO2 to air, amount: 0.5 }
      - { flow: SO2 to air, amount: 0.1 }
    resources:
      - { flow: Crude oil,   amount: 0.5 }
      - { flow: Limestone,   amount: 1.2 }
      - { flow: Silica sand, amount: 0.8 }

  - name: "P2 — Make Part"
    reference_output: { flow: Part, amount: 1.0 }
    inputs:
      - { flow: Material, amount: 0.5 }
    resources:
      - { flow: Water,       amount: 3.0 }
      - { flow: Natural gas, amount: 1.2 }
      - { flow: Bauxite,     amount: 2.0 }

  - name: "P3 — Extract Material"
    reference_output: { flow: Material, amount: 1.0 }
    resources:
      - { flow: Ore,  amount: 4.0 }
      - { flow: Coal, amount: 2.5 }

reference_process: "P1 — Assemble Widget"
---
