# Propuestas de Mejora — 1DAM Programación

> Archivo de referencia con todas las propuestas de mejora analizadas para el proyecto
> de apuntes de Programación (1º DAM). Clasificadas por estado de implementación.

---

## 🟢 Propuestas ACTIVAS (implementadas)

### A1. Admonitions en UD01 (coherencia con UD02–UD11)

**Descripción:** La UD01 es la única unidad que no utiliza admonitions (`!!!`). El resto del
proyecto sigue convenciones consistentes: `info "Definición"` para conceptos,
`danger "Atención"` para reglas críticas, `warning "Importante"` para notas relevantes,
`example "Ejemplo"` para código, etc. Se identificaron 39 oportunidades de inserción:

| Archivo | Inserciones |
|---|---|
| `UD01_ES.md` | 31 |
| `UD01_ejercicios_ES.md` | 1 |
| `UD01_T02_JDK&IDE.md` | 2 |
| `UD01_T04_Markdown.md` | 5 |

**Estado:** ✅ Implementado

---

### A2. Objetivos de aprendizaje al inicio de cada UD

**Descripción:** Añadir un bloque `!!! info "Al finalizar esta unidad serás capaz de..."`
con una checklist de objetivos alineados con los RA/CE del `index.md`. Ayuda a los
alumnos a saber qué esperar y a autoevaluarse.

**Archivos afectados:** `docs/UD{01..11}/*_ES.md` (11 archivos principales)

**Formato propuesto:**
```markdown
!!! info "Al finalizar esta unidad serás capaz de..."
    - [ ] Reconocer los elementos básicos de un programa informático
    - [ ] Identificar las fases del desarrollo de software
    - [ ] Utilizar el IDE para crear y ejecutar programas simples
```

**Estado:** ⏳ Pendiente

---

### A3. Resumen / Conceptos clave al final de cada UD

**Descripción:** Añadir una sección de resumen con los términos más importantes de la
unidad en formato tabla (`Concepto | Definición breve`). Facilita el repiro y la
preparación de exámenes.

**Archivos afectados:** `docs/UD{01..11}/*_ES.md`

**Formato propuesto:**
```markdown
!!! info "Resumen — Conceptos clave"
    | Concepto | Definición |
    |---|---|
    | Algoritmo | Conjunto de pasos finitos para resolver un problema |
    | Programa | Algoritmo codificado en un lenguaje de programación |
```

**Estado:** ⏳ Pendiente

---

### A4. Checklists de autoevaluación por UD

**Descripción:** Checklist al final de la unidad (o al final de los ejercicios) para que
el alumno marque su nivel de confianza en cada concepto.

**Formato propuesto:**
```markdown
### Autoevaluación
- [ ] Comprendo el concepto de clase y objeto
- [ ] Sé declarar atributos y métodos
- [ ] Puedo instanciar objetos
```

**Estado:** ⏳ Pendiente

---

### A5. Más diagramas Mermaid

**Descripción:** La extensión Mermaid ya está habilitada en `mkdocs.yml` pero solo se usa
12 veces en todo el proyecto. Ampliar su uso en:

| Unidad | Diagramas propuestos |
|---|---|
| UD03 | Flujo `if/else`, `switch`, bucles `for`/`while`/`do-while` |
| UD07 | Jerarquía del Collection Framework (`List`, `Set`, `Map`) |
| UD08 | Jerarquía de herencia, clases abstractas vs interfaces |
| UD10 | Flujo de conexión JDBC: `DriverManager` → `Connection` → `Statement` → `ResultSet` |

**Estado:** ⏳ Pendiente

---

### A6. Configuración de `mkdocs.yml`

**Descripción:** Varios ajustes menores en la configuración:

- **`navigation.indexes`** — permite que cada carpeta `UD*/` tenga una página índice
  automática, mejorando la navegación en el menú lateral
- **`content.tabs.link`** — mantiene sincronizada la pestaña activa entre páginas
  (útil para comparativas de código)
- **`magiclink`** — apunta actualmente a `squidfunk/mkdocs-material`. Cambiar a
  `martinezpenya/1DAMProgramacion` para que los enlaces a issues/PRs funcionen

**Estado:** ⏳ Pendiente

---

### A7. Ajustes CSS

**Descripción:**
- **Eliminar** la clase `.nocount` de `extra.css` (nunca se usa en los `.md`)
- **Descomentar** el fix de tablas 100% width para que las tablas anchas
  (ej: tabla de RA en `index.md`) no se vean comprimidas

**Estado:** ⏳ Pendiente

---

### A8. Consistencia en numeración de talleres

