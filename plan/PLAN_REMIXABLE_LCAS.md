# Remixable LCA Studies — Textiles & Fibres

Well-known, publicly available Life Cycle Assessment studies that can be
recreated as simplified educational models using the recipe card format in
this project. Each entry includes the key numbers, supply chain structure,
key findings, and scenario remix ideas.

---

## 1. Levi's 501 Jeans LCA (2015)

**What it covers:** Full cradle-to-grave lifecycle of one pair of Levi's® 501®
jeans (medium stone wash, 100% cotton denim).

**Functional unit:** One pair of Levi's 501 jeans worn over its full useful life.

**GWP result:** 33.4 kg CO₂-eq per pair (cradle to grave).

**Hotspot:** Consumer washing and drying (37% of total), followed by fabric
milling (27%).

**Supply chain:**
Cotton farm → Spinning + Weaving + Dyeing (fabric mill) → Cut + Sew (garment factory) → Distribution + Consumer use + End of life

**Stage breakdown:**

| Stage | CO₂ |
|---|---|
| Cotton farming | 2.9 kg |
| Fabric mill (electricity) | 9.0 kg |
| Garment factory (electricity) | 2.6 kg |
| Distribution + sundries + end of life | 6.4 kg |
| Consumer washing + drying (electricity) | 12.5 kg |
| **Total** | **33.4 kg** |

**Already in this project:** `lca_analysis/levis/` — base case plus 7 scenario variants.

### Key findings and conclusions

- The single biggest source of CO₂ is not the factory — it is **the customer's
  washing machine and tumble dryer**, responsible for 37% of the jeans' entire
  lifetime carbon footprint. This is deeply counterintuitive for most people.
- The fabric mill (spinning, dyeing, weaving) is the second largest contributor
  at 27%, driven almost entirely by electricity consumption in energy-intensive
  wet-processing steps like dyeing.
- Cotton farming itself is a relatively small contributor (just 9%) — a surprise
  to students who assume "natural fibre = green fibre."
- The study's most quoted business conclusion: **if a consumer washes their jeans
  every 10 wears instead of every 2–3 wears, they could cut the jeans' total
  climate impact by 25–30%** — without the brand changing anything in production.
- This means a brand's biggest lever for reducing product carbon footprint is
  **consumer education**, not factory investment — a major reframing for
  marketing and sustainability teams.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_wash1x` | Consumer washes only once (extreme care) | What is the theoretical minimum? |
| `_wash2x` | Consumer washes every 2 wears | What if care labelling said "wash less"? |
| `_wash5x` | Consumer washes every 5 wears | Realistic "conscious consumer" behaviour |
| `_wash10x` | Consumer washes every 10 wears | Levi's "wash less" campaign target |
| `_renewable` | Factory and mill switch to renewable energy | What if the supply chain decarbonised? |
| `_organic` | Organic cotton (no synthetic fertilizers) | Is organic cotton worth the premium? |
| `_longlife` | Jeans last twice as long (functional unit = per wear) | What is the value of durability? |
| `_bestcase` | Renewable energy + wash 10× + organic cotton | Maximum impact reduction combined |

---

## 2. Cotton Inc. U.S. Cotton Fiber LCA (2012)

**What it covers:** 1 kg of U.S. raw cotton fiber, cradle to farm gate (ginned
lint ready for spinning). Based on data from 753 cotton growers across 17 states.

**Functional unit:** 1 kg of cotton fiber at the gin gate.

**GWP result:** 1.45 kg CO₂-eq per kg fiber (fossil emissions only).
When biogenic carbon sequestration by the cotton plant is included, the net
figure is −0.264 kg CO₂-eq — effectively carbon-negative at the farm gate.

**Hotspot:** Nitrogen fertilizer application (N₂O emissions) and irrigation
energy.

**Supply chain:**
Land preparation → Planting + Growing (fertilizer, irrigation) → Harvest → Ginning (fibre separation)

### Key findings and conclusions

- U.S. cotton at farm gate has a **surprisingly low carbon footprint** compared
  to synthetic fibres — 1.45 kg CO₂/kg vs. ~9.5 kg CO₂/kg for virgin polyester.
  The problem is not where cotton comes from, but what happens to it after the
  farm (milling, dyeing, consumer use).
- The biogenic carbon finding — that cotton can be **net carbon-negative at the
  farm gate** — is scientifically contested but commercially significant. Cotton
  Inc. uses it to argue that cotton farming sequesters more CO₂ in biomass and
  soil than it emits. This is a live debate in the industry.
- **Nitrogen fertilizer is the dominant hotspot**: synthetic N fertilizer releases
  nitrous oxide (N₂O) during application, and N₂O has a global warming potential
  ~273× that of CO₂. Reducing fertilizer use or switching to precision application
  is the highest-leverage intervention.
- Irrigation is the second hotspot — not because of water use itself, but because
  pumping irrigation water is energy-intensive. In regions dependent on
  groundwater (e.g. the Texas High Plains), this is a major concern.
- The study shows wide **regional variation** across U.S. states — cotton grown
  in rainfed areas (e.g. Georgia) has a much lower footprint than cotton grown
  in arid irrigated areas (e.g. Arizona).

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_organic` | No synthetic N fertilizer, lower yield | Is organic cotton actually lower carbon? |
| `_precision_ag` | Fertilizer reduced 30% via precision application | What does smart farming technology save? |
| `_rainfed` | No irrigation (rainfall-dependent region) | What is the benefit of sourcing from wetter regions? |
| `_biogenic` | Include CO₂ sequestration credit for cotton plant | What if carbon sequestration is counted? |
| `_renewable_gin` | Gin powered by solar energy | What does electrification of farm processing save? |
| `_vs_polyester` | Side-by-side comparison with virgin polyester at farm/production gate | Which is lower carbon: cotton or polyester? |

