"""
Scans plan/ for PLAN_*.md files and writes plan/plans.json.
Run from the repo root:  python3 plan/generate_plans.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
ROOT = here.parent


def format_title(stem):
    """'PLAN_FOR_EDUCATIONAL_SKILLS' → 'For Educational Skills'"""
    name = re.sub(r'^PLAN_', '', stem)
    return ' '.join(w.capitalize() for w in name.replace('_', ' ').split())


plans = []

for md in sorted(here.glob('PLAN_*.md')):
    lines = md.read_text(encoding='utf-8').split('\n')
    # Use first # heading as title if present, else derive from filename
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
