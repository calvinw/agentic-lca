---
version: 0.2
name: damage-characterization
author: Junghyun Choi (elenachoi1)
description: >
  Teaching skill for the LCA concept of damage characterization — the step
  that goes beyond midpoint impact scores (kg CO2-eq, kg SO2-eq, PM 2.5-eq)
  to ask what those scores actually do to the world, in terms of three areas
  of protection: human health, ecosystem quality, and resource availability.
  Invoke as /damage-characterization <case-study>, for example
  /damage-characterization wool_yarn or /damage-characterization
  cotton_fiber. The skill reads the recipe card and lca_results.md for that
  case study and reasons qualitatively about which midpoint scores feed into
  which damage area, using a leading-indicator-vs-revenue retail analogy.
  Designed for FIT students with no science or coding background. Builds
  directly on the impact-characterization skill. Four to five exchanges to
  complete.
---

## What this skill does

This skill teaches **damage characterization** — the step in LCA that goes
one level beyond the midpoint impact scores (kg CO₂-eq, kg SO₂-eq, PM
2.5-eq) that students have already learned to calculate, and asks: *what do
these scores actually do to the world?*

**Important data note for whoever is running this skill:** this project's
openLCA pipeline computes TRACI 2.2 **midpoint** scores only. There are no
real, computed damage numbers (DALYs, species lost, resource scarcity index)
for any case study in `lca_results.md` — TRACI 2.2 as configured in this
project does not produce them. Going from midpoint to damage (sometimes
called "endpoint") requires an extended method that has not been run here.

Because of this, **do not invent precise damage numbers** for any case study.
This skill teaches the concept qualitatively: which real midpoint score(s)
feed into which damage area, and why, using reasoning rather than fabricated
arithmetic. The only numbers used in this skill are the real TRACI 2.2
midpoint scores already in `lca_results.md`, which students have already
calculated by hand in the impact-characterization skill.

Damage characterization sorts environmental harm into three **areas of
protection** — the things people actually care about, as opposed to the
chemistry that causes them:
- **Human health** — measured (in real LCA practice) in DALYs, or
  disability-adjusted life years: how many years of healthy human life are
  lost to disease, injury, or premature death caused by the pollution
- **Ecosystem quality** — how many species, across how much area and time,
  are harmed or lost
- **Resource availability** — how much harder or more expensive it becomes
  to extract natural resources in the future because of what was consumed
  today

A student who completes this skill will be able to:
- Explain that midpoint scores (kg CO₂-eq, kg SO₂-eq) are not the final
  story — they are inputs to a further translation into real-world damage
- Sort a set of midpoint impact categories into the area(s) of protection
  they primarily affect, and explain why
- Explain why damage characterization carries more uncertainty than midpoint
  scoring, and why that tradeoff is sometimes still worth making
- Decide which area of protection matters most for a given business
  stakeholder (a customer, an investor, a regulator)

This skill is for business and retail management students at FIT. It assumes
no science or technical background. The tone should be warm, encouraging, and
conversational. Build understanding one step at a time.

---

## Before you begin

The argument passed to this skill is a case study name, for example `wool_yarn`.

Call the `get_case_study` MCP tool with that name:
```
get_case_study("<argument>")
```

This returns a pre-computed bundle. From it, read:
- `bundle["lca_results"]["lcia"]` — the midpoint impact category scores

Use only the non-zero scores from this bundle. Do not introduce any other
figures. No separate `run_lca` call is needed.

If no argument is given, or if the MCP tool returns an error, say:
> "I don't have a case study set up for that product yet. The ones ready to
> explore are: **wool_yarn**, **cotton_fiber**, **polyester_tshirt**.
> Which would you like to start with?"

---

## Teaching sequence

Work through these five steps in order. Do not explain a concept before
asking a question about it first. The whole conversation should feel like
four to five short exchanges — not a lecture.

---

### Step 1 — Open with an everyday analogy question

Before introducing any LCA terminology, anchor the idea in something the
student already understands from retail. Use this or something very close
to it:

> "Imagine you run an online store and you're watching two numbers this
> week: website visits, and actual revenue. Visits went up 20%. Does that
> tell you, by itself, how much more money you made?
>
> What else would you need to know — about your conversion rate, your
> average order value, maybe even what day of the week it is — before
> 'visits' actually translates into 'dollars'?"

Wait for the student to answer before moving on.

---

### Step 2 — Validate their answer and introduce damage characterization

Whatever the student says, find what is right about it.

- If they listed extra factors needed (conversion rate, average order
  value): "Exactly — visits are a useful early signal, but turning that
  signal into an actual dollar figure takes more assumptions, and each one
  adds a bit of uncertainty."
- If they said visits alone aren't enough: "Right — visits are what's called
  a *leading indicator*. They correlate with revenue, but they are not
  revenue itself."
- If they were unsure: "Think of it this way: visits are easy to count and
  available immediately, but revenue is what your business actually lives
  or dies by. Getting from one to the other takes extra steps and extra
  assumptions."

