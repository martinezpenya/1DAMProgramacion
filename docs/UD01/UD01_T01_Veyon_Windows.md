# Taller UD01_01: Instalación de Veyon en Windows

Este manual instala en tu portátil el componente **Veyon Service**, que permite que el profesor vea y controle tu pantalla durante la clase.

## Qué necesitas

- Tu portátil con Windows conectado a la red del aula.
- El fichero de **clave pública** que te ha entregado el profesor (por ejemplo `veyon-aula-profesor.pem`), descargado desde AULES o recibido por USB.

## 1. Descargar el instalador

1. Ve a [https://veyon.io/download](https://veyon.io/download) y descarga el instalador de Windows (`veyon-<versión>.exe`), o descárgalo directamente desde [https://github.com/veyon/veyon/releases](https://github.com/veyon/veyon/releases). No lo descargues de ningún otro sitio.
2. Ejecuta el instalador.

### Aviso normal de Windows al descargar/ejecutar el instalador

Es muy probable que veas alguno de estos avisos, tanto al descargar como al ejecutar el `.exe`:

- En el navegador: *"Este archivo no se descarga con frecuencia"* o *"Archivo potencialmente peligroso"*.
- Al ejecutarlo, **SmartScreen de Windows**: pantalla azul *"Windows ha protegido su PC"*, con el mensaje de que la app es de un editor no reconocido.

!!! warning "Esto no significa que el programa sea malware"
    Veyon es software libre y de código abierto; el aviso aparece porque su instalador no acumula suficientes descargas/reputación en los sistemas de SmartScreen de Microsoft (algo habitual en programas menos populares que no pagan por un certificado de firma de código EV), no porque haya sido detectado como malicioso. Puedes comprobarlo tú mismo: el propio Windows Defender (antivirus), al analizar el fichero, no lo marca como virus; solo SmartScreen avisa por baja reputación de descarga.

Para continuar de forma segura:

1. **Verifica primero que lo has descargado del sitio oficial**: la URL debe empezar por `https://veyon.io/` o `https://github.com/veyon/`. Si el aviso apareciera al descargarlo de cualquier otra web, ahí sí desconfía y no lo instales.
2. Si el navegador bloquea la descarga, pulsa **"Conservar"** / **"Mostrar más"** → **"Conservar de todos modos"**.
3. Si al ejecutarlo aparece la pantalla azul de SmartScreen, pulsa **"Más información"** y luego **"Ejecutar de todas formas"**.

## 2. Elegir los componentes a instalar (importante)

En la pantalla de selección de componentes verás tres casillas:

| Componente | ¿Marcar? | Motivo |
|---|---|---|
| **Veyon Service** | ✅ Sí | Es el agente que permite que el profesor vea/controle tu equipo. Imprescindible. |
| **Veyon Master** | ❌ No | Es la consola de control del aula: solo la necesita el profesor, no los alumnos. |
| **Interception Driver** | ✅ Sí | Controlador de bajo nivel necesario para que el profesor pueda bloquear el teclado/ratón (por ejemplo, durante una explicación en la que bloquea las pantallas). Sin él, esa función puede no funcionar bien. |

No aparece ninguna casilla para "Veyon Configurator": se instala automáticamente junto con Veyon Service, no hay que seleccionarlo aparte.

## 3. Configurar la autenticación por clave

1. Abre **"Veyon Configurator"** desde el menú Inicio (se instaló automáticamente junto con Veyon Service).
2. Ve a la página **"Autenticación" (Authentication)** y en **Método** selecciona **"Autenticación mediante fichero de clave" (Key file authentication)**.
3. Ve a la página **"Claves de autenticación" (Authentication keys)**, pulsa **"Importar" (Import)**, ponle el mismo nombre que usó el profesor (`Docent`), y selecciona el fichero de clave pública que te ha dado el profesor.

## 4. Firewall de Windows

El instalador suele crear automáticamente la regla de Firewall de Windows necesaria para `veyon-service.exe`. Verifícalo:

1. Abre **"Firewall de Windows Defender"** → **"Permitir una aplicación a través del Firewall"**.
2. Comprueba que **Veyon Service** aparece marcado, al menos para redes **privadas**.
3. Si no aparece o la conexión no funciona desde la consola del profesor, añade manualmente una regla de entrada para el puerto **TCP 11100**.

## 5. Comprobación final

El servicio se inicia automáticamente al arrancar Windows. Avisa al profesor: tu equipo debería aparecer en su consola en unos segundos. Si no aparece o pide autenticación repetidamente, revisa la guía de [Resolución de problemas](UD01_T01_Veyon_Problemas.md) o avisa al profesor.

[⬅ Volver al taller T01](UD01_T01_Veyon.md)
