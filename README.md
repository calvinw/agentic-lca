# Agentic LCA — Life Cycle Assessment with openLCA

This project lets you calculate the **environmental footprint** of products using a tool called openLCA, all from inside a GitHub Codespace. It is designed for business and retail management students with no coding experience.

---

## What is a Life Cycle Assessment?

A Life Cycle Assessment (LCA) measures the environmental impact of a product across its entire life — from the raw materials used to make it, through manufacturing, all the way to disposal. The most common thing we measure is **CO₂ emissions** (the greenhouse gas that contributes to climate change), but an LCA can also track water use, land use, and other impacts.

For example: a cotton shirt doesn't just emit CO₂ when you buy it. It starts with a cotton farm that uses fertilizers and machinery. The cotton is spun into yarn in a mill using electricity. The yarn is woven into fabric in another facility. Then it's cut and sewn into a shirt in a factory. Every step uses energy and releases pollution. An LCA adds all of that up.

---

## How this project works

There are three main pieces:

### 1. The openLCA server
A professional life cycle assessment software called **openLCA** runs quietly in the background when your Codespace starts. You never see it directly — it just handles the maths when you run an analysis. Think of it like a calculator engine running behind the scenes.

### 2. The analysis files (`lca_analysis/`)
Each analysis lives in its own folder inside `lca_analysis/`. Every folder contains two files:

| File | What it is |
|---|---|
| `analysis.md` | The **recipe card** — you describe the product and its supply chain here |
| `lca_results.md` | The **report** — automatically generated after the analysis runs |

Current analyses:
```
lca_analysis/
├── coffee/          — carbon footprint of one cup of coffee
└── cotton_shirt/    — carbon footprint of one cotton shirt (cradle to gate)
```

### 3. The runner script (`lca_analysis.py`)
This is the engine that reads your recipe card and produces the report. You run it by pointing it at a specific analysis folder:

```bash
python3 lca_analysis.py lca_analysis/cotton_shirt/analysis.md
python3 lca_analysis.py lca_analysis/coffee/analysis.md
```

---

## Running an existing analysis

1. Open a terminal in your Codespace
2. Run the command for the analysis you want, for example:
   ```bash
   python3 lca_analysis.py lca_analysis/cotton_shirt/analysis.md
   ```
3. The results are saved to `lca_analysis/cotton_shirt/lca_results.md`
4. Open that file to read the full report

---

## Creating a new analysis

To study a new product, create a new folder under `lca_analysis/` and add an `analysis.md` file describing the supply chain. Use the coffee or cotton shirt examples as a starting point — the format is the same for any product.

The `analysis.md` file needs these sections:

| Section | What to fill in |
|---|---|
| `name` / `goal` | A title and one-sentence purpose |
| `functional_unit` | What "one unit" means (e.g. one shirt, one bottle) |
| `units` | Every unit of measurement used (kg, kWh, L, etc.) |
| `products` | The intermediate goods flowing between steps (yarn, fabric, electricity) |
| `elementary_flows` | Emissions to nature (CO₂, methane, etc.) |
| `processes` | Each step in the supply chain — what it produces, consumes, and emits |
| `reference_process` | The final step that delivers the finished product |

---

## Key files

| File | Purpose |
|---|---|
| `lca_analysis.py` | Runs an LCA from an `analysis.md` file |
| `lca_analysis/coffee/` | Coffee example — teaches the basic matrix maths |
| `lca_analysis/cotton_shirt/` | Cotton shirt — a realistic cradle-to-gate study |
| `LCACoffeeExlainer.md` | Written guide explaining the maths behind LCA step by step |
| `LCA_Paper_vs_Plastic_Cup_v2.xlsx` | Spreadsheet comparing paper vs. polystyrene cups |
| `.devcontainer/start_olca.sh` | Starts the openLCA server (runs automatically on Codespace start) |

---

## Prerequisites

The openLCA server starts automatically when your Codespace launches. To verify it is running:

```bash
curl -s http://localhost:8080/api/version
```

If it is not running:
```bash
bash .devcontainer/start_olca.sh
```

Python packages required (installed automatically on Codespace creation):
```bash
pip install olca-ipc olca-schema pyyaml numpy --break-system-packages
```

---

## Example result — Cotton Shirt

Running the cotton shirt analysis produces:

```
Total CO₂: 2.32 kg per shirt

Breakdown:
  Electricity generation   1.41 kg   61%
  Cotton farming           0.91 kg   39%
```

The biggest finding: almost two-thirds of the shirt's carbon footprint comes from the electricity used in the mills and factory — not the farm. Switching to renewable energy could cut the footprint nearly in half.

---

## Source

Built on top of the [calvinw/ai-agentic-tools](https://github.com/calvinw/ai-agentic-tools) dev container, which provides the AI coding assistants and MCP server infrastructure.
