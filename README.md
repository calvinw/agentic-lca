# Agentic LCA — Life Cycle Assessment with openLCA

This project lets you calculate the **environmental footprint** of products using a tool called openLCA, all from inside a GitHub Codespace. It is designed for business and retail management students with no coding experience.

---

## What is a Life Cycle Assessment?

A Life Cycle Assessment (LCA) measures the environmental impact of a product across its entire life — from the raw materials used to make it, through manufacturing, all the way to disposal. The most common thing we measure is **CO₂ emissions** (the greenhouse gas that contributes to climate change), but an LCA can also track water use, land use, resource extraction, and other impacts.

For example: a cotton shirt doesn't just emit CO₂ when you buy it. It starts with a cotton farm that uses fertilizers and machinery. The cotton is spun into yarn in a mill using electricity. The yarn is woven into fabric in another facility. Then it's cut and sewn into a shirt in a factory. Every step uses energy, extracts resources from nature, and releases pollution. An LCA adds all of that up.

---

## What this project currently calculates

The analyses in this project complete the **Life Cycle Inventory (LCI)** step of an LCA. Think of inventory as the data-collection phase — it tracks every flow crossing the boundary between the supply chain and the natural world:

- **Emissions** — substances released *to* nature (CO₂ to air, wastewater to rivers, etc.)

The next step — **Life Cycle Impact Assessment (LCIA)** — would convert those raw inventory numbers into scored impact categories like Global Warming Potential or Water Depletion. That step is not yet included in this project.

---

## How this project works

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
├── coffee/          — carbon footprint of one cup of coffee
├── cotton_shirt/    — carbon footprint of one cotton shirt (cradle to gate)
└── paper_cup/       — carbon footprint of one paper cup
```

You interact with this project by describing a product in a `recipe_card.md` file and then asking the AI assistant to run the analysis for you. The AI handles everything else.

---

## The recipe card format

The `recipe_card.md` file is where you describe the product you want to study. Think of it like filling out a form — each section asks for a specific piece of information about the supply chain. You do not need to understand the technical format; the AI assistant will help you fill it in. But it helps to know what each section represents.

### `name` and `goal`
A short title for the analysis and one sentence explaining what you are trying to find out.

> *Example: "Calculate the CO₂ emitted to produce one cotton shirt, from farm to finished garment."*

### `functional_unit`
The precise thing you are measuring. LCA always measures per *one unit* of something — one shirt, one cup, one kilometre driven. Being specific matters: comparing a paper cup to a ceramic mug is only fair if you account for the fact that the mug gets used hundreds of times.

> *Example: one cotton shirt*

### `units`
Every unit of measurement used anywhere in the recipe card — kilograms, kilowatt-hours, litres, and so on. Think of this as the glossary of measurements for your analysis.

### `products`
The intermediate goods that flow between steps in the supply chain — things that are made by one process and consumed by another. For a shirt, this would include raw cotton, yarn, fabric, and electricity. These stay *inside* the system boundary.

### `elementary_flows`
The flows that cross the boundary between the supply chain and the natural world — both substances released *to* nature (emissions such as CO₂ to air) and substances extracted *from* nature (resources such as water or crude oil).

### `processes`
Each step in the supply chain. For every process you describe:
- What it **produces** (its output — the thing it "sells" to the next step)
- What it **consumes** from other processes (its technosphere inputs)
- What it **emits** to nature (biosphere outputs)
- What it **extracts** from nature (biosphere inputs)

### `reference_process`
The final step that delivers the finished product — the one that connects to the functional unit. This is the starting point for all the calculations.

### Complete example — Cotton Shirt

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
    - { name: CO2 to air, unit: kg }
  resources:
    # (none in this example — emissions only)

processes:
  - name: P1 — Grow cotton
    reference_output: { flow: Raw cotton, amount: 1.0 }
    emissions:
      - { flow: CO2 to air, amount: 3.0 }

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
      - { flow: CO2 to air, amount: 0.5 }

reference_process: P4 — Cut and sew shirt
```

A few things to notice:
- **P1 (Grow cotton)** has no inputs from other processes — it takes from nature directly (CO₂ from machinery and fertilisers). It also doesn't use electricity.
- **P2, P3, P4** each consume intermediate products from earlier steps *and* draw electricity from the grid.
- **P5 (Generate electricity)** is where the biosphere boundary appears: CO₂ is emitted *to* nature (0.5 kg per kWh) as a result of burning coal.
- The `reference_process` is P4 — the final step that produces the finished shirt.

---

## Educational skills — learning LCA step by step

This project includes a set of **teaching skills** — guided, conversational lessons that walk you through the key ideas in Life Cycle Assessment using real case studies. You do not need any maths or science background. Each lesson works like a one-on-one tutorial: the AI asks you questions, you respond in plain English, and the concept builds up naturally through the conversation.

The three case studies used across all lessons are:

| Case study | What it covers |
|---|---|
| `wool_yarn` | 1 kg of wool yarn — from sheep farm to finished yarn |
| `polyester_tshirt` | 1 polyester T-shirt — from oil well to finished garment |
| `cotton_fiber` | 1 kg of cotton fiber — from fertilizer production to harvested cotton |

---

### `/supply-chain` — How to read a supply chain diagram

**What you will learn:** What a supply chain map is, how to read the boxes and arrows, what "upstream" and "downstream" mean, and why the boundary of a study matters.

**How to start:**
```
/supply-chain wool_yarn
```
or
```
/supply-chain polyester_tshirt
```
or
```
/supply-chain cotton_fiber
```

The lesson opens by asking you to think about the product's journey before showing you anything. It then walks you through the supply chain diagram step by step — each box (a production process), each arrow (a material flowing between steps), and the boundary around the whole system. It closes by connecting what you have seen to a real sourcing or sustainability decision.

**How long:** About 10–15 minutes of conversation.

---

### `/functional-unit` — What exactly are we measuring?

**What you will learn:** What a functional unit is, why the choice of unit matters, and how picking the wrong unit can make a misleading sustainability comparison.

**How to start:**
```
/functional-unit wool_yarn
```
or
```
/functional-unit polyester_tshirt
```
or
```
/functional-unit cotton_fiber
```

The lesson opens with a question from everyday retail life — something like "if a brand wanted to put a carbon footprint label on their yarn, what would you measure it per?" — and builds from your answer. By the end you will understand why "per kilogram" and "per garment" can tell completely different stories, and what to look for when a supplier hands you a sustainability claim.

**How long:** About 10–15 minutes of conversation.

---

### `/scaling-vector` — How much does each step need to run?

**What you will learn:** The scaling vector — the set of numbers that answers the question "to produce exactly one unit of the finished product, how many times does each step in the supply chain have to run?"

**How to start:**
```
/scaling-vector wool_yarn
```
or
```
/scaling-vector polyester_tshirt
```
or
```
/scaling-vector cotton_fiber
```

The lesson uses a cooking analogy to introduce the idea — if a bread recipe makes one loaf and you need three, you run it three times. It then walks you through the supply chain one step at a time, asking you to do each division yourself before confirming the answer. By the end you will understand why the cotton farm might only need to run 0.2 times to produce 1 kg of cotton fiber, and what that means for where the emissions actually come from.

**How long:** About 15–20 minutes of conversation.

---

### `/product-graph-svg` — Draw a supply chain diagram from a recipe card

**What you will learn / do:** Generate your own supply chain diagrams as SVG image files — no openLCA server needed. This skill is more hands-on than a lesson: you describe a supply chain in a recipe card and the tool draws it.

**How to start:** Just ask the AI to generate a diagram, for example:
```
generate a supply chain diagram for the coffee recipe card
```
or
```
draw the supply chain for cotton_shirt
```

There are nine ready-made recipe cards to experiment with — including coffee, cotton shirt, paper cup, light bulb, and a fictional teaching example called "Blorp". You can also edit any recipe card to change amounts, add processes, or add emissions and regenerate the diagram to see how it changes. No calculation server is needed for this — it works entirely from the recipe card file.

---

## Starting the openLCA server

The openLCA server does **not** start automatically — you need to start it yourself before running any analysis. There are three scripts at the top level of the project for managing it:

### `setup_olca.sh` — First-time setup (use this the very first time)

```bash
bash setup_olca.sh
```

This builds the openLCA software (like downloading and installing an app — this can take a minute or two and only happens once), installs the required tools, and starts the server. Use this the very first time you use a new Codespace, or if you have deleted and rebuilt everything from scratch.

### `start_olca.sh` — Start the server (use this every time after that)

```bash
bash start_olca.sh
```

This starts the server using the software that was already built by `setup_olca.sh`. It's much faster because it skips the build step. If the server is already running, it will simply say so and do nothing. Use this at the beginning of every working session.

### `stop_olca.sh` — Stop the server (use this when you are done)

```bash
bash stop_olca.sh
```

This shuts the server down cleanly. You do not have to run this — closing your Codespace will stop it too — but it is good practice if you want to free up resources while you are still in your session.

### Checking whether the server is running

To confirm the server is up and ready:

```bash
curl -s http://localhost:8080/api/version
```

If it replies with a version number, the server is running. If it gives an error or no response, run `bash start_olca.sh` to start it.

---

## Example result — Cotton Shirt

Running the cotton shirt analysis produces a report showing:

```
CO₂ emitted: 2.32 kg per shirt

Breakdown:
  Electricity generation (mills + factory)   1.41 kg   61%
  Cotton farming                             0.91 kg   39%
```

The biggest finding: almost two-thirds of the shirt's carbon footprint comes from the electricity used in the mills and the factory — not the farm. Switching to renewable energy could cut the footprint nearly in half.

---

## Source

Built on top of the [calvinw/ai-agentic-tools](https://github.com/calvinw/ai-agentic-tools) dev container, which provides the AI coding assistants and MCP server infrastructure.
