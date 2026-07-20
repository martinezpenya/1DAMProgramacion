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
