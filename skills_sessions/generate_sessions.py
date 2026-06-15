"""
Scans skills_sessions/ for *.md files and writes sessions.json.
Run from the repo root:  python3 skills_sessions/generate_sessions.py
Or from inside the folder: python3 generate_sessions.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent


_ACRONYMS    = {'lca', 'svp'}
_CONJUNCTIONS = {'and', 'or', 'of', 'the', 'a', 'an', 'in', 'on', 'at', 'to'}


def format_skill(slug):
    """'what-is-lca' → 'What Is LCA'  |  'goal-and-scope' → 'Goal and Scope'"""
    words = slug.lstrip('/').split('-')
    result = []
    for i, w in enumerate(words):
        if w in _ACRONYMS:
            result.append(w.upper())
        elif i > 0 and w in _CONJUNCTIONS:
            result.append(w)           # keep lowercase mid-title
        else:
            result.append(w.capitalize())
    return ' '.join(result)


def format_case_study(raw):
    """'wool_yarn' → 'Wool Yarn'  |  'polyester_tshirt' → 'Polyester Tshirt'"""
    if not raw:
        return None
    return ' '.join(w.capitalize() for w in raw.replace('_', ' ').split())


def format_model(raw):
    """'sonnet-4-6' → 'Sonnet 4.6'  |  'deepseek-v4-flash' → 'Deepseek V4 Flash'"""
    parts = raw.split('-')
    result = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if re.match(r'^\d+$', p):
            # Collect consecutive pure-digit parts into one version string: 4, 6 → 4.6
            ver = [p]
            while i + 1 < len(parts) and re.match(r'^\d+$', parts[i + 1]):
                i += 1
                ver.append(parts[i])
            result.append('.'.join(ver))
        elif re.match(r'^v\d', p):
            result.append(p.upper())   # v4 → V4
        else:
            result.append(p.capitalize())
        i += 1
    return ' '.join(result)


sessions = []

for md in sorted(here.glob('*.md')):
    lines = md.read_text(encoding='utf-8').split('\n')

    # Line 1 must be the slash command: # /skill-name [case_study]
    m = re.match(r'^#\s+/(\S+)(?:\s+(\S+))?', lines[0])
    if not m:
        continue

    skill_slug = m.group(1)   # e.g. 'system-boundary'
    case_raw   = m.group(2)   # e.g. 'wool_yarn' or None

    # Parse **Key:** value lines from the header (lines 2–10)
    meta = {}
    for line in lines[1:10]:
        mm = re.match(r'^\*\*([^*]+):\*\*\s*(.+)', line)
        if mm:
            key = mm.group(1).strip().lower().replace(' ', '_')
            meta[key] = mm.group(2).strip()

    # Session number from filename
    n_match = re.search(r'session(\d+)', md.stem)
    n = int(n_match.group(1)) if n_match else 1

    # command is the raw slash-command notation: '/life-cycle-stages wool_yarn'
    command = f'/{skill_slug}' if not case_raw else f'/{skill_slug} {case_raw}'

    sessions.append({
        'file':      md.name,
        'command':   command,
        'skill':     format_skill(skill_slug),
        'caseStudy': format_case_study(case_raw),
        'student':   meta.get('student', '').capitalize(),
        'model':     format_model(meta.get('model', '')),
        'version':   meta.get('skill_version', ''),
        'n':         n,
    })

out = here / 'sessions.json'
out.write_text(json.dumps(sessions, indent=2), encoding='utf-8')
print(f'sessions.json: wrote {len(sessions)} sessions', file=sys.stderr)
