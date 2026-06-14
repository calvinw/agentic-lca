---
name: Nordic Textile Waste — Scenario 2A — Cotton incineration with energy recovery
goal: >
  Model the climate change impact of incinerating one kilogram of used 100% cotton
  textiles at a Nordic waste-to-energy plant, including the credit for electricity
  and heat recovered. The system boundary starts at the point of textile collection
  (end of life) and ends at final disposal. Cotton fibre is biogenic (plant-based)
  so its CO₂ when burned is excluded — only fossil CO₂ from auxiliary materials
  (dyes, finishes, processing chemicals) is counted. Avoided burdens from displaced
  Nordic marginal electricity and heat are included as CO₂ credits.
  Based on Schmidt et al., TemaNord 2016:537.

functional_unit:
  description: Treatment of one kilogram of used 100% cotton textiles — collection to final grave
  amount: 1.0
  unit: kg

units:
  kg:  Mass in kilograms (the cotton textile)
  kWh: Energy in kilowatt-hours (electricity and heat recovered)

products:
  - { name: Cotton incineration service, unit: kg  }
  - { name: Nordic electricity credit,   unit: kWh }
  - { name: Nordic heat credit,          unit: kWh }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }

# ─────────────────────────────────────────────────────────────────────────────
# HOW AVOIDED BURDENS WORK IN THIS MODEL
#
# When the incinerator burns cotton it generates electricity and heat that
# it feeds into the Nordic grids. Those grids then do NOT have to generate
# that energy themselves, so the CO₂ those power stations would have emitted
# is SAVED. We model this by giving P2 and P3 a NEGATIVE emission factor:
# every kWh of "credit" that P2 or P3 "produces" carries a negative number
# of kg CO₂ — i.e. a saving.
#
# P1 (incineration) consumes 0.576 kWh of electricity credit and 3.194 kWh
# of heat credit. The scaling vector solution causes P2 to run 0.576 times
# and P3 to run 3.194 times, producing exactly those savings.
#
# Net CO₂ = +0.046 (fossil from combustion)
#           – 0.576 × 0.021 (electricity saving)
#           – 3.194 × 0.071 (heat saving)
#         = +0.046 – 0.012 – 0.227
#         = –0.193 kg CO₂ per kg cotton
# ─────────────────────────────────────────────────────────────────────────────

processes:
  - name: P1 — Incinerate cotton in Nordic waste-to-energy plant
    reference_output: { flow: Cotton incineration service, amount: 1.0 }
    inputs:
      - { flow: Nordic electricity credit, amount: 0.576 }
      - { flow: Nordic heat credit,        amount: 3.194 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.046 }

  - name: P2 — Nordic marginal electricity displaced by energy recovery
    reference_output: { flow: Nordic electricity credit, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: -0.021 }

  - name: P3 — Nordic marginal heat displaced by energy recovery
    reference_output: { flow: Nordic heat credit, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: -0.071 }

reference_process: P1 — Incinerate cotton in Nordic waste-to-energy plant

lcia:
  method_name: "TRACI 2.2"
---

## About this scenario

**Source:** Schmidt, A. et al. (2016). *Gaining benefits from discarded textiles —
LCA of different treatment pathways.* TemaNord 2016:537. Nordic Council of Ministers.

**Scenario 2A** is the baseline end-of-life option in the Nordic study: cotton
textiles are collected from households and organisations, transported to a Nordic
waste-to-energy (incineration) plant, and burned. The energy released heats water
and drives a turbine to generate electricity. Both the electricity and heat are
fed into the local grid.

---

### Key numbers from the PDF

| Data point | Value | Source |
|---|---|---|
| Fossil CO₂ from burning 1 kg cotton | 0.046 kg | Table 7 / Figure 10 |
| Electricity recovered per kg cotton (Nordic avg.) | 2.075 MJ = 0.576 kWh | Table 7 (avg. of DK, FI, NO, SE) |
| Heat recovered per kg cotton (Nordic avg.) | 11.5 MJ = 3.194 kWh | Table 7 (avg. of DK, FI, NO, SE) |
| Marginal electricity CO₂ factor (Nordic avg.) | 0.021 kg CO₂/kWh | Table 4 (2020–2030 scenario) |
| Marginal heat CO₂ factor (Nordic avg.) | 0.071 kg CO₂/kWh | Table 5 (2020–2030 scenario) |

### Why cotton CO₂ from burning is almost zero

Cotton is made from plant fibres. While the plant was growing, it absorbed CO₂
from the atmosphere. When it burns, that same CO₂ is released back. The net
effect on atmospheric CO₂ is therefore close to zero — the CO₂ was "borrowed"
from the air and returned, not added from underground fossil reserves. This is
called **biogenic carbon**, and under standard LCA methodology it is excluded
from the climate change score. Only the fossil CO₂ from the small amounts of
synthetic dyes, processing chemicals, and finishing agents is counted (0.046 kg/kg).

### Why the result is slightly negative

The Nordic electricity grid is dominated by wind, hydro, and nuclear — very
low carbon sources. The marginal CO₂ saved per kWh of electricity displaced is
therefore small (0.021 kg/kWh). However, the heat recovery is much larger in
volume (3.194 kWh of heat per kg cotton vs 0.576 kWh of electricity), and the
marginal heat in Denmark in particular involves some gas and coal, giving a
higher CO₂ factor (0.071 kg/kWh). Together, the energy savings outweigh the
small fossil CO₂ from combustion, producing a slight net benefit.

### Expected result

**−0.193 kg CO₂ per kg cotton** (approximately −193 kg CO₂ per tonne of cotton textiles)

This is a small net environmental benefit — meaning that incinerating cotton with
energy recovery is, from a climate perspective, marginally better than doing
nothing with it.