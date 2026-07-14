# PLAN: Set Up `quarto_docs/` for a New Repository

This plan tells another LLM (or a human) how to recreate the `quarto_docs/` website infrastructure in a new repository. The goal is a Quarto website that:

- Has **Sessions**, **Plans**, and **Skills** tabs in the navbar
- Has a **Sessions** sidebar grouped by skill name, with individual session transcripts
- Has a **Plans** sidebar listing planning documents
- Has a **Skills** sidebar listing AI skill definitions, each with a `(.md)` link pointing to the original `SKILL.md` on GitHub
- Includes `skills_references/` (LCA case-study data with diagrams) as a resource
- Deploys automatically via GitHub Actions to GitHub Pages

---

## 1. Source Folders Required in the Repo

These must exist **before** the generator scripts run. They are the canonical data sources:

| Folder | Purpose |
|---|---|
| `.skillshare/skills/<name>/SKILL.md` | AI teaching skill definitions (source of truth) |
| `skills_sessions/<skill>/<session>.md` | Session transcripts grouped by skill |
| `skills_sessions/index.md` | Sessions landing page |
| `plan/PLAN_*.md` | Planning documents |
| `plan/index.md` | Plans landing page |
| `skills_references/<product>/` | LCA case-study data (product graphs, diagrams, results) |
| `lca_analysis/<product>/` | LCA analysis folders with `product_graph.yaml` |

If any folder or file does not exist, the generator scripts skip it gracefully.

### Session file naming convention

Session files follow this pattern (see plan `PLAN_REFERENCE_EXAMPLES.md` for details):

```
skills_sessions/<skill-name>/<skill-name>-<case_study>-v<version>-<student>-<model>-session<n>.md
```

Each session file **must** have the slash command as its first line:

```markdown
# /<skill-name> [case_study]
```

And a header block with metadata:

```markdown
**Skill version:** <version>
**Student:** <name>
**Model:** <model-name>
**Date:** <date>
```

Images in session files reference `skills_references/` with this relative path (works from within `quarto_docs/skills_sessions/<skill>/`):

```
../../skills_references/<product>/<file>.svg
```

---

## 2. Files to Create in `quarto_docs/`

### 2a. Static files (create once, edit only to change content/style)

| File | Purpose |
|---|---|
| `quarto_docs/index.md` | Home page content |
| `quarto_docs/custom.css` | Sidebar font-size tweaks |
| `quarto_docs/sidebar-tweaks.html` | Rewrites `(.md)` links to GitHub blob URLs or local `.md` paths |
| `quarto_docs/Makefile` | `regenerate`, `render`, `serve`, `clean` targets |
| `quarto_docs/.gitignore` | Ignores generated output |

### 2b. Generator scripts (create once, run on every data change)

| File | Source location (in original repo) | Purpose |
|---|---|---|
| `quarto_docs/generate_quarto_yml.py` | `quarto_docs/generate_quarto_yml.py` | Copies source files into `quarto_docs/`, writes `_quarto.yml` |
| `skills_sessions/generate_sessions.py` | `skills_sessions/generate_sessions.py` | Scans sessions, writes `quarto_docs/sessions.json` |
| `plan/generate_plans.py` | `plan/generate_plans.py` | Scans plans, writes `quarto_docs/plans.json` |
| `lca_analysis/generate_analyses.py` | `lca_analysis/generate_analyses.py` | Scans analyses, writes `quarto_docs/analyses.json` |

### 2c. Generated files (created by scripts, do not edit manually)

| File | Created by |
|---|---|
| `quarto_docs/_quarto.yml` | `generate_quarto_yml.py` |
| `quarto_docs/skills/*.md` | `generate_quarto_yml.py` (copied from `.skillshare/skills/`) |
| `quarto_docs/skills/index.md` | `generate_quarto_yml.py` (written inline) |
| `quarto_docs/skills_sessions/*/*.md` | `generate_quarto_yml.py` (copied from `skills_sessions/`) |
| `quarto_docs/skills_sessions/index.md` | `generate_quarto_yml.py` (copied from `skills_sessions/index.md`) |
| `quarto_docs/plan/*.md` | `generate_quarto_yml.py` (copied from `plan/`) |
| `quarto_docs/plan/index.md` | `generate_quarto_yml.py` (copied from `plan/index.md`) |
| `quarto_docs/skills_references/` | `generate_quarto_yml.py` (copied from `skills_references/`) |
| `quarto_docs/sessions.json` | `skills_sessions/generate_sessions.py` |
| `quarto_docs/plans.json` | `plan/generate_plans.py` |
| `quarto_docs/analyses.json` | `lca_analysis/generate_analyses.py` |

