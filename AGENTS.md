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
| Check anchors (serve output) | Run `mkdocs serve` and review `INFO` lines for `contains a link ... but there is no such anchor` |

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

## PDF generation & Mermaid diagrams

The PDF (`docs/Libro.pdf`) is built by `mkdocs-with-pdf` from a combined
HTML document, rendered to PDF by WeasyPrint 62.3. `render_js` /
`headless_chrome_path` in `mkdocs.yml`'s `with-pdf` plugin config are
**intentionally commented out and must stay that way** — see the
incident below. Consequence: MathJax equations show as raw LaTeX in the
PDF instead of typeset math (a known, accepted limitation, not a bug).

Mermaid diagrams (`` ```mermaid `` fences) do **not** rely on
`mkdocs-with-pdf`'s Chrome path at all. `hooks.py`'s `on_page_content`
hook pre-renders each one to a PNG at build time instead, gated by the
`PRERENDER_MERMAID=1` env var:

| File | Function |
|---|---|
| `hooks.py:on_page_markdown()` | Replaces `{{ site_url }}` placeholder (always active) |
| `hooks.py:on_page_content()` | When `PRERENDER_MERMAID=1`, replaces `<pre class="mermaid"><code>` with an `<img>` pointing at a pre-rendered PNG |
| `hooks.py:_mmdc_render()` | Calls `mmdc -i in.mmd -o out.png -b transparent -s 1` via subprocess (mermaid-cli) |
| `hooks.py:_quote_labels()` | Fallback strategy: wraps `[label]` in `["label"]` for mmdc parser compatibility with special/accented characters |
| `puppeteer-config.json` | Points `mmdc`'s Puppeteer to the system Chrome (`/usr/bin/google-chrome`), skipping its own Chromium download |

Key details:
- Each diagram is written **once** to `<site_dir>/assets/mermaid/<sha256>.png` and referenced with a normal page-relative `<img src>` — not inlined as base64. `mkdocs-with-pdf` resolves that relative path to an absolute `file://` URL per page before combining articles, exactly like any other content image (verified against the installed `mkdocs_with_pdf/preprocessor/links/util.py`'s `replace_asset_hrefs`).
- **Keep mmdc's scale at `-s 1`.** Bumping it to `-s 2` for sharper images made one tall/narrow diagram (486×1114px) trigger a WeasyPrint layout bug that silently truncated the *entire* PDF to 26 pages with no error logged anywhere. Reproduced locally, confirmed fixed by reverting to `-s 1`. If diagram sharpness ever needs improving, test any scale change with a full local `mkdocs build` + page-count check on the resulting PDF before trusting it — this class of bug produces no warning.
- `mkdocs serve` (dev) also needs `PRERENDER_MERMAID=1` for Mermaid to render — `serve.sh` sets this automatically and installs `mermaid-cli` if missing (`PUPPETEER_SKIP_DOWNLOAD=true npm install -g @mermaid-js/mermaid-cli`).
- CI installs mermaid-cli and sets `PRERENDER_MERMAID=1` for the `mkdocs gh-deploy` step in `.github/workflows/ci.yml`.

### Incident: CI silently truncated the PDF to 118 pages (2026-07-21)

**Symptom:** local builds always produced a complete ~650-750 page
`Libro.pdf`. After enabling `render_js: true` + `headless_chrome_path`
in `mkdocs-with-pdf` (first to try rendering Mermaid via Chrome, later
kept for MathJax), the GitHub Actions build started silently producing
a **118-page PDF that just stops mid-book** — no error, exit code 0, a
structurally valid PDF with a self-consistent "118/118" page-count
footer.

**Ruled out, each with concrete evidence (not guesses):**
- *Dependency versions* — pinned every package (direct + transitive) to
  match the known-good local venv exactly; CI still truncated at 118.
- *Chrome's `--virtual-time-budget`* — raised 120s → 1200s (10x); zero
  effect on page count or on how long the step actually took.
- *The Python-side article-combining step* (`mkdocs-with-pdf`'s
  `on_post_page` / `on_post_build`) — instrumented with per-page
  logging; all 52 nav pages captured their full content correctly, in
  both size and content.
- *Mermaid's base64-inlined PNGs bloating the HTML* — switched to
  file-based `<img>` references; no change to the truncation point.
  (Also: UD02, where the truncation actually fell, has zero Mermaid
  diagrams — ruling out Mermaid as a factor for this specific incident.)
- *A WeasyPrint content-specific bug* — downloaded the *exact* combined
  HTML string CI fed into WeasyPrint (via a CI build artifact) and
  rendered it locally with the identical pinned WeasyPrint 62.3:
  **911 pages**, fully complete. The literal same input CI turns into
  118 pages renders fine elsewhere.
- *Memory exhaustion* — peak RSS in CI at the moment `render()` returned
  only 118 pages was ~2.2GB. Reproducing a real `MemoryError` locally
  required constraining virtual memory below ~2.5GB, and that failure
  mode is a loud crash with a traceback, not a silent truncation. CI
  never got near that ceiling.
- *Network access to `cdn.jsdelivr.net`* (Twemoji emoji icons WeasyPrint
  fetches during layout) — blocking DNS resolution to jsdelivr locally
  still produced 891 pages, not 118.

**Root cause: never conclusively identified.** `render.render()` itself
(WeasyPrint's layout call, confirmed via direct instrumentation) computed
118 pages in CI and 911 pages locally from byte-identical input, while
using comfortably less memory than would be needed to finish. This is a
genuine, unexplained difference in how WeasyPrint 62.3 paginates the same
content on the GitHub Actions runner vs. a normal dev machine — possibly
font availability/metrics, never confirmed.

**Resolution:** rather than keep chasing an elusive root cause, reverted
`render_js` / `headless_chrome_path` back to commented-out (their state
before this investigation began), which is confirmed to produce a
complete PDF in CI. MathJax-in-PDF and Mermaid-via-Chrome were both
abandoned. Mermaid was fixed separately via the PNG pre-render approach
described above, which does not depend on `render_js` at all and has
been verified end-to-end (locally and in CI) to produce a complete PDF.

**If `render_js` is ever re-enabled** (e.g. to attempt MathJax rendering
in the PDF again): test a full CI run immediately afterward and check
the *actual page count* of the resulting `docs/Libro.pdf` — a green CI
run does not mean the PDF is complete, since this failure mode produces
no error at all.

## Converting to Referenced Examples pattern

When creating a `## Ejemplos` section with numbered examples:
- Use `### EjemploXX` for headings — NO subtitle in the heading itself
  - Auto-anchor `#ejemploXX` only works if heading is exactly `### EjemploXX`
  - If you add a subtitle like `### EjemploXX — Título`, the anchor becomes `#ejemploXX-titulo` and breaks links
- Instead, add a one-line description **after** the heading (before the code block):
  ```
  ### EjemploXX

  Descripción breve del ejemplo.

  ```java
  ```
- Reference from theory: `[EjemploXX](#ejemploXX)`
- Add `{: #teoria-ejemploXX }` in the theory AFTER each reference paragraph (no blank line between paragraph and `{: }`)
  - For admonitions: place `{: #teoria-ejemploXX }` on an indented line inside the admonition
  - For headings: place `{: #teoria-ejemploXX }` on the same line as the heading
  - For lists: place `{: #teoria-ejemploXX }` on an indented line after the list item
- Add `[⬆ Volver a teoría](#teoria-ejemploXX)` in each example AFTER the last code block
- The `attr_list` extension is enabled in `mkdocs.yml`

## Pendientes / Ideas para futuras mejoras

- Añadir una sección sobre **impresión con formato y espacios reservados** (printf / String.format) para mostrar tablas alineadas sin que se corte la alineación. Ubicación por decidir.

### PDF: heading_shift y números de capítulo

Revisar la configuración de `with-pdf` en `mkdocs.yml`. Actualmente el plugin usa `heading_shift: true` (por defecto), lo que provoca que los archivos dentro de una sección del `nav` (Ejercicios, Talleres) vean sus encabezados rebajados un nivel. Para numerar correctamente en el PDF:
1. Desactivar `heading_shift: false` en `mkdocs.yml`.
2. En los Markdown de ejercicios/talleres, cambiar sus H1 (`# Título`) por H2 (`## Título`) para que queden al mismo nivel que `## Piensa como un programador`.
3. El H1 del archivo principal de teoría (`UDXX_ES.md`) debe contener el título completo (ej. `# UD01: Elementos de un programa informático`).

Pendiente de aplicar en todas las UDs.

### Propuestas de nuevos anexos

Anexos que se podrían crear para las unidades que actualmente no tienen ninguno:

| UD | Tema | Posibles anexos |
|---|---|---|
| **UD01** | Introducción / Elementos de un programa informático | **Anexo Git/GitHub** (comandos básicos, workflow, resolución de conflictos) |
| | | **Anexo IntelliJ IDEA** (instalación, atajos, debug, plugins, live templates) |
| | | **Anexo Tipos primitivos** (tabla completa de tipos, rangos, literales, conversiones) |
| **UD02** | Utilización de Objetos y Clases | **Anexo Scanner** (métodos, next/nextLine, delimitadores, manejo de errores) |
| | | **Anexo Math y Random** (funciones, trigonometría, seed, nextGaussian) |
| **UD03** | Estructuras de control y Excepciones | **Anexo Excepciones** (jerarquía, try-catch-finally, try-with-resources, excepciones personalizadas) |
| | | **Anexo Expresiones regulares** (Pattern/Matcher, sintaxis básica, validación) |
| **UD06** | Lectura y escritura de información | **Anexo java.nio.file** (Path, Files, walk, comparativa vs java.io) |
| | | **Anexo Serialización** (Serializable, ObjectOutputStream, ObjectInputStream, transient) |
| | | **Anexo CSV / JSON** (formato, parsing básico, Jackson/Gson) |
| **UD07** | Colecciones | **Anexo Comparator y Comparable** (ordenación natural vs personalizada, Comparator.comparing, thenComparing) |
| | | **Anexo Mapas** (HashMap, TreeMap, LinkedHashMap, concurrencia básica) |
| **UD08** | Composición, Herencia y Polimorfismo | **Anexo Genéricos** (clases, métodos, wildcards ? extends / ? super, type erasure) |
| | | **Anexo Records** (Java 14+, constructores compactos, equals/hashCode automáticos) |
| **UD09** | Interfaz gráfica (JavaFX) | **Anexo FXML** (estructura SceneBuilder, @FXML, controladores, fx:id) |
| | | **Anexo Layouts** (HBox, VBox, BorderPane, GridPane — cuándo usar cada uno) |
| | | **Anexo Eventos JavaFX** (ActionEvent, MouseEvent, KeyEvent, listeners lambda) |
| **UD10** | BB.DD. relacionales | **Anexo SQL Cheatsheet** (SELECT, INSERT, UPDATE, DELETE, JOIN, subconsultas) |
| | | **Anexo Connection Pool** (HikariCP vs DriverManager, configuración) |
| **UD11** | BB.DD. OO | **Anexo JPA** (anotaciones @Entity, @Id, @OneToMany, EntityManager) |
| | | **Anexo JPQL** (consultas, diferencias con SQL, parámetros) |

### Arreglos completados del patrón EjemploXX (3 condiciones)

- **UD03**: `<a id="ejemplo01">` → `{: #ejemplo01 }`. Creados 12 anchors individuales `{: #teoria-ejemplo12..23 }`. Back-links y auto-referencias corregidos. ✅
- **UD05**: Teoría anchors `01-08` creados, headings renombrados a `### Ejemplo01-08` con subtítulos. ✅
- **UD06**: Headings renombrados a `### Ejemplo01-10` con subtítulos, jerarquía aplanada, teoría anchors renumberados de `01-07` a `01-10`. ✅
- **UD07**: Anchors compartidos `08/09` y `10/11` divididos. Creados `teoria-ejemplo12/13/14`. Swaps `08↔09` y `10↔11` corregidos. ✅
- **UD08**: 19 headings `Ejemplo X.Y` → `### Ejemplo01-19` con subtítulos. Teoría anchors creados/renumberados. Back-links corregidos. ✅

## What NOT to do

- Do NOT add tests, linters, or CI — this is purely a documentation site
- Do NOT rename/move `UD*/assets/` folders without updating references
- Do NOT remove `use_directory_urls: false` from mkdocs.yml (URLs use `.html` extension)

## Downloadable files

- Place static files for students to download in `docs/UDXX/downloads/` (one folder per UD).
- Reference them in Markdown using the `{{ site_url }}` placeholder:
  ```markdown
  [filename]({{ site_url }}/UDXX/downloads/filename.ext)
  ```
- The `hooks.py` plugin replaces `{{ site_url }}` with the actual `site_url` from `mkdocs.yml` at build time, so the link works both on the web and avoids WeasyPrint anchor errors in the PDF.
