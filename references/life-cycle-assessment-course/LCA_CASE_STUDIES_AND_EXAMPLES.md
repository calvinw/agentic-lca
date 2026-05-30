# Life Cycle Assessment - Case Studies & Examples

*Detailed real-world applications demonstrating LCA methodology and decision-making*

---

## Part 1: Hand Drying Case Study

### 1.1 Problem Setup

**Product Function:** "Drying hands once for one person after washing"

**Alternatives Compared:**
1. Paper towels (single-use, disposable)
2. Cloth towels (reusable, launderable)
3. Warm air hand dryer (electric, slow)
4. High-speed air hand dryer (electric, efficient)

**Why This Matters:** Common decision in commercial buildings, represents billions of uses annually, results often counterintuitive

### 1.2 Life Cycle Stage Analysis

#### **Paper Towels - Raw Materials to Manufacturing**

**Forestry:**
- Wood harvested from managed forests
- Transportation to pulping mill
- Land use impacts (biodiversity, soil)

**Pulping Process (Chemical and Mechanical):**
- Chemical pulping uses sodium hydroxide and sodium sulfide
- Energy intensive (steam, electricity)
- Wastewater treatment required
- Bleaching chemicals added (chlorine or oxygen-based)

**Converting and Packaging:**
- Paper rolled into sheets
- Perforated for dispense
- Packaged in plastic or paper
- Transportation to distribution centers

**Key Data:**
- 1 paper towel sheet: ~2-3 grams
- Manufacturing impacts: ~15-25 gCO2-eq per sheet
- 50% of impact from paper production, 50% from processing

**Use Phase:**
- Minimal use-phase impacts
- User behavior critical: some people use 1 sheet, others use 5-10
- Study assumption: average 2-3 sheets per drying

**End-of-Life:**
- Typically landfill (contaminated with water, not effectively recycled)
- Landfill methane emissions: ~5 gCO2-eq per sheet
- Biodegradation timeframe: 2-3 weeks

**Total Lifecycle Paper Towel:** ~40-50 gCO2-eq per hand drying event

---

#### **Cloth Towels - Reusable System**

**Manufacturing:**
- Cotton or microfiber textile production
- Dyeing and finishing
- Sewing and packaging

**Key Data:**
- 1 towel: 50-100 grams of fabric
- Manufacturing: 500-1000 gCO2-eq per towel
- Design life: 200-500 uses

**Use Phase (Critical Stage):**
- Washing frequency determines impacts
- Hot water washing: 0.5 kg CO2-eq per wash (heating water is energy intensive)
- Detergent use: 5-10 gCO2-eq per wash
- Drying: Air dry (negligible) vs. machine dry (~30 gCO2-eq per wash)
- Assumption: Towel washed weekly with 5 other towels

**Laundry Calculation Example:**
```
Scenario: One towel washed weekly with 4 others (5 towels per load)
- Manufacturing impact: 750 gCO2-eq ÷ 250 uses = 3 gCO2-eq per use
- Per-wash hot water heating: 500 gCO2-eq ÷ 5 towels = 100 gCO2-eq per towel per wash
- Detergent per towel: 10 gCO2-eq ÷ 5 = 2 gCO2-eq
- Drying (machine, split across load): 150 gCO2-eq ÷ 5 = 30 gCO2-eq per towel
- Total per use: 3 + 100 + 2 + 30 = 135 gCO2-eq per hand drying
```

**End-of-Life:**
- Eventually landfilled after ~200-500 uses
- Final impact amortized across uses

**Total Lifecycle Cloth Towel (hot water, machine dry):** ~120-150 gCO2-eq per hand drying event

---

#### **Warm Air Dryer - Electric System**

**Manufacturing:**
- Metal (stainless steel or aluminum)
- Electric heating element
- Motor and fan
- Control circuitry

**Key Data:**
- Dryer weight: 2-3 kg
- Manufacturing impact: ~30 kg CO2-eq per unit
- Design life: 10-15 years (average building)
- Annual usage: ~10,000 hand drying events
- Lifetime uses: 100,000-150,000 drying events

**Use Phase:**
- Power rating: 1000-1500 watts
- Drying duration: 20-30 seconds
- Energy per use: 1000W × 25 seconds ÷ 3600s = 0.007 kWh
- Grid carbon intensity: ~0.4 kg CO2/kWh (European average)
- **Emissions per use: 0.007 × 0.4 = 2.8 gCO2-eq (use phase)**

