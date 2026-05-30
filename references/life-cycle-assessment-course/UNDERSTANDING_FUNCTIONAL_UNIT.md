# Understanding the Functional Unit - The Foundation of LCA

*The single most important decision in any Life Cycle Assessment*

---

## 1. What Is a Functional Unit?

### Definition

**A functional unit is a quantified description of what the product or service does.**

It answers the question: **"What specific service or benefit am I providing?"**

It is NOT the product itself. It is what the product delivers.

### Examples of Correct Functional Units

| Product | Product Description | Functional Unit |
|---------|---------|---------|
| Plastic bag | 1 plastic bag | Carrying 10 kg of groceries from store to home |
| Paper bag | 1 paper bag | Carrying 10 kg of groceries from store to home |
| Car | 1 automobile | Transporting 1 ton of payload 150,000 km |
| Light bulb | 1 incandescent bulb | Providing lighting for 50,000 hours in a room |
| T-shirt | 1 garment | Providing thermal coverage for 1 person for 100 wears |
| Hand dryer | 1 electric dryer | Drying hands once for one person |
| Coffee | 1 kg of coffee | Providing 200 cups of coffee beverages |
| Milk packaging | 1 bottle | Protecting and storing 1 liter of milk |
| Reusable cup | 1 ceramic cup | Providing beverage container for 1,000 uses |

### Why This Matters

The functional unit is the **reference point** for all calculations. Everything in the LCA is ultimately expressed per functional unit.

---

## 2. The Fundamental Problem: Products Are Different

### The Grocery Bag Dilemma

**Question:** Is a plastic bag or paper bag more sustainable?

**Naive Answer:** "Paper bag! Paper is biodegradable!"

**Reality Check:**
- Plastic bag capacity: 10 kg
- Paper bag capacity: 5 kg
- Shopping trip needs: Carrying 10 kg of groceries

**Correct Comparison:**
```
Option A (Plastic): 1 plastic bag × 30g = 30g material
Option B (Paper): 2 paper bags × 50g each = 100g material
```

**Result:** Plastic is lighter, but is that the full picture? Maybe the plastic gets reused...

### The Light Bulb Example

**Question:** Is LED or incandescent more sustainable?

**Naive Comparison:**
- Incandescent: costs $1, lasts 1,000 hours
- LED: costs $10, lasts 50,000 hours

**Manufacturing Impact:**
- Incandescent: Low manufacturing impact (simple)
- LED: High manufacturing impact (complex electronics)

**Without functional unit:** LED looks bad (higher manufacturing = higher impact)

**With functional unit:** "Providing 50,000 hours of light"
- Buy 50 incandescent bulbs → 50 × manufacturing impact + electricity use over 50,000 hours
- Buy 1 LED bulb → 1 × higher manufacturing impact + minimal electricity use

**With functional unit:** LED wins decisively on total impact!

### The Cloth Towel vs. Paper Towel Problem

**Question:** Should we use reusable cloth or disposable paper?

**Without functional unit, comparing 1 item:**
- 1 cloth towel: ~100g material, high manufacturing impact
- 1 paper towel: ~2g material, low manufacturing impact
- **Cloth seems bad!**

**With functional unit:** "Drying hands for 100 hand-drying events"
- 1 cloth towel used 100 times: 100g + washing impacts
- 100 paper towels: 200g + 0 washing
- **Impacts depend on washing water heating, drying method, etc.**

---

## 3. Why Products Are Incomparable Without a Functional Unit

### The Underlying Issue: Products Have Different Properties

**A plastic bag and paper bag are not interchangeable:**
- Different capacity
- Different durability
- Different reusability
- Different barrier properties (moisture, oxygen)

**If you compare them directly (1 to 1), you're comparing apples to oranges.**

### The "Carrying Capacity" Problem

