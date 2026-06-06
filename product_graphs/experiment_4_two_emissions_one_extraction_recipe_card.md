---
name: "Experiment 4 — 6 emissions + 4 extractions (convergent)"
goal: "Convergent topology with 6 emissions and 4 extractions across all three nodes."

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
  - { name: Widget, unit: widget }
  - { name: Part,   unit: part   }
  - { name: Raw,    unit: kg    }

elementary_flows:
  emissions:
    - { name: CO2 to air,  unit: kg }
    - { name: SO2 to air,  unit: kg }
    - { name: NOx to air,  unit: kg }
    - { name: CH4 to air,  unit: kg }
    - { name: CO to air,   unit: kg }
    - { name: PM to air,   unit: kg }
  resources:
    - { name: Water,      unit: L  }
    - { name: Ore,        unit: kg }
    - { name: Crude oil,  unit: L  }
    - { name: Natural gas, unit: kWh }

processes:
  - name: "P1 — Assemble Widget"
    reference_output: { flow: Widget, amount: 1.0 }
    inputs:
      - { flow: Part, amount: 3.0 }
      - { flow: Raw,  amount: 0.5 }
    emissions:
      - { flow: CO2 to air, amount: 0.8 }
      - { flow: CO to air,  amount: 0.3 }
    resources:
      - { flow: Water,      amount: 2.0 }
      - { flow: Ore,        amount: 1.5 }
      - { flow: Crude oil,  amount: 0.6 }

  - name: "P2 — Make Part"
    reference_output: { flow: Part, amount: 1.0 }
    emissions:
      - { flow: SO2 to air, amount: 0.7 }
      - { flow: NOx to air, amount: 0.5 }
      - { flow: PM to air,  amount: 0.2 }
    resources:
      - { flow: Natural gas, amount: 1.0 }

  - name: "P3 — Extract Raw"
    reference_output: { flow: Raw, amount: 1.0 }
    emissions:
      - { flow: CH4 to air, amount: 0.4 }

reference_process: "P1 — Assemble Widget"
---