**Standby Power Loss:**
- Many dryers have continuous standby (sensors, controls)
- Daily standby: ~10 watt-hours = 50 watts × 24 hours ÷ 2
- Not using continuously: 50% standby loss
- Annual standby loss: 10 watt-hours × 365 = 3.65 kWh/year
- Over 10 years: 36.5 kWh
- Standby impact: 36.5 × 0.4 × 100,000 uses ÷ 1,000,000 hours ≈ 1.5 gCO2-eq per use

**Total Use-Phase Impact:** ~4-5 gCO2-eq per hand drying event

**End-of-Life:**
- Metal recycling highly efficient
- ~90% material recovery value
- Minimal end-of-life impact

**Total Lifecycle Warm Air Dryer:** 
- Manufacturing: 30,000 gCO2-eq ÷ 100,000 uses = 0.3 gCO2-eq per use
- Use phase: 4-5 gCO2-eq per use
- **Total: ~4.5-5.5 gCO2-eq per hand drying event**

---

#### **High-Speed Air Dryer - Premium Electric System**

**Manufacturing:**
- Similar to warm dryer (stainless steel, motor)
- Enhanced motor and nozzle design
- Circuitry for optimized blade speed

**Design Improvements:**
- Brushless DC motor (more efficient)
- Optimized air nozzle design
- Velocity: 400+ mph air jet
- Drying time: 10-15 seconds (vs. 25-30 seconds)

**Use Phase:**
- Power rating: 1100-1500 watts
- Drying duration: 12 seconds (shorter due to high speed)
- Energy per use: 1100W × 12 seconds ÷ 3600s = 0.0037 kWh
- **Emissions per use: 0.0037 × 0.4 = 1.5 gCO2-eq (use phase)**

**Efficiency Advantage:**
- 50% less drying time than warm dryer
- ~40-50% lower electricity consumption per use
- Minimal standby impact

**Total Lifecycle High-Speed Dryer:**
- Manufacturing: 0.2-0.3 gCO2-eq per use
- Use phase: 1.5-2 gCO2-eq per use
- **Total: ~2-2.5 gCO2-eq per hand drying event**

---

### 1.3 Comparative Results Summary

| Method | Per-Use CO2 (gCO2-eq) | Relative Impact | Key Driver |
|--------|--------|--------|--------|
| Paper towels | 40-50 | 20× high-speed dryer | Paper production & waste |
| Cloth (hot water, machine dry) | 120-150 | 60× high-speed dryer | Laundry heating |
| Warm air dryer | 4.5-5.5 | ~2× high-speed dryer | Use-phase electricity |
| High-speed dryer | 2-2.5 | 1× (baseline) | Use-phase electricity (efficient) |

---

### 1.4 Critical Variables & Sensitivity Analysis

**1. Electricity Grid Carbon Intensity**
- Coal-heavy grid: 0.8 kg CO2/kWh → Dryer impacts double
- Renewable-heavy grid: 0.1 kg CO2/kWh → Dryer impacts 1/4
- Nuclear/hydro: 0.02 kg CO2/kWh → Dryer near zero-emission

**Impact:** In coal regions, dryer becomes less favorable. In renewable regions, dryer is best option.

**2. Hot Water Heating Method**
- Electric heating: 100 gCO2-eq per hot wash
- Natural gas heating: 50 gCO2-eq per hot wash
- Heat pump water heater: 20 gCO2-eq per hot wash

**Impact:** Cloth towel advantages improve with efficient water heating.

**3. Towel Washing Frequency**
- Daily washing: Manufacturing impact negligible; laundry impact dominates
- Weekly washing: Manufacturing and laundry impacts balanced
- Monthly washing (rare): Manufacturing impact becomes significant

**4. Paper Towel User Behavior**
- Minimal user (1 sheet): 20-25 gCO2-eq per use
- Average user (3 sheets): 50 gCO2-eq per use
- High consumer (5+ sheets): 100+ gCO2-eq per use

---

### 1.5 Decision Rules

**High-speed hand dryer is optimal IF:**
- Grid electricity is from non-coal sources
- Capital cost is acceptable
- Building has sufficient electrical capacity
- Users tolerate 10-15 second drying time

**Warm air dryer is acceptable IF:**
- High-speed dryer unavailable or too expensive
- Grid is reasonably clean (not coal-heavy)

**Cloth towels are viable IF:**
- Water heating is efficient (natural gas or heat pump)
- Towels are not washed individually (batch washing only)
- Building has washer/dryer infrastructure

**Paper towels should be avoided EXCEPT:**
- Emergency situations
- Single-occupancy use (bathroom in home)
- Users cannot be trusted with shared cloth towels (hygiene concerns)

---

## Part 2: Popcorn Packaging Case Study

### 2.1 Problem Setup

**Product Function:** "Protecting and containing 500g of popcorn during distribution, storage, and retail sale (3-month shelf life)"