```
Scenario 1: Comparing 1 plastic to 1 paper (WRONG)
  - Plastic impact: 10 kg CO2-eq
  - Paper impact: 15 kg CO2-eq
  - Conclusion: "Plastic is better!"

Scenario 2: Comparing by functional unit (CORRECT)
  - Functional unit: "Carrying 10 kg groceries home once"
  
  Plastic option:
    - Need: 1 plastic bag
    - Impact: 10 kg CO2-eq
    - Per functional unit: 10 kg CO2-eq
  
  Paper option:
    - Need: 2 paper bags (10 kg capacity needs 2 bags)
    - Impact: 15 kg CO2-eq × 2 = 30 kg CO2-eq
    - Per functional unit: 30 kg CO2-eq
  
  - Conclusion: "Plastic is better!" (but for a different reason)
```

**Same conclusion, but now justified by actual function!**

---

## 4. Properties That Vary Between Products Serving Same Function

### 1. Durability / Lifespan
```
Product A: Lasts 1 year (500 uses)
Product B: Lasts 5 years (2,500 uses)

Functional unit: "1 hand drying event"

Product A: 100 kg CO2-eq ÷ 500 uses = 0.2 kg CO2-eq per use
Product B: 120 kg CO2-eq ÷ 2,500 uses = 0.048 kg CO2-eq per use

Product B is 4× better per use, despite higher total manufacturing!
```

### 2. Capacity / Efficiency
```
Light bulb A: 60W, produces 600 lumens
Light bulb B: 9W, produces 600 lumens

Functional unit: "Producing 600 lumens of light for 1 hour"

Bulb A: 60 Wh electricity per hour
Bulb B: 9 Wh electricity per hour

Bulb B is 85% more efficient!
```

### 3. Barrier Performance / Product Loss
```
Packaging A: Poor barrier → 20% product spoilage
Packaging B: Good barrier → 0% spoilage

Functional unit: "Protecting 1 kg of popcorn for 3 months"

Package A: 50g material + spoilage loss = 50g + (0.2 × 1000g = 200g CO2-eq from wasted popcorn)
Package B: 80g material + no spoilage = 80g

Package A has hidden cost from product loss!
```

### 4. Reusability / Replacement Rate
```
Container A: Single-use, thrown away after 1 use
Container B: Reusable, washed and used 100 times

Functional unit: "Containing 1 liter of liquid for one meal"

Container A: 50g material per meal = 50 kg CO2-eq per meal
Container B: 500g material ÷ 100 uses = 5g per meal = 5 kg CO2-eq per meal (before washing impacts)

Even with washing, Container B usually wins!
```

---

## 5. How to Define a Functional Unit (Step-by-Step)

### Step 1: Identify the Product Function
**Answer: "What does this product do for the user?"**

NOT: "It's a plastic bag"
YES: "It carries things"

NOT: "It's a light bulb"
YES: "It provides light"

NOT: "It's a t-shirt"
YES: "It provides thermal coverage and modesty"

### Step 2: Quantify the Function

**Add a measurable amount to your answer:**

NOT: "It carries things"
YES: "It carries 10 kg of things"

NOT: "It provides light"
YES: "It provides 600 lumens of light for 1 hour"

NOT: "It provides thermal coverage"
YES: "It provides thermal coverage for one person for 100 wears in standard conditions"

### Step 3: Specify Conditions (if relevant)

**Some functions depend on context:**

NOT: "Transporting cargo"
YES: "Transporting 1 ton of cargo 1 km on an average road in temperate climate"

NOT: "Drying hands"
YES: "Drying hands once for one person after washing under standard conditions"

NOT: "Storing milk"
YES: "Storing and protecting 1 liter of milk at 4°C for 3 weeks in retail/home setting"

### Step 4: Consider Quality / Durability Dimensions

**Some products perform their function differently:**

**Performance quality matters:**
- Hand dryer A: Dries hands in 10 seconds
- Hand dryer B: Dries hands in 25 seconds
- Should these count the same? Maybe not if users prefer faster drying.

**This is why functional unit sometimes specifies:**
"Providing full hand drying (moisture content <5%) for one person"

---

## 6. Common Mistakes in Defining Functional Units

### Mistake 1: Using the Physical Product Instead of Function

**WRONG:**
- "1 plastic bag"
- "1 light bulb"
- "1 t-shirt"

**RIGHT:**
- "Carrying 10 kg of groceries once"
- "Providing 50,000 hours of 600-lumen lighting"
- "Providing thermal coverage for 100 wears"