---

## 3. Step-by-Step Setup Instructions

### Step 1: Create `quarto_docs/` directory and static files

Create the folder:

```bash
mkdir -p quarto_docs
```

Create `quarto_docs/index.md`:

```markdown
# Agentic LCA

Resources for Life Cycle Assessment at FIT.

- [Sessions](skills_sessions/index.md) — AI-guided teaching conversations, organised by LCA skill
- [Plans](plan/index.md) — Project and research planning documents
- [Skills](skills/index.md) — AI teaching skill definitions

## Contributors

- Calvin Williamson ([calvinw](https://github.com/calvinw))
- Junghyun Choi ([elenachoi1](https://github.com/elenachoi1))
```

*(Update the title and contributors for the new repo.)*

Create `quarto_docs/custom.css`:

```css
#quarto-sidebar .sidebar-item-text,
#quarto-sidebar .sidebar-link,
#quarto-sidebar .sidebar-section .sidebar-item {
  font-size: 0.8rem;
}
```

Create `quarto_docs/.gitignore`:

```
/.quarto/
**/*.quarto_ipynb
site_libs/
skills/*.html
plan/*.html
skills_sessions/**/*.html
```

### Step 2: Create `Makefile`

`quarto_docs/Makefile`:

```makefile
.PHONY: all regenerate render serve preview clean

all: regenerate render

regenerate:
	python3 generate_quarto_yml.py
	python3 ../skills_sessions/generate_sessions.py
	python3 ../plan/generate_plans.py
	python3 ../lca_analysis/generate_analyses.py

render:
	quarto render

serve: render
	cp skills/*.md _site/skills/
	python3 -m http.server 8080 --directory _site
	rm -f _site/skills/*.md

preview: serve

clean:
	rm -rf _site
```

### Step 3: Create `sidebar-tweaks.html`

**This file requires customisation.** Create `quarto_docs/sidebar-tweaks.html`:

```html
<script>
document.addEventListener('DOMContentLoaded', function () {
  var sidebar = document.getElementById('quarto-sidebar');
  if (!sidebar) return;
  var isGitHubPages = window.location.hostname.includes('github.io');
  const items = Array.from(sidebar.querySelectorAll('li.sidebar-item'));
  items.forEach(function (item, i) {
    const link = item.querySelector('a.sidebar-item-text');
    if (!link || link.textContent.trim() !== '(.md)') return;
    const prevItem = items[i - 1];
    if (!prevItem) return;
    const prevLink = prevItem.querySelector('a.sidebar-item-text');
    if (!prevLink) return;
    const prevHref = prevLink.getAttribute('href');
    const match = prevHref.match(/skills\/(.+)\.html/);
    if (!match) return;
    const skillName = match[1];
    if (isGitHubPages) {
      link.href = 'https://github.com/YOUR_ORG/YOUR_REPO/blob/main/.skillshare/skills/' + skillName + '/SKILL.md';
    } else {
      link.href = prevHref.replace('.html', '.md');
    }
    const prevContainer = prevItem.querySelector('.sidebar-item-container');
    if (!prevContainer) return;
    prevContainer.style.display = 'block';
    link.style.display = 'inline';
    link.style.marginLeft = '4px';
    link.style.fontSize = '0.72em';
    link.style.opacity = '0.55';
    link.style.fontWeight = 'normal';
    prevContainer.appendChild(link);
    item.style.display = 'none';
  });
});
</script>
```

**Crucial:** Replace `YOUR_ORG/YOUR_REPO` on the GitHub URL line with the actual GitHub organisation and repository name.

### Step 4: Create generator scripts

Create these four generator scripts. Copy them from their original locations:

1. **`quarto_docs/generate_quarto_yml.py`** — the main generator. It scans `.skillshare/skills/`, `skills_sessions/`, `plan/`, and `skills_references/`, copies files into `quarto_docs/`, and writes `_quarto.yml`.