**Alternatives Evaluated:**
1. Paper kraft bag (traditional popcorn packaging)
2. Plastic film bag (polypropylene, common modern packaging)
3. Compostable bioplastic (polylactic acid, PLA)
4. Recycled plastic blend (partially recycled content)

**Key Challenge:** Popcorn is highly sensitive to:
- Moisture absorption (loses crispness)
- Oxygen exposure (oxidation makes rancid)
- Light exposure (degrades oils, develops off-flavors)

**Therefore:** Barrier properties are critical - poor barriers lead to product spoilage and waste

---

### 2.2 Detailed Lifecycle Analysis

#### **Paper Kraft Bag - Biodegradable Baseline**

**Raw Materials:**
- Virgin kraft pulp from pine/spruce forests
- Chlorine-free bleaching (oxygen-based)
- No additional barrier coatings (for recyclability assumption)

**Manufacturing:**
```
Forestry → Pulping → Bleaching → Paper Making → Bag Converting
Energy intensity: High (steam for drying, machinery)
Water use: Moderate (bleached, treated wastewater)
```

**Critical Issue - Barrier Properties:**
- Paper is porous to water vapor
- Popcorn absorbs moisture from air
- Uncoated paper bags: high moisture permeability
- Shelf life: ~2-4 weeks before quality degradation
- In 3-month retail scenario: Significant product loss expected

**Product Loss Scenario:**
- Shelf display with paper bag: 30-40% moisture pickup
- Consumer complaints: "Stale popcorn"
- Retailer waste: 5-15% of stock marked down or discarded
- This ADDS environmental impact through wasted popcorn

**Manufacturing Impacts:**
- Material: 15 grams of kraft paper per bag
- Impacts: ~50 gCO2-eq per bag

**End-of-Life:**
- Recyclable (no coatings)
- Contamination risk (oil stains from popcorn)
- Biodegradable timeframe: 6-12 months in landfill
- Compostable in industrial facilities

**Lifecycle Carbon: Paper Bag**
```
Scenario A (Good Barrier, Coated Paper):
- Manufacturing: 80 gCO2-eq (includes coating)
- End-of-life: 10 gCO2-eq
- Product loss: 0% (effective barrier)
- Total: 90 gCO2-eq per functional unit

Scenario B (Poor Barrier, Uncoated Paper):
- Manufacturing: 50 gCO2-eq
- End-of-life: 5 gCO2-eq
- Product loss: 35% spoilage × 300g popcorn × 0.8 kg CO2/kg = 84 gCO2-eq
- TOTAL: 139 gCO2-eq per functional unit (higher due to waste!)
```

---

#### **Plastic Film Bag (Polypropylene, PP)**

**Raw Materials:**
- Petroleum crude oil extraction
- Refining and cracking to propylene monomer
- Polymerization in reactor

**Manufacturing:**
```
Oil Extraction → Refining → Cracking → Polymerization → Film Extrusion
Energy intensity: Moderate (chemical reactions exothermic)
Water use: Low (cooling only)
Emissions: Fugitive methane, VOCs
```

**Barrier Properties - Excellent:**
- Polypropylene naturally resistant to moisture
- Can be metallized (aluminum vacuum coat) for improved barrier
- Popcorn shelf life: 6-12 months without degradation
- Excellent oxygen barrier (prevents rancidity)

**Thickness Optimization:**
- Typical popcorn bag: 25-40 microns thickness
- More material = better barrier, more impact
- Trade-off between thin film (low material impact) and durability

**Manufacturing Impacts:**
- Material: 5-10 grams plastic film per bag
- Impacts: 30-50 gCO2-eq per bag (low material use despite higher carbon intensity)

**Use-Phase Impacts:**
- Minimal (packaging only, no electricity)
- Slight weight advantage in transportation

**End-of-Life - Major Issue:**
- ~90% of plastic bags end in landfill
- ~5% incinerated (energy recovery)
- <1% actually recycled (contamination from food)
- Landfill persistence: 200-500 years
- Landfill methane generation: Variable, typically ~5-10 gCO2-eq per bag

**Lifecycle Carbon: Plastic Film Bag**
```
Scenario (Standard Polypropylene):
- Manufacturing: 40 gCO2-eq
- Transportation: 2 gCO2-eq (lighter than paper)
- Product loss: 0% (excellent barrier)
- End-of-life: 8 gCO2-eq (landfill methane + persistence penalty)
- TOTAL: 50 gCO2-eq per functional unit
```

**Environmental Concerns Beyond Carbon:**
- Microplastic generation over 200+ years
- Ocean contamination if improperly disposed
- Toxicity of some plasticizers (if low-quality film)

