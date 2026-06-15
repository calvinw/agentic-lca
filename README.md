# Agentic LCA — Life Cycle Assessment with openLCA

This project lets you calculate the **environmental footprint** of products using a tool called openLCA, all from inside a GitHub Codespace. It is designed for business and retail management students with no coding experience.

---

## What is a Life Cycle Assessment?

A Life Cycle Assessment (LCA) measures the environmental impact of a product across its entire life — from the raw materials used to make it, through manufacturing, all the way to disposal. The most common thing we measure is **CO₂ emissions** (the greenhouse gas that contributes to climate change), but an LCA can also track water use, land use, resource extraction, and other impacts.

For example: a cotton shirt doesn't just emit CO₂ when you buy it. It starts with a cotton farm that uses fertilizers and machinery. The cotton is spun into yarn in a mill using electricity. The yarn is woven into fabric in another facility. Then it's cut and sewn into a shirt in a factory. Every step uses energy, extracts resources from nature, and releases pollution. An LCA adds all of that up.

---

## Educational Features

This project includes a set of **teaching skills** — guided, conversational lessons that walk you through the key ideas in Life Cycle Assessment using real case studies. You do not need any maths or science background. Each lesson works like a one-on-one tutorial: the AI asks you questions, you respond in plain English, and the concept builds up naturally through the conversation.

The three case studies available for all lessons are:

1. **`cotton_fiber`** — 1 kg of cotton fiber, from fertilizer production to harvested cotton

   ![cotton fiber supply chain — structure](skills_references/cotton_fiber/product_graph_structure.svg)

2. **`polyester_tshirt`** — 1 polyester T-shirt, from oil well to finished garment

   ![polyester T-shirt supply chain — structure](skills_references/polyester_tshirt/product_graph_structure.svg)

3. **`wool_yarn`** — 1 kg of wool yarn, from sheep farm to finished yarn

   ![wool yarn supply chain — structure](skills_references/wool_yarn/product_graph_structure.svg)

---

### `/what-is-lca` — What is a Life Cycle Assessment?

**What you will learn:** What LCA is, why it matters for people working in fashion or retail, and how a study is structured — without any maths or science background required.

**How to start:**

```
/what-is-lca
```

