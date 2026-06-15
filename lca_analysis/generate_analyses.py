"""
Scans lca_analysis/ for folders containing recipe_card.md and writes analyses.json.
Run from the repo root: python3 lca_analysis/generate_analyses.py
"""

import json, re, sys
from pathlib import Path

here = Path(__file__).parent
root = here.parent


def format_name(folder_name):
    return folder_name.replace('_', ' ').title()


def file_label(md_path, folder_name):
    """Derive a short readable label from a filename within its folder."""
    stem = md_path.stem                          # e.g. 'thredup_bestcase'
    # Strip folder-name prefix if filename starts with it
    prefix = folder_name + '_'
    if stem.startswith(prefix):
        stem = stem[len(prefix):]                # 'bestcase'
    return stem.replace('_', ' ')               # 'bestcase' / 'recipe card'


analyses = []

for recipe in sorted(here.rglob('recipe_card.md')):
    folder = recipe.parent
    rel    = folder.relative_to(root)            # lca_analysis/cotton_shirt
    name   = format_name(folder.name)
    group  = folder.parent.name if folder.parent != here else ''

    # Collect all .md files in this folder, sorted with recipe_card first
    mds = sorted(folder.glob('*.md'), key=lambda p: (p.name != 'recipe_card.md', p.name))
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

out = here / 'analyses.json'
out.write_text(json.dumps(analyses, indent=2), encoding='utf-8')
print(f'analyses.json: wrote {len(analyses)} analyses', file=sys.stderr)