---

#### **Compostable Bioplastic (PLA - Polylactic Acid)**

**Raw Materials:**
- Corn or sugarcane production
- Fermentation to lactic acid
- Polymerization to create PLA resin

**Sustainability Questions:**
- Land use impact (corn production for plastic vs. food)
- Fertilizer and pesticide use (agricultural inputs)
- Competition with food production

**Manufacturing:**
- Lower embodied energy than petro-plastic (fermentation is less energy intensive)
- Typical embodied carbon: 2-3 kg CO2/kg material
- Similar energy to polypropylene per mass unit

**Barrier Properties - Moderate:**
- Natural PLA: Good moisture barrier
- Oxygen barrier: Moderate (less than PP metallized)
- Shelf life: 4-8 months (acceptable for popcorn)

**Critical Issue - Composting Infrastructure:**
- Requires industrial composting at 58°C for 6-12 weeks
- Home composting does NOT work (temps too low)
- <5% of consumers have access to industrial composting
- Most PLA ends in landfill anyway

**In Landfill Scenario:**
- PLA is not biodegradable under anaerobic landfill conditions
- Persists 200+ years, same as conventional plastic
- No methane generation advantage

**Manufacturing Impacts:**
- Material: 5-10 grams PLA per bag
- Impacts: 50-70 gCO2-eq per bag (higher than PP due to processing)
- Agricultural impacts: Additional 10-20 gCO2-eq per bag

**Lifecycle Carbon: PLA Bioplastic Bag**
```
Scenario A (Proper Industrial Composting):
- Manufacturing: 60 gCO2-eq (includes agricultural impacts)
- Composting impact: -20 gCO2-eq (carbon sequestered in compost, offset)
- Product loss: 0% (adequate barrier)
- TOTAL: 40 gCO2-eq per functional unit (BEST CASE)

Scenario B (Realistic - Landfill Disposal):
- Manufacturing: 60 gCO2-eq
- Transportation: 1 gCO2-eq (light)
- Product loss: 0% (adequate barrier)
- End-of-life: 5 gCO2-eq (landfill, no biodegradation)
- TOTAL: 66 gCO2-eq per functional unit (REALISTIC CASE)
```

**Reality Check:** Unless consumer actually composts (5% likelihood), PLA provides no environmental benefit over conventional plastic.

---

#### **Recycled Content Plastic (Blend of Recycled + Virgin PP)**

**Material Composition:**
- 30-50% post-consumer recycled plastic
- 50-70% virgin polypropylene
- Same barrier properties as pure virgin plastic

**Manufacturing:**
- Recycled plastic collection and sorting: Energy and logistics
- Reprocessing through extruder: Lower energy than virgin polymerization
- Resin mixing with virgin plastic

**Manufacturing Impacts:**
- Material: 5-10 grams recycled blend per bag
- Impacts: 25-40 gCO2-eq per bag (20-30% lower than virgin due to recycling benefits)

**Barrier Properties:**
- Identical to virgin plastic
- Durability: Some quality loss possible if recycled content too high

**End-of-Life:**
- Recyclable (though further recycling efficiency decreases)
- Can be recycled 3-5 times before quality degrades
- Landfill methane: ~8 gCO2-eq per bag

**Lifecycle Carbon: Recycled Content Plastic**
```
Scenario (50% Recycled Content):
- Manufacturing: 32 gCO2-eq
- Transportation: 2 gCO2-eq
- Product loss: 0% (adequate barrier)
- End-of-life: 8 gCO2-eq
- TOTAL: 42 gCO2-eq per functional unit
```

---

### 2.3 Comparative Results Summary

| Material | Per-Unit CO2 (gCO2-eq) | Product Loss Factor | Lifecycle Total | Notes |
|----------|--------|--------|--------|--------|
| Uncoated kraft paper | 50 | 35% loss | **139** | Barrier failure adds waste |
| Coated kraft paper | 80 | 0% loss | 90 | Better but higher impact |
| Recycled plastic blend | 32 | 0% loss | **42** | Best environmental option |
| Virgin polypropylene | 40 | 0% loss | 50 | Good barrier, good impact |
| PLA (landfill scenario) | 60 | 0% loss | 66 | No environmental benefit |
| PLA (composted - rare) | 60 | 0% loss | 40 | Best IF properly composted |

---

### 2.4 Critical Decision Points

**Key Insight: Barrier Properties Determine Success**

The worst outcome is a package that LOOKS environmentally friendly but fails to protect the product, resulting in spoilage and food waste. Food waste has enormous embedded environmental impact.

**Decision Framework:**

1. **Minimum Barrier Requirement:** Popcorn must maintain quality for 12 weeks minimum
   - This rules out uncoated kraft paper as standalone

