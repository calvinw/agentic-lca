# Life Cycle Assessment - Structured Knowledge Base

*Organized by core LCA concepts for comprehensive understanding*

---

## Part 1: Foundations & Overview

### 1.1 What is Life Cycle Assessment (LCA)?

**Definition:** Life Cycle Assessment is a standardized method to assess the environmental impact of products and systems over their entire life cycle, from cradle to grave (raw material extraction through end-of-life).

**Key Characteristics:**
- Holistic approach covering all life stages
- Quantitative methodology based on standards (ISO 14040/14044)
- Compares environmental impacts of products/systems
- Identifies improvement opportunities
- Used in product development and decision-making

**When to Use LCA:**
- Product development and improvement
- Comparative claims between products
- Ecolabeling and certification
- Policy and strategy development
- Supply chain optimization

**When NOT to Use LCA:**
- Simple environmental comparisons (LCTs, LCA screening tools may be better)
- Single-issue assessments (use focused tools instead)
- When detailed data is unavailable
- When timeline is very limited

**Related Environmental Tools:**
- Life Cycle Costing (LCC)
- Environmental Risk Assessment
- Social Life Cycle Assessment (SLCA)
- Carbon footprint (subset of LCA)
- Streamlined LCA / Screening LCA

### 1.2 Brief History of LCA

**1960s-1970s:** Concept emergence ("Resource and Environmental Profile Analysis")

**1990s:** Standardization begins
- ISO 14040 published (1997)
- ISO 14041-14044 series developed

**2000s-Present:** Widespread adoption
- Environmental Product Declarations (EPD)
- Corporate sustainability reporting
- Supply chain transparency
- Regulatory requirements in some sectors

**Current Trends:**
- Integration with circular economy
- Social and economic dimensions
- Real-time digital product passports
- Scope 3 emissions in corporate reporting

---

## Part 2: LCA Phase 1 - Goal and Scope Definition

### 2.1 Goals of an LCA Study

**Primary Goals Define:**
- What question the LCA will answer
- Who will use the results
- How results will be communicated
- Level of detail required
- Types of impact categories
- Intended audience and applications

**Common Goal Types:**
1. **Product improvement** - Identify hotspots for environmental improvement
2. **Comparative claims** - Compare two products (must follow strict standards)
3. **Policy development** - Inform environmental regulations
4. **Supply chain optimization** - Identify sustainability opportunities
5. **Communication/Marketing** - Support environmental claims

**Critical Consideration:** The goal statement must be developed BEFORE the study to avoid bias

### 2.2 Scope Definition

#### 2.2.1 Product Function & Functional Unit

**Product Function:** What the product does for the user

**Functional Unit:** Quantified reference point for comparison
- Must be clearly defined
- Allows fair comparison between alternatives
- Examples:
  - "Packaging 1 liter of milk"
  - "Providing lighting for 50,000 hours in a residential room"
  - "Transporting 1 ton of cargo 1 km"
  - "Drying hands once for one person"

**Why It Matters:**
- Different products may serve the same function differently
- Functional unit ensures "apples to apples" comparison
- A lighter product might require more frequent replacement (higher life cycle impacts)

**Functional Unit Selection Example:**
- **NOT:** 1 plastic bag vs. 1 paper bag
- **YES:** "Carrying 10 kg of groceries from store to home" (a plastic bag can hold more, so fewer bags needed)

#### 2.2.2 Product System & System Boundaries

**Product System:** All processes required to fulfill the functional unit

**System Boundaries Include:**
- Raw material extraction
- Transportation between processes
- Manufacturing and processing
- Use/application phase
- End-of-life (disposal, recycling, reuse)
- Packaging and distribution

**What to Exclude:**
- Capital equipment (unless major impact)
- Personnel transport (usually negligible)
- Upstream energy production (already in energy inputs)
- Cleaning/maintenance of equipment (already in operations)

**Cradle-to-Grave vs. Cradle-to-Gate vs. Gate-to-Grave:**
- **Cradle-to-Grave:** Full product life cycle
- **Cradle-to-Gate:** Raw materials through manufacturing
- **Gate-to-Grave:** Manufacturing through disposal (for specific manufacturing stage)
- **Cradle-to-Cradle:** Includes recycling loops