2. **`skills_sessions/generate_sessions.py`** — scans `skills_sessions/` for session transcripts and writes `quarto_docs/sessions.json`.

3. **`plan/generate_plans.py`** — scans `plan/` for `PLAN_*.md` files and writes `quarto_docs/plans.json`.

4. **`lca_analysis/generate_analyses.py`** — scans `lca_analysis/` for `product_graph.yaml` files and writes `quarto_docs/analyses.json`.

The full contents of these scripts are in Appendix A below.

### Step 5: Maintain the `SKILL_ORDER` list consistently

Both `generate_quarto_yml.py` and `generate_sessions.py` contain an identical `SKILL_ORDER` list:

```python
SKILL_ORDER = [
    "what-is-lca", "system-boundary", "life-cycle-stages", "goal-and-scope",
    "functional-unit", "supply-chain", "technosphere-and-ecosphere",
    "life-cycle-inventory", "scaling-vector", "what-is-impact-assessment",
    "impact-characterization", "damage-characterization", "run-lca",
    "lca-from-url", "skill-creator",
]
```

These two lists **must be kept identical** to ensure the sessions sidebar and the skills sidebar follow the same order. Update both files when adding or removing a skill.

### Step 6: Verify `skills_references/` relative paths in session files

Every session file that embeds a supply chain diagram uses this relative path (from within `quarto_docs/skills_sessions/<skill>/<session>.md`):

```markdown
../../skills_references/<product>/<file>.svg
```

When `generate_quarto_yml.py` copies session files into `quarto_docs/skills_sessions/<skill>/`, the `skills_references/` directory sits at `quarto_docs/skills_references/` — exactly two `../` levels up. So the path `../../skills_references/...` resolves correctly from any session file at depth 3 (`quarto_docs/skills_sessions/<skill>/<file>.md`).

Session files in the source `skills_sessions/` folder use the same `../../` prefix. This works because `skills_sessions/` is at the repo root, and `skills_references/` is also at the repo root — again exactly two `../` levels up from `skills_sessions/<skill>/<file>.md`.

### Step 7: Create GitHub Actions workflow

Create `.github/workflows/deploy-quarto.yml`:

```yaml
name: Deploy Quarto Site to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Regenerate manifest and nav files
        run: |
          python3 skills_sessions/generate_sessions.py
          python3 plan/generate_plans.py
          python3 quarto_docs/generate_quarto_yml.py

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Publish to GitHub Pages
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
          path: quarto_docs
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Step 8: Enable GitHub Pages

1. Go to the repository **Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set **Branch** to `gh-pages` and folder to `/ (root)`
4. The first deployment from the GitHub Action will create the `gh-pages` branch automatically

### Step 9: Run the generators and test locally

```bash
# Regenerate all files
cd quarto_docs
python3 generate_quarto_yml.py
python3 ../skills_sessions/generate_sessions.py
python3 ../plan/generate_plans.py
python3 ../lca_analysis/generate_analyses.py

# Render and preview
make serve
```

Open `http://localhost:8080` in a browser.

---

## 4. Appendix A: Full Script Contents

### `quarto_docs/generate_quarto_yml.py`