2. **Realistic End-of-Life:** Assume landfill for most scenarios
   - PLA and compostable materials lose advantage unless consumer infrastructure exists
   - Recyclable materials only help if customers actually recycle (often <30%)

3. **Material Recommendation:** Recycled Content Polypropylene
   - Excellent barrier (protects product)
   - Lower carbon than virgin plastic (recycled content benefit)
   - Similar impacts to virgin plastic if not actually recycled, but no risk of worse outcomes
   - Supports circular economy signals

4. **Optimizations to Reduce Impacts:**
   - Minimize plastic film thickness (35 microns instead of 40)
   - Use thinner film with better sealing technology
   - Promote proper recycling (on-package messaging)
   - Consider lightweighting: 10% thinner film = ~5 gCO2-eq savings per bag

---

## Part 3: Automotive Case Study - Car Life Cycle Assessment

### 3.1 Problem Setup

**Product Function:** "Transportation of 1 ton of payload 150,000 kilometers over vehicle lifetime"

**Vehicles Compared:**
1. Conventional gasoline vehicle
2. Diesel vehicle
3. Hybrid electric vehicle (HEV)
4. Battery electric vehicle (BEV)

**Geographic Assumptions:**
- European grid mix (40% renewable, 20% nuclear, 40% fossil)
- Average driving cycle (mix of city and highway)
- End-of-life: 85% metal recycling, 15% landfill

---

### 3.2 Manufacturing Phase

#### **Material Composition - Typical Car (1500 kg)**

| Material | Mass (kg) | Impact (kg CO2-eq) |
|----------|--------|--------|
| Steel | 700 | 1,400 |
| Aluminum | 150 | 1,500 |
| Plastics & Composites | 200 | 600 |
| Glass | 50 | 150 |
| Electronics & Copper | 100 | 500 |
| Paint & Fluids | 50 | 300 |
| **Subtotal (Materials)** | **1250** | **4,450** |

#### **Assembly & Manufacturing Process**

| Process | Impact (kg CO2-eq) |
|----------|--------|
| Stamping & Forming | 800 |
| Welding & Assembly | 400 |
| Painting | 300 |
| Final Assembly | 300 |
| Testing & Transport | 200 |
| **Subtotal (Assembly)** | **2,000** |

#### **Battery Production (Electric Vehicles Only)**

**Battery Specifications (BEV):**
- Capacity: 60 kWh
- Specific carbon intensity: 50-60 kg CO2-eq per kWh
- **Battery impact: 3,000-3,600 kg CO2-eq**

**Battery Specifications (HEV):**
- Capacity: 10 kWh
- **Battery impact: 500-600 kg CO2-eq**

#### **Manufacturing Summary**

| Vehicle Type | Materials (kg CO2-eq) | Assembly (kg CO2-eq) | Battery (kg CO2-eq) | **Total** |
|----------|--------|--------|--------|--------|
| Gasoline | 4,450 | 2,000 | 0 | **6,450** |
| Diesel | 4,450 | 2,000 | 0 | **6,450** |
| Hybrid (HEV) | 4,450 | 2,000 | 550 | **7,000** |
| Electric (BEV) | 4,450 | 2,000 | 3,300 | **9,750** |

**Key Insight:** Battery production is major driver of EV manufacturing emissions. This is offset during use phase.

---

### 3.3 Use Phase - Fuel Consumption & Emissions

#### **Gasoline Vehicle**

**Specifications:**
- Fuel consumption: 7 liters per 100 km (typical European car)
- Driving 150,000 km: 10,500 liters total
- Fuel carbon intensity: ~2.31 kg CO2 per liter burned

**Well-to-Tank Emissions (Upstream):**
- Oil extraction, refining, transportation: ~0.15 kg CO2 per liter
- **Total upstream: 1,575 kg CO2-eq**

**Tank-to-Wheel Emissions (Combustion):**
- Direct CO2 from fuel: 10,500 liters × 2.31 = 24,255 kg CO2-eq
- Methane & N2O emissions: ~200 kg CO2-eq

**Total Use-Phase Impact:** 
```
Upstream: 1,575 kg CO2-eq
Combustion: 24,455 kg CO2-eq
END-OF-LIFE EXCLUDED (separate calculation)
TOTAL USE PHASE: 26,030 kg CO2-eq (150,000 km)
```

---

#### **Diesel Vehicle**

**Specifications:**
- Fuel consumption: 5.5 liters per 100 km (more efficient than gasoline)
- Driving 150,000 km: 8,250 liters total
- Fuel carbon intensity: ~2.68 kg CO2 per liter (higher carbon content than gasoline)