**Why it matters:** Different plastic bags have different capacities. Comparing "1 bag to 1 bag" ignores the actual function performed.

---

### Mistake 2: Not Quantifying the Function

**WRONG:**
- "Carrying groceries" (how much?)
- "Providing lighting" (how long? how bright?)
- "Keeping you warm" (for how long?)

**RIGHT:**
- "Carrying 10 kg of groceries from store to home"
- "Providing 1,000 lumens of lighting for 50,000 hours"
- "Providing thermal coverage for one person for 100 wears"

**Why it matters:** Without quantity, you can't do the math. How many bulbs do you need? How many towels? You need numbers.

---

### Mistake 3: Comparing Incompatible Products

**WRONG:**
Comparing a cloth towel (reusable, durable) to a paper towel (disposable, single-use) using the same functional unit:
- "Drying hands once for one person" - This ignores the different lifespans!

**BETTER:**
Define what "one drying event" means IN CONTEXT:
- "Drying hands 100 times for one person"
- "Drying hands 500 times for one person in an office"
- Or separate analyses: household vs. commercial use

**Why it matters:** The durability difference completely changes the comparison. A towel used once is not comparable to one used 100 times.

---

### Mistake 4: Including Quality Differences Without Specifying Them

**WRONG:**
Comparing two cars with the same functional unit without accounting for:
- One is small and efficient (150 hp)
- One is large and powerful (300 hp)

**Should be:**
Separate functional units:
- "Transporting one person 1 km on highways" (small car adequate)
- "Transporting 5 people plus cargo 1 km" (large car needed)

Or specify: "Transporting 1 ton of payload 150,000 km" (performance-neutral)

---

### Mistake 5: Making the Functional Unit Too Specific to One Product

**WRONG:**
Comparing paper bag to plastic bag using functional unit:
- "Carrying a paper bag's typical grocery load"
- This biases the analysis toward plastic (different capacity)

**RIGHT:**
Use a NEUTRAL functional unit independent of product design:
- "Carrying 10 kg of mixed groceries from store to home"

The functional unit should describe the USER'S NEED, not the product's characteristics.

---

## 7. Functional Unit and System Boundaries

### How They Work Together

**Functional Unit defines WHAT is being provided.**
**System Boundaries define HOW it's provided.**

### Example: Providing Lighting

```
Functional Unit: "Providing 50,000 hours of 600-lumen lighting in a residential room"

Different systems with same functional unit:

System 1: Incandescent bulbs
├─ Mining (tungsten for filament)
├─ Manufacturing (50 bulbs × 1,000 hours each)
├─ Use phase (50 bulbs × 50,000 hours electricity)
└─ End-of-life (landfill)
Impact: Very high (mostly from electricity)

System 2: LED bulbs
├─ Mining (rare earths for LEDs)
├─ Manufacturing (1 bulb, complex electronics)
├─ Use phase (1 bulb × 50,000 hours, minimal electricity)
└─ End-of-life (recycling)
Impact: Lower total, despite higher manufacturing

Same Functional Unit, Different System → Different Conclusion!
```

### System Boundaries Must Match the Functional Unit

**If functional unit includes "use phase," system boundaries must include use phase:**

**Example - Clothing:**
```
Functional unit: "Providing thermal coverage for one person for 100 wears"

System MUST include:
├─ Growing cotton
├─ Textile manufacturing
├─ Garment assembly
├─ Transportation to store
├─ Use phase (CRUCIAL - washing impacts!)
│  ├─ Hot water heating (energy)
│  ├─ Detergent production
│  ├─ Machine operation
│  └─ Drying (air or machine)
└─ End-of-life

If you exclude washing, you've excluded 40-60% of impacts!
```

---

## 8. Different Functional Units, Different Conclusions

### The Toothbrush Example

**Functional Unit Option 1: "Brushing teeth for 1 minute"**

Electric toothbrush: 100W × 1 min = 1.67 Wh
Manual toothbrush: 0 electricity use

**Conclusion:** Manual is better!

**Functional Unit Option 2: "Cleaning teeth effectively for 1 minute"**