**System Boundaries Visualization Example (Car):**
```
Mining → Steel/Aluminum Refining → Component Manufacturing → Assembly
    ↓                                                              ↓
   Transportation                                          Use Phase (150,000 km)
                                                                    ↓
                                          End-of-Life (Recycling/Disposal)
```

#### 2.2.3 Allocation in Multi-Product Systems

**Problem:** What if one process produces multiple products?

**Example:** Oil refining produces gasoline, diesel, heating oil, and chemical feedstock

**Allocation Methods:**
1. **Mass-based:** Allocate by mass of output
2. **Economic-based:** Allocate by economic value
3. **Process-based:** Subdivide processes where possible
4. **Input-output modeling:** Allocate based on economic relationships

**Best Practice:** Avoid allocation by subdividing processes when possible

---

## Part 3: LCA Phase 2 - Life Cycle Inventory (LCI)

### 3.1 Building the Life Cycle Inventory

**Purpose:** Quantify all flows in and out of the system
- **Elementary flows (inputs):** Energy, water, raw materials
- **Elementary flows (outputs):** Emissions to air, water, waste

**LCI Structure:**
1. Create process flow diagram
2. Define product tree (hierarchical breakdown)
3. Collect data for each process
4. Calculate energy and material balances
5. Aggregate flows across system
6. Allocate flows to functional unit

**Key Challenges:**
- Data availability and quality
- System boundary definition
- Temporal and geographical variations
- Allocation of shared processes
- Confidentiality of proprietary data

### 3.2 Primary Energy & CO2 Balance

**Primary Energy:** Total energy input to the system (not electricity alone)

**Energy Categories:**
- Renewable: Solar, wind, hydroelectric, geothermal, biomass
- Non-renewable: Fossil fuels (oil, coal, gas), nuclear

**CO2 Emissions Sources:**
1. **Combustion emissions:** Burning fuel releases CO2
   - Depends on fuel type and carbon content
   - Example: Natural gas (1 kg produces ~2 kg CO2)

2. **Process emissions:** Chemical reactions release CO2
   - Example: Limestone decomposition in cement production

3. **Upstream emissions:** Extraction, refining, transportation of energy
   - "Well-to-wheel" analysis for fuels

**Energy Balance Calculation:**
- Total primary energy = Direct fuel + Electricity (converted to primary)
- Electricity conversion: ~2.5-3.0 units primary energy per unit electricity (varies by grid)

**CO2 Balance Calculation:**
- Scope 1 (Direct): Emissions from burning fuel at the site
- Scope 2 (Indirect): Emissions from purchased electricity production
- Scope 3 (Other): Upstream/downstream emissions

### 3.3 LCI Databases

**Major Databases:**
- **ecoinvent:** Most comprehensive, covers Europe primarily, 20,000+ processes
- **USDA-NREL:** US agricultural data
- **GaBi:** Commercial database with geographic variations
- **OpenLCA:** Open-source database initiative
- **BEES:** Building-focused data

**Database Selection:**
- Geographic relevance (local vs. global data)
- Temporal relevance (how recent?)
- Process coverage (does it cover your products?)
- Transparency (methodology and sources documented?)
- Update frequency

**Using Database Data:**
- Typically for inputs (not product-specific data)
- Should be adjusted for location when possible
- Be aware of data year and methodology
- Check for allocation methods used

### 3.4 Special Topics: Allocation & Input-Output LCA

#### 3.4.1 Allocation Methods

**When Needed:** Multi-output systems (one process produces multiple products)

**Example 1: Oil Refining**
- One barrel of crude produces gasoline, diesel, fuel oil, naphtha
- How to allocate environmental burden?

**Example 2: Livestock**
- Beef and dairy production; by-products like leather, bone meal
- How to split between products?

**Allocation Hierarchy:**
1. **Avoid allocation:** Split processes where possible (best)
2. **Mass-based:** Allocate proportional to output mass
3. **Economic-based:** Allocate proportional to economic value
4. **Causal allocation:** Based on what causes the impact

**Mass vs. Economic - Example:**
```
Oil Refining (1 barrel crude = 100 kg)
├─ Gasoline 45 kg (60% mass, 85% value) → 60% or 85%?
├─ Diesel 35 kg (35% mass, 10% value) → 35% or 10%?
└─ Naphtha 20 kg (20% mass, 5% value) → 20% or 5%?
```

#### 3.4.2 Input-Output Life Cycle Assessment