**Well-to-Tank Emissions:**
- ~0.15 kg CO2 per liter upstream
- **Total upstream: 1,238 kg CO2-eq**

**Tank-to-Wheel Emissions:**
- Direct CO2 from fuel: 8,250 × 2.68 = 22,110 kg CO2-eq
- Particulate matter and NOx (health impacts): Not counted in carbon, but important

**Total Use-Phase Impact:**
```
Upstream: 1,238 kg CO2-eq
Combustion: 22,110 kg CO2-eq
TOTAL USE PHASE: 23,348 kg CO2-eq
```

**Comparison:** Diesel ~10% lower CO2 than gasoline due to better fuel efficiency, despite higher carbon content of diesel fuel.

---

#### **Hybrid Electric Vehicle (HEV)**

**Specifications:**
- Fuel consumption: 4.5 liters per 100 km (regenerative braking + electric assist)
- Driving 150,000 km: 6,750 liters total
- Combined cycle uses electricity + fuel

**Electricity Assumptions:**
- 20% of driving energy from battery (charged from grid)
- Energy consumption: 0.15 kWh per km from grid
- 150,000 km × 0.15 = 22,500 kWh from grid

**Well-to-Tank (Fuel):**
- ~0.15 kg CO2 per liter
- **Total upstream fuel: 1,013 kg CO2-eq**

**Tank-to-Wheel (Fuel Combustion):**
- 6,750 liters × 2.31 = 15,593 kg CO2-eq

**Electricity (Grid):**
- 22,500 kWh × 0.4 kg CO2/kWh = 9,000 kg CO2-eq

**Total Use-Phase Impact:**
```
Fuel upstream: 1,013 kg CO2-eq
Fuel combustion: 15,593 kg CO2-eq
Grid electricity: 9,000 kg CO2-eq
TOTAL USE PHASE: 25,606 kg CO2-eq
```

**Comparison:** HEV ~10% better than gasoline, similar to diesel. Benefits are moderate.

---

#### **Battery Electric Vehicle (BEV)**

**Specifications:**
- Battery capacity: 60 kWh
- Energy efficiency: 0.15 kWh per km
- 150,000 km × 0.15 = 22,500 kWh total required
- Charging efficiency: 85% (losses in charger, battery, grid)

**Electricity Required from Grid:**
- 22,500 kWh ÷ 0.85 = 26,470 kWh from grid

**Grid Electricity Emissions (EU Average: 0.4 kg CO2/kWh):**
- 26,470 kWh × 0.4 = 10,588 kg CO2-eq

**Electricity Upstream (Well-to-Grid):**
- Transmission losses, battery charging losses: ~2,000 kg CO2-eq

**Total Use-Phase Impact:**
```
Grid electricity: 10,588 kg CO2-eq
Upstream/losses: 2,000 kg CO2-eq
TOTAL USE PHASE: 12,588 kg CO2-eq
```

**Grid Sensitivity Analysis:**
```
Coal-heavy grid (0.8 kg CO2/kWh):
- 26,470 × 0.8 = 21,176 kg CO2-eq (barely better than gas!)

Renewable grid (0.1 kg CO2/kWh):
- 26,470 × 0.1 = 2,647 kg CO2-eq (5× better than gas!)

All-renewable (0.02 kg CO2/kWh):
- 26,470 × 0.02 = 529 kg CO2-eq (50× better than gas!)
```

---

### 3.4 End-of-Life Phase

**Assumptions:**
- 85% of car mass (mostly metals) are recyclable
- 15% goes to landfill (plastics, composites, fluids)

| Vehicle Type | Recycling Impact (kg CO2-eq) | Landfill Impact (kg CO2-eq) | **Total** |
|----------|--------|--------|--------|
| All types | -500 (credit for material recovery) | 300 | **-200** |

**Note:** Recycling credit is negative (reduces overall impact), but landfill penalties still apply.

---

### 3.5 Full Lifecycle Comparison

| Vehicle Type | Manufacturing | Use Phase | End-of-Life | **Total Lifecycle** |
|----------|--------|--------|--------|--------|
| Gasoline | 6,450 | 26,030 | -200 | **32,280** |
| Diesel | 6,450 | 23,348 | -200 | **29,598** |
| Hybrid (HEV) | 7,000 | 25,606 | -200 | **32,406** |
| Electric (BEV) - EU Grid | 9,750 | 12,588 | -200 | **22,138** |
| Electric (BEV) - Coal Grid | 9,750 | 21,176 | -200 | **30,726** |
| Electric (BEV) - Green Grid | 9,750 | 2,647 | -200 | **12,197** |

---

### 3.6 Break-Even Analysis

