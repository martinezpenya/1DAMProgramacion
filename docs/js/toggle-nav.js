/* Botón para plegar/desplegar el nav izquierdo (solo escritorio) */
(function () {
  var CLAVE = "nav-oculto";
  var raiz = document.documentElement;

  var ICONO_PLEGAR =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">' +
    '<path d="M18.41 7.41 17 6l-6 6 6 6 1.41-1.41L13.83 12l4.58-4.59m-6 0L11 6l-6 6 6 6 1.41-1.41L7.83 12l4.58-4.59Z"/></svg>';
  var ICONO_DESPLEGAR =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">' +
    '<path d="M5.59 7.41 7 6l6 6-6 6-1.41-1.41L10.17 12 5.59 7.41m6 0L13 6l6 6-6 6-1.41-1.41L16.17 12l-4.58-4.59Z"/></svg>';

  function leer() {
    try { return localStorage.getItem(CLAVE) === "1"; } catch (e) { return false; }
  }

  function guardar(valor) {
    try { localStorage.setItem(CLAVE, valor ? "1" : "0"); } catch (e) { /* sin almacenamiento */ }
  }

  function alternar() {
    guardar(raiz.classList.toggle(CLAVE));
  }

  function crearBoton(clase, titulo, icono) {
    var boton = document.createElement("button");
    boton.type = "button";
    boton.className = clase;
    boton.title = titulo + " (m)";
    boton.setAttribute("aria-label", titulo);
    boton.innerHTML = icono;
    boton.addEventListener("click", alternar);
    return boton;
  }

  function montar() {
    var sidebar = document.querySelector(".md-sidebar--primary");
    if (!sidebar || document.querySelector(".boton-plegar-nav")) return;

    // Nav desplegado: botón junto al título del sitio, dentro del nav
    var titulo = sidebar.querySelector(".md-nav--primary > .md-nav__title");
    if (titulo) {
      titulo.appendChild(crearBoton("boton-plegar-nav", "Plegar menú", ICONO_PLEGAR));
    }

    // Nav plegado: tira estrecha a la izquierda con la flecha arriba
    var tira = crearBoton("tira-desplegar-nav", "Desplegar menú", ICONO_DESPLEGAR);
    sidebar.parentNode.insertBefore(tira, sidebar);
  }

  // Aplicar el estado guardado lo antes posible para evitar parpadeo
  if (leer()) raiz.classList.add(CLAVE);

  if (typeof document$ !== "undefined") {
    document$.subscribe(montar);
  } else {
    document.addEventListener("DOMContentLoaded", montar);
  }

  // Atajo de teclado: tecla "m"
  document.addEventListener("keydown", function (e) {
    if (e.key !== "m" || e.ctrlKey || e.metaKey || e.altKey) return;
    var destino = e.target;
    if (destino.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(destino.tagName)) return;
    alternar();
  });
})();
