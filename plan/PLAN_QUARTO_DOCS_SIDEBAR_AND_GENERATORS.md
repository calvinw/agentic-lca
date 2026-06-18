# PLAN: Quarto Sidebar Width and Collapse Behaviour

## What this plan covers

Two usability improvements to a Quarto website that has a docked sidebar:

1. **Wider sidebar** — set a fixed pixel width wider than Quarto's default (~250 px).
2. **Sections collapsed by default** — sidebar sections that contain sub-items start
   closed so the list does not overwhelm the reader on first load.

---

## Why the standard resizable-sidebar approach does not work in Quarto

Quarto generates a complex named CSS grid layout. On a page with a docked sidebar the
`body` element gets class `docked` and the page container gets class `page-columns`.
The sidebar occupies `grid-column: screen-start / body-start`, spanning several named
grid tracks. Any JavaScript that tries to resize the sidebar by hardcoding a new
`grid-template-columns` string will break because:

- The actual track names and counts vary between Quarto versions and page types.
- Setting `sidebar.style.width` fights the grid rather than working with it.
- More sophisticated approaches (reading the computed grid at drag time) can work in
  theory but are fragile across Quarto updates.

**Recommendation:** set a fixed sidebar width in `_quarto.yml` using Quarto's own
`grid.sidebar-width` option. This is stable, survives Quarto upgrades, and requires
zero JavaScript.

---

## Change 1 — Wider sidebar (fixed width)

In `_quarto.yml`, add `sidebar-width` inside the `format.html.grid` block:

```yaml
format:
  html:
    grid:
      sidebar-width: 400px   # ← add this line
      body-width: 2000px     # (example — whatever you already have)
```

`sidebar-width` is a first-class Quarto grid option. Quarto bakes the value into the
generated CSS so the layout is correct on every page without any JavaScript.

Adjust the pixel value to taste. 300–450 px is a reasonable range for a documentation
sidebar.

---

## Change 2 — Sections collapsed by default

In `_quarto.yml`, add `collapse-level: 1` to the sidebar whose sections should start
closed:

```yaml
website:
  sidebar:
    - id: sessions
      title: "Sessions"
      style: docked
      collapse-level: 1      # ← add this line
      contents:
        - section: "What Is LCA"
          contents:
            - text: "..."
              href: ...
        - section: "System Boundary"
          contents:
            - ...
```

`collapse-level: 1` tells Quarto to collapse all first-level `section:` entries on
page load. The reader clicks a section heading to expand it. Quarto remembers which
sections are open as the user navigates between pages (via the Bootstrap collapse
component it uses internally).

Use `collapse-level: 2` if you want only deeper nesting collapsed and top-level
sections to remain open.

---

## Change 3 — Session label format in `generate_quarto_yml.py`

If the project uses a generator script to build `_quarto.yml` from the session
filenames, update the label function so changes survive regeneration.

Session files follow the naming convention:
```
{skill}-{arg}-{version}-{student}-{model}-session{n}.md
```

The `session_text` helper strips the skill prefix and returns the rest as the sidebar
label, which gives `arg-version-student-model-sessionN`:

```python
def session_text(stem, skill_prefix):
    # Strip skill prefix — everything remaining is arg-version-student-model-sessionN
    return stem[len(skill_prefix):].lstrip("-")
```

Also add the two sidebar options to the generator's output so they are not lost on the
next regeneration:

```python
lines += [
    "    - id: sessions",
    '      title: "Sessions"',
    "      style: docked",
    "      collapse-level: 1",   # ← add
    "      contents:",
    ...
]

lines += [
    "    grid:",
    "      sidebar-width: 400px",  # ← add
    "      body-width: 2000px",
    ...
]
```

---

## Change 4 — Consolidate all generators into `generate_quarto_yml.py`

### The problem

Generator scripts were scattered across source folders:

```
skills_sessions/generate_sessions.py   → wrote quarto_docs/sessions.json
plan/generate_plans.py                 → wrote quarto_docs/plans.json
lca_analysis/generate_analyses.py      → wrote quarto_docs/analyses.json
quarto_docs/generate_quarto_yml.py     → wrote quarto_docs/_quarto.yml
```

This created two problems:

1. **Confusion about when to run them.** Having a script called
   `skills_sessions/generate_sessions.py` sitting next to session transcripts made it
   look like a tool to run whenever a session was saved. The `CLAUDE.md` file even
   contained the instruction "After saving a session file, always run:
   `python3 skills_sessions/generate_sessions.py`" — causing every AI assistant reading
   those instructions to run the generator unnecessarily on every session save.

