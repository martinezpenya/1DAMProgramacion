# Taller UD09_02: Scene Builder, ScenicView y FXMLManager


## Introducción

En el desarrollo de aplicaciones con JavaFX, la eficiencia y la claridad en la creación de interfaces gráficas son fundamentales. Herramientas  como **SceneBuilder** permiten diseñar interfaces de  usuario de manera visual y rápida, arrastrando y soltando componentes,  lo que facilita la creación de layouts complejos sin necesidad de  escribir manualmente todo el código FXML. Por otro lado, **ScenicView** es una herramienta invaluable para depurar y analizar la estructura de  la interfaz gráfica en tiempo de ejecución, permitiendo identificar  problemas de diseño o rendimiento. Finalmente, **FXMLManager** ayuda a gestionar y organizar los archivos FXML, promoviendo un código  más modular y mantenible. Juntas, estas herramientas integradas en  IntelliJ IDEA optimizan el flujo de trabajo, permitiendo a los  desarrolladores centrarse en la lógica de la aplicación mientras  mantienen un diseño de interfaz limpio y funcional.

## SceneBuilder

Scene Builder es una alternativa orientada al diseño que puede ser más productiva. Además es multiplataforma y está disponible para GNU/Linux, Windows y Mac. Scene Builder funciona con el ecosistema JavaFX: controles oficiales, proyectos comunitarios y ofertas de Gluon que incluyen [Gluon Mobile](https://gluonhq.com/products/mobile), [Gluon Desktop](https://gluonhq.com/products /escritorio) y [Gluon CloudLink](https://gluonhq.com/products/cloudlink).

El diseño de la interfaz de usuario *drag&amp;drop* permite una iteración rápida. La separación de los archivos de diseño y lógica permite que los miembros del equipo se concentren rápida y fácilmente en su capa específica de desarrollo de aplicaciones.

Scene Builder es gratuito y de código abierto, pero cuenta con el respaldo de Gluon. Están disponibles [ofertas de soporte comercial](https://gluonhq.com/services), que incluyen [formación](https://gluonhq.com/services/training) y [servicios de consultoría personalizados](https://gluonhq.com /servicios/consultoría).

Descarga e información: https://gluonhq.com/products/scene-builder/

![](assets/SceneBuilder1.png)

![](assets/SceneBuilder2.png)

### Configurar en `IntelliJ` la localización de `SceneBuilder`

Con el fin de que cuando se abra un archivo `FXML` desde `NetBeans` se muestre directamente con la herramienta `SceneBuider`, se debe indicar en la configuración de NetBeans en qué carpeta se encuentra `SceneBuider`.

En el artículo Using [Scene Builder with IntelliJ IDEA](https://docs.oracle.com/javase/8/scene-builder-2/work-with-java-ides/sb-with-intellij.htm#JSBID102) de la web de Oracle se puede obtener también información sobre los pasos a seguir.

SceneBuilder se encuentra instalada por defecto en la carpeta `C:\Users\TU_USUARIO\AppData\Local\SceneBuilder\SceneBuilder.exe` (en Windows), tambien es posible usar esta aplicación en Mac o Linux. Lo más importante es que conozcas la ubicación del ejecutable y lo configures en IntelliJ:

![Path del SceneBuilder en IntelliJ](assets/SceneBuilderPathIntelliJ.png)

Puedes acceder a las opciones de configuración de NetBeans en el menú `Settings` -> `Languages & Frameworks`-> `JavaFx`. Ahí accede a la sección `Path to SceneBuilder` y escribe la ruta donde se encuentre el ejecutable de SceneBuilder (en la imágen superior tienes el ejemplo de mi máquina linux).

## `ScenicView`

Scenic View es una aplicación `JavaFX` diseñada para simplificar la comprensión del estado actual del gráfico de escena de su aplicación y también para manipular fácilmente las propiedades del gráfico de escena sin tener que seguir editando su código. Esto le permite encontrar errores y hacer que las cosas sean perfectas sin tener que hacer el baile de compilación, verificación y compilación.

![Scenic View](assets/ScenicView.png)

### Descargar e instalar `ScenicView`

Puedes descargar la versión adecuada para tu sistema operativo desde https://github.com/JonathanGiles/scenic-view

En realidad ScenicView se distribuye como una aplicación portable. Eso quiere decir que no es necesario instalarla, sino directamente ejecutar la aplicación desde la carpeta `bin` según el sistema operativo en el que nos encontremos.

### Usar `ScenicView`

Para examinar nuestra aplicación `JavaFX` con `ScenicView`, debemos en primer lugar ejecutar la aplicación `ScenicView`:

![Buscando aplicación JavaFX](assets/ScenicView2.png)

Una vez ejecutada la aplicación comienza a buscar aplicaciones que se esten ejecutando y que usen `JavaFX`.

En este punto solo queda que ejecutemos nuestra aplicación `JavaFX` (por ejemplo `HolaFX`) y `ScenicView` detectará la aplicación y nos mostrará toda su información y nos permitirá realizar modificaciones:

![Screenshot_20230416_104253](assets/ScenicView3.png)



## `FXMLManager`

**`FXMLManager`** ayuda a gestionar y organizar los archivos FXML. 

Para instalar `FXMLManager` solo debes ir al apartado `Plugins` de IntelliJ y buscar en el `Market` el nombre "`FXMLManager`" y marcarlo para instalar.

Nos permite añadir/eliminar código al controlador a partir de las modificaciones que realizamos a la vista con el `SceneBuilder`.

Una vez realizadas las modificaciones en nuestra vista (y guardados los cambios), solo tenemos que pulsar el botón derecho sobre el fichero `*.fxml` correspondiente y elegir la opción "**Update Controller from FXML**".

Esto hará que se añadan las etiquetas `@FXML` con todos los componentes y métodos definidos en la vista.

## Videos relacionados

- https://www.youtube.com/playlist?list=PLNjWMbvTJAIjLRW2qyuc4DEgFVW5YFRSR
- https://www.youtube.com/playlist?list=PLaxZkGlLWHGUWZxuadN3J7KKaICRlhz5-

## Tarea

Sigue esta guía para instalar en tu ordenador `SceneBuilder`, `ScenicView` y `FXMLManager`. 

Genera una memoria en pdf con capturas/explicaciones en las que se pueda ver en funcionamiento SceneBuilder (dede IntelliJ) y ScenicView en tu ordenador. `FXMLManager` lo usaremos en el siguiente Taller, pero puedes añadir capturas demostrando que lo has instalado como plugin.

Envía el archivo pdf a la tarea de Aules.