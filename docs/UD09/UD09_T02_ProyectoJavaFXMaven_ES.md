# Taller UD09_03: Proyecto JavaFX (con Maven)
## Crea un proyecto de JavaFx (con Maven)

Cuando creas un proyecto en Intellij, el mismo IDE ofrece un tipo de proyecto JavaFx: 

![Proyecto JavaFX, paso 1](assets/javafxmaven1.png)

!!! warning "Importante"
    Fíjate que al elegir el tipo de proyecto JavaFX a la parte derecha se selecciona el gestor de librerías Maven.
    Más adelante veremos como gestionar manualmente Maven, de momento dejaremos que IntelliJ genere el projecto Maven para JavaFx por nosotros.

Solo debes fijarte en escribir tu nombre y apellidos como en la imagen y seleccionar la versión 21 del jdk.

En la siguiente ventana debes marcar al menos estas dos opciones:

![Proyecto JavaFX, paso 2](assets/javafxmaven2.png)

Y por último pulsar el botón [Create]

Si esperas unos segundos aparecerá una notificación en la parte inferior derecha:

![Proyecto JavaFX, paso 3](assets/javafxmaven3.png)

Debes elegir la opción Load Maven Project, y esperar a que procese las dependencias solicitadas.



Estructura del proyecto JavaFx recien creado con el asistente de IntelliJ:

![Proyecto JavaFX, paso 4](assets/javafxmaven4.png)

En la imágen anterior puedes encontrar:

1. fichero `pom.xml` que gestiona las dependencias del proyecto maven.
2. `HelloApplication` clase que contiene el main de la aplicación JavaFx
3. `HelloController` clase con el controlador de la aplicación
4. `hello-view.fxml` archivo que contiene el formulario (vista) de la apliación

El proyecto sigue el patrón MVC que hemos visto en teoria, solo que es tan simple que no tiene ningún Modelo.

## Modificar el formulario con `SceneBuilder`

Si has configurado correctamente `SceneBuilder` en tu ordenador para usarlo desde IntelliJ, deberias poder pulsar con el botón derecho del ratón sobre el archivo (4) (`hello-view.fxml`) y elegir la opción `Abrir en SceneBuilder`:

![Proyecto JavaFX, Scene Builder](assets/javafxmavenSceneBuilder.png)

## Usa `FXMLManager`

Ahora, vamos a añadir cualquier componente a nuestra interfaz (preferiblemente mediante `SceneBuilder`), en nuestro caso, por ejemplo, otro botón (al que llamaremos "mola":

![Proyecto JavaFX, paso 5](assets/javafxmaven5.png)

Ahora nuestra vista tiene un componente más que nuestro controlador, y aquí es donde entra en acción `FXMLManager` ya que en lugar de estar pendientes de ir añadiendo nuestras modificaciones en la Vista a nuestro Controlador, `FXMLManager` se encargará de gestionarlo.

Hacemos clic derecho sobre el archivo `hello-view.fxml` y elegimos la opción:

![Proyecto JavaFX, paso 6](assets/javafxmaven6.png)

Ahora si abrimos de nuevo el fichero HelloController.java aparte del botón hello (que ya aparecia anteriormente) aparecerá el nuevo boton "mola":

![Proyecto JavaFX, paso 7](assets/javafxmaven7.png)

## Tarea

Usa el asistente de IntelliJ para crear proyecto `JavaFX` con maven. Modifica el formulario con `SceneBuilder` y cambia el texto del botón por tu nombre y apellidos. Añade un nuevo botón (con el nombre que quieras), pon el texto que quieras, y con `FXMLManager` añade el código correspondiente al `HelloController.java`.

Genera un zip con el proyecto de IntelliJ (o la carpeta src del IDE que uses). Envía el archivo zip a la tarea de Aules.