---

## 3. IWTO Wool Fibre LCA

**What it covers:** 1 kg of greasy (raw, unscoured) wool fibre at the farm gate.
Multiple studies synthesised across Australian, New Zealand, and U.S. farms.
Also covers a 300 g merino wool sweater worn over its useful life.

**Functional unit:** 1 kg of greasy wool at the farm gate.

**GWP result:** 8.6–26 kg CO₂-eq per kg greasy wool (wide range reflects
different farms and allocation methods). A commonly cited mid-range is ~17 kg
CO₂-eq per kg. One Australian study (Yass Region, NSW) found 24.9 kg CO₂-eq/kg.

**Hotspot:** Enteric fermentation (methane from sheep digestion) — typically
50–65% of total impact. Nitrous oxide from manure is second.

**Supply chain:**
Pasture management → Sheep (methane + manure) → Shearing → Wool classing → Transport to broker

### Key findings and conclusions

- Wool has one of the **highest carbon footprints of any fibre** per kilogram —
  much higher than cotton and even higher than virgin polyester — almost entirely
  because sheep are ruminant animals that produce methane during digestion.
  There is no technological fix for this at the animal level.
- **Methane is 27–30× more potent** as a greenhouse gas than CO₂ over a 100-year
  period. Because sheep produce so much of it, wool's climate impact is dominated
  by a gas that a fashion brand cannot currently eliminate from its supply chain.
- The **allocation method** — how environmental burden is split between wool and
  lamb/mutton from the same animal — is the most contested variable in wool LCAs
  and explains most of the 8.6–26 kg range. If most of the burden is allocated
  to meat (the higher-value product in some markets), wool looks better. If
  allocated equally by mass, wool looks worse.
- Despite this, wool has **genuine advantages** over synthetics in durability,
  biodegradability, and end-of-life. A well-cared-for wool sweater worn for 20+
  years may have a lower per-wear footprint than a cheap polyester alternative
  worn for 2 years.
