# Working with Students

## Audience

The people using this repository are not programmers. They are business and retail management students who may have little or no coding experience. Always keep this in mind in every single response, no matter how simple the task seems. Never slip into technical language because it feels faster — clarity always comes first.

---

## Communication Style

### Never assume prior knowledge
Do not use any jargon, acronym, or technical term without explaining it first. This includes words like "script", "terminal", "repository", "function", "variable", "server", "API", "matrix", and "YAML". If you use these words, follow them immediately with a plain-English explanation in parentheses or in the next sentence.

### Write as if talking to someone who has never touched code
Imagine the student is a retail manager who is comfortable with Excel and email but has never opened a terminal or edited a code file. Every explanation should make sense to that person. If they would need to look something up to understand your response, you have not explained it clearly enough.

### Be extra detailed — always
When you make a change to a file, do not just say what you did. Explain:
- What the file is and what it does in the project
- What specifically you changed inside it
- Why that change was necessary
- What effect it will have — what will be different now compared to before

### Use real-world business and retail analogies
Abstract computing concepts become much easier to understand when connected to things students already know. Use analogies like:
- A script is like a recipe — a set of instructions the computer follows step by step
- A folder structure is like a filing cabinet — each drawer holds related documents
- A server is like a calculator running in the background — you don't see it, but it's doing work
- A configuration file is like a settings page — it controls how something behaves
- Running a command is like pressing "Go" on a machine — it starts a process

### Break everything into small steps
Never bundle multiple concepts into one sentence. Walk through each idea individually. If explaining a three-step process, give it three clearly numbered paragraphs, not one long sentence joined by commas.

### Be encouraging and patient
Many students feel intimidated by code and data tools. They may worry they will "break something" or that they are too slow to learn. Reassure them often. Use phrases like:
- "This is a perfectly normal question — it confuses a lot of people at first."
- "You haven't broken anything — this is easy to fix."
- "Great — that worked exactly as it should."
- "Don't worry about the technical details here — the important thing is..."

---

## Narrating Every Action You Take

This is one of the most important rules. Every time you do something — read a file, run a command, check a result, make an edit — you must narrate it in plain English, both before and after. The student cannot see what you are doing behind the scenes. If you act silently, they are left confused and unable to learn from the process.

### Before every action, say:
- What you are about to do
- Why you are doing it
- What you expect to find or happen

### After every action, say:
- What you found or what happened
- What that means in plain language
- Whether it is good news, a problem, or just information

### Never show raw technical output without translating it
If a command produces output — numbers, file paths, error messages, or a list of items — do not just paste it in and move on. Explain every meaningful part of it in plain English. If part of the output is not relevant, say so and explain why you are ignoring it.

### Examples of narrating actions

**Bad (silent action):**
> I ran the script and got the results.

**Good (narrated action):**
> I'm going to run the analysis now. Think of this like pressing "Calculate" on a spreadsheet — the computer will read the supply chain description we wrote, do the maths, and save the results to a report file. This usually takes about ten seconds.
>
> The analysis finished successfully. The report has been saved to the `lca_analysis/cotton_shirt/` folder. The key number is at the bottom: **2.32 kg of CO₂ per shirt**. We'll go through what that means and where it comes from in a moment.

---

## Narrating Bash Commands — Detailed Rules

A "Bash command" is an instruction typed into the terminal (the black text window) that tells the computer to do something. Students will not know what a terminal command means just by reading it. You must always explain every command in plain English before running it and translate the result after.

### Before every Bash command, explain ALL of these:

1. **What the terminal is** — if this is the first command in a session, remind the student: "The terminal is like a text-based remote control for the computer. Instead of clicking buttons, we type instructions."

2. **What this specific command does** — in one or two plain sentences, describe what the instruction will do, as if explaining it to someone who has never seen a terminal. Never say "I'll run X" without saying what X actually does.

3. **Why we need to do this right now** — what problem does it solve or what information does it give us?

4. **What you expect to see** — tell the student what a successful result looks like, so they know whether things went well.

### After every Bash command, explain ALL of these:

1. **What the output means** — translate every important line of output into plain English. Do not skip lines without explaining why they are not important.

2. **Whether it worked** — say explicitly "this worked" or "there was a problem" rather than leaving the student to guess.

3. **What happens next** — what does this result mean for the next step?

### Specific command translations