```python
#!/usr/bin/env python3
"""Generate quarto_docs/ content and _quarto.yml from current project files."""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
QUARTO_DIR = Path(__file__).parent
SESSIONS_DIR = ROOT / "skills_sessions"
PLANS_DIR = ROOT / "plan"
SKILLS_DIR = ROOT / ".skillshare" / "skills"
REFS_DIR = ROOT / "skills_references"


def skill_title(folder_name):
    words = folder_name.replace("-", " ").split()
    stop = {"and", "or", "of", "the", "a"}
    return " ".join(
        w if w in stop else (w.upper() if w == "lca" else w.title())
        for w in words
    )


def session_text(stem, skill_prefix):
    rest = stem[len(skill_prefix):].lstrip("-")
    m = re.match(r'^(.+?)-(v[\d.]+)-.+-(session\d+)$', rest)
    if m:
        return f"{m.group(1)} {m.group(2)} {m.group(3)}"
    m = re.match(r'^(v[\d.]+)-.+-(session\d+)$', rest)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return rest


def plan_text(stem):
    return stem[5:] if stem.startswith("PLAN_") else stem


SKILL_ORDER = [
    "what-is-lca", "system-boundary", "life-cycle-stages", "goal-and-scope",
    "functional-unit", "supply-chain", "technosphere-and-ecosphere",
    "life-cycle-inventory", "scaling-vector", "what-is-impact-assessment",
    "impact-characterization", "damage-characterization", "run-lca",
    "lca-from-url", "skill-creator",
]


def q(path):
    return str(path.relative_to(QUARTO_DIR))


# --- Clean and recreate output dirs ---
for d in [QUARTO_DIR / "skills", QUARTO_DIR / "skills_sessions", QUARTO_DIR / "plan"]:
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True, exist_ok=True)

# --- Copy skills_references/ ---
QUARTO_REFS = QUARTO_DIR / "skills_references"
shutil.rmtree(QUARTO_REFS, ignore_errors=True)
if REFS_DIR.exists():
    shutil.copytree(REFS_DIR, QUARTO_REFS)

# --- Copy session files ---
session_groups = {}
for folder in sorted(SESSIONS_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith("."):
        continue
    md_files = sorted(folder.glob("*.md"))
    if not md_files:
        continue
    dest_folder = QUARTO_DIR / "skills_sessions" / folder.name
    dest_folder.mkdir(parents=True, exist_ok=True)
    copies = []
    for f in md_files:
        dest = dest_folder / f.name
        shutil.copy2(f, dest)
        copies.append(dest)
    session_groups[folder.name] = copies

# Copy sessions index
sessions_index = SESSIONS_DIR / "index.md"
if sessions_index.exists():
    shutil.copy2(sessions_index, QUARTO_DIR / "skills_sessions" / "index.md")

# --- Copy plan files ---
plan_copies = []
for f in sorted(PLANS_DIR.glob("PLAN_*.md")):
    dest = QUARTO_DIR / "plan" / f.name
    shutil.copy2(f, dest)
    plan_copies.append(dest)
plan_index = PLANS_DIR / "index.md"
if plan_index.exists():
    shutil.copy2(plan_index, QUARTO_DIR / "plan" / "index.md")

# --- Copy skill files ---
all_skill_files = {f.parent.name: f for f in SKILLS_DIR.glob("*/SKILL.md")}
ordered_names = [n for n in SKILL_ORDER if n in all_skill_files]
remaining = sorted(n for n in all_skill_files if n not in SKILL_ORDER)
skill_files = [all_skill_files[n] for n in ordered_names + remaining]

skill_copies = []
for f in skill_files:
    dest = QUARTO_DIR / "skills" / f"{f.parent.name}.md"
    shutil.copy2(f, dest)
    skill_copies.append(dest)

(QUARTO_DIR / "skills" / "index.md").write_text(
    "# Skills\n\nAI teaching skills for the LCA course.\nBrowse by skill in the sidebar on the left.\n"
)

# --- Write _quarto.yml ---
lines = [
    "project:",
    "  type: website",
    "  output-dir: _site",
    "  resources:",
    "    - skills_references/",
    "  render:",
    "    - index.md",
    "    - skills_sessions/index.md",
]
for files in session_groups.values():
    for f in files:
        lines.append(f"    - {q(f)}")
lines.append("    - plan/index.md")
for f in plan_copies:
    lines.append(f"    - {q(f)}")
lines.append("    - skills/index.md")
for f in skill_copies:
    lines.append(f"    - {q(f)}")

lines += [
    "",
    "website:",
    '  title: "Agentic LCA"',
    "  navbar:",
    "    left:",
    "      - text: Home",
    "        href: index.md",
    "      - text: Sessions",
    "        href: skills_sessions/index.md",
    "      - text: Plans",
    "        href: plan/index.md",
    "      - text: Skills",
    "        href: skills/index.md",
    "",
    "  sidebar:",
    "    - id: sessions",
    '      title: "Sessions"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: skills_sessions/index.md",
]
ordered_folders = [n for n in SKILL_ORDER if n in session_groups] + \
                  sorted(n for n in session_groups if n not in SKILL_ORDER)
for folder_name in ordered_folders:
    files = session_groups[folder_name]
    lines.append(f'        - section: "{skill_title(folder_name)}"')
    lines.append(f"          contents:")
    for f in files:
        text = session_text(f.stem, folder_name)
        lines.append(f'            - text: "{text}"')
        lines.append(f"              href: {q(f)}")

lines += [
    "",
    "    - id: plans",
    '      title: "Plans"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: plan/index.md",
]
for f in plan_copies:
    lines.append(f'        - text: "{plan_text(f.stem)}"')
    lines.append(f"          href: {q(f)}")

lines += [
    "",
    "    - id: skills",
    '      title: "Skills"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: skills/index.md",
]
for src, copy in zip(skill_files, skill_copies):
    label = skill_title(src.parent.name)
    lines.append(f'        - text: "{label}"')
    lines.append(f"          href: {q(copy)}")
    lines.append(f'        - text: "(.md)"')
    lines.append(f"          href: '#'")

lines += [
    "",
    "format:",
    "  html:",
    "    theme: cosmo",
    "    css: custom.css",
    "    toc: true",
    "    include-after-body: sidebar-tweaks.html",
    "    grid:",
    "      body-width: 2000px",
    "",
]

(QUARTO_DIR / "_quarto.yml").write_text("\n".join(lines))
n_sessions = sum(len(v) for v in session_groups.values())
print(f"quarto_docs/ generated — {n_sessions} sessions, {len(plan_copies)} plans.")
```