- **Pasture management matters enormously**: farms that sequester carbon in soil
  through regenerative grazing can partially offset methane emissions. Some
  certified regenerative wool farms claim near-carbon-neutral outcomes.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_allocation_meat` | 80% of burden allocated to lamb/mutton, 20% to wool | How does allocation method change the story? |
| `_allocation_wool` | 80% of burden allocated to wool | Worst-case wool impact |
| `_regenerative` | Carbon sequestration credit added for regenerative grazing | What does certified regenerative wool look like? |
| `_merino_fine` | Finer merino wool (higher value per kg, fewer sheep needed) | Does premium wool have a lower footprint? |
| `_new_zealand` | NZ farm (mostly rainfall, less irrigation, lower emissions factor) | How much does geography matter? |
| `_vs_cotton` | Side-by-side with cotton fibre | Is wool better or worse than cotton? |
| `_per_wear` | Functional unit changed to "per wear" for a wool sweater worn 10 years | What happens when you account for durability? |

---

## 4. Patagonia Synchilla Snap-T Fleece Jacket LCA (2013)

**What it covers:** Patagonia Synchilla Snap-T fleece pullover made from
recycled polyester (rPET from post-consumer plastic bottles), compared to an
equivalent jacket made from virgin polyester.

**Functional unit:** One fleece jacket worn over its useful life.

**GWP result:** Making from recycled polyester uses ~42% less CO₂ than virgin
polyester. Energy use is approximately 50% lower.

**Hotspot:** Fibre production stage — the difference between petroleum-derived
virgin PET and bottle-recycled rPET drives almost all of the savings.

**Supply chain (virgin path):**
Crude oil → Naphtha → PTA → PET granules → Fibre spinning → Fabric knitting → Garment assembly

**Supply chain (recycled path):**
Collected PET bottles → Shredding + washing → Pelletising → Fibre spinning → Fabric knitting → Garment assembly

**Note:** Patagonia has not released a full public LCA report — only summary
findings. The numbers are well-cited in trade press but the underlying data
is not publicly available.

### Key findings and conclusions

- **Switching from virgin to recycled polyester cuts the jacket's carbon footprint
  by roughly 42%** — entirely at the fibre production stage. Everything downstream
  (knitting, sewing, consumer care) is the same.
- The key insight for brands: **recycled polyester is not a premium or niche
  choice** — it is already cost-competitive with virgin polyester at scale, and
  several major brands (Patagonia, H&M, Nike, Adidas) have committed to high
  percentages of recycled content.
- A critical limitation: recycled polyester still ends up as microplastic in
  waterways when washed. The recycled content reduces the carbon footprint but
  does **not** solve the microplastic problem — a distinction that students often
  conflate.
- **Bottle-to-fibre recycling is not infinite**: rPET fibre cannot itself be
  easily recycled back into bottles or high-quality fibre. Each cycle downgrades
  the material. True circularity would require fibre-to-fibre recycling
  technology (e.g. chemical recycling), which is still emerging.
- Patagonia's finding that energy use drops by ~50% aligns with the broader
  industry understanding that the oil-extraction and PTA-synthesis steps are
  the most energy-intensive in polyester production.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_virgin_polyester` | Base case: jacket made from virgin PET | What is the benchmark impact? |