**Question:** How many kilometers until BEV manufacturing carbon is offset by operational savings?

**BEV Break-Even Calculation (EU Grid):**
```
BEV manufacturing advantage loss: 9,750 - 6,450 = 3,300 kg CO2-eq
Per-km advantage (gasoline vs BEV): (26,030 - 12,588) ÷ 150,000 = 0.0896 kg CO2-eq per km
Break-even: 3,300 ÷ 0.0896 = 36,830 km (~2.5 years typical driving)
```

**Critical Insight:** BEV breaks even in 2-3 years of typical driving, then advantages accumulate rapidly.

---

### 3.7 Lifecycle Impact Breakdown - Gasoline vs. BEV (EU Grid)

```
GASOLINE VEHICLE (32,280 kg CO2-eq total)
├─ Manufacturing: 20% (6,450 kg)
├─ Use Phase: 81% (26,030 kg)
└─ End-of-Life: -1% (-200 kg)

ELECTRIC VEHICLE (22,138 kg CO2-eq total)
├─ Manufacturing: 44% (9,750 kg) ← Higher proportion
├─ Use Phase: 57% (12,588 kg) ← Much lower absolute
└─ End-of-Life: -1% (-200 kg)
```

**Key Observations:**
1. Manufacturing dominates EV lifecycle (44% vs. 20% for gasoline)
2. Use phase is where EV wins decisively
3. The longer the vehicle lifetime, the better EV advantage
4. Grid carbon intensity critical - makes or breaks cost-benefit

---

## Part 4: Tesla Model 3 Case Study (Detailed Example)

### 4.1 Vehicle Specifications

**Model 3 Standard Plus (2023):**
- Battery capacity: 60 kWh
- Curb weight: 1,608 kg
- Estimated lifetime: 200,000 km
- Target efficiency: 15 kWh per 100 km

---

### 4.2 Manufacturing Impacts

**Material Impacts:**
- Steel/Aluminum body: 1,600 kg × 2.5 kg CO2-eq per kg = 4,000 kg CO2-eq
- Electronics/wiring: ~500 kg CO2-eq
- Plastic/interior: ~400 kg CO2-eq
- **Subtotal materials: 4,900 kg CO2-eq**

**Battery Manufacturing:**
- 60 kWh × 50 kg CO2-eq per kWh = 3,000 kg CO2-eq
- Cell production, pack assembly, integration: Additional 500 kg CO2-eq
- **Subtotal battery: 3,500 kg CO2-eq**

**Assembly & Factory:**
- Giga factory operations, testing, transport: 1,500 kg CO2-eq

**Total Manufacturing: ~9,900 kg CO2-eq (similar to generic BEV estimate)**

---

### 4.3 Use Phase - European Grid Mix

**Electricity Consumption:**
- 200,000 km ÷ 15 kWh per 100 km = 30,000 kWh required
- Grid supply needed (with 90% charging efficiency): 33,333 kWh from grid

**EU Grid Average (0.4 kg CO2/kWh):**
- 33,333 × 0.4 = 13,333 kg CO2-eq

**Use Phase Total: ~13,500 kg CO2-eq**

---

### 4.4 Full Lifecycle - Multiple Scenarios

**Scenario A: EU Average Grid (0.4 kg CO2/kWh)**
```
Manufacturing: 9,900 kg CO2-eq
Use Phase: 13,500 kg CO2-eq
End-of-Life: -300 kg CO2-eq (recycling credit)
TOTAL: 23,100 kg CO2-eq over 200,000 km
Per-km: 0.116 kg CO2-eq/km
```

**Scenario B: German Grid - High Renewables (0.25 kg CO2/kWh)**
```
Manufacturing: 9,900 kg CO2-eq
Use Phase: 33,333 × 0.25 = 8,333 kg CO2-eq
End-of-Life: -300 kg CO2-eq
TOTAL: 17,933 kg CO2-eq over 200,000 km
Per-km: 0.090 kg CO2-eq/km
```

**Scenario C: US Average Grid - Coal-Heavy (0.55 kg CO2/kWh)**
```
Manufacturing: 9,900 kg CO2-eq
Use Phase: 33,333 × 0.55 = 18,333 kg CO2-eq
End-of-Life: -300 kg CO2-eq
TOTAL: 27,933 kg CO2-eq over 200,000 km
Per-km: 0.140 kg CO2-eq/km
```

---

### 4.5 Comparison with Gasoline Alternative (Same Function)

**Comparable Gasoline Car (2023):**
- Fuel consumption: 6 L/100 km
- 200,000 km × 6/100 = 12,000 liters gasoline
- Manufacturing: ~6,000 kg CO2-eq (smaller vehicle, no battery)