### `skills_sessions/generate_sessions.py`

```python
"""
Scans skills_sessions/ for *.md files and writes sessions.json.
Run from the repo root:  python3 skills_sessions/generate_sessions.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
ROOT = here.parent


_ACRONYMS    = {'lca', 'svp'}
_CONJUNCTIONS = {'and', 'or', 'of', 'the', 'a', 'an', 'in', 'on', 'at', 'to'}

SKILL_ORDER = [
    "what-is-lca", "system-boundary", "life-cycle-stages", "goal-and-scope",
    "functional-unit", "supply-chain", "technosphere-and-ecosphere",
    "life-cycle-inventory", "scaling-vector", "what-is-impact-assessment",
    "impact-characterization", "damage-characterization", "run-lca",
    "lca-from-url", "skill-creator",
]


def format_skill(slug):
    words = slug.lstrip('/').split('-')
    result = []
    for i, w in enumerate(words):
        if w in _ACRONYMS:
            result.append(w.upper())
        elif i > 0 and w in _CONJUNCTIONS:
            result.append(w)
        else:
            result.append(w.capitalize())
    return ' '.join(result)


def format_case_study(raw):
    if not raw:
        return None
    return ' '.join(w.capitalize() for w in raw.replace('_', ' ').split())


def format_model(raw):
    parts = raw.split('-')
    result = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if re.match(r'^\d+$', p):
            ver = [p]
            while i + 1 < len(parts) and re.match(r'^\d+$', parts[i + 1]):
                i += 1
                ver.append(parts[i])
            result.append('.'.join(ver))
        elif re.match(r'^v\d', p):
            result.append(p.upper())
        else:
            result.append(p.capitalize())
        i += 1
    return ' '.join(result)


sessions = []

for md in sorted(here.glob('**/*.md')):
    lines = md.read_text(encoding='utf-8').split('\n')
    m = re.match(r'^#\s+/(\S+)(?:\s+(\S+))?', lines[0])
    if not m:
        continue
    skill_slug = m.group(1)
    case_raw   = m.group(2)
    meta = {}
    for line in lines[1:10]:
        mm = re.match(r'^\*\*([^*]+):\*\*\s*(.+)', line)
        if mm:
            key = mm.group(1).strip().lower().replace(' ', '_')
            meta[key] = mm.group(2).strip()
    n_match = re.search(r'session(\d+)', md.stem)
    n = int(n_match.group(1)) if n_match else 1
    command = f'/{skill_slug}' if not case_raw else f'/{skill_slug} {case_raw}'
    sessions.append({
        'file':      str(md.relative_to(here)),
        'command':   command,
        'skill':     format_skill(skill_slug),
        'caseStudy': format_case_study(case_raw),
        'student':   meta.get('student', '').capitalize(),
        'model':     format_model(meta.get('model', '')),
        'version':   meta.get('skill_version', ''),
        'n':         n,
        '_slug':     skill_slug,
    })

slug_order = {s: i for i, s in enumerate(SKILL_ORDER)}
sessions.sort(key=lambda s: (slug_order.get(s['_slug'], 999), s['file']))
for session in sessions:
    del session['_slug']

out = ROOT / 'quarto_docs' / 'sessions.json'
out.write_text(json.dumps(sessions, indent=2), encoding='utf-8')
print(f'sessions.json: wrote {len(sessions)} sessions', file=sys.stderr)
```