| `_recycled_polyester` | Jacket made from rPET (Patagonia's actual product) | What does switching to recycled save? |
| `_50pct_recycled` | Blended: 50% virgin + 50% recycled content | What if a brand makes a partial commitment? |
| `_renewable_factory` | Manufacturing powered by renewable energy | What if factories also clean up? |
| `_longlife` | Jacket worn 20 years vs. typical 5-year assumption | What is the value of a repair programme? |
| `_fibre_to_fibre` | Future scenario: chemical recycling (90% lower vs. virgin) | What does true circularity look like? |

---

## 5. Virgin Polyester (PET) Fibre LCA

**What it covers:** 1 kg of virgin polyester (PET) staple fibre, cradle to
gate. Standard dataset used across the industry via ecoinvent and the Higg MSI.

**Functional unit:** 1 kg of polyester fibre ready for spinning.

**GWP result:** 9.5–14.0 kg CO₂-eq per kg fibre. A commonly cited figure from
ecoinvent is ~9.5 kg CO₂-eq/kg. Chinese production studies find ~12 kg CO₂-eq/kg.

**Hotspot:** PTA (purified terephthalic acid) production and PET polymerisation
— both energy-intensive petrochemical processes.

**Supply chain:**
Crude oil → Naphtha (refinery) → PTA production → PET polymerisation → Fibre spinning → Staple cutting

### Key findings and conclusions

- Virgin polyester has a **much higher carbon footprint per kg than cotton** at
  the fibre stage (~9.5 vs ~1.45 kg CO₂/kg), but this comparison is often
  misleading because polyester garments tend to be lighter, dry faster, and
  require less energy in consumer care.
- **Geography of production matters significantly**: the same PET fibre
  manufactured in China (coal-heavy grid) has a ~25% higher carbon footprint
  than the same fibre made in Europe (lower-carbon grid). A brand sourcing from
  different countries gets very different footprints for the "same" product.
- Polyester is essentially **fossilised carbon in fibre form** — it is made from
  oil, worn for a few years, and then landfilled or incinerated, releasing that
  carbon back to the atmosphere. This is a fundamentally non-circular model.
- Despite its high production footprint, polyester dominates the market (over 50%
  of all fibre produced globally) because it is **cheap, durable, versatile, and
  easy to care for**. Understanding why polyester won commercially is important
  for understanding how to change the industry.
- **Polyester vs. cotton is the central debate** in sustainable fashion — but the
  correct answer almost always depends on the functional unit and the use phase
  assumptions. An LCA that ignores washing frequency will reach different
  conclusions than one that includes it.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_china_grid` | High-carbon electricity (coal-heavy Chinese grid, 0.8 kg CO₂/kWh) | What does sourcing location do to the footprint? |
| `_europe_grid` | Lower-carbon grid (European average, 0.3 kg CO₂/kWh) | What if production moved to cleaner grids? |
| `_renewable_factory` | Factory runs on 100% renewable energy | What does full electrification save? |
| `_vs_recycled` | Side-by-side with rPET fibre | How much does the recycled label actually matter? |
| `_vs_cotton` | Side-by-side with cotton fibre at equivalent use stage | Which is actually better for a t-shirt? |
| `_bio_pet` | Bio-based PET (from sugarcane, not oil) | What if oil is replaced with plant feedstock? |

---

## 6. Made-By Environmental Benchmark for Fibres (2012–2017)

**What it covers:** Comparative benchmark across 9 common fibre types, rated
A (lowest impact) to E (highest). Made-By closed as an organisation in 2018
but the benchmark is widely archived and cited.

**Functional unit:** 1 kg of fibre at the spinning stage (cradle to fibre).

**Rankings (A = best, E = worst):**

| Class | Fibres |
|---|---|
| A | Recycled polyester, recycled nylon, recycled cotton |
| B | Organic cotton (with certifications) |
| C | Conventional linen, hemp |
| D | Conventional cotton, conventional polyester |
| E | Virgin nylon, conventional wool, conventional viscose/rayon |

### Key findings and conclusions

- The benchmark's most striking finding: **recycled synthetics outperform natural
  fibres** on climate impact at the fibre production stage. Recycled polyester
  (Class A) is better than organic cotton (Class B) and far better than
  conventional wool (Class E). This directly contradicts the common consumer
  assumption that "natural = sustainable."
- **Conventional cotton and conventional polyester are rated the same** (Class D)
  — a finding that challenges both the "cotton is bad" narrative and the
  "synthetics are fine" assumption.
- **Wool is rated Class E** (worst category) — alongside virgin nylon. Most
  fashion consumers do not know this. For a sustainability-focused brand, wool
  sourcing requires careful justification beyond "it's natural."
- The benchmark only covers fibre production — it does not include dyeing,
  finishing, consumer care, or end of life. A complete LCA might reorder some
  fibres significantly (e.g. wool's durability advantage over a long life).
- As a teaching tool, the A–E class system is **more powerful than raw numbers**
  for non-technical audiences because it removes false precision and focuses on
  relative comparison.

### Remix scenarios

The Made-By benchmark is best modelled as a **multi-product comparison** rather
than a single recipe card. The most effective approach is to build individual
recipe cards for each fibre and run them side by side:

| Comparison | Recipe cards needed | What it teaches |
|---|---|---|
| Cotton vs. polyester vs. wool | 3 fibre recipe cards | The core triangle of the fashion industry |
| Conventional vs. organic cotton | 2 recipe cards | Is organic certification worth the cost? |
| Virgin vs. recycled (polyester or nylon) | 2 recipe cards | The recycled content argument |
| Class A vs. Class E fibres | 2 recipe cards | Best case vs. worst case in the industry |
| Full 9-fibre comparison | 9 recipe cards | Complete picture for a sourcing decision |

---

## 7. Viscose / Rayon Fibre LCA (IVL Swedish Environmental Research Institute)

**What it covers:** 1 kg of conventional viscose (rayon) staple fibre, from
wood pulp through chemical dissolution and wet spinning. Published as part of
IVL's screening LCA of Swedish textile consumption.

**Functional unit:** 1 kg of viscose fibre at spinning gate.

**GWP result:** ~10.1 kg CO₂-eq per kg viscose fibre (cradle to gate).
For comparison, lyocell (TENCEL) — which uses a closed-loop solvent process —
comes in at ~3–5 kg CO₂-eq per kg.

**Hotspot:** The xanthation step (dissolving cellulose in carbon disulfide
solvent) is highly energy-intensive and releases toxic emissions. The energy
use in spinning is also significant.

**Supply chain:**
Forest / plantation → Wood chipping → Pulping → Alkali cellulose production → Xanthation (CS₂ solvent) → Wet spinning → Fibre washing + drying

### Key findings and conclusions

- Viscose is one of the most misunderstood fibres in fashion. It is widely
  marketed as a **"natural" or "plant-based" fibre** (it comes from wood pulp),
  but its production process is one of the most chemically intensive in the
  textile industry, using carbon disulfide (CS₂) — a highly toxic solvent.
- At ~10 kg CO₂/kg, viscose's carbon footprint is **comparable to virgin
  polyester** — much higher than most consumers assume for a "natural" fibre.
- **TENCEL (lyocell)** uses a closed-loop process where 99%+ of the solvent is
  recovered and reused, dramatically cutting emissions to ~3–5 kg CO₂/kg. This
  is the most important comparison in the viscose family and a powerful lesson
  in how process chemistry determines environmental impact.
- The **sourcing of wood pulp** is a significant variable: viscose from certified
  sustainably managed forests (FSC/PEFC) has a better land-use profile than
  from ancient or endangered forests. Canopy, an NGO, publishes an annual ranking
  of viscose producers by forest risk.
- Carbon emissions are only part of the picture for viscose: **water use, toxic
  chemical discharge, and worker health risks** from CS₂ exposure are arguably
  more significant. A full multi-impact LCA tells a very different story than
  a carbon-only study.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_conventional_viscose` | Base case: standard viscose process | What does conventional rayon actually cost? |
| `_lyocell_tencel` | Closed-loop solvent process (TENCEL) | What does choosing TENCEL instead save? |
| `_modal` | Modal (improved viscose, less chemical intensive) | Is modal better than standard viscose? |
| `_certified_wood` | FSC-certified sustainably managed forest source | Does sustainable sourcing matter for carbon? |
| `_renewable_mill` | Mill powered by renewable energy | How much does energy source affect viscose? |
| `_vs_cotton` | Side-by-side with cotton at fibre stage | Is viscose better or worse than cotton? |

---

## 8. Repreve Recycled Polyester LCA (Unifi / TNO, 2021–2023)

**What it covers:** 1 kg of Repreve recycled polyester fibre (made from
post-consumer PET bottles) compared directly to 1 kg of virgin polyester
fibre. Peer-reviewed study published in Textile Research International (2021),
with updated findings from Unifi in 2023.

**Functional unit:** 1 kg of polyester fibre (recycled vs. virgin).

**GWP result:** Recycled polyester reduces GHG emissions by 42–80% vs. virgin,
depending on the methodology and allocation assumptions. A published peer-reviewed
figure is ~3–5 kg CO₂-eq per kg for recycled vs. ~9.5–14 kg for virgin.

**Hotspot:** The avoided petroleum extraction and PTA production — switching
from oil to bottles eliminates the most energy-intensive steps.

**Supply chain (recycled):**
Collected PET bottles → Sorting + baling → Shredding + washing → Melt extrusion → Chip drying → Fibre spinning

### Key findings and conclusions

- The 42–80% range in reported savings is not scientific uncertainty — it
  reflects **genuine methodological choices** about how to allocate the burden
  of the original bottle production. If the bottle is given zero burden
  (it is waste), recycled polyester looks much better. If the bottle shares
  its production burden, it looks somewhat less good. This is a live debate.
- **Collection and sorting infrastructure is a hidden bottleneck**: recycled
  polyester is only as good as the collection system feeding it. In countries
  with poor bottle collection rates, the "recycled" supply chain becomes much
  harder to sustain at scale.
- Repreve specifically sources from post-consumer bottles (not industrial waste),
  which is held to a **higher standard of circularity** but also has higher
  collection and cleaning costs than industrial scrap recycling.
- Even at the optimistic end (80% reduction), recycled polyester still emits
  roughly **2–3 kg CO₂ per kg** — not zero. It is much better than virgin, but
  not carbon-neutral. Brands should be careful with language like "sustainable"
  or "green" without qualification.
- The study is a good example of a **named-brand LCA** — Unifi commissioned it
  specifically to support Repreve's marketing claims, which means the methodology
  choices likely favour the most favourable plausible result. Independent
  replication would be useful.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_virgin_baseline` | Virgin polyester (base case for comparison) | What is the starting point? |
| `_recycled_optimistic` | 80% reduction (zero burden on bottle) | Best-case recycled polyester claim |
| `_recycled_conservative` | 42% reduction (partial burden on bottle) | Conservative, defensible recycled claim |
| `_low_collection_rate` | 30% bottle collection rate in supply country | What happens in markets with poor recycling? |
| `_chemical_recycling` | Future technology: fibre-to-fibre chemical recycling | What could true circularity achieve? |
| `_renewable_reprocessing` | Recycling facility powered by renewables | Stacking recycled content + renewable energy |

---

## 9. Nylon 6 Fibre LCA

**What it covers:** 1 kg of virgin Nylon 6 (polyamide 6) fibre, cradle to
gate. Compared alongside recycled nylon (e.g. Econyl, made from discarded
fishing nets and carpet waste).

**Functional unit:** 1 kg of nylon fibre ready for spinning or weaving.

**GWP result:**
- Virgin Nylon 6: 5.5–8.0 kg CO₂-eq per kg (commonly cited ~6.5 kg CO₂-eq/kg)
- Recycled nylon (Econyl): ~0.2–3.0 kg CO₂-eq per kg (varies significantly
  by methodology and what credit is given for avoiding virgin production)

**Hotspot:** The adipic acid production step releases nitrous oxide (N₂O) as a
byproduct — a greenhouse gas ~273× more potent than CO₂. This makes nylon's
climate impact disproportionately high relative to its energy use alone.

**Supply chain:**
Crude oil → Benzene (refinery) → Cyclohexane → Adipic acid (N₂O released here) → Caprolactam → Polymerisation → Fibre spinning

### Key findings and conclusions

- Nylon's headline carbon number (~6.5 kg CO₂/kg) seems lower than polyester
  (~9.5 kg CO₂/kg), but this is somewhat misleading: **nylon's N₂O emissions
  from adipic acid production are so potent** that they dominate the climate
  impact even at small quantities. The chemistry, not the energy, is the hotspot.
- Modern adipic acid plants have catalytic N₂O abatement technology that can
  destroy up to 99% of N₂O before it is released. Plants with this technology
  have footprints as low as **~3–4 kg CO₂-eq/kg**; plants without it are
  closer to **8+ kg CO₂-eq/kg**. A sourcing decision that specifies abatement
  technology can cut the fibre's climate impact in half.
- **Nylon is predominantly used in activewear, hosiery, swimwear, and performance
  outerwear** — categories where there is often no direct natural fibre substitute
  with equivalent performance. This makes the recycled nylon (Econyl) story
  particularly commercially relevant.
- **Econyl** (recycled nylon from fishing nets, carpet, and industrial waste)
  has achieved widespread brand adoption (Gucci, Stella McCartney, Adidas).
  Its carbon footprint of ~0.2–3.0 kg CO₂/kg is dramatically lower than virgin,
  and it also removes plastic pollution from oceans and landfills.
- The wide range for Econyl (0.2–3.0 kg) again reflects **allocation choices**:
  if fishing nets are treated as zero-burden waste, Econyl looks nearly carbon-
  neutral. If some net-production burden is shared, it rises.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_virgin_no_abatement` | No N₂O abatement at adipic acid plant | What is worst-case nylon production? |
| `_virgin_abatement` | 99% N₂O abatement technology installed | What does specifying abatement technology achieve? |
| `_econyl_optimistic` | Recycled nylon, zero burden on waste feedstock | Best-case Econyl claim |
| `_econyl_conservative` | Recycled nylon, partial burden on waste feedstock | Defensible Econyl claim |
| `_vs_polyester` | Side-by-side nylon vs. polyester for a swimwear application | Which synthetic is better for this use case? |
| `_renewable_plant` | Polymerisation powered by renewable electricity | What if the factory switches to clean energy? |

---

## 10. thredUP / Green Story — Second-Hand vs. New Clothing LCA (2019)

**What it covers:** Comparative LCA of buying one average second-hand garment
from thredUP vs. buying an equivalent new garment. Covers 22 clothing categories
and 26 fibre types. Prepared by Green Story Inc. for thredUP, following ISO
14040/14044.

**Functional unit:** One average second-hand item of apparel sold online by
thredUP in the USA, which replaces a similar new item bought by consumers in
the USA.

**GWP result:**
- New garment (manufacturing + end of life): 39.4 kg CO₂-eq per kg = ~15.8 kg per average 0.4 kg garment
- thredUP operations only (collection + sorting + shipping): ~4.8 kg CO₂-eq per kg = ~1.9 kg per garment
- Net saving from buying secondhand: 22.8 kg CO₂-eq per kg (~58% less on a per-wear basis)

**Key assumption:** The study assumes 100% displacement — every thredUP buyer
would have bought new if thredUP didn't exist. Relaxing this to 72% (the 2022
updated estimate) reduces the headline savings by ~28%.