Electric toothbrush: Higher cleaning efficiency, 1.67 Wh, gets better cleaning
Manual toothbrush: Lower cleaning efficiency, 0 energy, less effective

Now you need data on cleaning effectiveness. Maybe electric is better?

**Functional Unit Option 3: "Maintaining dental health for 1 year"**

Electric: Fewer cavities due to superior cleaning? Lower dental disease?
Manual: More cavities possible?

Now the lifetime health impacts change the conclusion!

**Key Insight:** Different functional units can flip the conclusion. You must choose one that's NEUTRAL and COMPLETE.

---

## 9. Functional Unit for Complex Products

### Multi-Function Products

**Example: Smartphone**

**Function 1: Communication**
- "Making 1,000 phone calls of 5 minutes each"

**Function 2: Computing**
- "Providing 1,000 hours of computing capability"

**Function 3: Entertainment**
- "Providing 500 hours of entertainment"

**Which functional unit is correct?**

**Answer:** It depends on the PURPOSE of the study.
- For comparing phones as communication devices: Use communication function
- For comparing phones as computers: Use computing function
- For holistic assessment: May need to combine all three (but this is complex!)

**Real practice:** Usually choose the DOMINANT function.

---

### Multi-Component Systems

**Example: Vehicle**

**Could define as:**

Option A: "Transporting 1 ton of payload 1 km"
- Includes car plus passenger weight
- Neutral, capacity-independent

Option B: "Transporting 1 person 1 km"
- Simpler but ignores cargo capacity
- May bias toward smaller vehicles

Option C: "Providing mobility for one person for 10 years"
- Includes frequency of use
- More complex, more realistic

**Typical practice:** Option A (transporting 1 ton 1 km) is standard automotive LCA.

---

## 10. The "Apple to Apples" Test

### How to Know You Have a Good Functional Unit

**Test 1: Substitutability**
Could you truly substitute one product for another to provide this function?

"Hand drying for one person" → Yes, you could substitute dryer, cloth, towel, air-dry
"One electric dryer vs. one paper towel roll" → No! You need multiple items to serve the same function.

**Test 2: Completeness**
Does the functional unit fully describe what the product must do?

"Transporting 1 km" → Incomplete (how much weight? person or cargo?)
"Transporting 1 ton 1 km" → Complete and clear

**Test 3: Neutrality**
Is the functional unit independent of the product's design?

"Carrying a plastic bag's worth of groceries" → Not neutral (biases toward plastic)
"Carrying 10 kg of groceries" → Neutral (independent of design)

**Test 4: Quantifiability**
Can you measure if the product meets the functional unit?

"Being a good cup" → Not quantifiable
"Providing beverage container for 1,000 uses without breaking" → Quantifiable

---

## 11. Functional Unit and Allocation Problems

### How Functional Unit Relates to Allocation

**Example: Milk Production**

**Product:** 1 liter of milk produced by a dairy farm

**By-products:** Whey, buttermilk, butter, cream (from the same process)

**Question:** How much of the farm's environmental impact belongs to milk vs. butter?

**Answer depends on your functional unit:**

**If FU is "1 liter of milk":**
- Only include the milk's share of impacts
- Need allocation method (mass, economic, etc.)
- Results depend heavily on allocation method!

**If FU is "Milk and Butter production package":**
- No allocation needed
- But now you're comparing different things (milk vs. milk+butter)

**If FU is "Providing 1 protein unit":**
- Different from volume-based
- Could change which product "shares" the impact

**Key insight:** Functional unit choice drives allocation requirements.

---

## 12. Real-World Examples: How Functional Unit Changes Everything

### Example 1: Paper Bag vs. Plastic Bag (Grocery Context)

**Study Setup (from Swedish LCA):**

**Functional Unit: "Protecting groceries during transportation from store to home"**