No case study argument needed — this is the very first skill, designed to be used before anything else. It opens with a question about something familiar from retail life (like why a cotton T-shirt might have a larger footprint than you'd expect) and builds from your answer. By the end you will be able to explain to a colleague why LCA is relevant to sourcing, product design, and sustainability claims.

**How long:** About 10 minutes of conversation.

---

### `/system-boundary` — What is inside and outside the study?

**What you will learn:** Every LCA study has a boundary — a fence that decides what gets counted and what gets ignored. This lesson teaches you how to read that fence, why it matters, and why two studies of the same product can give completely different numbers if their boundaries are drawn differently.

**How to start** — pick one of the three case studies:

```
/system-boundary cotton_fiber
/system-boundary polyester_tshirt
/system-boundary wool_yarn
```

The lesson opens with a simple everyday analogy (a restaurant receipt that only covers certain costs) and then applies the same idea to a real supply chain diagram. By the end you will understand why knowing what a study *left out* is just as important as knowing what it included.

**How long:** About 10 minutes of conversation.

---

### `/life-cycle-stages` — Where does the study start and stop?

**What you will learn:** The four named boundary types used across the fashion and retail industry — cradle to gate, cradle to grave, cradle to cradle, and gate to grave — what each one includes and when companies use it.

**How to start** — pick one of the three case studies:

```
/life-cycle-stages cotton_fiber
/life-cycle-stages polyester_tshirt
/life-cycle-stages wool_yarn
```

The lesson shows how the same product can have four different carbon footprint numbers depending on where the boundary is drawn, and teaches you to spot when two studies are using different scopes and therefore cannot be fairly compared.

**How long:** About 10–15 minutes of conversation.

---

### `/goal-and-scope` — What are we studying and why?

**What you will learn:** The two foundational decisions every LCA study must make before any numbers are calculated — the goal (why you are doing it and who it is for) and the scope (what is included and excluded). These decisions shape every result that follows.

**How to start** — pick one of the three case studies:

```
/goal-and-scope cotton_fiber
/goal-and-scope polyester_tshirt
/goal-and-scope wool_yarn
```

The lesson opens by asking what question a retailer might want an LCA to answer, then walks you through how that question becomes a formal study design. By the end you will understand what "cradle to gate" and "cradle to grave" mean, why two LCA studies of the same product can reach different conclusions, and what to look for when a supplier hands you a sustainability report.

**How long:** About 10–15 minutes of conversation.

---

### `/functional-unit` — What exactly are we measuring?

**What you will learn:** What a functional unit is, why the choice of unit matters, and how picking the wrong unit can make a misleading sustainability comparison.

**How to start** — pick one of the three case studies:

```
/functional-unit cotton_fiber
/functional-unit polyester_tshirt
/functional-unit wool_yarn
```

The lesson opens with a question from everyday retail life — something like "if a brand wanted to put a carbon footprint label on their yarn, what would you measure it per?" — and builds from your answer. By the end you will understand why "per kilogram" and "per garment" can tell completely different stories, and what to look for when a supplier hands you a sustainability claim.

**How long:** About 10–15 minutes of conversation.

---

### `/supply-chain` — How to read a supply chain diagram

**What you will learn:** What a supply chain map is, how to read the boxes and arrows, what "upstream" and "downstream" mean, and why the boundary of a study matters.

**How to start** — pick one of the three case studies:

```
/supply-chain cotton_fiber
/supply-chain polyester_tshirt
/supply-chain wool_yarn
```

The lesson opens by asking you to think about the product's journey before showing you anything. It then walks you through the supply chain diagram step by step — each box (a production process), each arrow (a material flowing between steps), and the boundary around the whole system. It closes by connecting what you have seen to a real sourcing or sustainability decision.

**How long:** About 10–15 minutes of conversation.

---

### `/technosphere-and-ecosphere` — What counts as environmental harm?

**What you will learn:** The difference between the human-made world (the technosphere — factories, farms, mills, trucks) and the natural world (the ecosphere — air, water, soil, ecosystems). Environmental harm only happens when something *crosses the boundary* between the two — and understanding that crossing is what separates a real impact from a transaction inside the supply chain.

**How to start** — pick one of the three case studies:

```
/technosphere-and-ecosphere cotton_fiber
/technosphere-and-ecosphere polyester_tshirt
/technosphere-and-ecosphere wool_yarn
```

The lesson opens with a town-wall analogy, then walks through a real supply chain and asks you to sort each flow into "stays inside the wall" or "crosses into nature". By the end you will know why CO₂ to air counts as an impact while raw wool moving from a farm to a mill does not.

**How long:** About 10–15 minutes of conversation.

---

### `/scaling-vector` — How much does each step need to run?

**What you will learn:** The scaling vector — the set of numbers that answers the question "to produce exactly one unit of the finished product, how many times does each step in the supply chain have to run?"

**How to start** — pick one of the three case studies:

```
/scaling-vector cotton_fiber
/scaling-vector polyester_tshirt
/scaling-vector wool_yarn
```

The lesson uses a cooking analogy to introduce the idea — if a bread recipe makes one loaf and you need three, you run it three times. It then walks you through the supply chain one step at a time, asking you to do each division yourself before confirming the answer. By the end you will understand why the cotton farm might only need to run 0.2 times to produce 1 kg of cotton fiber, and what that means for where the emissions actually come from.

**How long:** About 15–20 minutes of conversation.

---

## Advanced Features

### What this project currently calculates

When you run an analysis with `/run-lca`, the tool works through these steps and saves the results to `lca_results.md`:

| Step | What happens |
|---|---|
| 1 | **Goal and scope** — sets the functional unit and the reference flow |
| 2 | **Technology matrix (A)** — the grid of what each process produces and consumes |
| 3 | **Scaling vector (s)** — solves how many times each process must run to deliver one functional unit |
| 4 | **Intervention matrix (B)** — the grid of what each process emits or extracts per run |
| 5 | **LCI results** — total inventory (B × s): all emissions and extractions for the whole supply chain |
| 6 | **Contribution analysis** — breaks down which process is responsible for how much of each emission |
| 7 | **LCIA results** — converts inventory flows into impact category scores using **TRACI 2.2** |

The inventory tracks two types of flow crossing the boundary between the supply chain and the natural world:

- **Emissions** — substances released *to* nature (CO₂ to air, wastewater to rivers, etc.)
- **Extractions** — substances drawn *from* nature (crude oil, water, land, minerals, etc.)

The **Life Cycle Impact Assessment (LCIA)** step converts those raw inventory numbers into scored impact categories. This project uses **TRACI 2.2** (Tool for the Reduction and Assessment of Chemicals and other environmental Impacts), the US EPA's standard impact method. It covers eight categories:

| Impact category | What it measures | Unit |
|---|---|---|
| Global warming | Greenhouse gases contributing to climate change | kg CO₂ equivalent |
| Acidification | Acid rain and ecosystem acidification | kg SO₂ equivalent |
| Smog formation | Ground-level ozone (smog) | kg O₃ equivalent |
| Human health — particulate matter | Fine particle pollution affecting lungs | kg PM 2.5 equivalent |
| Eutrophication (freshwater) | Excess nutrients causing algal blooms | kg N equivalent |
| Human health — cancer | Toxic substances linked to cancer | CTUh |
| Human health — non-cancer | Other toxic health impacts | CTUh |
| Ozone depletion | Damage to the stratospheric ozone layer | kg CFC-11 equivalent |

TRACI 2.2 uses the **Federal Elementary Flow List (FEDEFL)** — the US EPA's standard naming system for substances like "Carbon dioxide" and "Methane". Recipe cards must use these exact FEDEFL names so the tool can match each emission to its correct impact factors.

---

### How this project works

Each product you study gets its own folder inside `lca_analysis/`. Every folder contains:

| File | What it is |
|---|---|
| `recipe_card.md` | The **recipe card** — you describe the product and its supply chain here |
| `lca_results.md` | The **report** — automatically generated after the analysis runs |
| `product_graph_scaled.svg` | The **scaled diagram** — supply chain map with amounts and scaling factors |
| `product_graph_structure.svg` | The **structure diagram** — supply chain map with flow names only |

Current analyses:
```
lca_analysis/
├── coffee/                    — carbon footprint of one cup of coffee
├── cotton_shirt/              — carbon footprint of one cotton shirt (cradle to gate)
├── paper_cup/                 — carbon footprint of one paper cup
├── apple/                     — carbon footprint of one apple (farm to retail)
├── electricity/               — emissions from producing 200 kWh of electricity
├── hand_dryer/                — hand dryer vs paper towels energy comparison
├── hoodie/                    — carbon footprint of one cotton hoodie
├── light_bulb/                — LED vs incandescent bulb over lifetime
├── nordic_cotton_reuse/       — Nordic textile reuse scenario
├── nordic_textile_waste/      — Nordic textile waste scenario
├── plastic_broom/             — carbon footprint of one plastic broom
├── polystyrene/               — carbon footprint of 1 kg polystyrene packing
├── popcorn/                   — popcorn vs polystyrene packing (per kg)
└── levis/                     — Levi's 501 jeans: baseline + six what-if scenarios
    ├── levi_jeans/            — baseline (standard manufacturing)
    ├── levi_jeans_bestcase/   — all best-case assumptions combined
    ├── levi_jeans_longlife/   — worn for 10 years instead of 3
    ├── levi_jeans_organic/    — organic cotton substituted
    ├── levi_jeans_renewable/  — renewable energy at all factories
    ├── levi_jeans_wash1x/     — washed once a week
    ├── levi_jeans_wash2x/     — washed twice a week
    ├── levi_jeans_wash5x/     — washed five times a week
    └── levi_jeans_wash10x/    — washed ten times a week
```

You interact with this project by describing a product in a `recipe_card.md` file and then asking the AI assistant to run the analysis for you. The AI handles everything else.

---

### The recipe card format

The `recipe_card.md` file is where you describe the product you want to study. Think of it like filling out a form — each section asks for a specific piece of information about the supply chain. You do not need to understand the technical format; the AI assistant will help you fill it in. But it helps to know what each section represents.

#### `name` and `goal`
A short title for the analysis and one sentence explaining what you are trying to find out.

> *Example: "Calculate the CO₂ emitted to produce one cotton shirt, from farm to finished garment."*

#### `functional_unit`
The precise thing you are measuring. LCA always measures per *one unit* of something — one shirt, one cup, one kilometre driven. Being specific matters: comparing a paper cup to a ceramic mug is only fair if you account for the fact that the mug gets used hundreds of times.

> *Example: one cotton shirt*

#### `units`
Every unit of measurement used anywhere in the recipe card — kilograms, kilowatt-hours, litres, and so on. Think of this as the glossary of measurements for your analysis.

#### `products`
The intermediate goods that flow between steps in the supply chain — things that are made by one process and consumed by another. For a shirt, this would include raw cotton, yarn, fabric, and electricity. These stay *inside* the system boundary.

#### `elementary_flows`
The flows that cross the boundary between the supply chain and the natural world — both substances released *to* nature (emissions such as CO₂ to air) and substances extracted *from* nature (resources such as water or crude oil).

#### `processes`
Each step in the supply chain. For every process you describe:
- What it **produces** (its output — the thing it "sells" to the next step)
- What it **consumes** from other processes (its technosphere inputs)
- What it **emits** to nature (biosphere outputs)
- What it **extracts** from nature (biosphere inputs)

#### `reference_process`
The final step that delivers the finished product — the one that connects to the functional unit. This is the starting point for all the calculations.

#### Complete example — Cotton Shirt

Here is the full recipe card for the cotton shirt analysis. Read through it top to bottom and you will see how each section connects to the supply chain description above it.

```yaml
name: Cotton Shirt LCA — cradle to gate
goal: >
  Calculate the total CO₂ emitted to produce one cotton shirt,
  tracing the full supply chain from cotton farming through
  yarn spinning, fabric weaving, and garment assembly.

functional_unit:
  description: One cotton shirt (cradle to gate)
  amount: 1.0
  unit: shirt

units:
  shirt: Shirt count
  kg:   Mass
  kWh:  Energy

products:
  - { name: Raw cotton,   unit: kg    }
  - { name: Yarn,         unit: kg    }
  - { name: Fabric,       unit: kg    }
  - { name: Cotton shirt, unit: shirt }
  - { name: Electricity,  unit: kWh   }

elementary_flows:
  emissions:
    - { name: Carbon dioxide, compartment: air, unit: kg }
  resources:
    # (none in this example — emissions only)

processes:
  - name: P1 — Grow cotton
    reference_output: { flow: Raw cotton, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 3.0 }

  - name: P2 — Spin yarn
    reference_output: { flow: Yarn, amount: 1.0 }
    inputs:
      - { flow: Raw cotton,  amount: 1.1 }
      - { flow: Electricity, amount: 3.0 }

  - name: P3 — Weave fabric
    reference_output: { flow: Fabric, amount: 1.0 }
    inputs:
      - { flow: Yarn,        amount: 1.1 }
      - { flow: Electricity, amount: 4.0 }

  - name: P4 — Cut and sew shirt
    reference_output: { flow: Cotton shirt, amount: 1.0 }
    inputs:
      - { flow: Fabric,      amount: 0.25 }
      - { flow: Electricity, amount: 1.0  }

  - name: P5 — Generate electricity
    reference_output: { flow: Electricity, amount: 1.0 }
    emissions:
      - { flow: Carbon dioxide, amount: 0.5 }

reference_process: P4 — Cut and sew shirt

lcia:
  method_name: "TRACI 2.2"
```

A few things to notice:
- **P1 (Grow cotton)** has no inputs from other processes — it takes from nature directly (CO₂ from machinery and fertilisers). It also doesn't use electricity.
- **P2, P3, P4** each consume intermediate products from earlier steps *and* draw electricity from the grid.
- **P5 (Generate electricity)** is where the biosphere boundary appears: CO₂ is emitted *to* nature (0.5 kg per kWh) as a result of burning coal.
- The `reference_process` is P4 — the final step that produces the finished shirt.
- The `lcia:` section at the bottom tells the tool which impact method to use. Always set this to `"TRACI 2.2"`.

#### FEDEFL flow names

Flow names in the `elementary_flows` and `emissions` sections must use the exact names from the **Federal Elementary Flow List (FEDEFL)** — the US EPA's standard. The most common ones are:

| What you are describing | FEDEFL name to use |
|---|---|
| Carbon dioxide (CO₂) | `Carbon dioxide` |
| Methane (CH₄) | `Methane` |
| Nitrous oxide (N₂O) | `Nitrous oxide` |
| Ammonia (NH₃) | `Ammonia` |
| Nitrogen oxides (NOx) | `Nitrogen oxides` |
| Sulfur dioxide (SO₂) | `Sulfur dioxide` |
| Water | `Water` |

Do not use abbreviations like `CO2`, `CH4`, or `CO2 to air` — these will not match the TRACI 2.2 characterisation factors and the LCIA step will return zero for that flow.

---

### Starting the openLCA server

The openLCA server does **not** start automatically — you need to start it yourself before running any analysis. There are three scripts at the top level of the project for managing it:

#### `setup_olca.sh` — First-time setup (use this the very first time)

```bash
bash setup_olca.sh
```

This does everything needed to get the system ready from scratch — in order:

1. Installs the required Python tools
2. Downloads the FEDEFL elementary flow list (214 MB) and TRACI 2.2 impact method (126 MB) from the project's GitHub release — only if they are not already present
3. Builds the openLCA calculation engine (only happens once per Codespace)
4. Starts the server
5. Imports all the flow and impact data into the database — only if the database is empty

The whole process takes a few minutes the first time, but each step is skipped on subsequent runs if it has already been done.

#### `start_olca.sh` — Start the server (use this every time after that)

```bash
bash start_olca.sh
```

This starts the server using the software that was already built by `setup_olca.sh`. It's much faster because it skips the build step. If the server is already running, it will simply say so and do nothing. Use this at the beginning of every working session.

#### `stop_olca.sh` — Stop the server (use this when you are done)

```bash
bash stop_olca.sh
```

This shuts the server down cleanly. You do not have to run this — closing your Codespace will stop it too — but it is good practice if you want to free up resources while you are still in your session.

#### Checking whether the server is running

To confirm the server is up and ready:

```bash
curl -s http://localhost:8080/api/version
```

If it replies with a version number, the server is running. If it gives an error or no response, run `bash start_olca.sh` to start it.

---

## Source

Built on top of the [calvinw/ai-agentic-tools](https://github.com/calvinw/ai-agentic-tools) dev container, which provides the AI coding assistants and MCP server infrastructure.