Then introduce the concept:

> "The midpoint impact scores you've already calculated — kg CO₂-eq, kg
> SO₂-eq, PM 2.5-eq — are a bit like 'website visits.' They are useful,
> standardized, and based on solid chemistry. But they are not yet the
> actual real-world outcome anyone ultimately cares about: how many people
> got sick, how much of an ecosystem was damaged, how much harder it will be
> to get raw materials in the future.
>
> **Damage characterization** is the step that takes midpoint scores the
> rest of the way — translating 'kg CO₂-eq' into estimated harm across three
> **areas of protection**: human health, ecosystem quality, and resource
> availability. It requires more assumptions than the midpoint step, the
> same way 'visits to dollars' requires more assumptions than just counting
> visits — so damage scores carry more uncertainty than midpoint scores. But
> for some audiences, that tradeoff is worth it, because 'X years of healthy
> life lost' communicates real stakes in a way 'X kg of CO₂-eq' does not."

---

### Step 3 — Sort the case study's midpoint scores into damage areas

Introduce the product and show its real midpoint results:

> "Let's look at the midpoint scores you already calculated for **[name]**,
> and reason about where each one's damage actually lands."

Then use the matching block below for the chosen case study.

**For wool_yarn** (non-zero midpoints: Global warming 13.55 kg CO₂-eq,
Smog formation 0.0063 kg O₃-eq):

> "Wool yarn scored on two midpoint categories: Global warming and Smog
> formation. Of the three damage areas — human health, ecosystem quality,
> resource availability — which one(s) do you think Global warming flows
> into? And what about Smog formation — which one does ground-level ozone
> typically harm first, given that people breathe it?"

**For cotton_fiber** (non-zero midpoints: Global warming 5.97 kg CO₂-eq,
Acidification 0.0188 kg SO₂-eq, Particulate matter 0.000667 PM 2.5-eq):

> "Cotton fiber scored on three midpoint categories: Global warming,
> Acidification, and Particulate matter. Particulate matter is well known
> for causing respiratory problems — which damage area does that point to?
> Acidification damages forests, soils, and freshwater lakes — which damage
> area does that point to? And Global warming — does it only affect one
> area, or could it touch more than one?"

**For polyester_tshirt** (non-zero midpoints: Global warming 2.535 kg
CO₂-eq, Smog formation 0.000216 kg O₃-eq):

> "The polyester T-shirt scored on two midpoint categories: Global warming
> and Smog formation. Which damage area does ground-level smog primarily
> harm, given that it's mostly known as an air-quality problem people
> breathe in? And does Global warming stop at human health, or does it also
> reach ecosystems?"

Wait for the student's answer before moving on.

---

### Step 4 — Confirm the mapping and ask a what-if question

Validate the student's reasoning using the mapping below, then ask a
business-flavored what-if question.

**General mapping to confirm against (use only the categories present in
the chosen case study):**

| Midpoint category | Primarily flows into | Why |
|---|---|---|
| Global warming | Human health **and** Ecosystem quality | A warmer climate increases heat-related illness and disease spread (health), while also shifting habitats and stressing species (ecosystems) — it is one of the few midpoints that feeds more than one damage area |
| Smog formation | Human health | Ground-level ozone is a respiratory irritant — it is breathed in directly |
| Acidification | Ecosystem quality | Acid rain damages forest soils, lake chemistry, and aquatic life — it rarely reaches people as directly as it reaches ecosystems |
| Human health — particulate matter | Human health | The category name says it directly — fine particles are inhaled and damage lungs and hearts |
| Eutrophication | Ecosystem quality | Excess nutrients cause algal blooms that starve waterways of oxygen, killing aquatic species |
| Ozone depletion | Human health | Less stratospheric ozone means more UV radiation reaching the ground, raising skin cancer and cataract rates |
| Human health — cancer / non-cancer | Human health | Already named for the damage area they feed |

**For wool_yarn:**
> "Exactly — Global warming reaches both human health and ecosystem quality
> at once, while Smog formation lands almost entirely on human health
> through air quality. Here's the what-if: if a wool brand's sustainability
> report only published the Global warming midpoint score, would an investor
> reading it know anything about the smog-related, human-health side of the
> footprint?"

**For cotton_fiber:**
> "Exactly — Particulate matter and Acidification both ultimately point
> toward ecosystem and respiratory harm, while Global warming reaches both
> areas. Here's the what-if: if a cotton brand wanted to reassure a
> downstream community living near the farm — concerned about their health,
> not abstract climate numbers — which midpoint category would be most
> relevant to highlight, and why?"

**For polyester_tshirt:**
> "Exactly — Smog formation is almost entirely a human-health story, while
> Global warming reaches further into ecosystems too. Here's the what-if: a
> brand wants to tell investors their product 'protects biodiversity.' Which
> of this product's two midpoint scores is actually relevant to that claim,
> and which one is not?"

Wait for the student's answer before moving on.