**What it is:** Hybrid approach using economic input-output tables to fill data gaps

**When Used:**
- Background processes with missing data
- Supply chains that are complex/uncertain
- Upstream emissions estimation

**Advantages:**
- Comprehensive (covers entire supply chain)
- Fills data gaps
- Consistent methodology

**Disadvantages:**
- Less detailed than process LCA
- Aggregates diverse products
- Based on average economic data, not specific products
- Can include processes outside system boundary

**Hybrid LCA:** Combines detailed process LCA with input-output models for completeness

---

## Part 4: LCA Phase 3 - Life Cycle Impact Assessment (LCIA)

### 4.1 LCIA Principles & Framework

**Purpose:** Convert inventory data into environmental impact categories

**LCIA Steps:**
1. **Classification:** Assign inventory flows to impact categories
2. **Characterization:** Apply factors to quantify impact (midpoint)
3. **Normalization (optional):** Compare to baseline
4. **Grouping (optional):** Organize results
5. **Weighting (optional):** Value trade-offs between categories

### 4.2 Environmental Impact Categories

**Midpoint (Problem-Oriented) Indicators:**
- **Climate change:** kg CO2-eq (measure of warming potential)
- **Ozone depletion:** kg CFC-11-eq
- **Eutrophication:** kg PO4-eq (nutrient overload)
- **Acidification:** kg SO2-eq (acid rain)
- **Photochemical smog:** kg NMVOC-eq or kg O3-eq
- **Human toxicity:** CTUh (Comparative Toxic Unit)
- **Ecotoxicity:** CTUe
- **Resource depletion:** kg Sb-eq (antimony equivalent)
- **Ozone layer depletion:** kg CFC-11-eq

**Endpoint (Damage-Oriented) Indicators:**
- Damage to human health (DALY - Disability Adjusted Life Years)
- Damage to ecosystems (PDF·m²·year - Potentially Disappeared Fraction)
- Damage to resources (MJ-eq or cost-based)

**Common Methods:**
- **Impact World+:** Comprehensive, includes damage assessment
- **CML:** Problem-oriented, European standard
- **ReCiPe:** Combines problem and damage orientation
- **TRACI:** US-focused
- **BEES:** Building materials specific

### 4.3 LCIA Methodology - Characterization Example

**Example: Climate Change Assessment**

**Inventory:** 
- CO2 emission: 100 kg
- CH4 emission: 5 kg
- N2O emission: 0.1 kg

**Characterization Factors (GWP):**
- CO2: 1 kg CO2-eq per kg CO2
- CH4: 28 kg CO2-eq per kg CH4 (over 100 years)
- N2O: 265 kg CO2-eq per kg N2O

**Results:**
- CO2: 100 × 1 = 100 kg CO2-eq
- CH4: 5 × 28 = 140 kg CO2-eq
- N2O: 0.1 × 265 = 26.5 kg CO2-eq
- **Total: 266.5 kg CO2-eq**

### 4.4 LCIA Methodology - Damage Assessment

**From Midpoint to Endpoint:**

```
Inventory Flows
    ↓
Classification (assign to categories)
    ↓
Characterization (midpoint indicators)
    ↓
Damage Assessment (endpoint indicators)
    ↓
Human Health Damage (DALY)
Ecosystem Damage (PDF·m²·year)
Resource Depletion (MJ-eq)
```

**Example - Eutrophication Damage Chain:**
```
PO4 emissions → Nutrient loading in water → Algal bloom 
    → O2 depletion → Fish death → Ecosystem damage (PDF)
```

### 4.5 Normalization & Weighting

**Normalization (optional):**
- Compare results to reference baseline (e.g., average European impacts)
- Expresses results relative to "normal" levels
- Shows relative importance of impacts

**Weighting (optional but controversial):**
- Assigns relative importance to different impact categories
- Based on societal values (not scientific)
- Examples:
  - Climate change: 30% importance
  - Human toxicity: 20%
  - Eutrophication: 15%
  - etc.

**Warning:** Weighting is subjective and can bias results toward preferred outcomes

---

## Part 5: LCA Phase 4 - Interpretation

### 5.1 Interpreting LCA Results

**Key Findings:**
1. Identify **hotspots** (processes with highest impacts)
2. Assess **contribution analysis** (which activities/stages dominate?)
3. Evaluate **uncertainty** (data quality, variability)
4. Make **recommendations** for improvement

