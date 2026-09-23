# Taller UD01_01: Instalación de Veyon en macOS

Este manual instala en tu portátil el componente **Veyon Service**, que permite que el profesor vea y controle tu pantalla durante la clase.

## Qué necesitas

- Tu portátil con macOS conectado a la red del aula.
- El fichero de **clave pública** que te ha entregado el profesor (por ejemplo `veyon-aula-profesor.pem`), descargado desde AULES o recibido por USB.

## 1. Descargar e instalar

1. Ve a [https://veyon.io/download](https://veyon.io/download) y descarga el instalador de macOS (`veyon-<versión>.pkg`), o descárgalo directamente desde [https://github.com/veyon/veyon/releases](https://github.com/veyon/veyon/releases).
2. Abre el `.pkg` y sigue el asistente de instalación.

!!! warning "Aviso de Gatekeeper"
    Al abrir el instalador o la app por primera vez, macOS puede avisar de que es de un "desarrollador no identificado". Ve a **Ajustes del Sistema → Privacidad y seguridad**, baja hasta el aviso sobre Veyon y pulsa **"Abrir de todos modos"**.

## 2. Conceder permisos del sistema (imprescindible)

macOS exige permiso explícito para que una app pueda ver o controlar la pantalla. Sin esto, el profesor no podrá verte aunque el servicio esté instalado:

1. Ve a **Ajustes del Sistema → Privacidad y seguridad → Grabación de pantalla**.
2. Activa el permiso para **Veyon Service**.
3. Ve también a **Ajustes del Sistema → Privacidad y seguridad → Accesibilidad**.
4. Activa el permiso para **Veyon Service** (necesario para que el profesor pueda controlar el ratón/teclado, no solo ver la pantalla).
5. Es posible que macOS te pida **cerrar sesión o reiniciar** para que los permisos surtan efecto.

## 3. Configurar la autenticación por clave

1. Abre **"Veyon Configurator"** (Launchpad o Aplicaciones).
2. Ve a la página **"Autenticación" (Authentication)** y en **Método** selecciona **"Autenticación mediante fichero de clave" (Key file authentication)**.
3. Ve a la página **"Claves de autenticación" (Authentication keys)**, pulsa **"Importar" (Import)**, ponle el mismo nombre que usó el profesor (`Docent`), y selecciona el fichero de clave pública que te ha dado el profesor.

## 4. Firewall de macOS

Si tienes activado el Firewall (**Ajustes del Sistema → Red → Firewall**), asegúrate de que no está bloqueando **Veyon Service**; si lo bloquea, permite las conexiones entrantes para esa aplicación.

## 5. Comprobación final

Avisa al profesor: tu equipo debería aparecer en su consola en unos segundos. Si no aparece, revisa que has concedido **ambos** permisos (Grabación de pantalla y Accesibilidad), ya que es la causa más común de fallo en macOS. Si el problema persiste, consulta la guía de [Resolución de problemas](UD01_T01_Veyon_Problemas.md) o avisa al profesor.

[⬅ Volver al taller T01](UD01_T01_Veyon.md)