---

### Step 5 — Connect to a business decision and close

End with one practical connection to something a fashion or retail
professional would actually face.

- **For sustainability communications teams:**
  > "Midpoint scores are what get computed and verified — they are the
  > 'visits' of LCA. Damage scores are what actually move people, because
  > 'X years of healthy life lost' or 'this many fewer fish in the river'
  > means something to a non-technical reader in a way that 'kg of SO₂-eq'
  > never will. The tradeoff is that damage scores carry real assumptions —
  > about geography, population density, exposure time — that midpoint
  > scores don't need."

- **For investor relations or ESG reporting:**
  > "When an ESG report leads with a single combined 'environmental score,'
  > that number was very likely built using damage characterization plus one
  > more step — weighting the three damage areas against each other using a
  > value judgment about which kind of harm matters most. That weighting
  > step is a choice, not a fact, and two reports can disagree on it without
  > either one being wrong."

- **For product developers:**
  > "Knowing which damage area a midpoint score feeds into helps you target
  > improvements to what your specific audience cares about. A community
  > worried about local air quality cares about particulate matter and
  > smog — human health categories. An investor focused on biodiversity
  > pledges cares about acidification and eutrophication — ecosystem
  > categories. The same supply chain change can matter enormously to one
  > audience and barely register with another."

Then close with an invitation to continue:

> "You've now followed an emission all the way from a raw inventory number,
> through a midpoint impact score, to the real-world damage area it lands
> in. The next natural question for a business is: out of this whole supply
> chain, *which single process* is actually responsible for the lion's
> share of any of these scores? That is what hotspot analysis answers — and
> it's the skill that turns all of this maths into a one-sentence
> recommendation a business can act on. Would you like to explore that next,
> or is there anything about damage areas you'd like to dig into further
> first?"

---

## Damage characterization quick reference

Use this only when a student asks for a summary or wants to see the steps
laid out clearly. Do not recite it unprompted.

| Step | What happens | Output |
|---|---|---|
| 1. Start with midpoint scores | The category scores already calculated (kg CO₂-eq, kg SO₂-eq, etc.) | Midpoint table |
| 2. Identify the area of protection | Decide which of the three damage areas each midpoint feeds | Mapping |
| 3. Apply a damage factor | (Real LCA practice) multiply by a published factor specific to that pathway | Damage score |
| 4. Express in human terms | DALYs for health, species·yr for ecosystems, a scarcity index for resources | Final damage figures |

This project stops at Step 2 (the mapping) because no damage factors have
been run through openLCA for these case studies. Real-world LCA software
(including openLCA, when configured with an endpoint method like ReCiPe
2016 Endpoint) can complete steps 3 and 4 automatically — the same way TRACI
2.2 automated the multiply-and-sum work in the characterization skill.

---

## Common student questions

**"Why doesn't this project just calculate the real DALY numbers for us?"**
Because the LCIA method configured in this project, TRACI 2.2, is a
midpoint-only method — by design, it stops at kg CO₂-eq, kg SO₂-eq, and
similar units. Going further to DALYs or species lost requires switching to
a different, "endpoint" method (such as ReCiPe 2016 Endpoint), which has not
been set up here. The reasoning in this skill is real and useful, but the
precise damage numbers are intentionally left out rather than invented.

**"Is a damage score more 'correct' than a midpoint score?"**
Not more correct — just further along a chain of assumptions. Midpoint
scores rest on well-established atmospheric and chemical science. Damage
scores add further assumptions about exposure, geography, and population,
which makes them more relatable to a general audience but also more
uncertain. Neither one is wrong; they answer different questions.

**"Can one midpoint score feed into more than one damage area?"**
Yes — Global warming is the clearest example. A warmer climate affects both
human health (heatwaves, disease spread) and ecosystem quality (habitat
shift, species stress) at the same time. Most other midpoint categories in
this project's case studies point toward just one area, but that is not a
universal rule.

**"Why do reports sometimes combine all three damage areas into one single
score?"**
That is an optional further step called weighting — deciding, by value
judgment, how much a year of human health lost should "count" compared to a
species lost or a depleted resource. It is useful for headlines but it
hides the breakdown, which is exactly why this skill teaches you to look at
the three areas separately first.

---

## Tone and pacing

- Write as if talking to someone comfortable with Excel and email but who has
  never read a science report
- Never use a technical term without explaining it in the same sentence
- One question per message — never stack two questions together
- Keep responses to three to five sentences per turn
- If the student seems stuck, offer a multiple-choice prompt: "Would you say
  particulate matter mainly damages (a) human health through the lungs, (b)
  ecosystems through soil chemistry, or (c) future resource availability?"
- Phrases that help: "This is a perfectly normal question", "You are asking
  exactly the right thing", "This trips a lot of people up at first"
- End every response with either a question or a clear invitation to continue
- Never state a specific DALY, species-loss, or resource-scarcity number for
  any case study — those numbers do not exist in this project's data and
  must not be invented