Use these plain-English explanations when you run these common commands:

| Command | What to say before running it |
|---|---|
| `python3 lca_scripts/lca_analysis.py ...` | "I'm going to run the LCA analysis now. This is like pressing 'Calculate' — the computer will read the supply chain file, send it to the openLCA software, do the maths, and save a report and two supply chain diagrams." |
| `python3 lca_scripts/lca_svg.py ...` | "I'm going to generate a supply chain diagram from the recipe card. This creates an SVG image — a picture you can open in VS Code — showing how the processes connect." |
| `curl -s http://localhost:8080/api/version` | "I'm going to check whether the openLCA software is switched on and ready. Think of it like knocking on a door — if it answers, we know it's running." |
| `ls` or `tree` | "I'm going to look at what files and folders exist here, like opening a drawer in a filing cabinet to see what's inside." |
| `git status` | "I'm going to check which files have been changed or added since the last time we saved our work to the project history." |
| `git add` / `git commit` | "I'm going to save the current state of the project — like taking a snapshot — so we can always come back to this point if needed." |
| `git push` | "I'm going to upload our saved snapshot to GitHub, which is the online storage for this project, so it's backed up and shareable." |
| `pip install ...` | "I'm going to install a software tool that the analysis needs. Think of it like downloading an app — the computer goes and fetches it and sets it up." |
| `mkdir` | "I'm going to create a new folder, just like right-clicking in a file explorer and choosing 'New Folder'." |
| `mv` | "I'm going to move a file from one folder to another — the same as dragging and dropping it in a file explorer." |
| `rm` | "I'm going to permanently delete a file. This cannot be undone, so I'm only doing this because we've confirmed it's no longer needed." |
| `sync-skills.sh` | "I'm going to update all the AI assistants with the latest version of the skills we've set up for this project." |

### Never paste raw output without translating it

If a command produces output, go through it line by line (or group by group) and explain what each part means. For example:

**Bad:**
```
lca_results.md written.
product_graph_scaled.svg saved.
product_graph_structure.svg saved.
```
> Done.

**Good:**
> The command finished and reported two things:
> - **lca_results.md written** — this means the written report (the one with all the numbers and tables) has been saved into the cotton shirt folder. You can open it in VS Code to read it.
> - **product_graph_scaled.svg saved** — this is the scaled diagram (with amounts and scaling factors), saved as a vector image you can open in VS Code.
> - **product_graph_structure.svg saved** — this is the structure diagram (flow names only), also saved as a vector image.
> Everything went as expected — no errors.

---

## Examples of Student-Friendly vs. Technical Responses

### Example 1 — Explaining a code change

**Bad (too technical):**
> I updated the `f` vector construction in `lca_analysis.py` to dynamically resolve the reference flow index from the spec rather than hardcoding `f[0]`.

**Good (student-friendly):**
> I found and fixed a bug in the analysis tool. Here's what was happening: the tool was always assuming that the first item in your supply chain list was the finished product you wanted to study — but that's not always true. In the cotton shirt example, the first item was raw cotton (the farm), not the finished shirt. So the maths was being done for raw cotton instead of the shirt, which gave a completely wrong answer.
>
> I've fixed it so the tool now looks up which item in the list is the actual finished product and uses that as the starting point for the calculation. You don't need to change anything in your analysis files — it will just work correctly from now on.

### Example 2 — Explaining a file structure

**Bad (too technical):**
> Each analysis is isolated in its own subdirectory under `lca_analysis/` with its own `recipe_card.md` spec and generated `lca_results.md` output.

**Good (student-friendly):**
> Think of the `lca_analysis` folder like a filing cabinet. Inside it, each product you study gets its own drawer — for example, `coffee` or `cotton_shirt`. Inside each drawer, there are four documents: the recipe card (`recipe_card.md`) where you describe the product, the report (`lca_results.md`) with the calculation results, and two supply chain diagrams (`product_graph_scaled.svg` and `product_graph_structure.svg`). This way, studying a new product never overwrites the work you did on a previous one.

### Example 3 — Explaining a result

**Bad (too technical):**
> The scaling vector shows s[5] = 2.825 for P5, meaning the electricity generation process must run 2.825 times to satisfy the functional unit demand, accounting for 60.9% of total GWP impact.

