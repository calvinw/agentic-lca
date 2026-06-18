#!/usr/bin/env python3
"""Generate quarto_docs/ content and _quarto.yml from current project files."""

import json
import re
import shutil
import sys
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
    # Strip skill prefix — everything that remains is arg-version-student-model-sessionN
    return stem[len(skill_prefix):].lstrip("-")


def plan_text(stem):
    return stem[5:] if stem.startswith("PLAN_") else stem


# Clean and recreate output dirs
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
# Copy plan index
plan_index = PLANS_DIR / "index.md"
if plan_index.exists():
    shutil.copy2(plan_index, QUARTO_DIR / "plan" / "index.md")

# --- Copy skill files ---
SKILL_ORDER = [
    "what-is-lca", "system-boundary", "life-cycle-stages", "goal-and-scope",
    "functional-unit", "supply-chain", "technosphere-and-ecosphere",
    "life-cycle-inventory", "scaling-vector", "what-is-impact-assessment",
    "impact-characterization", "damage-characterization", "run-lca",
    "lca-from-url", "skill-creator",
]
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

# --- Write _quarto.yml (all paths are local to quarto_docs/) ---
def q(path):
    return str(path.relative_to(QUARTO_DIR))

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
    "      collapse-level: 1",
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
    "      sidebar-width: 400px",
    "      body-width: 2000px",
    "",
]

(QUARTO_DIR / "_quarto.yml").write_text("\n".join(lines))
n_sessions = sum(len(v) for v in session_groups.values())
print(f"quarto_docs/ generated — {n_sessions} sessions, {len(plan_copies)} plans.")

# ---------------------------------------------------------------------------
# sessions.json
# ---------------------------------------------------------------------------
_ACRONYMS     = {"lca", "svp"}
_CONJUNCTIONS = {"and", "or", "of", "the", "a", "an", "in", "on", "at", "to"}


def _fmt_skill(slug):
    words = slug.lstrip("/").split("-")
    out = []
    for i, w in enumerate(words):
        if w in _ACRONYMS:
            out.append(w.upper())
        elif i > 0 and w in _CONJUNCTIONS:
            out.append(w)
        else:
            out.append(w.capitalize())
    return " ".join(out)


def _fmt_case(raw):
    if not raw:
        return None
    return " ".join(w.capitalize() for w in raw.replace("_", " ").split())


def _fmt_model(raw):
    parts = raw.split("-")
    out = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if re.match(r"^\d+$", p):
            ver = [p]
            while i + 1 < len(parts) and re.match(r"^\d+$", parts[i + 1]):
                i += 1
                ver.append(parts[i])
            out.append(".".join(ver))
        elif re.match(r"^v\d", p):
            out.append(p.upper())
        else:
            out.append(p.capitalize())
        i += 1
    return " ".join(out)


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
        "skill":     _fmt_skill(skill_slug),
        "caseStudy": _fmt_case(case_raw),
        "student":   meta.get("student", "").capitalize(),
        "model":     _fmt_model(meta.get("model", "")),
        "version":   meta.get("skill_version", ""),
        "n":         int(n_match.group(1)) if n_match else 1,
        "_slug":     skill_slug,
    })

slug_order = {s: i for i, s in enumerate(SKILL_ORDER)}
sessions_json.sort(key=lambda s: (slug_order.get(s["_slug"], 999), s["file"]))
for s in sessions_json:
    del s["_slug"]

(QUARTO_DIR / "sessions.json").write_text(
    json.dumps(sessions_json, indent=2), encoding="utf-8"
)
print(f"sessions.json: wrote {len(sessions_json)} sessions", file=sys.stderr)

# ---------------------------------------------------------------------------
# plans.json
# ---------------------------------------------------------------------------
plans_json = []
for md in sorted(PLANS_DIR.glob("PLAN_*.md")):
    lines_md = md.read_text(encoding="utf-8").split("\n")
    title = None
    for line in lines_md[:5]:
        m = re.match(r"^#\s+(.+)", line)
        if m:
            title = m.group(1).strip()
            break
    if not title:
        name = re.sub(r"^PLAN_", "", md.stem)
        title = " ".join(w.capitalize() for w in name.replace("_", " ").split())
    plans_json.append({"file": md.name, "title": title})

(QUARTO_DIR / "plans.json").write_text(
    json.dumps(plans_json, indent=2), encoding="utf-8"
)
print(f"plans.json: wrote {len(plans_json)} plans", file=sys.stderr)