### `plan/generate_plans.py`

```python
"""
Scans plan/ for PLAN_*.md files and writes plan/plans.json.
Run from the repo root:  python3 plan/generate_plans.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
ROOT = here.parent


def format_title(stem):
    name = re.sub(r'^PLAN_', '', stem)
    return ' '.join(w.capitalize() for w in name.replace('_', ' ').split())


plans = []

for md in sorted(here.glob('PLAN_*.md')):
    lines = md.read_text(encoding='utf-8').split('\n')
    title = None
    for line in lines[:5]:
        m = re.match(r'^#\s+(.+)', line)
        if m:
            title = m.group(1).strip()
            break
    if not title:
        title = format_title(md.stem)
    plans.append({
        'file': md.name,
        'title': title,
    })

out = ROOT / 'quarto_docs' / 'plans.json'
out.write_text(json.dumps(plans, indent=2), encoding='utf-8')
print(f'plans.json: wrote {len(plans)} plans', file=sys.stderr)
```

### `lca_analysis/generate_analyses.py`

```python
"""
Scans lca_analysis/ for folders containing product_graph.yaml and writes analyses.json.
Run from the repo root: python3 lca_analysis/generate_analyses.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
root = here.parent


def format_name(folder_name):
    return folder_name.replace('_', ' ').title()


def file_label(md_path, folder_name):
    stem = md_path.stem
    prefix = folder_name + '_'
    if stem.startswith(prefix):
        stem = stem[len(prefix):]
    return stem.replace('_', ' ')


analyses = []

for product_graph in sorted(root.rglob('product_graph.yaml')):
    folder = product_graph.parent
    rel    = folder.relative_to(root)
    name   = format_name(folder.name)
    group  = folder.parent.name if folder.parent != root else ''
    mds = sorted(folder.glob('*.md'), key=lambda p: (p.name != 'product_graph.yaml', p.name))
    files = [
        {
            'file':  str(rel / md.name),
            'label': file_label(md, folder.name),
        }
        for md in mds
    ]
    analyses.append({
        'folder': str(rel),
        'name':   name,
        'group':  group if group != 'lca_analysis' else '',
        'files':  files,
    })

out = root / 'quarto_docs' / 'analyses.json'
out.write_text(json.dumps(analyses, indent=2), encoding='utf-8')
print(f'analyses.json: wrote {len(analyses)} analyses', file=sys.stderr)
```

---

## 5. Summary: What to Customise Per Repository

| Item | Where to change |
|---|---|
| Website title | `_quarto.yml` `title:` (set by `generate_quarto_yml.py` — edit the string there) |
| GitHub repo URL | `sidebar-tweaks.html` — the line with `https://github.com/...` |
| `SKILL_ORDER` | Both `generate_quarto_yml.py` and `generate_sessions.py` (must match) |
| Home page content | `quarto_docs/index.md` |
| Theme | `theme:` in `_quarto.yml` (set by `generate_quarto_yml.py`) |
| GitHub Actions branch | `.github/workflows/deploy-quarto.yml` `branches:` list |

---

## 6. Key Gotchas

- The `SKILL_ORDER` list in `generate_quarto_yml.py` and `generate_sessions.py` **must be identical**. If they diverge, the sidebar ordering will be inconsistent.
- Session files **must** start with `# /<skill-name>` on line 1. Files without this header are silently skipped by `generate_sessions.py`.
- `skills_sessions/` subfolder names must match the skill slugs used in `SKILL_ORDER` for proper grouping.
- The `sidebar-tweaks.html` GitHub URL is hardcoded to the original repo. When setting up a new repo, this URL **must** be changed to the new repository.
- The `Makefile` `serve` target copies `.md` files into `_site/skills/` so that `(.md)` sidebar links work in local preview. This only works for local development — on GitHub Pages, the JS uses the GitHub blob URL.
- Generated files (`_quarto.yml`, files in `quarto_docs/skills/`, `quarto_docs/plan/`, `quarto_docs/skills_sessions/`, `quarto_docs/skills_references/`, `*.json`) should **not** be edited by hand. They are overwritten every time the generator runs.
