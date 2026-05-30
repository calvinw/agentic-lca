# 01_life-cycle-inventory-databases-part-a_EHS672_3.3.4_LCI_Databases_STUDENT_COPY


---

<!-- Slide 1 -->

## Life Cycle Inventory DatabasesWhere to find consistent and high quality LCI data?
## Olivier Jolliet, PhD

---

<!-- Slide 2 -->

- Learning Objectives
- Describe the different life cycle inventory (LCI) databases
- Illustrate the data format of the ecoinvent database
- Recognize the different types of data and energy-based inventory flows, and use them adequately
- Identify sources for guidance for direct LCI data collection

---

<!-- Slide 3 -->

- CONSEQUENTIAL
- Main LCI database
## Two types of modeling, answering different questions
## “What are the environmental impacts related to those activities that are expected to change when producing, consuming, and disposing of the product?”
##  identify the marginal production (e.g. gas power plant or coal powerplant)
## “What are (the environmental impacts related to) the allocated shares of the activities that have contributed to the production, consumption, and disposal of the product?”
##  use average electricity mix
- ATTRIBUTIONAL:

---

<!-- Slide 4 -->

- LCI Data
## Existing databases for all background processes, ensuring consistency between data – A lot of data are available!
## 1
## 2
- Finding appropriate LCI data will rely on:
## 3
## Adapting existing data to the product or service, technology and country or region studied.
## Collection of new LCI data, especially for the foreground system.Hard work and requires to be very systematic.

---

<!-- Slide 5 -->

- Global LCA Data Access network (GLAD)
## 1

---

<!-- Slide 6 -->

- Main LCI databases
## Other available databases in Japan, Korea, China, Australia
## Ecoinvent database developed by research institutions for the Swiss government
## European Platform on Life Cycle Assessment – Product Environmental Footprint (PEF)select data from either node or database – some are free
## US databases
## Input-output data: 400+ sectors for US – Access via SIMAPRO
## Sector specific databases (e.g. agriculture and foods)
## Agrifootprint database – access via SimaproWorld Food database: Quantis – access via EU platform – nodeAgribalyse – Access via the GLAD network
## LCA commons - access to USDA LCI data sets

---

<!-- Slide 7 -->

- The Ecoinvent database
- Energy systems - non renewable & renewable
- Materials and building
- Chemicals and metals
- Transports
- Packaging
- Waste treatment
- Agriculture
- The broadest Unit Process level database worldwide
- 400 Inventory flows for 4000 unit processes

---

<!-- Slide 8 -->

- Aggregated or unit processes in databases
- The ecoinvent database provides all intermediary and elementary flows both
- for direct emissions and extractions at unit process level (U=UP level), and
- for aggregated inventory emissions and extractions of a given product, summed up over the entire supply chain from “cradle to gate” (S=system level)
- Many other databases only provide aggregated flows

---

<!-- Slide 9 -->

- Life cycle inventory database
## Calculate the aggregated inventory flows of the total system per FU
## 1
## 2
## 3
## 4
- Life cycle databases provide either:
- The direct intermediary and elementary flows at the Unit Process level
- The aggregated flows at the System level, accounting for the entire supply chain of the considered process
- OR
## Find the direct emission and extraction factors of each unit process
## Identify the amount of each Unit process per FU
## Calculate the elementary flows of each UP per FU

---

<!-- Slide 10 -->

## Direct intermediary and elementary flows at Unit Process level
## 1
## Aluminum,
## primary,
## liquid
### 1 kg
### Transport, transoceanic freight ship 3.8 tkm
### Disposal, filter dust Al electrolysis 2.00 g
### Electricity mix, aluminum industry 15.9 kWh
### Heat, light fuel oil 0.089 MJ
### Heat, natural gas 0.084 MJ
### Aluminum electrolysis plant 1.54·10-10 p
### Aluminum oxide 1.93 kg
### Anode, aluminum electrolysis 0.448 kg
### Cathode, aluminum electrolysis 0.0181 kg
### Disposal, redmud from bauxite digestion 1.36 kg
### Nitrogen oxides 63.9 mg
### Heat, waste 56.0 MJ/kg Al primary liquid
### Hydrogen fluoride 539 mg
### Benzo(a)pyrene 1.30 mg
### Carbon dioxide, fossil 1.50 kg
### Carbon monoxide, biogenic 91.7 g
### PAH 45.7 mg
### Particulates, < 2.5 µm 2.61 g
### Sulfur dioxide 8.83 g
## These are the direct intermediary flows and emission or extraction from the considered process, i.e. the direct elementary flows per unit of this UP

---

<!-- Slide 11 -->

- Unit Process data: aluminum liquid, ecoinvent in Simapro
### Disposal intermediary processes
### Product output
### Direct Resource extractions

---

<!-- Slide 12 -->

- Unit Process data: aluminum liquid, ecoinvent in Simapro
### Direct emissions to air
### Disposal intermediary processes
### Data quality pedigree
### 1=best, 5=worst
### Data uncertainty
## Data uncertainty: For a lognormal distribution, an SD2 of 3 means that the 95% confidence interval is between amount/3 and amount × 3

---

<!-- Slide 13 -->

