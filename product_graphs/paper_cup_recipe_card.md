---
name: Paper Cup LCA — one cup
goal: >
  Calculate the total CO₂ emitted to produce one paper cup,
  tracing the full chain from electricity generation through
  paper manufacturing to cup production.

functional_unit:
  description: One paper cup
  amount: 1.0
  unit: cup

units:
  cup: Cup count
  kg:  Mass
  kWh: Energy

products:
  - { name: Paper cup,   unit: cup }
  - { name: Paper,       unit: kg  }
  - { name: Electricity, unit: kWh }

elementary_flows:
  emissions:
    - { name: CO2 to air, unit: kg }

processes:
  - name: P1 — Make paper cup
    reference_output: { flow: Paper cup,   amount: 1.0  }
    inputs:
      - { flow: Paper,       amount: 0.02 }

  - name: P2 — Make paper
    reference_output: { flow: Paper,       amount: 1.0  }
    inputs:
      - { flow: Electricity, amount: 2.5  }

  - name: P3 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0  }
    emissions:
      - { flow: CO2 to air,  amount: 1.0  }

reference_process: P1 — Make paper cup
---

## About this analysis

Simple three-process chain used to study the carbon footprint of a disposable paper cup.

The chain is: electricity generation → paper manufacturing → cup production.
All CO₂ originates in P3 (generating electricity by burning coal); P1 and P2 have no direct emissions.

Expected result: **0.05 kg CO₂ per cup**.

---

## Product Graph

```mermaid
flowchart LR
    subgraph nature_in["🌍 From Nature"]
        coal["Coal\n(from ground)"]
    end

    subgraph tech["⚙️ Supply Chain (Technosphere)"]
        P3["P3 — Generate electricity\nProduces: 1 kWh"]
        P2["P2 — Make paper\nProduces: 1 kg paper"]
        P1["P1 — Make paper cup\nProduces: 1 cup"]
    end

    subgraph nature_out["🌍 To Nature"]
        co2["CO₂ to air\n1 kg per kWh"]
    end

    coal -->|fuel| P3
    P3 -->|"2.5 kWh"| P2
    P2 -->|"0.02 kg"| P1
    P1 -->|"1 cup"| fu["☕ 1 paper cup\n(functional unit)"]
    P3 -->|"1.0 kg CO₂"| co2
```
