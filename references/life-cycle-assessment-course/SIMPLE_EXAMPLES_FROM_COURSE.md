# Simple Examples Used Throughout the LCA Course

*Practical, real-world examples used to teach LCA concepts*

---

## 1. FUNCTIONAL UNIT EXAMPLES

### 1.1 Packaging Examples
- **Milk Packaging:** "Packaging 1 liter of milk"
- **Grocery Bags:** "Carrying 10 kg of groceries from store to home"
  - NOT: "1 plastic bag vs. 1 paper bag" (different capacity)
  - YES: Compare bags that carry the same amount

### 1.2 Service Examples
- **Lighting:** "Providing lighting for 50,000 hours in a residential room"
- **Transportation:** "Transporting 1 ton of cargo 1 km"
- **Hand Drying:** "Drying hands once for one person"

### 1.3 Product Examples
- **Beverages:** Per liter consumed
- **Clothing:** Per wearing (if durability differs)
- **Electronics:** Per hour of use

---

## 2. CARBON FOOTPRINT CALCULATION EXAMPLES

### 2.1 Food Carbon Footprint (Excel Example)

**Setup:**
Three people with different consumption patterns:
- Person 1: 10 servings/day
- Person 2: 20 servings/day
- Person 3: 30 servings/day

Two foods with different carbon footprints:
- Food 1: 0.1 kg CO2 per serving
- Food 2: 0.5 kg CO2 per serving

**Calculation:**
```
Person 1 + Food 1: 10 servings × 0.1 kg CO2 = 1 kg CO2 per day
Person 2 + Food 1: 20 servings × 0.1 kg CO2 = 2 kg CO2 per day
Person 3 + Food 1: 30 servings × 0.1 kg CO2 = 3 kg CO2 per day

Person 1 + Food 2: 10 servings × 0.5 kg CO2 = 5 kg CO2 per day
Person 2 + Food 2: 20 servings × 0.5 kg CO2 = 10 kg CO2 per day
Person 3 + Food 2: 30 servings × 0.5 kg CO2 = 15 kg CO2 per day
```

**Daily Totals:**
- Person 1: 1 + 5 = 6 kg CO2/day
- Person 2: 2 + 10 = 12 kg CO2/day
- Person 3: 3 + 15 = 18 kg CO2/day

**Annual Conversion (using Excel $ to lock cells):**
- Use conversion factor: 365.25 days/year
- Person 1 annual: 6 × 365.25 = 2,191.5 kg CO2/year

---

## 3. GREENHOUSE GAS EXAMPLES

### 3.1 GHG Characterization Factor Example

**Inventory Data:**
- CO2 emission: 100 kg
- CH4 emission: 5 kg
- N2O emission: 0.1 kg

**Characterization Factors (Global Warming Potential, GWP):**
- CO2: 1 kg CO2-eq per kg CO2
- CH4: 28 kg CO2-eq per kg CH4 (100-year horizon)
- N2O: 265 kg CO2-eq per kg N2O

**Impact Calculation:**
```
CO2:  100 kg × 1 = 100 kg CO2-eq
CH4:  5 kg × 28 = 140 kg CO2-eq
N2O:  0.1 kg × 265 = 26.5 kg CO2-eq
─────────────────────────
TOTAL: 266.5 kg CO2-eq
```

**Key Insight:** CH4 and N2O, though emitted in much smaller quantities, have large warming potential. The methane from 5 kg is equivalent to 140 kg of CO2!

---

## 4. ENERGY & EMISSIONS EXAMPLES

### 4.1 Natural Gas Combustion
- **Input:** 1 kg of natural gas
- **Output:** ~2 kg of CO2
- **Why:** Natural gas (CH4) + oxygen → CO2 + water, mass increases due to oxygen addition

### 4.2 Electricity Conversion
- **Direct electricity use:** 1 kWh
- **Primary energy equivalent:** 2.5-3.0 kWh (because generation efficiency is ~33-40%)
- **Example:** 1 kWh electricity from fossil fuel required ~3 kWh primary energy input

### 4.3 Oil Refining (Multi-Product Example)
**Input:** 1 barrel of crude oil (100 kg)

**Outputs:**
- Gasoline: 45 kg (45%)
- Diesel: 35 kg (35%)
- Fuel oil: 15 kg (15%)
- Naphtha/Other: 5 kg (5%)

**Allocation Problem:**
- Mass-based: Use percentages above
- Economic-based: Different because gasoline is more valuable than fuel oil
- Creates uncertainty in environmental burden split