```
Plastic bag option:
- Material: 30g plastic film
- Need: 1 bag (10 kg capacity)
- Impact: 10 kg CO2-eq
- Per function: 10 kg CO2-eq

Paper bag option:
- Material: 50g kraft paper per bag
- Need: 2 bags (5 kg capacity each) for 10 kg groceries
- Impact: 15 kg CO2-eq × 2 = 30 kg CO2-eq
- Per function: 30 kg CO2-eq

Heavy-duty plastic bag option:
- Material: 70g for thicker, more durable plastic
- Need: 1 bag, can be reused 10 times
- First use impact: 20 kg CO2-eq
- Reused 10 times: 20 ÷ 10 = 2 kg CO2-eq per use
- Per function: 2 kg CO2-eq (best option!)

Reusable cloth bag option:
- Material: 200g cotton
- Manufacturing impact: 40 kg CO2-eq
- Reused 100 times
- Per function: 40 ÷ 100 = 0.4 kg CO2-eq (best!)
```

**Conclusion:** Reusable cloth wins, IF actually reused that many times.

**But:** If cloth bag is only used 10 times before being thrown away:
- 40 ÷ 10 = 4 kg CO2-eq per use (worse than heavy-duty plastic!)

**Key lesson:** Functional unit alone isn't enough. Need to know actual use patterns.

---

### Example 2: Electric Car vs. Gasoline Car

**Naive Comparison (WRONG):**
- EV manufacturing impact: 10 tonnes CO2-eq
- Gasoline car manufacturing: 6 tonnes CO2-eq
- Conclusion: "Gasoline is better!" ❌

**With Functional Unit: "Transportation of 1 ton of payload 150,000 km"**

```
Gasoline car:
├─ Manufacturing: 6 tonnes
├─ Use (fuel consumption): 26 tonnes CO2-eq
├─ End-of-life: -0.5 tonnes (recycling credit)
└─ Total: 31.5 tonnes CO2-eq for 150,000 km
   Per km: 0.21 kg CO2-eq/km

Electric car (EU average grid 0.4 kg CO2/kWh):
├─ Manufacturing: 10 tonnes
├─ Use (electricity): 9 tonnes CO2-eq
├─ End-of-life: -0.5 tonnes
└─ Total: 18.5 tonnes CO2-eq for 150,000 km
   Per km: 0.123 kg CO2-eq/km

Conclusion: EV is 40% better, despite higher manufacturing! ✓
```

**Break-even:** Manufacturing penalty is paid back after ~50,000 km (about 3 years of driving)

**Key lesson:** Functional unit reveals that use phase dominance makes EV attractive despite manufacturing penalty.

---

### Example 3: Cloth Towel vs. Paper Towel in Office

**Functional Unit: "Drying hands for one employee, one year of work (250 work days)"**

**Cloth towel option (commercial laundry):**
```
Material: 1 large towel (500g)
Manufacturing: 15 kg CO2-eq

Use phase:
- 250 days × 5 hand dryings per day = 1,250 dryings per year
- Daily laundry (towels wash daily)
- Professional hot water laundry: 5 kg CO2-eq per day
- 250 days × 5 kg = 1,250 kg CO2-eq per year
- Plus drying (machine): 2 kg CO2-eq per day
- 250 days × 2 kg = 500 kg CO2-eq per year
- Laundry chemicals: 50 kg CO2-eq per year

Total annual: 15 amortized + 1,250 + 500 + 50 = 1,815 kg CO2-eq
Per hand drying: 1,815 ÷ 1,250 = 1.45 kg CO2-eq per drying
```

**Paper towel option:**
```
Material: 1,250 sheets per year (1,250 dryings)
Sheet weight: 2g each = 2,500g total
Impact per gram: 10 g CO2-eq/g (manufacturing + waste)
2,500g × 10 = 25,000 kg CO2-eq per year

Per hand drying: 25,000 ÷ 1,250 = 20 kg CO2-eq per drying
```

**Conclusion:** Cloth towel with commercial laundry is 13× better!

**But:** If towel in home laundry with hot water and machine drying:
- Much lower commercial scale efficiency
- Results might flip

**Key lesson:** Functional unit must include actual use context (commercial vs. residential).

---

## 13. Functional Unit in Different Types of Studies

### Attributional LCA
**Functional Unit:** Describes the product "as currently made"
- "Providing electricity from a coal plant for 1 kWh"
- Describes average, current reality

