# AGENTS.md — 1DAM Programació

MkDocs Material documentation site for a Spanish programming course (Java, OOP, JavaFX, DB).
Deployed at: https://martinezpenya.es/1DAMProgramacion/

## Commands

| Action | Command |
|---|---|
| Dev server (hot-reload) | `mkdocs serve` |
| Build static site | `mkdocs build` |
| Build PDF | `mkdocs build` (output: `docs/Libro.pdf`) |
| Unused asset scan | `python find_unused_assets.py` |

## Setup

```sh
python3 -m venv ~/virtual-envs/mkdocs
source ~/virtual-envs/mkdocs/bin/activate
pip install -r requirements.txt
```

Or run `./serve.sh` (automates venv + install + serve).

## Content structure

- All content written in Spanish from Spain (es-ES)
- All docs: `docs/UD{01..11}/` — Markdown (`.md`), Spanish language
- Images: `docs/UD*/assets/` per unit
- Site config: `mkdocs.yml` (nav, plugins, theme, extensions)
- Extra CSS: `docs/css/extra.css`
- Extra SASS (print): `extra_sass/style.css.scss`
- Cover templates: `templates/cover.html`, `templates/back_cover.html`
- Math: MathJax via `js/mathjax-config.js` + CDN, activated by `pymdownx.arithmatex`
- PDF button hook: `pdf_event_hook/__init__.py`

## Key plugins (mkdocs.yml)

- `mkdocs-video`, `mkdocs-git-revision-date-localized-plugin`, `mkdocs-minify-plugin`, `mkdocs-extra-sass-plugin`, `mkdocs-with-pdf`
- PDF output path: `docs/Libro.pdf`

## What NOT to do

- Do NOT add tests, linters, or CI — this is purely a documentation site
- Do NOT rename/move `UD*/assets/` folders without updating references
- Do NOT remove `use_directory_urls: false` from mkdocs.yml (URLs use `.html` extension)
