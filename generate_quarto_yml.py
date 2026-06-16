#!/usr/bin/env python3
"""Generate _quarto.yml from the current session and plan files."""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SESSIONS_DIR = ROOT / "skills_sessions"
PLANS_DIR = ROOT / "plan"
SKILLS_DIR = ROOT / ".skillshare" / "skills"


def skill_title(folder_name):
    words = folder_name.replace("-", " ").split()
    stop = {"and", "or", "of", "the", "a"}
    return " ".join(
        w if w in stop else (w.upper() if w == "lca" else w.title())
        for w in words
    )


def session_text(stem, skill_prefix):
    rest = stem[len(skill_prefix):].lstrip("-")
    # With case study arg: arg-vX.Y-student-model-sessionN
    m = re.match(r'^(.+?)-(v[\d.]+)-.+-(session\d+)$', rest)
    if m:
        arg, version, session = m.group(1), m.group(2), m.group(3)
        return f"{arg} {version} {session}"
    # Without arg (what-is-lca style): vX.Y-student-model-sessionN
    m = re.match(r'^(v[\d.]+)-.+-(session\d+)$', rest)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return rest


def plan_text(stem):
    return stem[5:] if stem.startswith("PLAN_") else stem


# Collect sessions grouped by skill folder
session_groups = {}
for folder in sorted(SESSIONS_DIR.iterdir()):
    if not folder.is_dir() or folder.name.startswith("."):
        continue
    md_files = sorted(folder.glob("*.md"))
    if md_files:
        session_groups[folder.name] = md_files

# Collect plan files
plan_files = sorted(PLANS_DIR.glob("PLAN_*.md"))

# Collect skill files and copy them into skills/ for rendering
SKILLS_OUT = ROOT / "skills"
SKILLS_OUT.mkdir(exist_ok=True)
skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
skill_copies = []
for f in skill_files:
    dest = SKILLS_OUT / f"{f.parent.name}.md"
    shutil.copy2(f, dest)
    skill_copies.append(dest)

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
        lines.append(f"    - {f.relative_to(ROOT)}")
lines.append("    - plan/index.md")
for f in plan_files:
    lines.append(f"    - {f.relative_to(ROOT)}")
lines.append("    - skills/index.md")
for f in skill_copies:
    lines.append(f"    - {f.relative_to(ROOT)}")

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
for folder_name, files in session_groups.items():
    lines.append(f'        - section: "{skill_title(folder_name)}"')
    lines.append(f"          contents:")
    for f in files:
        text = session_text(f.stem, folder_name)
        lines.append(f'            - text: "{text}"')
        lines.append(f"              href: {f.relative_to(ROOT)}")

lines += [
    "",
    "    - id: plans",
    '      title: "Plans"',
    "      style: docked",
    "      contents:",
    "        - text: Overview",
    "          href: plan/index.md",
]
for f in plan_files:
    lines.append(f'        - text: "{plan_text(f.stem)}"')
    lines.append(f"          href: {f.relative_to(ROOT)}")

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
    raw_url = f"https://raw.githubusercontent.com/calvinw/agentic-lca/main/{src.relative_to(ROOT)}"
    lines.append(f'        - text: "{label}"')
    lines.append(f"          href: {copy.relative_to(ROOT)}")
    lines.append(f'        - text: "(.md version)"')
    lines.append(f"          href: {raw_url}")

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

out = ROOT / "_quarto.yml"
out.write_text("\n".join(lines))
n_sessions = sum(len(v) for v in session_groups.values())
print(f"_quarto.yml written — {n_sessions} sessions, {len(plan_files)} plans.")