---

## 5. PRODUCT SYSTEM BOUNDARY EXAMPLES

### 5.1 Coffee Supply Chain

**Stages Included:**
```
Coffee Farm (Colombia) 
  ↓ (shipping & processing)
Processing Plant (Colombia)
  ↓ (air freight)
Distribution Center (Europe)
  ↓ (truck/rail)
Retailer/Consumer
  ↓ (home brewing)
Use Phase (hot water, electricity)
  ↓ (disposal/composting)
End-of-Life
```

**Key Finding:** About 80% of impacts happen UPSTREAM (farming, processing, transport) before you buy the coffee. Only ~20% from your brewing at home.

### 5.2 Electricity Usage - Scope Definition
**What to Include:**
- Direct combustion of fuel at power plant (Scope 1)
- Emissions from grid electricity purchased (Scope 2)
- Upstream extraction, refining, transportation of fuel (Scope 3)

**What NOT to Include:**
- Power plants' capital equipment construction (already amortized)
- Workers' transport to the plant (negligible)

---

## 6. LIFECYCLE IMPACT ASSESSMENT (LCIA) EXAMPLES

### 6.1 Eutrophication Impact Chain

**Simple Example - Phosphorus in Water:**
```
Phosphate (PO4) emission
        ↓
Nutrient loading in water (agricultural runoff)
        ↓
Algal bloom growth (rapid reproduction)
        ↓
Oxygen depletion (algae dies, bacteria decompose)
        ↓
Fish death / Dead zone formation
        ↓
ECOSYSTEM DAMAGE (measured in PDF·m²·year)
```

**Quantification:**
- Input: 10 kg of PO4
- Characterization factor: ~3 kg PO4-eq per kg PO4 (midpoint)
- Result: 30 kg PO4-eq impact
- Damage: Potential loss of fish in ~100 m² of water for ~1 year

### 6.2 Acidification - SO2 Example

**Simple Cause-and-Effect:**
```
Sulfur Dioxide (SO2) emission (from coal burning)
        ↓
Atmospheric conversion (SO2 + water → sulfuric acid)
        ↓
Acid rain deposition
        ↓
Soil acidification / Forest damage
        ↓
Aquatic ecosystem acidification
        ↓
DAMAGE (fish mortality, plant death)
```

**Characterization:**
- SO2 is converted to "SO2-equivalents" for comparison
- Different acids have different potencies

---

## 7. ALLOCATION METHOD EXAMPLES

### 7.1 Oil Refining Allocation

**Scenario:**
```
Input: 1 barrel crude oil (requires 100 MJ energy to refine)

Outputs:
├─ Gasoline: 45 kg (valuable, high demand)
├─ Diesel: 35 kg (valuable, high demand)
├─ Heating oil: 15 kg (lower value)
└─ Naphtha: 5 kg (chemical feedstock)
```

**Different Allocation Methods → Different Results:**

**Method 1: Mass-based**
```
Gasoline: 100 MJ × (45/100) = 45 MJ per kg gasoline
Diesel: 100 MJ × (35/100) = 35 MJ per kg diesel
Heating oil: 100 MJ × (15/100) = 15 MJ per kg
Naphtha: 100 MJ × (5/100) = 5 MJ per kg
```

**Method 2: Economic-based (hypothetical values)**
```
Gasoline: $600/barrel (60% value)
Diesel: $300/barrel (30% value)
Heating oil: $80/barrel (8% value)
Naphtha: $20/barrel (2% value)

Energy allocated:
Gasoline: 100 MJ × (60%) = 60 MJ
Diesel: 100 MJ × (30%) = 30 MJ
Heating oil: 100 MJ × (8%) = 8 MJ
Naphtha: 100 MJ × (2%) = 2 MJ
```

**Result:** Gasoline burden differs: 45 vs 60 MJ (33% difference!)

---

## 8. SYSTEM BOUNDARY EXAMPLES

### 8.1 Car Lifecycle Boundary (Cradle-to-Grave)

**Included:**
```
Mining & Refining (steel, aluminum, oil, plastics)
        ↓
Parts Manufacturing (engine, transmission, electronics)
        ↓
Assembly (welding, painting, testing)
        ↓
Distribution (shipping to dealer)
        ↓
Use Phase (150,000 km driving, fuel consumption)
        ↓
End-of-Life (recycling, landfill)
```

**Excluded (typically):**
- Capital equipment at factories (too indirect)
- Workers' commuting (negligible)
- Office building where designers work (not product-specific)

