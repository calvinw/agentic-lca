"""
Scans lca_analysis/ for folders containing recipe_card.md and writes analyses.json.
Run from the repo root: python3 lca_analysis/generate_analyses.py
"""

import json, sys
from pathlib import Path

here = Path(__file__).parent


def format_name(folder_name):
    return folder_name.replace('_', ' ').title()


analyses = []

for recipe in sorted(here.rglob('recipe_card.md')):
    folder = recipe.parent
    rel    = folder.relative_to(here.parent)   # e.g. lca_analysis/cotton_shirt
    name   = format_name(folder.name)
    results_file = folder / 'lca_results.md'

    analyses.append({
        'folder':      str(rel),
        'name':        name,
        'recipe':      str(rel / 'recipe_card.md'),
        'results':     str(rel / 'lca_results.md') if results_file.exists() else None,
    })

out = here / 'analyses.json'
out.write_text(json.dumps(analyses, indent=2), encoding='utf-8')
print(f'analyses.json: wrote {len(analyses)} analyses', file=sys.stderr)
