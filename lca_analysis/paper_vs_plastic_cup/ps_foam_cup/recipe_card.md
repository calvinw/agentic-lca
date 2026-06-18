---
name: "Polystyrene Foam Cup LCA — cradle to grave"
goal: >
  Calculate the total environmental impact of producing and disposing of
  one polystyrene (PS) foam cup used to serve one hot beverage, tracing
  the full supply chain from petrochemical feedstock through manufacturing,
  distribution, and landfill disposal.
  Compare with the paper cup to determine which has lower impact.

functional_unit:
  description: "One PS foam cup used to serve one hot beverage (approx. 355 mL)"
  amount: 1
  unit: cup

system_boundary: "Cradle to grave: petrochemical extraction → resin production → cup manufacturing → distribution → landfill disposal"

units:
  cup: Cup count
  kg: Mass
  L: Volume
  MJ: Energy

products:
  - { name: Raw materials for PS cup, unit: cup }
  - { name: PS foam cup, unit: cup }
  - { name: Electricity for PS cup, unit: MJ }
  - { name: Steam for PS cup, unit: MJ }
  - { name: Transport for PS cup, unit: MJ }
  - { name: Landfill disposal PS, unit: cup }

elementary_flows:
  emissions:
    - { name: Carbon dioxide,  compartment: air, unit: kg }
    - { name: Methane,         compartment: air, unit: kg }
    - { name: Sulfur dioxide,  compartment: air, unit: kg }
    - { name: Nitrogen oxides, compartment: air, unit: kg }
  resources:
    - { name: Water, unit: L }

processes:
  - name: P1 — Petrochemical and resin production
    reference_output: { flow: Raw materials for PS cup, amount: 1 }
    resources:
      - { flow: Water, amount: 0.7 }

  - name: P2 — PS foam cup manufacturing
    reference_output: { flow: PS foam cup, amount: 1 }
    inputs:
      - { flow: Raw materials for PS cup, amount: 1 }
      - { flow: Electricity for PS cup,   amount: 0.012 }
      - { flow: Steam for PS cup,         amount: 0.031 }
      - { flow: Transport for PS cup,     amount: 0.003 }
      - { flow: Landfill disposal PS,     amount: 1 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.002 }
      - { flow: Nitrogen oxides, amount: 0.00001 }

  - name: P3 — Grid electricity
    reference_output: { flow: Electricity for PS cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.1 }
      - { flow: Sulfur dioxide, amount: 0.001 }

  - name: P4 — Steam generation
    reference_output: { flow: Steam for PS cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.056 }
      - { flow: Sulfur dioxide, amount: 0.0001 }

  - name: P5 — Road transport
    reference_output: { flow: Transport for PS cup, amount: 1 }
    emissions:
      - { flow: Carbon dioxide,  amount: 0.074 }
      - { flow: Sulfur dioxide,  amount: 0.0002 }

  - name: P6 — Landfill disposal
    reference_output: { flow: Landfill disposal PS, amount: 1 }
    emissions:
      - { flow: Methane, amount: 0.000004 }

reference_process: "P2 — PS foam cup manufacturing"

lcia:
  method_name: "TRACI 2.2"
---

# Polystyrene Foam Cup LCA — Cradle to Grave

## Data source

Based on Hocking (1991, 1994) and Franklin Associates, as presented in
*LCA_Paper_vs_Plastic_Cup_v2.xlsx*. Values are illustrative order-of-magnitude
estimates suitable for teaching.

## Supply chain

| Process | What it does |
|---|---|
| P1 — Petrochemical and resin production | Produces PS resin (3.5 g) and petroleum feedstock (5.5 g); withdraws 0.7 L of freshwater |
| P2 — PS foam cup manufacturing | Moulds polystyrene into one finished cup; uses electricity, steam, and transport; emits CO₂ and NOₓ |
| P3 — Grid electricity | Supplies 0.012 MJ of electricity to the factory; emits 0.1 kg CO₂/MJ |
| P4 — Steam generation | Supplies 0.031 MJ of process heat; emits 0.056 kg CO₂/MJ |
| P5 — Road transport | Delivers cup to point of sale; emits 0.074 kg CO₂/MJ of diesel |
| P6 — Landfill disposal | Cup goes to landfill; PS does not biodegrade, emits minimal CO₂ (0.0001 kg) |

## Expected results

| Impact | Value |
|---|---|
| Global warming (CO₂-eq) | ~0.005 kg |
| Freshwater withdrawn | 0.7 L |

The PS foam cup has **lower GWP** (~0.005 kg) than the paper cup (~0.011 kg) because
PS manufacturing requires less energy and PS does not decompose in landfill (no methane).
However, PS uses **far less water** (0.7 L vs 14.3 L) but relies on non-renewable
petroleum feedstock and does not biodegrade — impacts not fully captured here.