2. **Multiple entry points.** Any LLM reading the project could find and run any of the
   four scripts independently, producing partial or inconsistent output.

### The fix

Merge the logic of all three external scripts into `generate_quarto_yml.py` and delete
the external scripts. The `quarto_docs/` directory is now the single home for everything
that feeds the quarto build. Nothing outside it needs to be run.

Add `json` and `sys` to the imports at the top of `generate_quarto_yml.py`, then append
these two sections at the bottom:

```python
import json, re, sys

# --- sessions.json ---
sessions_json = []
for md in sorted(SESSIONS_DIR.glob("**/*.md")):
    lines_md = md.read_text(encoding="utf-8").split("\n")
    m = re.match(r"^#\s+/(\S+)(?:\s+(\S+))?", lines_md[0])
    if not m:
        continue
    skill_slug = m.group(1)
    case_raw   = m.group(2)
    meta = {}
    for line in lines_md[1:10]:
        mm = re.match(r"^\*\*([^*]+):\*\*\s*(.+)", line)
        if mm:
            meta[mm.group(1).strip().lower().replace(" ", "_")] = mm.group(2).strip()
    n_match = re.search(r"session(\d+)", md.stem)
    sessions_json.append({
        "file":      str(md.relative_to(SESSIONS_DIR)),
        "command":   f"/{skill_slug}" if not case_raw else f"/{skill_slug} {case_raw}",
        "skill":     skill_slug,          # format as needed
        "caseStudy": case_raw,
        "student":   meta.get("student", "").capitalize(),
        "model":     meta.get("model", ""),
        "version":   meta.get("skill_version", ""),
        "n":         int(n_match.group(1)) if n_match else 1,
    })
(QUARTO_DIR / "sessions.json").write_text(json.dumps(sessions_json, indent=2))

# --- plans.json ---
plans_json = []
for md in sorted(PLANS_DIR.glob("PLAN_*.md")):
    lines_md = md.read_text(encoding="utf-8").split("\n")
    title = next(
        (re.match(r"^#\s+(.+)", l).group(1) for l in lines_md[:5] if re.match(r"^#\s+", l)),
        md.stem,
    )
    plans_json.append({"file": md.name, "title": title})
(QUARTO_DIR / "plans.json").write_text(json.dumps(plans_json, indent=2))
```

Then delete the three external scripts:

```bash
rm skills_sessions/generate_sessions.py
rm plan/generate_plans.py
rm lca_analysis/generate_analyses.py
```

Update the Makefile's `regenerate` target to a single line:

```makefile
regenerate:
	python3 generate_quarto_yml.py
```

### Rule to add to CLAUDE.md

Remove any instruction that says to run a generator script after saving a session or
editing a skill. Replace it with:

> **Do not run any generator scripts after saving a session file.** The generators run
> automatically as part of `make` inside `quarto_docs/`. Running them manually at other
> times is unnecessary and should be avoided.

---

## When generators run

| Action | Generator runs | Quarto renders |
|---|---|---|
| Edit a skill or session file | No | No |
| `make` in `quarto_docs/` | Yes | Yes |
| `git commit` / `git push` | No | No |

The generator is fast (under one second). The render is slow (30–60 s for a large site).
Keep them separate so committing a typo fix does not force a full render.

---

## Summary of files changed

| File | Change |
|---|---|
| `_quarto.yml` | Added `sidebar-width: 400px` and `collapse-level: 1` |
| `quarto_docs/generate_quarto_yml.py` | Absorbed `sessions.json` and `plans.json` generation; updated `session_text()`; added sidebar-width and collapse-level to generated YAML |
| `quarto_docs/Makefile` | Reduced `regenerate` target to a single `python3 generate_quarto_yml.py` call |
| `skills_sessions/generate_sessions.py` | Deleted — logic merged into `generate_quarto_yml.py` |
| `plan/generate_plans.py` | Deleted — logic merged into `generate_quarto_yml.py` |
| `lca_analysis/generate_analyses.py` | Deleted — not needed for quarto docs |
| `custom.css` | Removed leftover drag-handle CSS |
| `sidebar-tweaks.html` | Removed old broken resize JavaScript; kept `.md` link fixer |
| `CLAUDE.md` | Removed instruction to run `generate_sessions.py` after saving a session |