### Consequential LCA
**Functional Unit:** Describes demand change
- "Meeting 1 additional kWh of electricity demand"
- Different from attributional (may use renewable sources on the margin)

### Comparative Claims
**Functional Unit:** Must be identical for both products
- "Transporting 1 ton 1 km" for comparing two vehicles
- ISO 14040 requires strict matching

### Screening LCA
**Functional Unit:** May be simpler but still quantified
- "Producing 1 ton of product" (rather than 1 year of output)
- Faster, less detailed, but still clear

---

## 14. Quick Reference: How to State a Functional Unit

### Template

**"[QUANTITY] of [FUNCTION/SERVICE] under [CONDITIONS]"**

### Examples

✓ "Providing 1 liter of milk in a protective container for 3 weeks of storage at 4°C"

✓ "Transporting 1 ton of payload 1 km on roads of average condition"

✓ "Drying hands after washing for one person under standard temperature/humidity"

✓ "Providing thermal insulation for one person for 100 wears under temperate climate"

✓ "Delivering 1 cup of coffee beverage to a consumer"

✓ "Storing and protecting 500g of popcorn during 3-month retail shelf life"

---

## 15. Why Functional Unit Matters (Summary)

### 1. Enables Fair Comparison
Without it: "Plastic bag = 10 CO2-eq, Paper bag = 15 CO2-eq"
**Problem:** Plastic bag holds twice as much!

With it: "Carrying 10 kg groceries: Plastic = 10 CO2-eq, Paper = 30 CO2-eq"
**Solution:** Now comparing apples to apples

### 2. Reveals True Hotspots
Without it: "Cloth towel = 40 kg CO2-eq, Paper = 2 kg CO2-eq"
**Wrong conclusion:** Paper is better

With it (per 100 uses): "Cloth = 0.4 kg CO2-eq per use, Paper = 2 kg CO2-eq per use"
**Correct conclusion:** Cloth is better when used multiple times

### 3. Prevents Bias
A poorly chosen functional unit biases results toward a particular product.
A neutral, quantified functional unit prevents this bias.

### 4. Enables Standardization
Different researchers can compare their studies if they use the same functional unit.
"Transportation: 1 ton, 1 km" is a global standard.

### 5. Clarifies Decision Context
The functional unit forces you to think about what the user actually needs.
This clarity often reveals the real answer.

---

## 16. Common Questions About Functional Units

### Q: Can a product have multiple functional units?
**A:** Yes, if it serves multiple functions. But for a comparative LCA, you typically analyze one function at a time.

### Q: What if the functional unit is hard to define?
**A:** That's a sign you need to narrow the scope. Either clarify what the product does, or split into separate studies.

### Q: Is there a "standard" functional unit?
**A:** Some product categories have standard functional units (set by industry). For example:
- Cars: "Transporting 1 ton, 150,000 km"
- Light bulbs: "50,000 lumen-hours"
- Buildings: "Per m² of floor area per year"

### Q: Can the functional unit change during a study?
**A:** No. Once defined and approved, the functional unit should not change. Changing it mid-study invalidates comparisons.

### Q: How specific should the functional unit be?
**A:** Specific enough to be measurable and clear, but not so specific that it becomes arbitrary. "Drying hands once" is better than "Drying hands once in a 25°C room with 40% humidity in Northern Europe."

---

## 17. The Functional Unit is the Foundation

**Every number in an LCA ultimately serves to answer:**

### "Per [FUNCTIONAL UNIT], what is the environmental impact?"

- Manufacturing phase: "X kg CO2-eq per [functional unit]"
- Use phase: "Y kg CO2-eq per [functional unit]"
- End-of-life: "Z kg CO2-eq per [functional unit]"
- **Total: (X + Y + Z) kg CO2-eq per [functional unit]**

Without a clear, quantified functional unit, these numbers are meaningless.

**With a clear functional unit, LCA becomes a powerful decision-making tool.**

---

*The functional unit is not a minor detail—it's the entire foundation of LCA. Get it right, and all your analysis is meaningful. Get it wrong, and you're comparing apples to oranges, regardless of how precise your other numbers are.*