**Common Patterns:**
- **Use phase dominance:** For high-energy products (vehicles, appliances)
- **Manufacturing dominance:** For material-intensive products
- **Upstream dominance:** For goods with energy-intensive inputs
- **End-of-life dominance:** Rare, but occurs with hazardous disposal

### 5.2 Checks & Uncertainty Assessment

**Data Quality Checks:**
- Is inventory data recent? (±5 years acceptable)
- Geographic representativeness (local vs. average data)
- Technology representativeness (old vs. new processes)
- Completeness (all flows captured?)

**Sensitivity Analysis:**
- Which data assumptions most affect results?
- How much do results change with ±10% variations?
- Prioritize data collection efforts

**Uncertainty Sources:**
1. Data gaps (filled with estimates)
2. Methodological choices (allocation, system boundaries)
3. Temporal variations (seasonal, year-to-year)
4. Spatial variations (geography, climate)
5. Technology variations (outdated vs. cutting-edge)

### 5.3 Product Classification & Design Recommendations

**Environmental Product Declaration (EPD):**
- Standardized way to communicate LCA results
- Third-party verified
- Specific product category rules

**Sustainable Design Strategies:**
1. **Material reduction:** Lighter/smaller products
2. **Material substitution:** Lower-impact alternatives
3. **Design for disassembly:** Easier recycling/repair
4. **Extend product life:** Durability, repairability
5. **Design for recycling:** Use mono-materials, minimize contaminants
6. **Reduce use-phase impacts:** Energy efficiency, water saving
7. **Supplier engagement:** Lower-impact sourcing

**Circular Economy Strategies:**
- **Reuse:** Design for multiple life cycles
- **Repair:** Design for serviceability
- **Remanufacturing:** Recover components
- **Recycling:** Material recovery
- **Composting:** Biodegradable materials

---

## Part 6: Key Case Studies & Examples

### 6.1 Lighting Case Study (Hand Drying)

**Product Function:** "Drying hands once for one person"

**Alternatives Compared:**
- Paper towels
- Cloth towels
- Warm air hand dryer
- High-speed hand dryer

**Typical Results:**
- Paper towels: Dominated by paper production (forestry, pulping, bleaching)
- Warm air dryer: Dominated by electricity use (standby power, heating time)
- High-speed dryer: Better than warm air due to efficiency

**Key Variables:**
- Electricity grid carbon intensity (coal vs. hydro makes huge difference)
- Air dryer efficiency (high-speed is 3-4× more efficient)
- Paper towel usage (users sometimes dispense too many)
- Product lifetime (amortization over thousands of uses)

**Lessons:**
- Use-phase impacts matter (electricity for dryers)
- Efficiency improvements reduce overall impacts
- Electricity source (grid mix) critical
- Small products still have measurable impacts

### 6.2 Popcorn Packaging Case Study

**Product Function:** "Storing and protecting 1 kg of popcorn"

**Alternatives:**
- Paper bag packaging
- Plastic film packaging
- Corn-based bioplastic

**Analysis Stages:**
1. **Raw material extraction & production:**
   - Paper: Forestry → pulping → bleaching → converting
   - Plastic: Petroleum extraction → cracking → polymerization → film extrusion

2. **Use phase:**
   - Barrier properties (keep popcorn fresh/dry)
   - If poor barriers: product spoilage → repurchase needed

3. **End-of-life:**
   - Paper: Recyclable, biodegradable
   - Plastic: Often landfill (low recycling rates)
   - Compostable: May not actually compost (needs industrial facilities)

**Decision Variables:**
- Is barrier performance adequate?
- Will packaging degradation cause product loss?
- What is actual end-of-life scenario?

### 6.3 Automotive Case Study (Car LCA)

**Product Function:** "Transportation of 1 ton of payload 150,000 km"

**Life Cycle Stages:**

**Manufacturing (10-25% of total impact):**
- Steel, aluminum production
- Battery production (if electric)
- Paint, glass, electronics
- Assembly

**Use Phase (60-75% of impact for combustion vehicles):**
- Fuel consumption over 150,000 km
- Depends on:
  - Fuel type (gasoline, diesel, electricity source)
  - Driving cycle (city vs. highway)
  - Driver behavior (acceleration, idling)
  - Vehicle efficiency (engine technology, aerodynamics, weight)