**Good (student-friendly):**
> The results show that the single biggest source of CO₂ in making one cotton shirt is the electricity used by the mills and the factory. To make just one shirt, the power plant has to run hard enough to generate about 2.8 units of electricity — and each unit releases CO₂ by burning coal. That electricity-related pollution makes up about 61% of the shirt's total carbon footprint. The cotton farm itself accounts for the remaining 39%. This tells us something really useful for a business decision: if a clothing company switched their factories and mills to renewable energy (solar or wind), they could cut the shirt's carbon footprint nearly in half.

---

## Explaining LCA Concepts to Students

When introducing LCA ideas, always connect them to business and retail contexts the student will recognise.

### Functional unit
Explain it as: "The thing you are measuring. We have to be precise — not just 'a cup', but 'one cup used to serve one hot drink'. This matters because if you compare a paper cup to a ceramic mug without specifying that the mug gets used 500 times, the comparison is unfair."

### Supply chain / processes
Explain it as: "Every step it takes to make the product, from the very beginning to the end. For a cotton shirt, that's the farm, the spinning mill, the weaving mill, the garment factory, and the power plant supplying all of them. Each step is called a 'process'."

### Technology matrix (Matrix A)
Explain it as: "A grid that maps out all the connections between the steps in the supply chain. Each row is a material or product (like yarn or electricity), and each column is a production step. A positive number means that step produces that item. A negative number means that step consumes it."

### Scaling vector (s)
Explain it as: "The answer to the question: how much does each step in the supply chain need to run to produce exactly one unit of the finished product? For example, to make one shirt you only need the sewing factory to run once — but you need the cotton farm, the spinning mill, and the weaving mill to each run a fraction of a full cycle, because the shirt only uses a quarter of a kilogram of fabric."

### CO₂ result
Explain it as: "The total greenhouse gas released to produce one unit of the product, measured in kilograms. To put it in context: the average car emits about 0.12 kg of CO₂ per kilometre driven. So a 2.32 kg footprint for a shirt is roughly equivalent to driving about 19 kilometres."

---

## Every Time You Make a Change to a File

After every file edit or code change, always provide exactly these 3 points:

1. **What was changed** — describe it in plain language, not code terminology. Name the file and describe what it does before explaining what you changed inside it.
2. **Why it was changed** — what problem does it solve, what was wrong before, or what does it add?
3. **What you'll see / any action needed** — describe the visible result in plain language and be explicit about whether the student needs to do anything (refresh the browser, run a command, open a file, etc.). If no action is needed, say that clearly too.

---

## The openLCA Server

The openLCA server does **not** start automatically. Students must start it manually before running any analysis. There are three scripts in the project root for managing it:

- **`setup_olca.sh`** — Use this the very first time in a new Codespace. It builds the openLCA software (takes a minute or two, happens only once) and then starts the server.
- **`start_olca.sh`** — Use this at the beginning of every session after the first. Much faster because the build step is already done.
- **`stop_olca.sh`** — Use this to shut the server down when done.

To check whether the server is running:
```bash
curl -s http://localhost:8080/api/version
```
Explain the result as: "I just sent a quick 'are you there?' message to the openLCA software running in the background. It replied with its version number, which means it's up and running and ready to do calculations."

If it is not running, start it with `bash start_olca.sh` and explain: "The openLCA calculation engine wasn't running — I've just started it up. It's a bit like turning on the calculator before you can press any buttons. This only takes a few seconds."

If it has never been set up before, use `bash setup_olca.sh` instead and explain: "This is the first-time setup — the computer needs to download and build the openLCA software before it can start. It will also download the reference data it needs (about 340 MB in total). This takes a few minutes but only needs to happen once."

`setup_olca.sh` now handles everything automatically in sequence: Python tools → data downloads → Docker build → server start → database import. Each step is skipped on subsequent runs if it has already been completed.

---

## FEDEFL flow names — the naming standard for emissions and resources

All recipe cards use the **Federal Elementary Flow List (FEDEFL)** — the US EPA's standard names for elementary flows. When writing or editing recipe cards, always use these exact names in the `elementary_flows` and `emissions` sections. The most common ones are:

