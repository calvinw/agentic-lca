# Remixable LCA Studies — Textiles & Fibres

Well-known, publicly available Life Cycle Assessment studies that can be
recreated as simplified educational models using the recipe card format in
this project. Each entry includes the key numbers, supply chain structure,
and links to the original source data.

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

**Source:**
- Full LCA Results Deck (free PDF): https://www.levistrauss.com/wp-content/uploads/2015/03/Full-LCA-Results-Deck-FINAL.pdf
- Summary via EU Cluster Collaboration Platform: https://www.clustercollaboration.eu/content/life-cycle-assessment-levis-jeans-case

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

**Source:**
- Full 2012 LCA report (free PDF): https://cottoncultivated.cottoninc.com/wp-content/uploads/2015/06/2012-LCA-Full-Report.pdf
- Summary via CottonWorks: https://cottonworks.com/cotton-sustainability/life-cycle-assessment-of-cotton/
- 2026 updated technical report via Textile Exchange: https://textileexchange.org/app/uploads/2026/03/Cotton-LCA-Technical-Report.pdf

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

**Source:**
- IWTO LCA guidelines (free PDF): https://iwto.org/wp-content/uploads/2020/04/IWTO-Guidelines-for-Wool-LCA.pdf
- IWTO LCA summary page: https://iwto.org/sustainability/life-cycle-assessment/

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

**Source:**
- Patagonia environmental responsibility page: https://www.patagonia.com/our-responsibility-programs.html
- Trade summary: https://bettertrail.com/sustainability/patagonia-reclaimed-fleece-jacket-report

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

**Source:**
- Higg Materials Sustainability Index (Cascale/Worldly): https://cascale.org/tools-programs/higg-index-tools/product-tools/
- LCA benchmarking study (ResearchGate, free): https://www.researchgate.net/publication/258220983_LCA_benchmarking_study_on_textiles_made_of_cotton_polyester_nylon_acryl_or_elastane
- ecoinvent database (subscription required): https://ecoinvent.org

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

**Best for teaching:** Side-by-side comparison across fibre types without
overwhelming students with raw numbers.

**Source:**
- Benchmark chart and methodology (ResearchGate, free): https://www.researchgate.net/figure/Made-By-Environmental-Benchmark-for-fibres_fig1_320307130
- Textile Exchange LCA FAQ (references the benchmark): https://textileexchange.org/lca-faq/

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

**Source:**
- IVL environmental impact of Swedish textile consumption (free PDF, Diva Portal): https://www.diva-portal.org/smash/get/diva2:826159/FULLTEXT01.pdf
- IVL LCA services page: https://www.ivl.se/english/ivl/our-offer/our-services/life-cycle-assessment-of-textiles.html

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

**Source:**
- Peer-reviewed journal article (Sage Journals, 2021): https://journals.sagepub.com/doi/abs/10.1177/00405175211006213
- Repreve/Unifi LCA announcement (FashionUnited, 2023): https://fashionunited.com/news/business/repreve-lca-shows-climate-impact-of-recycled-polyester-vs-virgin-polyester/2023072655058

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

**Source:**
- LCA benchmarking study — cotton, polyester, nylon, acrylic, elastane (ResearchGate, free): https://www.researchgate.net/publication/258220983_LCA_benchmarking_study_on_textiles_made_of_cotton_polyester_nylon_acryl_or_elastane
- Made-By benchmark (nylon classified Class E): https://www.researchgate.net/figure/Made-By-Environmental-Benchmark-for-fibres_fig1_320307130
- Higg MSI (Cascale): https://cascale.org/tools-programs/higg-index-tools/product-tools/

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

**Source:**
- Full LCA study PDF (free, from thredUP): https://cf-assets-tup.thredup.com/about/pwa/thredUP-Clothing-Lifecycle-Study.pdf
- thredUP annual resale reports (updated displacement figures): https://www.thredup.com/resale/

---

## Priority order for building recipe cards

| Priority | Study | Why |
|---|---|---|
| ✅ Done | Levi's 501 Jeans | Multi-stage supply chain, consumer use hotspot |
| ✅ Done | thredUP Secondhand | Displacement concept, system expansion |
| Next | Cotton Inc. Cotton Fibre | Clean linear chain, farm-gate emissions |
| Next | IWTO Wool | Methane from animals — surprises students |
| Next | Virgin vs. Recycled Polyester | Natural A-vs-B scenario comparison |
| Later | Viscose / Rayon | "Natural-origin but chemical-intensive" lesson |
| Later | Nylon 6 | N₂O hotspot, high-impact fibre |
| Later | Made-By Benchmark | Multi-fibre comparison table |
| Later | Patagonia Fleece | Limited public data — needs estimation |