**Supply chain (new garment):**
Fibre production → Yarn spinning → Fabric weaving → Dyeing + finishing → Assembly → Distribution → End of life

**Supply chain (secondhand):**
Seller ships clean-out kit → thredUP sorts + lists online → Ships to buyer → End of life

**Already in this project:** `lca_analysis/thredup/` — base case (new garment)
plus 5 secondhand scenario variants.

### Key findings and conclusions

- Buying secondhand can be **88% lower carbon** than buying new on a per-garment
  basis — but only if the buyer truly would have bought new otherwise. The
  displacement assumption is everything.
- The study's most commercially important conclusion: **secondhand is only
  sustainable if it displaces new purchasing**. If a customer buys secondhand
  as an *addition* to their existing new purchases (what researchers call
  "additionality failure"), there is no net saving at all.
- The study found (in 2019) that 100% of thredUP's customers were first-time
  secondhand buyers who said they would have bought new otherwise. By 2022,
  as secondhand became mainstream, this figure had dropped to ~72% — meaning
  the headline savings figure shrank significantly as thredUP's own success
  brought in customers who were already secondhand shoppers.
- The **remaining useful life of the garment** is a second major variable.
  The study assumes 70% of useful life remains when thredUP sells it. Premium
  resale platforms (e.g. The RealReal for luxury) may have garments with 85–90%
  of useful life remaining; lower-grade platforms may have 50%.
