# Plan: Switch Documentation Site from MkDocs to Quarto

## What This Plan Covers

This plan describes switching the project documentation website from MkDocs
(what we set up recently) to **Quarto**, a markdown-based publishing system
that is more familiar and more flexible for academic and teaching contexts.

The goal is the same as before: a public website on GitHub Pages that shows
the skill sessions and project plans in a readable, searchable format.
The switch changes the tool doing the rendering — the content files (the
`.md` files in `skills_sessions/` and `plan/`) stay exactly where they are.

---

## Why Quarto Instead of MkDocs

- You already know Quarto — less friction when tweaking layouts or navigation
- Quarto renders standard `.md` files natively with no special syntax needed
- Quarto's website theme is cleaner for document-heavy sites
- Quarto has strong GitHub Actions support — no local rendering required
- No Python dependency for the docs build itself (Quarto is a standalone tool)

---

## Will Files Need to Be Pre-rendered Locally?

**No.** Quarto can render everything on GitHub's servers using GitHub Actions.
The workflow is:

1. You push a change to `main` (e.g., a new session file)
2. GitHub automatically installs Quarto on a cloud server
3. Quarto renders all the `.md` files to HTML
4. The rendered site is pushed to the `gh-pages` branch
5. GitHub Pages serves the site publicly

You never need to run Quarto locally unless you want a preview before pushing.
If you do want a local preview, it is one command: `quarto preview`.

---

## What Needs to Change

### Remove (no longer needed)
- `mkdocs.yml` — the MkDocs configuration file
- `requirements-docs.txt` — the Python package list for MkDocs
- `.github/workflows/deploy-docs.yml` — the MkDocs deploy action
- `site/` folder in `.gitignore` — replace with `_site/` (Quarto's output folder)

### Add
- `_quarto.yml` — Quarto's configuration file (replaces `mkdocs.yml`)
- `.github/workflows/deploy-quarto.yml` — new GitHub Action using `quarto-dev/quarto-actions`
- `index.qmd` or keep `docs/index.md` — the homepage

### Keep unchanged
- `docs/sessions` symlink → `../skills_sessions`
- `docs/plans` symlink → `../plan`
- All session `.md` files and plan `.md` files
- `generate_sessions.py`, `generate_plans.py` (still needed for the hand-rolled viewer)
- `skills_sessions/index.html` and root `index.html` (the hand-rolled viewer stays)

---

## The `_quarto.yml` Configuration

Quarto uses a single `_quarto.yml` file at the project root. For a website
with a sidebar showing Sessions and Plans, it looks like this:

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "LCA Learning Hub"
  navbar:
    left:
      - href: docs/index.md
        text: Home
      - href: docs/sessions/
        text: Sessions
      - href: docs/plans/
        text: Plans

format:
  html:
    theme: cosmo
    toc: true
```

Quarto's `cosmo` theme (or `flatly`, `litera`, `journal`) is clean and
readable. The `toc: true` adds a table of contents to each page automatically.

---

## The GitHub Actions Workflow

The deploy workflow for Quarto is simpler than MkDocs because the Quarto
team provides pre-built Actions:

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

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Regenerate manifest files
        run: |
          python3 skills_sessions/generate_sessions.py
          python3 plan/generate_plans.py

      - name: Publish to GitHub Pages
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Note: the `quarto-dev/quarto-actions/publish` step handles the `_site/`
build and the push to `gh-pages` in one go. No `mkdocs gh-deploy` needed.

---

## Navigation Structure

Quarto auto-discovers `.md` files inside the folders listed in `_quarto.yml`.
The sidebar for Sessions will show one entry per skill subfolder
(`functional-unit/`, `system-boundary/`, etc.) and Plans will list each
`PLAN_*.md` file. No manual file lists needed.

Files to exclude from Quarto rendering (same idea as MkDocs `exclude_docs`):

```yaml
project:
  type: website
  render:
    - docs/index.md
    - docs/sessions/**/*.md
    - docs/plans/PLAN_*.md
```

Using an explicit `render:` list is the cleanest way to tell Quarto exactly
which files to include, avoiding the other files in `docs/`.

---

## Steps to Implement

1. **Delete MkDocs files** — remove `mkdocs.yml`, `requirements-docs.txt`,
   `.github/workflows/deploy-docs.yml`

2. **Create `_quarto.yml`** — at the repo root with website config and
   explicit `render:` list for `docs/sessions/` and `docs/plans/`

3. **Create the deploy Action** — `.github/workflows/deploy-quarto.yml`
   using `quarto-dev/quarto-actions`

4. **Update `.gitignore`** — replace `site/` with `_site/`

5. **Push and watch the Action** — first run installs Quarto on GitHub's
   servers and publishes to `gh-pages`

6. **Switch GitHub Pages source** — if not already on `gh-pages` branch,
   change it in repo Settings → Pages

---

## Things to Watch Out For

- **Symlinks**: Quarto follows symlinks on Linux/Mac but behaviour can be
  inconsistent. If `docs/sessions` and `docs/plans` symlinks cause issues,
  the fallback is to list the real paths (`skills_sessions/` and `plan/`)
  directly in the `render:` list — no symlinks needed.

- **Image links in session files**: Session files link to diagrams using
  `../../skills_references/...`. These images exist on disk but are not
  inside the Quarto render tree. Quarto will render the page but the images
  will be broken. Fix later by either copying the SVGs into `docs/` or
  adding a `docs/skills_references` symlink.

- **`index.md` vs `index.qmd`**: Quarto prefers `.qmd` files but renders
  `.md` fine. The homepage can stay as `docs/index.md`.

- **No PDF output needed**: set `format: html` only in `_quarto.yml`. This
  keeps the build fast and avoids needing LaTeX installed on the GitHub runner.
