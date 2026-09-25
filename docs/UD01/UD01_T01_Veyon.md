# Taller UD01_01: Instalar Veyon para el control del aula

## ¿Qué es `Veyon`?

[Veyon](https://veyon.io) (*Virtual Eye On Networks*) es un software **libre, gratuito y de código abierto** para la gestión de aulas informáticas. Permite al profesor ver en tiempo real las pantallas de los equipos del alumnado, tomar el control de un equipo para ayudar, bloquear las pantallas durante una explicación o mostrar su propia pantalla a toda la clase.

Veyon se compone de varias piezas que se instalan por separado:

| Componente | Dónde se instala | Qué hace |
|---|---|---|
| **Veyon Master** | Solo en el equipo del profesor | Consola gráfica desde la que se ve y controla el aula. **Tú no la necesitas.** |
| **Veyon Service** | En tu portátil | Agente en segundo plano que permite que el profesor vea y controle tu equipo. |
| **Interception Driver** | En tu portátil | Controlador de bajo nivel necesario para que el profesor pueda bloquear el teclado y ratón durante una explicación. |
| **Veyon Configurator** | En tu portátil (se instala junto con Veyon Service) | Herramienta gráfica de configuración (claves, red, permisos). |

## ¿Por qué usamos `Veyon`?

Hasta ahora utilizábamos `NoMachine` para el control remoto de los equipos, pero ha pasado a ser **de pago**. `Veyon` es una alternativa libre y gratuita que, además, está pensada específicamente para aulas y funciona en **Linux, Windows y macOS**, por lo que cubre todos los portátiles que traéis a clase.

En clase lo utilizaremos para:

- **Pedir ayuda y resolver dudas**: el profesor puede ver tu pantalla (o tomar el control) sin tener que desplazarse hasta tu sitio.
- **Corregir las tareas diarias** directamente en tu equipo.
- **Bloquear las pantallas** durante las explicaciones para mantener la atención.
- **Mostrar la pantalla del profesor** (o la de un compañero) a toda la clase.
- **Supervisar los exámenes** que se realicen con el ordenador.

## ¿Cómo funciona? Seguridad y privacidad

Veyon utiliza un **par de claves asimétrico** (pública/privada), identificado con el nombre `Docent`:

- La **clave privada** se queda **únicamente en el equipo del profesor** y nunca se distribuye.
- La **clave pública** (el fichero `veyon-aula-profesor.pem`) es la que te proporcionará el profesor a través de AULES y tendrás que importar en tu portátil. Con ella, tu equipo puede comprobar que las peticiones de control vienen realmente del profesor y de nadie más. Repartirla no supone ningún riesgo: es pública por diseño.

Además, la comunicación se realiza por el puerto **TCP 11100** y la detección de equipos solo funciona **dentro de la red del aula**. Es decir, el profesor solo podrá conectarse a tu portátil mientras estés conectado a la red del instituto; **no podrá acceder cuando estés en casa**.

## Instalación según tu sistema operativo

Sigue el manual correspondiente a tu sistema operativo:

- 🐧 [Instalación de Veyon en Linux](UD01_T01_Veyon_Linux.md)
- 🪟 [Instalación de Veyon en Windows](UD01_T01_Veyon_Windows.md)
- 🍎 [Instalación de Veyon en macOS](UD01_T01_Veyon_macOS.md)

!!! tip "Consejo"
    Ten en cuenta que los navegadores pueden cambiar las extensiones de los archivos. Es conveniente activar las opciones de "ver extensiones de archivos" y "ver archivos ocultos" en tu gestor de archivos habitual y comprobar que la clave conserva la extensión `.pem`.

## Resolución de problemas

Si tu equipo no aparece en la consola del profesor o falla la autenticación, consulta la guía de [Resolución de problemas con Veyon](UD01_T01_Veyon_Problemas.md).

## Tarea

Debes enviar un archivo `*.pdf` a la plataforma de AULES que contenga:

1. Una captura del **Veyon Configurator** en la página **"Autenticación"**, donde se vea seleccionado el método **"Autenticación mediante fichero de clave"**.
2. Una captura de la página **"Claves de autenticación"**, donde se vea importada la clave pública `Docent`.
3. Una captura que demuestre que el profesor se ha podido conectar a tu equipo (por ejemplo, tu equipo visible en la consola del profesor o el aviso de conexión en tu portátil).

!!! danger "Obligatorio"
    Debes mantener `Veyon Service` instalado y activo, y permitir las conexiones por parte del profesor, para pedir ayuda y consultar dudas en clase, para corregir las tareas diarias y para realizar los exámenes.