## Aggregated inventory at system level: aluminum primary liquid
## These are ALL elementary flows since by definition the aggregated inventory is the sum of all elementary flows per FU of all unit processes
## Aluminum,
## primary,
## liquid
### 1 kg
### Methane, biogenic 51.7 mg
### Crude oil in ground 1.18 kg
### Natural gas in ground 525 dm3
### Brown coal in ground 1.20 kg
### Nitrogen oxides 19.6 g
### Carbon monoxide, biogenic 91.8 g
### Heat, waste 66.6 MJ
### Carbon dioxide, fossil 9.40 kg
### Arsenic 1.88 mg
### Arsenic, ion 44.0 mg
### Benzo[a]pyrene 2.74 mg
### CFC-14 252 mg
### Dioxins 1.74 ng
### HFC-116 28.2 mg
### Hydrogen fluoride 676 mg
### PAH 88.7 mg
### Sulfur dioxide 38.0 g
### Uranium in ground 58.3 mg
### Aluminum in ground, 24% in bauxite, 11% in crude ore 1.16 kg
### Occupation, forest, intensive 0.101 m2a
- Hard coal in ground 2.01 kg
## 4

---

<!-- Slide 14 -->

## Aggregated system data: aluminum liquid, ecoinvent in Simapro
### Aggregated Resource extractions from environment

---

<!-- Slide 15 -->

## Aggregated system data: aluminum liquid, ecoinvent in Simapro
### Aggregated emissions to air

---

<!-- Slide 16 -->

- Use of ecoinvent: tips for good use – be careful
## Be sure to include end-of-life process & only use fossil CO2, not biogenic CO2. Avoid to use heavy metal uptake by crops.
## ELECTRICITY:select the mix corresponding to each scenario
## Medium voltage for industrial use, Low voltage for household use
## TRANSPORT:beware the load rate
## (includes 40% empty trips for trucks)
## Data in energy sector available in three forms:
## Energy data per fuel unit quantity, e.g. per kg oil or liter gasoline: without combustion,
## Energy per MJ final (bought) energy: "burned" = with combustionUse the net calorific values to convert back to fuel quantities (kg oil, m3 gas or liter gasoline)
## Energy per MJ useful (delivered) energy: "heat" = with combustion

---

<!-- Slide 17 -->

- Use of ecoinvent: Air emissions interpretation
## Benzene emissions are reported under “benzene” rather than “aromatic hydrocarbons” or “non-methane volatile organic compounds” (NMVOCs).
## Particulate emissions classified between PM2.5 (particles less than 2.5 µm in aerodynamic diameter) , PM10-PM2.5 and TPM-PM10 (greater than 10 µm).
## For CO2, CO, and CH4, a distinction is made between fossilized sources and biogenic sources in that case CO2 fixed during biomass growth is accounted for  special care to ensure that the corresponding combustion of CO2 is also taken into account during use or product end-of-life (e,g, incineration, landfill). A pragmatic solution to ensure reliability is to only account for fossil (non-biogenic)
## For the polycyclic aromatic hydrocarbons (PAHs), benzo[a]pyrene emissions are separate.
## The dioxin and furan emissions are expressed as equivalent 2,3,7,8-trichloro-dibenzodioxine (TCDD) emissions.

---

<!-- Slide 18 -->

- New features of ecoinvent 3
## Modelling of water flows
## Updated datasets for electricity production (>20 additional countries worldwide), wood sector, recycling activities, chemicals, fruit and vegetables.
## Different modelling strategies: attributional, cut-off and consequential modeling.
## At present recommended to use the cut-off version (called “recycled content unit option”). In the cut-off model, the primary producer does not receive any credit for the provision of any recyclable materials. As a consequence, recyclable materials are available burden-free to recycling processes.
## In the future, allocation at the point of substitution could be of interest… but if separation first applied

---

<!-- Slide 19 -->

- Collecting LCI data
### See Sonneman et al., 2.2.3.1 Global guidance principles
## The following options for data collection exist, as data collection procedures or sources:
## Primary data can include
## interviews, questionnaires or surveys, bookkeeping or enterprise, resource planning (ERP) system, data collection tools (online, offline) and on-site measurements.
## Secondary data can include
## interviews, statisticsand literature
## Data generation can include
## calculations (e.g., missing emission factors from input data) and estimates.

---

<!-- Slide 20 -->

- Data collection: focus on the foreground system
## Whenever possible, primary data shall be collected for all foreground processes and significant background processes under the financial control or operational control of the company undertaking the product inventory. For all other processes, data of the highest quality shall be collected.
## This can be achieved by extrapolation, adapting a similar (but not representative) process to match the considered process, or by simply using a similar process as a proxy.
## Sonnemann and Vigon (2011) provide additional guidance on how to collect data for a given unit process.
## As suggested by the greenhouse gas protocol (WRI and WBCSD 2011, appendix C), it may be useful to establish a management plan,
## identifying all unit processes,
## collecting screening data for all processes, and
## refining the data collection for the processes contributing most to the Life Cycle Impacts.

---

<!-- Slide 21 -->

- Summary
- Availability of LCI data has made the realization of an LCA substantially easier, enabling the practitioner to focus on the foreground system
- Consistency between background data (e.g. electricity mix) is key when comparing different products
- Care must be take when using ecoinvent data to recognize what type of energy and resource use is has been modelled for a given process
- Direct LCI data collection is hard work!