- **thredUP's own operations** (sorting, warehousing, shipping) account for
  only ~10–12% of the total secondhand system's emissions — meaning even a
  dramatic improvement in warehouse energy (e.g. switching to solar) would
  only modestly change the headline saving. The big lever is the displacement
  rate, not the warehouse.

### Remix scenarios

| Scenario | What changes | Business question it answers |
|---|---|---|
| `_secondhand_base` | 100% displacement, 70% life remaining (study base case) | What does thredUP claim? |
| `_renewable_warehouse` | thredUP warehouse on solar/wind | What does warehouse decarbonisation achieve? |
| `_highquality` | 85% useful life remaining (premium curation) | Does quality curation improve the case? |
| `_partial_displacement_50` | Only 50% of buyers truly switch from new | What if half the customers were already secondhand shoppers? |
| `_partial_displacement_72` | 72% displacement (2022 updated estimate) | What is the real-world adjusted saving? |
| `_bestcase` | Renewable warehouse + 85% life + 100% displacement | What is the ceiling for secondhand's benefit? |
| `_electric_delivery` | Last-mile delivery by electric van | What does green logistics add? |
| `_local_resale` | No shipping (in-person charity shop equivalent) | What if there were no delivery at all? |

---

## Priority order for building recipe cards

| Priority | Study | Why |
|---|---|---|
| ✅ Done | Levi's 501 Jeans | Multi-stage supply chain, consumer use hotspot |
| ✅ Done | thredUP Secondhand | Displacement concept, system expansion |
| Next | Cotton Inc. Cotton Fibre | Clean linear chain, farm-gate emissions |
| Next | IWTO Wool | Methane from animals — surprises students |
| Next | Virgin vs. Recycled Polyester | Natural A-vs-B scenario comparison |
| Later | Viscose / Rayon vs. TENCEL | "Natural-origin but chemical-intensive" lesson |
| Later | Nylon 6 vs. Econyl | N₂O hotspot, abatement technology lever |
| Later | Made-By Benchmark | Multi-fibre comparison table |
| Later | Patagonia Fleece | Limited public data — needs estimation |