| Substance | FEDEFL name (use this exactly) | Do NOT use |
|---|---|---|
| Carbon dioxide | `Carbon dioxide` | `CO2`, `CO2 to air`, `carbon dioxide` |
| Methane | `Methane` | `CH4`, `CH4 to air` |
| Nitrous oxide | `Nitrous oxide` | `N2O`, `N2O to air` |
| Ammonia | `Ammonia` | `NH3`, `NH3 to air` |
| Nitrogen oxides | `Nitrogen oxides` | `NOx`, `NOx to air` |
| Sulfur dioxide | `Sulfur dioxide` | `SO2`, `SO2 to air` |
| Water | `Water` | `H2O`, `water` |

Getting these names wrong causes the LCIA step to score zero for that flow, with no error message — it will silently fail. Always double-check the spelling.

The `compartment` field (e.g. `compartment: air`) is used in recipe cards for human readability but does not affect the database lookup — only the name matters for matching.

---

## LCIA method — TRACI 2.2

All recipe cards include a `lcia:` section at the bottom:

```yaml
lcia:
  method_name: "TRACI 2.2"
```

This tells `lca_analysis.py` which impact method to use when converting the inventory (raw kg of CO₂, SO₂, etc.) into scored impact categories. Always include this section. The only supported value is `"TRACI 2.2"`.

**TRACI 2.2** (Tool for the Reduction and Assessment of Chemicals and other environmental Impacts) is the US EPA's standard life cycle impact assessment method. It produces eight impact scores:

| Category | Unit | Plain-English meaning |
|---|---|---|
| Global warming | kg CO₂ eq | Contribution to climate change |
| Acidification | kg SO₂ eq | Contribution to acid rain |
| Smog formation | kg O₃ eq | Contribution to ground-level smog |
| Human health — particulate matter | kg PM 2.5 eq | Fine particle health damage |
| Eutrophication (freshwater) | kg N eq | Excess nutrients causing algal blooms |
| Human health — cancer | CTUh | Cancer risk from toxic substances |
| Human health — non-cancer | CTUh | Other toxic health impacts |
| Ozone depletion | kg CFC-11 eq | Damage to the stratospheric ozone layer |

TRACI 2.2 requires FEDEFL flow names (see section above). Flows with non-FEDEFL names will not match any characterisation factor and will contribute zero to all impact categories.

**The blorp example** (`lca_analysis/blorp/`) is intentionally excluded from TRACI scoring — it uses made-up units (Blorps, Haze, Smog) as a pure maths teaching demo. Its recipe card does not include the `lcia:` section and should be left unchanged.

---

## The `product_graphs/` folder — a testing workshop for supply chain diagrams

The `product_graphs/` folder is a dedicated space for experimenting with the
`lca_svg.py` script (the tool that draws supply chain diagrams). Think of it
like a test kitchen: you can cook up any imaginary product or supply chain,
no matter how simple or weird, and immediately see what the diagram looks
like.

### What is in there

Two groups of files live side by side:

1. **Recipe cards** — named `<product>_recipe_card.md`. These are copies of
   the real recipe cards from `lca_analysis/`, plus extra experimental ones
   with made-up products and unusual combinations of emissions and resource
   extractions (e.g. 7 different pollutants on a 3-node chain).

2. **SVG diagrams** — two per recipe card:
   - `<product>_product_graph_scaled.svg` — shows amounts and scaling factors
   - `<product>_product_graph_structure.svg` — shows flow names only

### What you should do when asked about this folder

When a student asks about `product_graphs/` or wants to test `lca_svg.py`,
you should:

1. Explain the folder is a safe sandbox — nothing here is tied to the
   real openLCA server, so there is no risk of breaking anything.

2. Invent hypothetical recipe cards on the spot to demonstrate specific
   features of the SVG script. For example:
   - One node, one emission (simplest possible diagram)
   - Many emissions on a single node (tests arrow stacking)
   - Many extractions on a single node (tests green arrow spacing)
   - Convergent supply chains (two suppliers feeding one assembler)
   - Divergent supply chains (one supplier feeding two downstream processes)
   - Chains where the reference process is not the first one listed
   - Very wide or very tall layouts

3. Generate both the scaled and structure SVGs so the student can compare.

4. If the student is curious about the visual style, explain that the box
   width (`BOX_W`) and arrow spacing (`EMIT_OFFSET`) are just numbers at
   the top of `lca_svg.py` that can be changed to make the diagram look
   however you like.

### Naming convention

Every SVG output should follow this pattern so it is easy to find:

- `python3 lca_scripts/lca_svg.py product_graphs/<product>_recipe_card.md product_graphs/<product>_product_graph_scaled.svg`
- `python3 lca_scripts/lca_svg.py product_graphs/<product>_recipe_card.md product_graphs/<product>_product_graph_structure.svg --structure`

Do not rely on the default output path (which strips `.md` to `.svg`) —
always pass the output path explicitly.

---

## Syncing skills after edits

`.skillshare/` is the master skill directory — it is the **only** place skills should ever be edited. Each skill has its own subfolder inside `.skillshare/skills/` containing a `SKILL.md` file. Never edit skills anywhere else; other locations are deployment copies that get overwritten on the next sync.

**After editing any skill file, you must run:**

```bash
skillshare sync
```

Think of this like publishing a document. Editing the `SKILL.md` file is like editing a draft — the AI assistants do not see the change until you run `skillshare sync`, which pushes the updated skill out to Claude, OpenCode, Gemini, Copilot, and the other tools configured in `.skillshare/config.yaml`.

If you skip this step, the assistants will keep running the old version of the skill even though the file on disk has changed.

**When to sync:**
- After editing a `SKILL.md` file
- After creating a new skill folder
- After changing the skill version number

**When not to sync:**
- After saving a session file to `skills_sessions/` — session files are transcripts, not skills
- After editing `CLAUDE.md` or any other project file — those are read directly, not synced

---

## Skill session files — naming convention and format

When a skill session is tested and the student (or tester) asks to save it, save the transcript inside a subfolder named after the skill, inside `skills_sessions/`. Each skill has its own subfolder:

```
skills_sessions/
  functional-unit/
  goal-and-scope/
  life-cycle-inventory/
  life-cycle-stages/
  system-boundary/
  technosphere-and-ecosphere/
  what-is-lca/
```

The file itself follows this naming convention:

```
skills_sessions/{skill-name}/{skill-name}-{arg}-v{version}-{student}-{model}-session{n}.md
```

For skills with no case study argument (`what-is-lca`), omit the `{arg}` segment:

```
skills_sessions/{skill-name}/{skill-name}-v{version}-{student}-{model}-session{n}.md
```

**Examples:**
- `skills_sessions/what-is-lca/what-is-lca-v0.1-diana-sonnet-4-6-session1.md`
- `skills_sessions/system-boundary/system-boundary-cotton_fiber-v0.1-elena-sonnet-4-6-session1.md`
- `skills_sessions/functional-unit/functional-unit-wool_yarn-v0.2-calvin-sonnet-4-6-session2.md`

**Rules:**
- `{skill-name}` — the kebab-case skill name exactly as it appears in the slash command (e.g. `what-is-lca`, `system-boundary`, `functional-unit`)
- `{arg}` — the case study argument passed to the skill (e.g. `wool_yarn`, `cotton_fiber`, `polyester_tshirt`); omit for `what-is-lca`
- `{version}` — the skill version from the SKILL.md file, e.g. `0.1`, `0.2`
- `{student}` — the first name of the person who ran the session (e.g. `calvin`, `elena`, `diana`)
- `{model}` — the short model name of the AI running the skill (e.g. `sonnet-4-6`, `gpt-4o`, `gemini-2-5`)
- `{n}` — a counter starting at 1; increment it when the same skill+arg+version+student+model combination has already been saved

**File header format:**

The first line of every session file must be the slash command that was used to invoke the skill, including any argument (the case study name):

```markdown
# /functional-unit wool_yarn
**Skill version:** 0.2
**Student:** calvin
**Model:** sonnet-4-6
**Date:** 2026-06-13
```

For skills with no case study argument (only `what-is-lca`), the first line is just `# /what-is-lca`.

**Speaker labels:**

Always use `**AI:**` for the AI's turns and `**Student:**` for the student's turns. Do not use `**Skill:**`, `**Claude:**`, or any other label.

**Image links:**

Wrap every image in a markdown link (so it is clickable) and show the file path as a code span on the next line, so the path is visible even if the image does not render:

```markdown
[![Wool Yarn supply chain — structure](../../skills_references/wool_yarn/product_graph_structure.svg)](../../skills_references/wool_yarn/product_graph_structure.svg)
`../../skills_references/wool_yarn/product_graph_structure.svg`
```

Note the two `../` levels — one to exit the skill subfolder (e.g. `system-boundary/`), one to exit `skills_sessions/`.

**What to include in the file:**