### 8.2 Clothing Lifecycle Boundary

**Typical Inclusions:**
```
Cotton farming (pesticides, fertilizers, irrigation)
        ↓
Fiber processing (spinning, dyeing)
        ↓
Fabric production (weaving)
        ↓
Garment assembly (sewing, quality control)
        ↓
Distribution (shipping to retailers)
        ↓
Use Phase (washing, drying, ironing - BIG impact!)
        ↓
End-of-Life (landfill or recycling)
```

**Use Phase Dominance:**
- A t-shirt washed 20+ times: Washing impacts often exceed manufacturing impacts!
- Hot water = high energy use
- Machine drying = very high energy

---

## 9. DATA SOURCE EXAMPLES

### 9.1 Primary vs. Secondary Data

**Primary Data (Company-Specific):**
- "Our steel mill uses 8 MWh electricity per ton of steel"
- "Our production generates 50 kg waste per 1000 units"
- **Accuracy:** High, **Cost:** High, **Time:** Weeks

**Secondary Data (Database):**
- ecoinvent: "Average European steel: 8.5 MWh/ton"
- USDA-NREL: "US corn: 1.2 kg CO2/kg grain"
- **Accuracy:** Moderate, **Cost:** Low, **Time:** Days

**Hybrid Approach (Best Practice):**
- Collect primary data for hotspots (highest impact processes)
- Use generic data for minor impacts
- Balance effort with accuracy

---

## 10. SENSITIVITY ANALYSIS EXAMPLES

### 10.1 Grid Carbon Intensity - Electric Vehicle Example

**Tesla Model 3 Use Phase (150,000 km):**
- Electricity needed: 22,500 kWh
- Impact varies with grid carbon intensity:

```
Coal-heavy grid (0.8 kg CO2/kWh):
  22,500 × 0.8 = 18,000 kg CO2

Average grid (0.4 kg CO2/kWh):
  22,500 × 0.4 = 9,000 kg CO2

Renewable grid (0.1 kg CO2/kWh):
  22,500 × 0.1 = 2,250 kg CO2
```

**Result:** Same car, 8× difference in impacts depending on region!

### 10.2 Product Lifetime - Durable Goods

**T-Shirt Lifecycle Impact per Wear:**

**Scenario A: Worn 20 times (low durability)**
- Manufacturing: 5 kg CO2-eq
- Laundry (hot water): 20 washes × 1.5 kg CO2 = 30 kg CO2-eq
- **Total per wear: 35/20 = 1.75 kg CO2-eq per wear**

**Scenario B: Worn 100 times (high durability)**
- Manufacturing: 5 kg CO2-eq (amortized)
- Laundry (hot water): 100 washes × 1.5 kg CO2 = 150 kg CO2-eq
- **Total per wear: 155/100 = 1.55 kg CO2-eq per wear**

**Scenario C: Worn 100 times (but with cold water, line dry)**
- Manufacturing: 5 kg CO2-eq
- Laundry (cold water + line dry): 100 washes × 0.1 kg CO2 = 10 kg CO2-eq
- **Total per wear: 15/100 = 0.15 kg CO2-eq per wear**

**Key Insight:** Use phase (laundry) dominates, not manufacturing!

---

## 11. MULTI-PRODUCT SYSTEM EXAMPLES

### 11.1 Livestock Production (Beef vs. Leather)

**Problem:** A cow produces both:
- Meat (0.3 tons per cow)
- Leather (0.1 tons per cow)
- By-products (bones, organs, etc.)

**Question:** How much environmental burden belongs to beef vs. leather?

**Solution Methods:**

**Method 1: Mass-based**
```
Total cow impact: 5,000 kg CO2-eq

Meat (0.3 tons / 0.5 tons total) = 60% = 3,000 kg CO2-eq
Leather (0.1 tons / 0.5 tons total) = 20% = 1,000 kg CO2-eq
By-products = 20% = 1,000 kg CO2-eq
```

**Method 2: Economic-based** (depends on market prices)
```
If beef worth $3,000 and leather worth $500:
Meat: (3,000/3,500) × 5,000 = 4,286 kg CO2-eq
Leather: (500/3,500) × 5,000 = 714 kg CO2-eq
```

**Result:** Allocation method can change leather's impact by 40%!

---

## 12. REAL-WORLD DECISION EXAMPLES

### 12.1 Plastic vs. Paper Bag Choice

**The Wrong Question:**
"Is plastic or paper better?"

**The Right Question:**
"What is the functional unit for comparison?"