**End-of-Life (5-10% of impact):**
- Recycling of metals
- Recovery of fluids
- Landfill/incineration of non-recyclables

**Electric vs. Gasoline:**
- Manufacturing: EV higher (battery production)
- Use phase: Depends on electricity grid
  - Coal-heavy grid: EV only slightly better
  - Renewable-heavy grid: EV 4-5× better
  - Break-even: Usually 2-3 years of driving

**Lessons:**
- Vehicle use phase dominates (focus on efficiency)
- Electricity source matters (grid matters)
- Manufacturing impacts matter for EVs
- Product lifetime assumptions critical

### 6.4 Tesla Case Study Data

**Tesla Model 3 Manufacturing Impact:**
- Battery production: Major contributor (30-40 kg CO2-eq per kWh)
- Steel/aluminum: 50-60 kg CO2-eq per vehicle for structure
- Total manufacturing: ~8-10 tonnes CO2-eq

**Use Phase (150,000 km lifetime):**
- Electricity consumption: ~15 kWh/100 km
- EU grid average: ~0.4 kg CO2/kWh
- Total use phase: 90 tonnes CO2-eq (breakeven with gasoline around 2 years)

**Comparison:**
- Comparable gasoline vehicle: 130-150 tonnes CO2-eq over lifetime
- Tesla: 100-110 tonnes CO2-eq (30% reduction)
- With renewable electricity: 40-50 tonnes CO2-eq (70% reduction)

---

## Part 7: LCA Methodology Comparison

### Quantitative LCA
- Detailed, comprehensive
- Data-intensive
- Time: weeks to months
- Suitable for: Major decisions, regulatory requirements, scientific credibility

### Qualitative LCA / Screening LCA
- Simple, quick overview
- Assumption-based
- Time: days to weeks
- Suitable for: Initial assessment, rough comparisons, priority setting

### Input-Output LCA
- Broad scope coverage
- Economic data-based
- Fills data gaps
- Suitable for: Background processes, supply chain analysis

### Hybrid LCA
- Combines process + input-output
- Comprehensive and detailed
- Time: weeks to months
- Suitable for: Complex supply chains, academic research

---

## Part 8: Standards & Guidance

### ISO 14040/14044 (International Standards)

**ISO 14040: LCA Principles & Framework**
- Defines LCA methodology
- Requires goal and scope definition
- Defines system boundaries
- Specifies cut-off criteria

**ISO 14044: LCA Requirements & Guidance**
- Data quality requirements
- Impact assessment methodology
- Sensitivity analysis requirements
- Critical review requirements

**Critical Review:**
- Independent expert validation required
- Increases credibility
- Adds cost and time
- Required for comparative assertions

### Environmental Product Declaration (EPD)

**Purpose:** Standardized communication of LCA results

**Requirements:**
- Product category rules (PCR) specific to product type
- Third-party verification
- LCA following ISO 14040/44
- Standardized presentation format

**Audience:** Business to business (B2B) primarily

### Other Guidance

**Product Environmental Footprint (PEF):** EU method
**Organization Environmental Footprint (OEF):** Company-level assessment
**Corporate Standard:** GHG Protocol scopes 1-3

---

## Part 9: Common Pitfalls & Solutions

**1. Undefined Functional Unit**
- Problem: Comparing incompatible products
- Solution: Define quantitatively before starting

**2. Hidden Allocation Issues**
- Problem: Results sensitive to allocation method
- Solution: Use mass-based, perform sensitivity analysis

**3. Insufficient Data**
- Problem: Filling gaps with poor estimates
- Solution: Prioritize hotspot data collection

**4. Inappropriate System Boundaries**
- Problem: Missing major impacts or adding irrelevant ones
- Solution: Document boundaries with rationale

**5. Ignoring Uncertainty**
- Problem: Presenting results as precise when uncertain
- Solution: Sensitivity analysis, data quality statement

**6. Outdated Data**
- Problem: Using 10+ year old data
- Solution: Verify data age, use temporal correction factors

**7. Misinterpreting Results**
- Problem: Oversimplifying complex findings
- Solution: Communicate uncertainty, hotspots, limitations

---

*This knowledge base captures the core concepts of LCA methodology. Refer to complete course transcripts for detailed examples, calculations, and methodological discussions.*