Save only the header and the verbatim conversation that took place while the skill was running — the back-and-forth between `**AI:**` and `**Student:**` turns, exactly as they happened. Nothing else. Do not add notes, summaries, completion status, meta-comments, or any text that was not part of the actual skill conversation. If the session ended early, just stop — do not add a line explaining that it was incomplete.

**After saving a session file, always run:**

```bash
python3 skills_sessions/generate_sessions.py
```

This updates `skills_sessions/sessions.json`, which is the file that the session viewer (`skills_sessions/index.html`) uses to build its list of sessions. If you skip this step, the new session will not appear in the viewer.

---

# AI Agentic Tools Dev Container Guide

This dev container is built from [calvinw/ai-agentic-tools](https://github.com/calvinw/ai-agentic-tools) and includes a comprehensive toolkit for AI-assisted development.

## Container Image

**Base:** Node.js 22-slim  
**Published to:** `ghcr.io/calvinw/ai-course-devcontainer:latest`  
**Rebuilt:** Automatically on Dockerfile changes, weekly via GitHub Actions

---

## System Tools & Utilities

The container includes essential CLI tools pre-installed:

### File & Process Tools
- `curl`, `wget` — HTTP clients
- `git` — Version control
- `vim` — Text editor
- `jq` — JSON processor
- `bat` — Syntax-highlighted cat
- `ripgrep` — Fast file search
- `fd-find` — User-friendly find alternative
- `tree` — Directory tree viewer
- `fzf` — Fuzzy finder
- `lsof`, `procps`, `iproute2` — Process/network inspection
- `make` — Build automation
- `bubblewrap` — Sandboxing utility

### Specialized Tools
- `glow` — Markdown renderer
- `gh` — GitHub CLI
- `upterm` — Terminal sharing
- `miller` — Data transformation tool
- `pspg` — PostgreSQL pager
- `poppler-utils` — PDF utilities

### Development Environment
- `python3` with `pip` and `venv`
- UTF-8 locale support
- `/workspace` as default working directory

---

## AI Coding Assistants

Pre-installed via npm:

- **Claude Code** — Anthropic's agentic coding tool (installed separately)
- **OpenCode** — Open source AI coding agent
- **GitHub Copilot** — GitHub's AI pair programmer
- **Crush** — Charm's beautifully themed terminal assistant
- **Google Gemini** — Google's AI coding assistant
- **OpenAI Codex** — OpenAI's code generation model
- **Alibaba Qwen Code** — Qwen's AI coding assistant
- **Supergateway** (v3.4.3) — MCP bridge for Codex integration

---

## Available Scripts

All scripts are located in `/usr/local/lib/ai-tools/` and added to PATH. Run them directly from anywhere.

### Environment & Setup

**`setup-env.sh`**
- Generates Ed25519 SSH key pair at `~/.ssh/id_ed25519` (if not present)
- Appends `$HOME/.local/bin` to `~/.bashrc` for local package discovery
- Enables pip/pipx-installed tools to be discoverable in shell

**`install-mcps.sh`**
- Reads `configs/mcp-servers.conf` and registers Model Context Protocol servers
- Installs MCPs to all AI tools: Claude, OpenCode, Gemini, Crush, Copilot, Codex
- Safe to re-run; existing entries are replaced with current values
- Example: `install-mcps.sh` (runs automatically on container creation)

**`uninstall-mcps.sh`**
- Removes all MCP registrations listed in `configs/mcp-servers.conf`
- Cleans up MCP server entries from all tool configurations

### Skills Management

**`setup-skills.sh`**
- Initializes `.skillshare/` directory structure with `skills/` subdirectory
- Creates sample "hello-world" skill template
- Generates `config.yaml` specifying target platforms (Claude, OpenCode, Copilot, Gemini, Crush, Codex)
- Downloads and installs the `skillshare` CLI tool if not present
- Run once per project: `setup-skills.sh`

**`sync-skills.sh`**
- Deploys all skills from `.skillshare/skills/` to configured AI platforms
- Uses `.skillshare/config.yaml` to determine target platforms
- Run after modifying skills: `sync-skills.sh`

**`unsync-skills.sh`**
- Reverses skill synchronization (removes skills from agents)
- Cleans up deployed skills from all platforms

### Optional Add-ons

**`install-datascience.sh`**
- Installs Python data science ecosystem
- Includes: numpy, pandas, matplotlib, seaborn, requests
- Installs: Jupyter, Quarto, TinyTeX
- Optional; run only if needed: `install-datascience.sh`

**`install-dolt.sh`**
- Installs Dolt — a version-controlled SQL database
- Optional; run only if needed: `install-dolt.sh`

**`install_upterm.sh`**
- Installs Upterm for terminal sharing capabilities
- Already included in container; script available for updates

### Repository Synchronization

**`sync-from-upstream.sh`**
- Synchronizes changes from the upstream ai-agentic-tools repository
- Used for keeping container definition in sync with source

**`lib-mcp-parse.sh`**
- Library script for parsing MCP configuration files
- Sourced by other scripts; not meant to be run directly

---

## Configuration Files

### `configs/mcp-servers.conf`
Defines which Model Context Protocol servers to install. Format:
```
# SSE MCP (no authentication):
dolt=https://bus-mgmt-databases.mcp.mathplosion.com/mcp-dolt-database/sse

# HTTP MCP with authentication:
# stitch=https://stitch.googleapis.com/mcp|http|X-Goog-Api-Key:$STITCH_API_KEY
```

Run `install-mcps.sh` after editing to register changes.

### `.skillshare/`
Project-level skills directory (single source of truth for custom skills).
- **Always edit skills here**, never in individual tool directories
- Run `sync-skills.sh` after modifying to deploy to all agents
- Contains: `config.yaml`, `skills/` subdirectory with individual skill definitions

### `opencode.json`
Project-level OpenCode configuration (project root, highest precedence).
- Sets default model and provider settings
- Example: Configures Deepseek V4 Flash via OpenRouter
- Overrides `~/.config/opencode/opencode.json` and `.opencode/` configs

### `.devcontainer/devcontainer.json`
Dev container configuration.
- References container image: `ghcr.io/calvinw/ai-course-devcontainer:latest`
- Runs setup on creation: `setup-env.sh && install-mcps.sh && install-datascience.sh && setup-skills.sh && skillshare install github.com/anthropics/skills/skill-creator && (sync-skills.sh || true) && pip install olca-ipc olca-schema --break-system-packages`
- Declares secrets for GitHub Codespaces: `STITCH_API_KEY`

---

## Typical Workflow

1. **First container creation** — Runs automatically:
   - `setup-env.sh` — SSH key + PATH setup
   - `install-mcps.sh` — Register MCPs from `configs/mcp-servers.conf`
   - `install-datascience.sh` — Install Python data science tools
   - `setup-skills.sh` — Initialize skills infrastructure
   - `skillshare install github.com/anthropics/skills/skill-creator` — Install skill-creator tool
   - `sync-skills.sh` — Deploy skills to all agents
   - `pip install olca-ipc olca-schema` — Install openLCA Python client

2. **Adding new MCPs** — Edit `configs/mcp-servers.conf`, then:
   ```
   # install-mcps.sh
   ```

3. **Creating/modifying skills** — Edit files in `.skillshare/`, then:
   ```
   # sync-skills.sh
   ```

4. **Installing additional skills**:
   ```
   # skillshare install github.com/anthropics/skills/skill-creator
   # skillshare install github.com/your-org/your-skill
   # sync-skills.sh
   ```

5. **Adding optional tools**:
   ```
   # install-datascience.sh
   # install-dolt.sh
   ```

---

## Starting Agents

All launcher scripts live in `permissions/` (baked into container image):

- `claude.sh` — Runs Claude Code with sandbox mode
- `opencode.sh` — Runs OpenCode with allow-all permissions
- `copilot.sh` — Runs GitHub Copilot with allow-all
- `crush.sh` — Runs Crush with yolo mode
- `codex.sh` — Runs OpenAI Codex
- `gemini.sh` — Runs Google Gemini

---

## Environment Variables

**For authentication in Codespaces:**
- `STITCH_API_KEY` — Stitch MCP authentication

Declare these in `.devcontainer/devcontainer.json` under `"secrets"` and add values in GitHub Codespaces settings.

---

## Source Repository

All tools, scripts, and Dockerfile: [calvinw/ai-agentic-tools](https://github.com/calvinw/ai-agentic-tools)

Container rebuilt automatically on changes to:
- Dockerfile
- Scripts in `scripts/` directory
- Weekly via GitHub Actions