**Descripción:** UD09 y UD10 tienen T01 fuera del nav (archivo físico pero no listado),
mientras que UD11 no tiene T01. Esto crea discontinuidad numérica visible en el TOC.

**Propuesta:** Eliminar la entrada T01 del nav en UD09 y UD10, o explicar con una nota.
Añadir nota en UD11 indicando que no hay T01.

**Estado:** ⏳ Pendiente

---

### A9. Comprimir vídeos locales

**Descripción:** Los 11 vídeos `.mp4` en `docs/UD*/assets/` suman ~130MB. Cada uno pesa
entre 8 y 21MB. Usar `ffmpeg` con H.265 o H.264 (CRF 28) para reducir el tamaño
~50-70% sin pérdida apreciable. Beneficios: `git clone` más rápido, carga más rápida
del sitio.

**Estado:** ⏳ Pendiente

---

## 🔴 Propuestas DESCARTADAS (con justificación)

### D1. Eliminar archivos huérfanos del disco

- `docs/UD01/Introduction to Java Programming and Problem Solving.wav` (21 MB)
- `docs/UD09/UD09_T01_GitHubClassroom.md`
- `docs/UD10/UD10_T01_GitHubClassroom.md`
- `docs/UD05/assets/ContraReloj.java`
- `docs/UD10/assets/tablas.sql`

**Motivo:** El profesor decide mantenerlos por ahora. Posiblemente los .java y .sql
tengan utilidad futura, y los stubs de GitHub Classroom se conservan como referencia.

---

### D2. Dividir UD05 y UD08 en subpáginas

- UD05_ES.md: 139K / 2.412 líneas
- UD08_ES.md: 149K / 2.574 líneas

**Motivo:** El profesor prefiere mantenerlas como una sola página por ahora.

---

### D3. Navegación anterior/siguiente entre unidades

**Motivo:** El profesor considera que los enlaces entre unidades no tienen sentido,
probablemente porque cada unidad se estudia de forma independiente y secuencial
en el curso.

---

### D4. Indicadores de dificultad en ejercicios (🟢🟡🔴)

**Motivo:** El profesor no quiere etiquetar los ejercicios por dificultad.

---

### D5. Soluciones colapsables a ejercicios

**Motivo:** El profesor proporciona las soluciones más tarde a los alumnos que las
necesitan, no quiere que estén visibles en los apuntes.

---

### D6. Pestañas comparativas (`pymdownx.tabbed`)

**Descripción:** Usar pestañas para comparar `if/else` vs `switch`,
`ArrayList` vs `LinkedList`, `Statement` vs `PreparedStatement`, etc.

**Motivo:** Al generar el PDF, solo se muestra la primera pestaña, por lo que el
contenido comparativo se pierde en papel. Inviable mientras se use `mkdocs-with-pdf`.

---

### D7. Cambiar logo del PDF a ruta local

**Descripción:** `cover_logo` apunta a una URL remota
(`https://martinezpenya.es/1DAMProgramacion/assets/portada.png`).

**Motivo:** En local no funciona al generar el PDF en GitHub Actions. La URL remota
es necesaria para el pipeline de CI/CD.

---

### D8. Modificar sintaxis `[[]]` en `index.md`

**Descripción:** Las fórmulas de evaluación usan `[[1AVA]]`, `[[FEE]]`, `[[UD09_T01]]`,
etc., que es sintaxis de Obsidian. En MkDocs se renderizan como texto literal.

**Motivo:** El profesor usa este mismo archivo en Moodle, donde la sintaxis `[[]]`
es procesada correctamente por el sistema de calificaciones. No es un error.

---

## 🟡 Propuestas para el FUTURO (a considerar)

| # | Propuesta | Descripción |
|---|---|---|
| F1 | Meta-descripciones por página | Añadir descripciones personalizadas en cada `.md` para SEO y preview en redes sociales. |
| F2 | Enlazar assets huérfanos | `ContraReloj.java` y `tablas.sql` podrían enlazarse desde contenidos existentes. |
| F3 | Enriquecer stubs de GitHub Classroom | Añadir rúbricas, instrucciones detalladas y criterios de evaluación. |
| F4 | Transcripciones de vídeo | Añadir transcripciones o subtítulos para accesibilidad. |
| F5 | Versión descargable offline | Explorar el plugin `offline` de MkDocs para permitir descarga completa del sitio. |
| F6 | Consentimiento de cookies | El bloque `consent` en `mkdocs.yml` está comentado. Activarlo si se necesita GDPR. |
| F7 | Función de búsqueda en PDF | El PDF generado no tiene índice interactivo; explorar opciones con `mkdocs-with-pdf`. |