**Gasoline Lifecycle (Europe):**
- Manufacturing: 6,000 kg CO2-eq
- Use phase: 12,000 × 2.31 = 27,720 kg CO2-eq
- Upstream fuel: 12,000 × 0.15 = 1,800 kg CO2-eq
- End-of-life: -300 kg CO2-eq
- **TOTAL: 35,220 kg CO2-eq**

**Comparative Advantage (EU Grid):**
- Tesla: 23,100 kg CO2-eq
- Gasoline: 35,220 kg CO2-eq
- **Reduction: 12,120 kg CO2-eq (34% lower)**

**Payback Period:**
- Manufacturing carbon difference: 9,900 - 6,000 = 3,900 kg CO2-eq
- Per-km operational advantage: (27,720 + 1,800 - 13,500) ÷ 200,000 = 0.081 kg CO2-eq/km
- Break-even: 3,900 ÷ 0.081 = 48,000 km (~3 years typical driving)

---

### 4.6 Extended Lifetime Analysis

**Question:** What if vehicle lasts 300,000 km (increasingly common with EV durability)?

**Tesla Extended (300,000 km on EU grid):**
- Manufacturing: 9,900 kg CO2-eq
- Use phase: 50,000 kWh × 0.4 = 20,000 kg CO2-eq
- **TOTAL: 29,900 kg CO2-eq (0.100 kg CO2-eq/km)**

**Gasoline Extended (300,000 km):**
- Manufacturing: 6,000 kg CO2-eq
- Use phase: 18,000 liters × 2.31 = 41,580 kg CO2-eq
- Upstream: 18,000 × 0.15 = 2,700 kg CO2-eq
- **TOTAL: 50,280 kg CO2-eq (0.168 kg CO2-eq/km)**

**Extended Use Advantage:**
- Tesla: 29,900 kg CO2-eq
- Gasoline: 50,280 kg CO2-eq
- **Reduction: 20,380 kg CO2-eq (40% lower)**

**Key Insight:** EV advantage grows with vehicle lifetime. Longer-lasting vehicles are more sustainable than shorter-lived replacements.

---

## Part 5: Cross-Case Synthesis & Decision Framework

### 5.1 Common Themes Across Cases

**1. Operational Phase Usually Dominates**
- Hand dryer: 92% from electricity use
- Gasoline car: 81% from fuel combustion
- Exception: Paper towel case where manufacturing dominates but waste amplifies impact

**2. Electricity Grid Carbon Intensity is Critical**
- Coal grid: Doubles or triples use-phase impacts
- Renewable grid: Reduces use-phase by 75%+
- This single variable can flip recommendations

**3. Product Durability & Lifespan Matters**
- Longer-lasting products = lower per-unit impact
- Cloth towel must be used 100+ times to break even
- EV advantage grows with lifetime kilometers

**4. Barrier/Performance Properties Critical**
- Popcorn packaging must protect product or waste increases impact
- Hand dryer must actually dry hands in reasonable time
- Poor performance creates hidden environmental costs

**5. User Behavior Often Decisive**
- Cloth towel impact depends on wash frequency and water heating
- Paper towel impact depends on sheets used per hand drying
- Car impact depends on driving patterns and grid mix

---

### 5.2 Decision Framework for LCA Application

**Step 1: Define Functional Unit Clearly**
- "Drying hands once for one person" ← Specific
- NOT "hand dryer vs. towels" ← Ambiguous

**Step 2: Establish System Boundaries**
- What stages to include? (manufacturing, use, end-of-life)
- What geographic scope? (local, regional, global)
- What time scope? (1 year, 10 years, product lifetime)

**Step 3: Collect Data with Priority**
- Identify hotspots (highest impact stages)
- Collect detailed data for hotspots
- Use generic data for minor impacts

**Step 4: Perform Sensitivity Analysis**
- Grid carbon intensity (for electric products)
- Product lifetime and usage rates
- User behavior assumptions
- Allocation methods

**Step 5: Communicate Results Clearly**
- Show uncertainty ranges (not false precision)
- Highlight key assumptions
- Explain trade-offs and limitations

---

### 5.3 When NOT to Use LCA

- **Single-issue decisions** (use focused tools instead)
- **Time-constrained decisions** (LCA takes weeks/months)
- **Insufficient data** (garbage in = garbage out)
- **Trivial impacts** (carbon footprint of a pen: mL CO2, not worth study)
- **When weighting prevents consensus** (too subjective)

---

*This case study collection illustrates how LCA methodology applies to real products and decisions. Each case demonstrates the importance of clear boundaries, critical thinking about hidden impacts, and sensitivity to key assumptions.*