**Correct Setup:**
```
Functional Unit: "Carrying 10 kg of groceries from store to home"

Number of bags needed:
- Paper bag (capacity): ~5 kg → requires 2 bags
- Plastic bag (capacity): ~10 kg → requires 1 bag

Impact comparison:
- 2 paper bags (50g each): ~100 g × 20 g CO2-eq/g = 2 kg CO2-eq
- 1 plastic bag (30g): 30 g × 10 g CO2-eq/g = 0.3 kg CO2-eq
```

**Conclusion:** Plastic wins on weight basis, but:
- Assume 20% of plastic bags are reused (reduces impact)
- Assume 10% of paper bags are reused
- Final comparison less clear!

### 12.2 Reusable vs. Single-Use Cups

**Setup:**
- Reusable cup: 200g ceramic, manufacturing impact = 2 kg CO2-eq
- Single-use cup: 5g plastic, manufacturing impact = 0.05 kg CO2-eq
- Use phase (washing reusable cup): 0.5 kg CO2-eq per wash

**Break-even Analysis:**
```
Extra manufacturing impact: 2 - 0.05 = 1.95 kg CO2-eq

Per-wash savings: 0.5 kg CO2-eq (washing vs. manufacturing new cup)

Break-even: 1.95 ÷ 0.5 = 3.9 uses

Conclusion: After ~4 uses, reusable cup is more sustainable!
```

**Caution:** Assumes single-use cup would NOT be reused. If consumers reuse single-use cups, calculation changes!

---

## 13. COMMON MISCONCEPTIONS CORRECTED

### 13.1 "Lighter Product = Lower Impact"
**Wrong!** A lighter plastic bag requires less material, BUT if it tears easily and needs replacing, total impact could be higher.
- **Better frame:** "Durable product serving same function"

### 13.2 "Organic = Lower LCA Impact"
**Not always!** Organic farming:
- ✓ Avoids synthetic pesticides
- ✗ Often has lower yields (need more land)
- ✗ May require more tillage (more fuel use)
- **Verdict:** Depends on specific product and location

### 13.3 "Recycled Material = Zero Impact"
**Wrong!** Recycled materials still require:
- Collection and sorting (energy, logistics)
- Reprocessing (cleaning, melting, re-forming)
- Quality loss (some recycled content < virgin)
- **But:** Typically 20-40% lower impact than virgin material

### 13.4 "Biodegradable = Environmentally Friendly"
**Not in landfill!** Compostable materials:
- Only decompose in industrial composting facilities (58°C, 6+ weeks)
- In home composting: Persist like regular plastic
- In landfill: Essentially permanent like conventional plastic
- **Reality:** <5% of consumers have access to industrial composting

---

## 14. QUICK REFERENCE - TYPICAL HOTSPOTS BY PRODUCT

| Product Type | Dominant Impact Stage | Why |
|----------|--------|--------|
| **Car** | Use phase (70-85%) | Fuel consumption over lifetime |
| **Appliances (fridge, washer)** | Use phase (60-80%) | Electricity consumption |
| **Clothing** | Use phase (washing) (40-60%) | Hot water heating |
| **Food** | Production/Farming (80%+) | Agricultural inputs (N2O, methane) |
| **Packaging** | Manufacturing (60-80%) | Material production |
| **Electronics** | Manufacturing (70%+) | Rare earth extraction, chip fabrication |
| **Furniture** | Manufacturing (usually 70%+) | Material-intensive (wood, foam, leather) |
| **Building/Construction** | Manufacturing (80%+) | Concrete, steel, insulation production |

---

## 15. SIMPLE FORMULAS TO REMEMBER

### Impact = Flow × Characterization Factor
```
CO2-eq = (100 kg CO2 × 1) + (5 kg CH4 × 28) + (0.1 kg N2O × 265)
       = 100 + 140 + 26.5
       = 266.5 kg CO2-eq
```

### Per-Unit Impact = Total Impact ÷ Functional Units
```
Impact per km = 10,000 kg CO2-eq ÷ 150,000 km
              = 0.067 kg CO2-eq/km
```

### Break-Even Calculation
```
Break-even uses = (Additional Manufacturing Impact) ÷ (Per-Use Savings)
                = (Reusable - Disposable Impact) ÷ (Disposable Impact per use)
                = 1.95 kg ÷ 0.5 kg per use
                = 3.9 uses
```

---

*These simple examples form the foundation for understanding complex LCA studies. Master these, and you can tackle any product lifecycle assessment.*
