#!/usr/bin/env python3
"""Generate _quarto.yml from the current session and plan files."""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SESSIONS_DIR = ROOT / "skills_sessions"
PLANS_DIR = ROOT / "plan"


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
        return f"{arg.replace('_', ' ')} {version} {session}"
    # Without arg (what-is-lca style): vX.Y-student-model-sessionN
    m = re.match(r'^(v[\d.]+)-.+-(session\d+)$', rest)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    return rest.replace("_", " ")


ACRONYMS = {"lca", "lci", "lcia", "bafu", "traci", "lcas", "lcis"}
STOP = {"and", "or", "of", "the", "a", "to", "for"}

def plan_text(stem):
    rest = stem[5:] if stem.startswith("PLAN_") else stem
    words = rest.replace("_", " ").lower().split()
    out = []
    for w in words:
        if w in ACRONYMS:
            out.append(w.upper())
        elif w in STOP:
            out.append(w)
        else:
            out.append(w.title())
    return " ".join(out)


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

lines += [
    "",
    "website:",
    '  title: "LCA Learning Hub"',
    "  navbar:",
    "    left:",
    "      - text: Home",
    "        href: index.md",
    "      - text: Sessions",
    "        href: skills_sessions/index.md",
    "      - text: Plans",
    "        href: plan/index.md",
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
    "format:",
    "  html:",
    "    theme: cosmo",
    "    toc: true",
    "",
]

out = ROOT / "_quarto.yml"
out.write_text("\n".join(lines))
n_sessions = sum(len(v) for v in session_groups.values())
print(f"_quarto.yml written — {n_sessions} sessions, {len(plan_files)} plans.")
