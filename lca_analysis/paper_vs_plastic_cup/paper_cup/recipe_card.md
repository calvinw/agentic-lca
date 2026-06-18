---
name: "Paper Cup LCA — cradle to grave"
goal: >
  Calculate the total environmental impact of producing and disposing of
  one paper cup used to serve one hot beverage, tracing the full supply
  chain from wood pulp through manufacturing, distribution, and landfill.
  Compare with the PS foam cup to determine which has lower impact.

functional_unit:
  description: "One paper cup used to serve one hot beverage (approx. 355 mL)"
  amount: 1
  unit: cup

system_boundary: "Cradle to grave: forestry → raw material production → cup manufacturing → distribution → landfill disposal"

units:
  cup: Cup count
  kg: Mass
  L: Volume
  MJ: Energy

products:
  - { name: Raw materials for paper cup, unit: cup }
  - { name: Paper cup, unit: cup }
  - { name: Electricity for paper cup, unit: MJ }
  - { name: Steam for paper cup, unit: MJ }
  - { name: Transport for paper cup, unit: MJ }
  - { name: Landfill disposal paper, unit: cup }

elementary_flows:
  emissions:
    - { name: Carbon dioxide,  compartment: air, unit: kg }
    - { name: Methane,         compartment: air, unit: kg }
    - { name: Sulfur dioxide,  compartment: air, unit: kg }
    - { name: Nitrogen oxides, compartment: air, unit: kg }
  resources:
    - { name: Water, unit: L }

processes:
  - name: P1 — Forestry and raw material production
    reference_output: { flow: Raw materials for paper cup, amount: 1 }
    resources:
      - { flow: Water, amount: 14.3 }

  - name: P2 — Paper cup manufacturing
    reference_output: { flow: Paper cup, amount: 1 }
    inputs:
      - { flow: Raw materials for paper cup, amount: 1 }
      - { flow: Electricity for paper cup,   amount: 0.025 }
      - { flow: Steam for paper cup,         amount: 0.062 }
      - { flow: Transport for paper cup,     amount: 0.005 }
      - { flow: Landfill disposal paper,     amount: 1 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.004 }
      - { flow: Nitrogen oxides, amount: 0.00002 }

  - name: P3 — Grid electricity
    reference_output: { flow: Electricity for paper cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.1 }
      - { flow: Sulfur dioxide, amount: 0.001 }

  - name: P4 — Steam generation
    reference_output: { flow: Steam for paper cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.056 }
      - { flow: Sulfur dioxide, amount: 0.0001 }

  - name: P5 — Road transport
    reference_output: { flow: Transport for paper cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.074 }
      - { flow: Sulfur dioxide,  amount: 0.0002 }

  - name: P6 — Landfill disposal
    reference_output: { flow: Landfill disposal paper, amount: 1 }
    emissions:
      - { flow: Methane, amount: 0.000032 }

reference_process: "P2 — Paper cup manufacturing"

lcia:
  method_name: "TRACI 2.2"
---

# Paper Cup LCA — Cradle to Grave

## Data source

Based on Hocking (1991, 1994) and Franklin Associates, as presented in
*LCA_Paper_vs_Plastic_Cup_v2.xlsx*. Values are illustrative order-of-magnitude
estimates suitable for teaching.

## Supply chain

| Process | What it does |
|---|---|
| P1 — Forestry and raw material production | Grows trees, produces wood pulp (10.1 g) and PE coating resin (1.5 g); withdraws 14.3 L of freshwater |
| P2 — Paper cup manufacturing | Converts raw materials into one finished cup; uses electricity, steam, and transport; emits CO₂ and NOₓ from combustion |
| P3 — Grid electricity | Supplies 0.025 MJ of electricity to the factory; emits 0.1 kg CO₂/MJ |
| P4 — Steam generation | Supplies 0.062 MJ of process heat; emits 0.056 kg CO₂/MJ |
| P5 — Road transport | Delivers cup to point of sale; emits 0.074 kg CO₂/MJ of diesel |
| P6 — Landfill disposal | Cup goes to landfill; paper decomposes and emits CH₄ (modelled as 0.0008 kg CO₂-eq) |

## Expected results

| Impact | Value |
|---|---|
| Global warming (CO₂-eq) | ~0.011 kg |
| Freshwater withdrawn | 14.3 L |

The paper cup uses roughly **20× more water** than the PS foam cup (14.3 L vs 0.7 L)
because pulping and papermaking are highly water-intensive. However, paper has a
higher GWP (~0.011 kg) compared to PS foam (~0.005 kg) due to the energy-intensive
pulping process and methane from landfill decomposition.
