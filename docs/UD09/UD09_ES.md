# Interfaz gráfica

![type:video](assets/UD09_Interfaz_grafica.mp4)

## Introducción

[JavaFX](https://openjfx.io/) fue desarrollado por Chris Oliver. Inicialmente, el proyecto se denominó Form Follows Functions (F3). Está destinado a proporcionar las funcionalidades más ricas para el desarrollo de aplicaciones GUI. Posteriormente, Sun Micro-systems adquirió el proyecto F3 como JavaFX en junio de 2005.

Sun Micro-systems lo anuncia oficialmente en 2007 en la Conferencia W3. En octubre de 2008, se lanzó JavaFX 1.0. En 2009, la corporación ORACLE adquiere Sun Micro-Systems y lanzó JavaFX 1.2. la última versión de JavaFX es JavaFX 23. 

JavaFX es una tecnología que nos permite crear aplicaciones de escritorio RIA (Ritch Internet Applications), esto es, aplicaciones web que tienen las características y capacidades de aplicaciones de escritorio, incluyendo aplicaciones multimedia interactivas que pueden ejecutarse en una amplia variedad de dispositivos. JavaFX está destinado a reemplazar a Swing como la biblioteca de GUI estándar para Java SE.

La biblioteca de JavaFX está escrita como una API de Java, las aplicaciones JavaFX pueden hacer referencia a APIs de código de cualquier biblioteca Java. Por ejemplo, las aplicaciones JavaFX pueden utilizar las bibliotecas de API de Java para acceder a las capacidades del sistema nativas y conectarse a aplicaciones de middleware basadas en servidor.

La apariencia de las aplicaciones JavaFX se pueden personalizar. Las Hojas de Estilo en Cascada (CSS) separan la apariencia y estilo de la lógica de la aplicación para que los desarrolladores puedan concentrarse en el código. Los diseñadores gráficos pueden personalizar fácilmente el aspecto y el estilo de la aplicación a través de CSS. Si se tiene un diseño de fondo de la web, o si se desea separar la interfaz de usuario (UI) y la lógica de servidor, entonces, se pueden desarrollar los aspectos de la presentación de la interfaz de usuario en el lenguaje de scripting FXML y utilizar el código de Java para la aplicación lógica. Si se prefiere diseñar interfaces de usuario sin necesidad de escribir código, entonces, utilizaremos JavaFXSceneBuilder . Al diseñar la interfaz de usuario con javaFX Scene Builder el crea código de marcado FXML que puede ser portado a un entorno de desarrollo integrado (IDE) de forma que los desarrolladores pueden añadir la lógica de negocio.

## Gráfico de escena

### Descripción general

Un gráfico de escena es una estructura de datos de árbol que organiza (y agrupa) objetos gráficos para una representación lógica más sencilla. También permite que el motor de gráficos represente los objetos de la manera más eficiente al omitir total o parcialmente los objetos que no se verán en la imagen final. La siguiente figura muestra un ejemplo de la arquitectura del gráfico de escena JavaFX.

![gráfico de escena](assets/scene_graph.jpg){width=400}

En la parte superior de la arquitectura hay un `Stage`. Una etapa es una representación JavaFX de una ventana de sistema operativo nativo. En un momento dado, un escenario puede tener un solo `Scene`adjunto. Una escena es un contenedor para el gráfico de escena JavaFX.

Todos los elementos en el gráfico de escena JavaFX se representan como `Node`objetos. Hay tres tipos de nudos: raíz, rama y hoja. El nodo raíz es el único nodo que no tiene un padre y está contenido directamente en una escena, que se puede ver en la figura anterior. La diferencia entre una rama y una hoja es que un nodo hoja no tiene hijos.

En el gráfico de escena, los nodos secundarios comparten muchas propiedades de un nodo principal. Por ejemplo, una transformación o un evento aplicado a un nodo padre también se aplicará recursivamente a sus hijos. Como tal, una jerarquía compleja de nodos se puede ver como un solo nodo para simplificar el modelo de programación. Exploraremos transformaciones y eventos en secciones posteriores.

En la siguiente figura se puede ver un ejemplo de un gráfico de escena "Hola Mundo".

![gráfico de escena específico](assets/specific_scene_graph.jpg){width=400}

Una posible implementación que producirá un gráfico de escena que coincida con la figura anterior es la siguiente.

**`E01_HolaMundo.java`**

```java
import javafx.application.Application;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class HolaMundo extends Application {

    private Parent createContent() {
        return new StackPane(new Text("Hola Mundo"));
    }

    @Override
    public void start(Stage stage) throws Exception {
        stage.setScene(new Scene(createContent(), 400, 400));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

El resultado de ejecutar el código se ve en la siguiente figura.

![](assets/HolaMundo.png){width=400}

Notas importantes:

- Un nodo puede tener como máximo 1 padre.
- Un nodo en el gráfico de escena "activo" (adjunto a una escena actualmente visible) solo se puede modificar desde el subproceso de la aplicación JavaFX.

### Transformaciones

Usaremos la siguiente aplicación como ejemplo para demostrar las 3 transformaciones más comunes.

**`E02_TransformApp.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

/**
 *
 * @author David Martínez (wwww.martinezpenya.es|ieseduardoprimo.es)
 */
public class E02_TransformApp extends Application {

    private Parent createContent() {
        Rectangle box = new Rectangle(100, 50, Color.BLUE);

        transform(box);

        return new Pane(box);
    }

    private void transform(Rectangle box) {
        //Aplicaremos las transformaciones aquí

        //Descomentar para traslación
        //box.setTranslateX(100);
        //box.setTranslateY(200);

        //Descomentar para escalado
        //box.setScaleX(1.5);
        //box.setScaleY(1.5);

        //Descomentar para rotación
        //box.setRotate(30);
    }

    @Override
    public void start(Stage stage) throws Exception {
        stage.setScene(new Scene(createContent(), 300, 300, Color.GRAY));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}

```

Ejecutar la aplicación dará como resultado la primera imagen (y si descomentamos por grupos, las siguientes).

| Sin transformaciones                                   | Traslación                                    | Escalado                                    | Rotación                                    |
| ------------------------------------------------------ | --------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| ![Sin transformaciones](assets/bluebox.png){width=150} | ![Traslación](assets/bluebox1.png){width=150} | ![Escalado](assets/bluebox2.png){width=150} | ![Rotacioń](assets/bluebox3.png){width=150} |

En JavaFX, puede ocurrir una transformación simple en uno de los 3 ejes: X, Y o Z. La aplicación de ejemplo está en 2D, por lo que solo consideraremos los ejes X e Y.

#### Traslación

En JavaFX y gráficos por computadora, `translate` significa moverse. Podemos trasladar nuestra caja en 100 píxeles en el eje X y 200 píxeles en el eje Y.

```java
box.setTranslateX(100);
box.setTranslateY(200);
```

#### Escala

Puede aplicar la escala para hacer un nodo más grande o más pequeño. El valor de escala es una relación. Por defecto, un nodo tiene un valor de escala de 1 (100%) en cada eje. Podemos agrandar nuestra caja aplicando una escala de 1.5 en los ejes X e Y.

```java
box.setScaleX(1.5);
box.setScaleY(1.5);
```

#### Rotación

La rotación de un nodo determina el ángulo en el que se representa el nodo. En 2D el único eje de rotación sensible es el eje Z. Giremos la caja 30 grados.

```java
box.setRotate(30);
```

### Manejo de eventos

Un evento notifica que ha ocurrido algo importante. Los eventos suelen ser lo "primitivo" de un sistema de eventos (también conocido como bus de eventos). Generalmente, un sistema de eventos tiene las siguientes 3 responsabilidades:

- `fire` (desencadenar) un evento,
- notificar `listeners` (a las partes interesadas) sobre el evento y
- `handle` (procesar) el evento.

El mecanismo de notificación de eventos lo realiza la plataforma JavaFX automáticamente. Por lo tanto, solo consideraremos cómo disparar (`fire`) eventos, escuchar (`listen`) eventos y cómo manejarlos (`handle`).

Primero, vamos a crear un evento personalizado.

**`E03_EventoUsuario.java`**

```java
import javafx.event.Event;
import javafx.event.EventType;

public class E03_EventoUsuario extends Event {

    public static final EventType<E03_EventoUsuario> ANY = new EventType<>(Event.ANY, "ANY");

    public static final EventType<E03_EventoUsuario> LOGIN_SUCCEEDED = new EventType<>(ANY, "LOGIN_SUCCEEDED");

    public static final EventType<E03_EventoUsuario> LOGIN_FAILED = new EventType<>(ANY, "LOGIN_FAILED");

    public E03_EventoUsuario(EventType<? extends Event> eventType) {
        super(eventType);
    }
    // cualquier otro atributo importante como la fecha, la hora...
}
```

Dado que los tipos de eventos son fijos, generalmente se crean dentro del mismo archivo de origen que el evento. Podemos ver que hay 2 tipos específicos de eventos: `LOGIN_SUCCEEDED`y `LOGIN_FAILED`. Podemos escuchar estos tipos específicos de eventos:

```java
Node node = ...
node.addEventHandler(UserEvent.LOGIN_SUCCEEDED, event -> {
    // handle event
});
```

Alternativamente, podemos manejar cualquier `UserEvent`:

```java
Node node = ...
node.addEventHandler(UserEvent.ANY, event -> {
    // handle event
});
```

Finalmente, podemos construir y disparar nuestros propios eventos:

```java
UserEvent event = new UserEvent(UserEvent.LOGIN_SUCCEEDED);
Node node = ...
node.fireEvent(event);
```

Por ejemplo, `LOGIN_SUCCEEDED`o `LOGIN_FAILED` podría activarse cuando un usuario intenta iniciar sesión en una aplicación. Según el resultado del inicio de sesión, podemos permitir que el usuario acceda a la aplicación o bloquearlo. Si bien se puede lograr la misma funcionalidad con una `if` declaración simple, hay una ventaja significativa de un sistema de eventos. Los sistemas de eventos se diseñaron para permitir la comunicación entre varios módulos (subsistemas) en una aplicación sin acoplarlos estrechamente. Como tal, un sistema de audio puede reproducir un sonido cuando el usuario inicia sesión. Por lo tanto, mantiene todo el código relacionado con el audio en su propio módulo. Sin embargo, no profundizaremos en los estilos arquitectónicos.

#### Eventos de entrada

Los eventos de teclado y ratón son los tipos de eventos más comunes utilizados en JavaFX. Cada `Node ` proporciona los llamados "métodos de conveniencia" para manejar estos eventos. Por ejemplo, podemos ejecutar algún código cuando se presiona un botón:

```java
Button button = ...
button.setOnAction(event -> {
    // button was pressed
});
```

Para mayor flexibilidad también podemos usar lo siguiente:

```java
Button button = ...
button.setOnMouseEntered(e -> ...);
button.setOnMouseExited(e -> ...);
button.setOnMousePressed(e -> ...);
button.setOnMouseReleased(e -> ...);
```

El objeto `e` anterior es de tipo `MouseEvent` y se puede consultar para obtener información diversa sobre el evento, por ejemplo, `x` posiciones `y`, número de clics, etc. Finalmente, podemos hacer lo mismo con las teclas:

```java
Button button = ...
button.setOnKeyPressed(e -> ...);
button.setOnKeyReleased(e -> ...);
```

El objeto `e ` aquí es de tipo `KeyEvent` y lleva información sobre el código de la tecla, que luego se puede asignar a una tecla física real en el teclado.

Veremos más ejemplos más adelante en este tema.

## Controles de la interfaz de usuario

### `Label`

La clase `Label` que reside en el paquete `javafx.scene.control` de la API de JavaFX se puede usar para mostrar un elemento de texto.

La etiqueta de la izquierda es un elemento de texto de color azul, que se auto-ajusta si cambiamos el tamaño de la ventana, la etiqueta del centro representa texto girado y la etiqueta de la derecha representa un texto con imagen, que además aumenta su tamaño cuando pasamos por encima.

![Label](assets/label.png){width=600}

La API de JavaFX proporciona tres constructores de la clase `Label` para crear etiquetas en su aplicación.


```java
//Creamos la etiqueta vacia
Label label1 = new Label();

//Creamos la etiqueta con texto
Label label2 = new Label("Etiqueta2");

//Creamos la etiqueta con imágen
Image image = new Image("UD09/label.png");
Label label3 = new Label("Search", new ImageView(image));
```

Una vez que haya creado una etiqueta, puede cambiar sus propiedades con los métodos;

- `setText(String text)` especifica el texto para la etiqueta.
- `setGraphic(Node graphic)`: especifica el icono gráfico,
- `setTextFill` especifica el color para pintar el elemento de texto de la etiqueta.
- `setGraphicTextGap` para establecer el espacio entre ellos.
- `setWrapText` para indicar si debe autoajustarse (`true`) o no (`false`)
- `setTextAlignment` puede variar la posición del contenido de la etiqueta dentro de su área de diseño
- `setContentDisplay` puede definir la posición del gráfico en relación con el texto aplicando el método y especificando una de las siguientes constantes `ContentDisplay`: `LEFT`, `RIGHT`, `CENTER`, `TOP`, `BOTTOM` .

Cuando se activa el evento `MOUSE_ENTERED` en la etiqueta, se establece el factor de escala de 1,5 para los métodos `setScaleX` y `setScaleY`. Cuando un usuario mueve el cursor del ratón fuera de la etiqueta y ocurre el evento `MOUSE_EXITED`, el factor de escala se establece en 1.0 y la etiqueta se representa en su tamaño original.


```java
label3.setOnMouseEntered((MouseEvent event) -> {
    label3.setScaleX(1.5);
    label3.setScaleY(1.5);
});

label3.setOnMouseExited((MouseEvent event) -> {
    label3.setScaleX(1);
    label3.setScaleY(1);
});
```

**`E05_Label.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class E05_Label extends Application {

    private Parent createContent() {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        //Creamos la etiqueta vacia
        Label label1 = new Label();
        //añadimos texto una vez creada
        label1.setText("Texto añadido después de la creación, autoajustable");
        //cambiamos la fuente y tamaño
        label1.setFont(new Font("Ubuntu", 12));
        //establecemos su color
        label1.setTextFill(Color.web("#0076a3"));
        //activamos la propiedad de autoajustable a true
        label1.setWrapText(true);
        //añadimos la etiqueta a la columna 0 fila 0
        grid.add(label1, 0, 0);

        //Creamos la etiqueta con texto
        Label label2 = new Label("Etiqueta2");
        grid.add(label2, 1, 0);
        label2.setFont(Font.font("FreeMono", 32));
        label2.setRotate(270);

        //Creamos la etiqueta con imágen
        Image image = new Image("UD09/label.png");
        Label label3 = new Label("Search", new ImageView(image));
        label3.setGraphicTextGap(20);
        grid.add(label3, 2, 0);

        label3.setOnMouseEntered((MouseEvent event) -> {
            label3.setScaleX(1.5);
            label3.setScaleY(1.5);
        });

        label3.setOnMouseExited((MouseEvent event) -> {
            label3.setScaleX(1);
            label3.setScaleY(1);
        });

        return grid;
    }

    @Override
    public void start(Stage stage) throws Exception {
        stage.setScene(new Scene(createContent(), 500, 200));
        stage.setTitle("Ejemplo con Label");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### `Button`

La clase `Button` disponible a través de la API de JavaFX permite a los desarrolladores procesar una acción cuando un usuario hace clic en un botón. La clase `Button` es una extensión de la clase `Labeled`. Puede mostrar texto, una imagen o ambos.

![Button](assets/button.png){width=400}

Puede crear un control `Button` en una aplicación JavaFX usando tres constructores de la clase Button como se muestra a continuación


```java
//Creamos el botón vacio
Button button1 = new Button();
//Creamos el botón con texto
Button button2 = new Button("Sí");
//Creamos el botón con texto e imágen
Image image = new Image("UD09/ok.png");
Button button4 = new Button("Aceptar", new ImageView(image));
```

La clase `Button` puede usar los siguientes métodos:

- `setText(String text)`: especifica el título de texto para el botón
- `setGraphic(Node graphic)`: especifica el icono gráfico
- `setOnAction`: La función principal de cada botón es producir una acción cuando se hace clic en él. En nuestro ejemplo cambiar el texto de un label.


```
button2.setOnAction((ActionEvent e) -> {
    label.setText("Aceptado");
});
```

Vemos cómo procesar un `ActionEvent`, de modo que cuando un usuario presiona button2 el título de texto de la etiqueta label se establece en "Aceptado".

Puede usar la clase `Button` para establecer tantos métodos de manejo de eventos como necesite para causar el comportamiento específico o aplicar efectos visuales.

Debido a que la clase `Button` amplía la clase `Node`, puede aplicar cualquiera de los efectos del paquete `javafx.scene.effect` para mejorar la apariencia visual del botón. En este caso añadimos una sobra al botón con imagen cuando pasamos el ratón sobre el.


```java
//Creamos el estilo de sombra
DropShadow shadow = new DropShadow();
//Añadimos la sombra cuando pasamos sobre el botón
button4.addEventHandler(MouseEvent.MOUSE_ENTERED, (MouseEvent e) -> {
    button4.setEffect(shadow);
});

//Eliminamos la sombra al salir del botón
button4.addEventHandler(MouseEvent.MOUSE_EXITED, (MouseEvent e) -> {
    button4.setEffect(null);
});
```

El siguiente paso para mejorar la apariencia visual de un botón es aplicar estilos CSS definidos por la clase `Skin`. Usar CSS en aplicaciones JavaFX 2 es similar a usar CSS en HTML, porque cada caso se basa en la misma especificación de CSS.

Puede definir estilos en un archivo CSS separado y habilitarlos en la aplicación usando el método `getStyleClass`. 

El fichero style.css:

```css
.button1{
    -fx-font: 22 ubuntu; 
    -fx-base: #b6e7c9;
}
```

La propiedad `-fx-font` establece el nombre y el tamaño de la fuente para el button1. La propiedad `-fx-base` anula el color predeterminado aplicado al botón.

Y desde java usamos:


```java
//Asociamos el fichero css a nuestra escena
scene.getStylesheets().add("UD09/style.css");
[...]
//establecemos la clase correspondiente del css
button1.getStyleClass().add("button1");
```

 Como resultado, el button1 es de color verde claro con un tamaño de texto mayor.

**`E06_Button.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.effect.DropShadow;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class E06_Button extends Application {

    private Parent createContent() {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER_LEFT);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        //Creamos el botón vacio
        Button button1 = new Button();
        //añadimos texto una vez creado
        button1.setText("Botón CSS");
        //establecemos la clase correspondiente del css
        button1.getStyleClass().add("button1");
        //añadimos el botón a la columna 0 fila 0 con colspan 3 y rowspan 1
        grid.add(button1, 0, 0, 3, 1);

        //Creamos el botón con texto
        Button button2 = new Button("Sí");
        grid.add(button2, 0, 1);
        Button button3 = new Button("No");
        grid.add(button3, 1, 1);
        //Añadimos el label que cambiará segun el botón presionado
        Label label = new Label("Aceptado");
        grid.add(label, 2, 1);

        //Creamos el botón con texto e imágen
        Image image = new Image("UD09/ok.png");
        Button button4 = new Button("Aceptar", new ImageView(image));
        grid.add(button4, 0, 2, 2, 1);

        //métodos para cambiar el label segun el botón pulsado
        button2.setOnAction((ActionEvent e) -> {
            label.setText("Aceptado");
        });

        button3.setOnAction((ActionEvent e) -> {
            label.setText("Denegado");
        });

        //Creamos el estilo de sombra
        DropShadow shadow = new DropShadow();
        //Añadimos la sombra cuando pasamos sobre el botón
        button4.addEventHandler(MouseEvent.MOUSE_ENTERED, (MouseEvent e) -> {
            button4.setEffect(shadow);
        });

        //Eliminamos la sombra al salir del botón
        button4.addEventHandler(MouseEvent.MOUSE_EXITED, (MouseEvent e) -> {
            button4.setEffect(null);
        });

        return grid;
    }

    @Override
    public void start(Stage stage) throws Exception {
        Scene scene = new Scene(createContent(), 300, 200);
        scene.getStylesheets().add("UD09/style.css");
        stage.setScene(scene);

        stage.setTitle("Ejemplo con Button");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### `RadioButton`

Un control `RadioButton` se puede seleccionar o deseleccionar. Por lo general, se combinan en un grupo donde solo se puede seleccionar un botón a la vez. 

Abajo se muestran tres capturas de pantalla del ejemplo `RadioButton`, en las que se agregan tres botones de opción a un grupo.

| Opción 1                                 | Opción 2                               | Opción 3                            |
| ---------------------------------------- | -------------------------------------- | ----------------------------------- |
| ![En coche](assets/coche.png){width=200} | ![En moto](assets/moto.png){width=200} | ![A pie](assets/pie.png){width=200} |

La clase `RadioButton` disponible en el paquete `javafx.scene.control` del SDK de JavaFX proporciona dos constructores con los que puede crear un botón de opción. 


```java
//Creamos el botón vacio
RadioButton rButton1 = new RadioButton();
//añadimos texto una vez creado
rButton1.setText("Coche");
//Creamos los RadioButton con texto
RadioButton rButton2 = new RadioButton("Moto");
```

Puede seleccionar explícitamente un botón de radio utilizando el método `setSelected` y especificando su valor como `true`. Si necesita verificar si un usuario seleccionó un botón de radio en particular, aplique el método `isSelected`.

Debido a que la clase `RadioButton` es una extensión de la clase `Labeled`, puede especificar no solo una leyenda de texto, sino también una imagen. Utilice el método `setGraphic` para especificar una imagen.


```java
//Añadimos las imágenes a los Radio Button
ImageView imageCoche = new ImageView("UD09/coche.png");
rButton1.setGraphic(imageCoche);
```

Los `RadioButton` se utilizan normalmente en un grupo para presentar varias opciones mutuamente excluyentes. El objeto `ToggleGroup` proporciona referencias a todos los botones de radio asociados con él y los administra para que solo se pueda seleccionar uno de los botones de radio a la vez. A continuación se muestra como se crea un grupo de alternancia y especifica qué botón debe seleccionarse cuando se inicia la aplicación.


```java
//Creamos el grupo de alternancia
final ToggleGroup grupo = new ToggleGroup();
rButton1.setToggleGroup(grupo);
rButton1.setSelected(true); //si queremos que la primera opción este marcada por defecto
rButton2.setToggleGroup(grupo);
rButton3.setToggleGroup(grupo);
```

Normalmente, la aplicación realiza una acción cuando se selecciona uno de los botones de opción del grupo. En este caso cambiará la imágen que acompaña al grupo de alternancia.


```java
//Añadimos una imágen que cambiara al cambiar la selección
ImageView image = new ImageView();
grid.add(image, 1, 0, 1, 3);

//añadimos el listener al grupo para que capture el evento cuando se cambie la selección
grupo.selectedToggleProperty().addListener(
        (ObservableValue<? extends Toggle> ov, Toggle old_toggle, Toggle new_toggle) -> {
            if (grupo.getSelectedToggle() != null) {
                image.setImage(new Image("UD09/" + grupo.getSelectedToggle().getUserData().toString() + ".png"));
            }
        });
```

Los datos de usuario se asignaron para cada botón de opción. El objeto `ChangeListener<Toggle>` verifica un conmutador seleccionado en el grupo. Utiliza el método `getSelectedToggle` para identificar qué botón de opción está actualmente seleccionado y extrae sus datos de usuario llamando al método `getUserData`. Luego, los datos del usuario se aplican para construir un nombre de archivo de imagen para cargar.

Por ejemplo, cuando se selecciona `rButton3`, el método `getSelectedToggle` devuelve "rButton3" y el método `getUserData` devuelve "coche" Por lo tanto, la imágen será "UD09/coche.png".

**`E07_RadioButton.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.beans.value.ObservableValue;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.RadioButton;
import javafx.scene.control.Toggle;
import javafx.scene.control.ToggleGroup;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class E07_RadioButton extends Application {

    private Parent createContent() {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER_LEFT);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        //Creamos el botón vacio
        RadioButton rButton1 = new RadioButton();
        //añadimos texto una vez creado
        rButton1.setText("Coche");
        //añadimos el RadioButton a la columna 0 fila 0 con colspan 3 y rowspan 1
        grid.add(rButton1, 0, 0);

        //Creamos los RadioButton con texto
        RadioButton rButton2 = new RadioButton("Moto");
        grid.add(rButton2, 0, 1);
        //Creamos un RadioButton con imágen
        RadioButton rButton3 = new RadioButton("A pie");
        grid.add(rButton3, 0, 2);

        //Añadimos las imágenes a los Radio Button
        //ImageView imageCoche = new ImageView("UD09/coche.png");
        //rButton1.setGraphic(imageCoche);
        //Creamos el grupo de alternancia
        final ToggleGroup grupo = new ToggleGroup();
        rButton1.setToggleGroup(grupo);
        //rButton1.setSelected(true); //si queremos que la primera opción este marcada por defecto
        rButton2.setToggleGroup(grupo);
        rButton3.setToggleGroup(grupo);

        //Añadimos un valor personalizado a cada control con el nombre de la imágen correspondiente
        rButton1.setUserData("coche");
        rButton2.setUserData("moto");
        rButton3.setUserData("pie");

        //Añadimos una imágen que cambiara al cambiar la selección
        ImageView image = new ImageView();
        grid.add(image, 1, 0, 1, 3);

        //añadimos el listener al grupo para que capture el evento cuando se cambie la selección
        grupo.selectedToggleProperty().addListener(
                (ObservableValue<? extends Toggle> ov, Toggle old_toggle, Toggle new_toggle) -> {
                    if (grupo.getSelectedToggle() != null) {
                        image.setImage(new Image("UD09/" + grupo.getSelectedToggle().getUserData().toString() + ".png"));
                    }
                });
                      
        return grid;
    }

    @Override
    public void start(Stage stage) throws Exception {
        Scene scene = new Scene(createContent(), 300, 200);
        stage.setScene(scene);

        stage.setTitle("Ejemplo RadioButton");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### `CheckBox`

Aunque las casillas de verificación se parecen a los `RadioButton`, no se pueden combinar en grupos de alternancia.

Más abajo se muestra una captura de pantalla de una aplicación en la que se usan tres casillas de verificación para habilitar o desactivar iconos en la barra de herramientas de una aplicación.

A continuación se crean tres casillas de verificación simples.


```java
//Creamos el CheckBox vacio
CheckBox check1 = new CheckBox();
//añadimos texto una vez creado
check1.setText("Coche");

//Creamos los CheckBox con texto
CheckBox check2 = new CheckBox("Moto");

//Hademos aparezca marcado por defecto
CheckBox check3 = new CheckBox("A pie");
check3.setSelected(true);
```

Una vez que haya creado una casilla de verificación, puede modificarla utilizando los métodos disponibles a través de las API de JavaFX. Por ejemplo el método `setText` define el título de texto de la casilla de verificación `check1`. El método `setSelected` se establece en `true` para que la casilla de verificación `check3` se seleccione cuando se inicie la aplicación.

La casilla de verificación puede estar definida o indefinida. Cuando está definido, puede seleccionarlo o deseleccionarlo. Sin embargo, cuando la casilla de verificación está indefinida, no se puede seleccionar ni deseleccionar. Se usa una combinación de los métodos `setSelected` y `setIndeterminate` de la clase `CheckBox` para especificar el estado de la casilla de verificación. En la tabla se muestran tres estados de una casilla de verificación en función de sus propiedades `INDETERMINADO` y `SELECCIONADO `.

| Valores de propiedad | Apariencia de la casilla de verificación |
| ---------------------------------------------- | -------------------------------------------------- ---------- |
| `INDETERMINADO` = **falso**<br />`SELECCIONADO` = **falso** | ![La casilla de verificación no está seleccionada.](assets/checkbox-state1.png) |
| `INDETERMINADO` =**falso**<br />`SELECCIONADO` = **verdadero** | ![La casilla de verificación está seleccionada.](assets/checkbox-state3.png) |
| `INDETERMINADO` = **verdadero**<br />`SELECCIONADO` = **verdadero/falso** | ![La casilla de verificación no está definida.](assets/checkbox-state2.png) |

Es posible que deba habilitar tres estados para las casillas de verificación en su aplicación cuando representan elementos de la interfaz de usuario que pueden estar en estados mixtos, por ejemplo, "Sí", "No", "No aplicable". La propiedad `allowIndeterminate` del objeto `CheckBox` determina si la casilla de verificación debe pasar por los tres estados: seleccionada, deseleccionada e indefinida. Si la variable es "verdadera", el control recorrerá los tres estados. Si es `falso`, el control recorrerá los estados seleccionado y deseleccionado. La aplicación descrita en la siguiente sección construye tres casillas de verificación y habilita solo dos estados para ellas.


```java
//Ahora crearemos los 3 checkboxes en un bucle y tendran 3 estados
final String[] nombres = new String[]{"Coche3", "Moto3", "Pie3"};
final CheckBox[] checkBox = new CheckBox[nombres.length];

for (int i = 0; i < nombres.length; i++) {
    final CheckBox cb = checkBox[i] = new CheckBox(nombres[i]);
    cb.setAllowIndeterminate(true);
    grid.add(cb, 1, i);
}
```

En la siguiente imagen se puede observar como la columna derecha de checkbox permite los 3 estados:

![CheckBox con tres estados](assets/checkbox.png){width=400}

**`E08_CheckBox.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class E08_CheckBox extends Application {

    private Parent createContent() {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER_LEFT);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        //Creamos el CheckBox vacio
        CheckBox check1 = new CheckBox();
        //Añadimos texto una vez creado
        check1.setText("Coche");
        //Añadimos el CheckBox a la columna 0 fila 0
        grid.add(check1, 0, 0);

        //Creamos los CheckBox con texto
        CheckBox check2 = new CheckBox("Moto");
        grid.add(check2, 0, 1);
        //Hademos aparezca marcado por defecto
        CheckBox check3 = new CheckBox("A pie");
        check3.setSelected(true);
        grid.add(check3, 0, 2);

        //Ahora crearemos los 3 checkboxes en un bucle y tendran 3 estados
        final String[] nombres = new String[]{"Coche3", "Moto3", "Pie3"};
        final CheckBox[] checkBox = new CheckBox[nombres.length];
        
        for (int i = 0; i < nombres.length; i++) {
            final CheckBox cb = checkBox[i] = new CheckBox(nombres[i]);
            cb.setAllowIndeterminate(true);
            grid.add(cb, 1, i);
        }

        return grid;
    }

    @Override
    public void start(Stage stage) throws Exception {
        Scene scene = new Scene(createContent(), 300, 200);
        stage.setScene(scene);

        stage.setTitle("Ejemplo CheckBox");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### `TextField` y `PasswordField`

Ahora veremos los componentes para campos de texto, la clase `TextField` implementa un control de interfaz de usuario que acepta y muestra la entrada de texto. Junto con otro control de entrada de texto, `PasswordField`, esta clase amplía la clase `TextInput`, una superclase para todos los controles de texto disponibles a través de la API de JavaFX.

![Ejemplo TextField y PasswordField](assets/textPasswordField.png){width=600}

Puede aplicar el método `setPrefColumnCount` de la clase `TextInput` para establecer el tamaño del campo de texto, definido como el número máximo de caracteres que puede mostrar a la vez.


```java
//Creamos el TextkField vacio
TextField textField1 = new TextField();
//Establecemos el número de caracteres que mostrará por defecto
textField1.setPrefColumnCount(10);
```

Puede crear un campo de texto campo con un dato de texto particular en él. Para crear un campo de texto con el texto predefinido:

```java
TextField tFComentario = new TextField();
//Establecemos el contenido por defecto del campo de texto
tFComentario.setText("Comentario por defecto");
//Seria lo mismo que haber creado el TextField de esta manera:
TextField tFComentario2 = new TextField("Comentario por defecto");
```

En lugar de añadir etiquetas para acompañar a los campos de texto en este fragmento de código se han añadido los subtítulos, que notifican a los usuarios qué tipo de datos deben ingresar en los campos de texto. El método `setPromptText` define la cadena que aparece en el campo de texto cuando se inicia la aplicación. 

```java
//definimos setPromptText para que indique la información que espera el campo
tFNombre.setPromptText("Nombre");
```

Puede obtener el valor de un campo de texto en cualquier momento llamando al método `getText`. Aquí por ejemplo hacemos que se muestre el campo oculto en un label:

```java
Button btnMostraTexto = new Button("Mostrar apellidos");
Label label = new Label();
btnMostraTexto.setOnAction((ActionEvent e) -> {
    label.setText(tFApellidos.getText());
});
```

Revise algunos métodos útiles que puede usar con los campos de texto.

- `copy()`– transfiere el rango actualmente seleccionado en el texto al portapapeles, dejando la selección actual.
- `cut()`– transfiere el rango actualmente seleccionado en el texto al portapapeles, eliminando la selección actual.
- `selectAll()` - selecciona todo el texto en la entrada de texto.
- `pegar()`– transfiere el contenido del portapapeles a este texto, reemplazando la selección actual.

**`E09_TextBox.java`**

```java
package UD09;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class E09_TextBox extends Application {

    private Parent createContent() {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER_LEFT);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        //Creamos el TextkField vacio
        TextField tFNombre = new TextField();
        //Establecemos el número de caracteres que mostrará por defecto
        tFNombre.setPrefColumnCount(10);
        //definimos setPromptText para que indique la información que espera el campo
        tFNombre.setPromptText("Nombre");
        grid.add(tFNombre, 0, 0);

        //Creamos el campo PasswordField que no mostrará por pantalla la información
        PasswordField tFApellidos = new PasswordField();
        tFApellidos.setPrefColumnCount(10);
        tFApellidos.setPromptText("Apellidos");
        grid.add(tFApellidos, 0, 1);

        TextField tFComentario = new TextField();
        //Establecemos el contenido por defecto del campo de texto
        tFComentario.setText("Comentario por defecto");
        //Seria lo mismo que haber creado el TextField de esta manera:
        //TextField tFComentario = new TextField("Comentario por defecto");
        tFComentario.setPrefColumnCount(10);
        tFComentario.setPromptText("Comentario");
        grid.add(tFComentario, 0, 2);

        Button btnMostraTexto = new Button("Mostrar apellidos");
        Label label = new Label();
        btnMostraTexto.setOnAction((ActionEvent e) -> {
            label.setText(tFApellidos.getText());
        });

        grid.add(label, 1, 0);
        grid.add(btnMostraTexto, 1, 1);

        return grid;

    }

    @Override
    public void start(Stage stage) throws Exception {
        Scene scene = new Scene(createContent(), 500, 200);
        stage.setScene(scene);

        stage.setTitle("Ejemplo TextField y PasswordField");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### Mucho más

https://docs.oracle.com/javase/8/javafx/user-interface-tutorial/ui_controls.htm

## Diseño (Layouts)

### VBox y HBox

El diseño en JavaFX comienza con la selección de los controles de contenedor correctos. Los dos controles de diseño que uso con más frecuencia son `VBox`y `HBox`. 

- `VBox` es un contenedor que organiza a sus hijos en una pila vertical.
- `HBox` ordena a sus hijos en una fila horizontal. 

El poder de estos dos controles proviene de envolverlos y establecer algunas propiedades clave: `alineación`, `hgrow` y `vgrow`.

Este artículo demostrará estos controles a través de un proyecto de ejemplo. Una maqueta del proyecto muestra una interfaz de usuario con lo siguiente:

- Una fila de controles superiores que contiene *Actualizar* `Button` y *Cerrar sesión* `Hyperlink`,
- Una *Tabla* `TableView` que crecerá para ocupar el espacio vertical adicional, y
- Un `Button` *Cerrar*.

La interfaz de usuario también presenta un `Separator`panel que divide la parte superior de la pantalla con lo que puede convertirse en un panel inferior estándar (Guardar `Button`, Cancelar `Button`, etc.) para la aplicación.

![maqueta de vboxandhboxapp](https://fxdocs.github.io/docs/html5/images/layout/vboxandhboxapp_mockup.png){width=600}

#### Estructura

`VBox` será el contenedor más externo "vbox". Este será el `Parent` proporcionado a la Escena. El simple hecho de colocar los controles de la interfaz de usuario en este `VBox` permitirá que los controles, sobre todo el `TableView` , se estiren para adaptarse al espacio horizontal disponible. Los controles superiores, *Actualizar* `Button` y *Cerrar sesión* `Hyperlink`, están envueltos en un contenedor `HBox`. Del mismo modo, se envolverá el `Button` inferior *Cerrar* en un `HBox`, lo que permite botones adicionales.

```java
VBox vbox = new VBox();

        HBox controlesArriba = new HBox();
        VBox.setMargin( controlesArriba, new Insets(10.0d) );
        controlesArriba.setAlignment( Pos.BOTTOM_LEFT );

        Button btnActualizar = new Button("Actualizar");

        HBox controlesArribaDerecha = new HBox();
        HBox.setHgrow(controlesArribaDerecha, Priority.ALWAYS );
        controlesArribaDerecha.setAlignment( Pos.BOTTOM_RIGHT );
        Hyperlink lnkCerrarSesion = new Hyperlink("Cerrar sesión");
        controlesArribaDerecha.getChildren().add( lnkCerrarSesion );

        controlesArriba.getChildren().addAll( btnActualizar, controlesArribaDerecha );

        TableView<Cliente> tblClientes = new TableView<>();
        tblClientes.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
        VBox.setMargin( tblClientes, new Insets(0.0d, 10.0d, 10.0d, 10.0d) );
        VBox.setVgrow( tblClientes, Priority.ALWAYS );

        TableColumn<Cliente, String> columnaApellidos = new TableColumn<>("Apellidos");
        columnaApellidos.setCellValueFactory(new PropertyValueFactory<>("apellidos"));

        TableColumn<Cliente, String> columnaNombre = new TableColumn<>("Nombre");
        columnaNombre.setCellValueFactory(new PropertyValueFactory<>("nombre"));

        tblClientes.getColumns().addAll( columnaApellidos, columnaNombre );

        Separator sep = new Separator();

        HBox controlesAbajo = new HBox();
        controlesAbajo.setAlignment(Pos.BOTTOM_RIGHT );
        VBox.setMargin( controlesAbajo, new Insets(10.0d) );

        Button btnCerrar = new Button("Cerrar");

        controlesAbajo.getChildren().add( btnCerrar );

        vbox.getChildren().addAll(
                controlesArriba,
                tblClientes,
                sep,
                controlesAbajo
        );

        Scene scene = new Scene(vbox );

        primaryStage.setScene( scene );
        primaryStage.setWidth( 800 );
        primaryStage.setHeight( 600 );
        primaryStage.setTitle("Aplicación con VBox y HBox");
        primaryStage.setOnShown( (evt) -> loadTable(tblClientes) );
        primaryStage.show();
```

Esta imagen muestra la maqueta desglosada por contenedor. El padre `VBox` es el rectángulo azul más externo. Los HBoxes son los rectángulos interiores (rojo y verde).

![Esquema de VBoxAndHBoxApp](assets/VBoxHBox01.png){width=800}

#### Alineación y Hgrow

El `Button` *Actualizar* está alineado a la izquierda mientras que el `Hyperlink` *Cerrar sesión* está alineado a la derecha. Esto se logra usando dos HBoxes. `controlesArriba` es un `HBox` que contiene el `Button` *Actualizar* y también contiene un `HBox`con el `Hyperlink` *Cerrar sesión*. A medida que la pantalla se hace más ancha, el `Hyperlink` *Cerrar sesión* se desplazará hacia la derecha, mientras que el `Button` *Actualizar* mantendrá su alineación izquierda.

La alineación es la propiedad que le dice a un contenedor dónde colocar un control. `controlesArriba` establece la alineación en `BOTTOM_LEFT`. `controlesArribaDerecha` establece la alineación con `BOTTOM_RIGHT`. `BOTTOM` se asegura de que la línea de base del texto *Actualizar* coincida con la línea de base del texto *Cerrar sesión*.

Para que el `Hyperlink` *Cerrar sesión* se mueva hacia la derecha cuando la pantalla se ensancha, es necesario `Priority.ALWAYS`. Esta es una señal para que JavaFX amplíe `controlesArribaDerecha`. De lo contrario, `controlesArriba` mantendrá el espacio y `controlesArribaDerecha` aparecerá a la izquierda. El `Hyperlink` *Cerrar sesión* todavía estaría alineado a la derecha pero en un contenedor más estrecho.

Tenga en cuenta que `setHgrow()` es un método estático y no se invoca el `HBox` `controlesArriba` ni en sí mismo, `controlesArribaDerecha`. Esta es una faceta de la API de JavaFX que puede resultar confusa porque la mayoría de las API establece propiedades a través de setters en objetos.

```java
controlesArriba.setAlignment( Pos.BOTTOM_LEFT );
HBox.setHgrow(controlesArribaDerecha, Priority.ALWAYS ); //en lugar de controlesArribaDerecha.setHgrow(Priority.ALWAYS);
controlesArribaDerecha.setAlignment( Pos.BOTTOM_RIGHT );
```

El `Button` `Cerrar` se envuelve en un `HBox` y se posiciona usando la prioridad `BOTTOM_RIGHT`.

```java
controlesAbajo.setAlignment(Pos.BOTTOM_RIGHT );
```

#### Crecer

Dado que el contenedor más externo es `VBox`, el hijo `TableView` se expandirá para ocupar espacio horizontal adicional cuando se amplíe la ventana. Sin embargo, cambiar el tamaño vertical de la ventana producirá un espacio en la parte inferior de la pantalla. `VBox` no cambia automáticamente el tamaño de ninguno de sus elementos secundarios . Al igual que con el  `HBox` `controlesArribaDerecha`, se puede configurar un indicador de crecimiento. En el caso del `HBox`, se trataba de una instrucción de cambio de tamaño horizontal `setHgrow()`. Para el  contenedor `VBox` `TableView`, será `setVgrow()`.

```java
VBox.setVgrow( tblClientes, Priority.ALWAYS ); //también estático
```

#### Margen

Hay algunas formas de espaciar los controles de la interfaz de usuario. Nosotros usaremos la propiedad `margin` en varios de los contenedores para agregar espacios en blanco alrededor de los controles. Estos se configuran individualmente en lugar de usar un espacio en el `VBox` para que el *Separador* abarque todo el ancho.

```java
VBox.setMargin(controlesArriba, new Insets(10.0d));
VBox.setMargin(tblClientes, new Insets(0.0d, 10.0d, 10.0d, 10.0d));
VBox.setMargin(controlesAbajo, new Insets(10.0d));
```

El `Insets` usado por `tblClientes` omite cualquier espacio superior para mantener el espacio uniforme. JavaFX no consolida los espacios en blanco como en el diseño web. Si el Recuadro superior se estableciera en `10.0d` para el `tblClientes`, la distancia entre los controles superiores y el `TableView` sería el doble de ancha que la distancia entre cualquiera de los otros controles.

Tenga en cuenta que estos son métodos estáticos como el `Priority`.

Esta imagen muestra la aplicación cuando se ejecuta en su tamaño inicial de 800x600.

![VBoxAndHBoxApp 800x600](assets/VBoxHBox02.png){width=800}

Esta imagen muestra la aplicación redimensionada a un alto y ancho más pequeños.

![VBoxAndHBoxApp más pequeña](assets/VBoxHBox03.png){width=600}

#### Seleccione los contenedores correctos

La filosofía del diseño de JavaFX es la misma que la filosofía de Swing. Seleccione el contenedor adecuado para la tarea en cuestión. Aquí hemos mostrado los dos contenedores más versátiles: `VBox` y `HBox`. Al establecer propiedades como alineación, `hgrow` y `vgrow`, puede crear diseños increíblemente complejos mediante el anidamiento. Estos son los contenedores que más uso y, a menudo, son los únicos contenedores que necesitaras.

#### Código completo

El código se puede probar con un par de archivos .java. Hay un POJO para la clase `Cliente` utilizado por el `TableView`

**`Cliente.java`**

```java
package UD09._02_VBoxHBox;

public class Cliente {
    private String nombre;
    private String apellidos;

    public Cliente(String nombre, String apellidos) {
        this.nombre = nombre;
        this.apellidos = apellidos;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
}

```

y la subclase JavaFX completa y principal:

**`VBoxAndHBoxApp.java`**

```java
package UD09._02_VBoxHBox;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Hyperlink;
import javafx.scene.control.Separator;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class VBoxAndHBoxApp extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        VBox vbox = new VBox();

        HBox controlesArriba = new HBox();
        VBox.setMargin( controlesArriba, new Insets(10.0d) );
        controlesArriba.setAlignment( Pos.BOTTOM_LEFT );

        Button btnActualizar = new Button("Actualizar");

        HBox topRightControls = new HBox();
        HBox.setHgrow(topRightControls, Priority.ALWAYS );
        topRightControls.setAlignment( Pos.BOTTOM_RIGHT );
        Hyperlink lnkCerrarSesion = new Hyperlink("Cerrar sesión");
        topRightControls.getChildren().add( lnkCerrarSesion );

        controlesArriba.getChildren().addAll( btnActualizar, topRightControls );

        TableView<Cliente> tblClientes = new TableView<>();
        tblClientes.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
        VBox.setMargin( tblClientes, new Insets(0.0d, 10.0d, 10.0d, 10.0d) );
        VBox.setVgrow( tblClientes, Priority.ALWAYS );

        TableColumn<Cliente, String> columnaApellidos = new TableColumn<>("Apellidos");
        columnaApellidos.setCellValueFactory(new PropertyValueFactory<>("apellidos"));

        TableColumn<Cliente, String> columnaNombre = new TableColumn<>("Nombre");
        columnaNombre.setCellValueFactory(new PropertyValueFactory<>("nombre"));

        tblClientes.getColumns().addAll( columnaApellidos, columnaNombre );

        Separator sep = new Separator();

        HBox controlesAbajo = new HBox();
        controlesAbajo.setAlignment(Pos.BOTTOM_RIGHT );
        VBox.setMargin( controlesAbajo, new Insets(10.0d) );

        Button btnCerrar = new Button("Cerrar");

        controlesAbajo.getChildren().add( btnCerrar );

        vbox.getChildren().addAll(
                controlesArriba,
                tblClientes,
                sep,
                controlesAbajo
        );

        Scene scene = new Scene(vbox );

        primaryStage.setScene( scene );
        primaryStage.setWidth( 800 );
        primaryStage.setHeight( 600 );
        primaryStage.setTitle("Aplicación con VBox y HBox");
        primaryStage.setOnShown( (evt) -> loadTable(tblClientes) );
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

    private void loadTable(TableView<Cliente> tblCustomers) {
        tblCustomers.getItems().add(new Cliente("David", "Martinez"));
        tblCustomers.getItems().add(new Cliente("Ada", "Lovelace"));
        tblCustomers.getItems().add(new Cliente("Alan", "Turing"));
    }
}
```

### StackPane

El layout `StackPane` coloca a sus hijos uno encima de otro. El último `Node` agregado es el más alto. Por defecto `StackPane` alineará los hijos usando `Pos.CENTER`, como se puede ver en la siguiente imagen, donde están los 3 hijos (en orden de creación): `Rectangle`, `Circle` y `Button`.

![Ejemplo de StackPane](assets/StackPane01.png){width=400}

Esta imagen fue producida por el siguiente fragmento:

**`StackPaneApp.java`**

```java
package UD09._03_StackPane;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class StackPaneApp extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        StackPane pane = new StackPane(
                new Rectangle(200, 100, Color.BLACK),
                new Circle(40, Color.RED),
                new Button("Hello StackPane")
        );

        //pane.setAlignment(Pos.CENTER_LEFT);
        
        stage.setScene(new Scene(pane, 300, 300));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

Podemos cambiar la alineación predeterminada descomentando la linea `pane.setAlignment(Pos.CENTER_LEFT);`para producir el siguiente efecto:

![Cambio de alineación de StackPane](assets/StackPane02.png){width=400}

### Posicionamiento absoluto con panel (`Pane`)

Contenedores como `VBox` o `BorderPane` alinear y distribuir a sus hijos. La superclase `Pane` también es un contenedor, pero no impone un orden a sus hijos. Los hijos se posicionan a sí mismos a través de propiedades como `x`, `centerX` y `layoutX`. Esto se llama posicionamiento absoluto y es una técnica para colocar un `Shape` o un `Node` en un lugar determinado de la pantalla.

Esta captura de pantalla muestra una vista *Acerca de*. La vista *Acerca de* contiene un `Hyperlink` en el medio de la pantalla "Acerca de esta aplicación". La vista *Acerca de* utiliza varias formas JavaFX para formar un diseño que se recorta para que parezca una tarjeta de presentación.

![Captura de pantalla de la Aplicación Pane](assets/Pane01.png){width=500}

#### Tamaño del panel

A diferencia de la mayoría de los contenedores, `Pane` cambia de tamaño para adaptarse a su contenido y no al revés. Esta imagen es una captura de pantalla de Scenic View tomada antes de agregar el Arco inferior derecho. El `Pane` es el área resaltada en amarillo. Tenga en cuenta que no ocupa la totalidad `Stage`.

![Falta el arco inferior](assets/Pane02.png){width=500}

A continuación se muestra una captura de pantalla tomada después de agregar la esquina inferior derecha `Arc`. Esto `Arc`se colocó más cerca del borde inferior derecho del archivo `Stage`. Esto obliga al Panel a estirarse para acomodar los contenidos expandidos.

![Pane crece para adaptarse al arco inferior añadido](assets/Pane03.png){width=500}

#### El panel (`Pane`)

El contenedor más externo de la vista *Acerca de* es un `VBox` cuyo único contenido es el archivo `Pane`. El `VBox` se utiliza para encajar en el conjunto `Stage` y proporciona un fondo.

```java
VBox vbox = new VBox();
vbox.setPadding( new Insets( 10 ) );
vbox.setBackground(
    new Background(
        new BackgroundFill(Color.BLACK, new CornerRadii(0), new Insets(0))
        ));

Pane p = new Pane();
```

#### Las formas (`Shape`)

En la parte superior izquierda de la pantalla, hay un grupo de 4 Arcos y 1 Círculo. Este código posiciona `largeArc` en (0,0) a través de los argumentos `centerX` y `centerY` en el constructor `Arc`. Observa que `backgroundArc` también se coloca en (0,0) y aparece debajo de `largeArc`. `Pane` no intenta eliminar el conflicto de formas superpuestas y, en este caso, lo que se busca es la superposición. `smArc1` se coloca en (0,160), que está abajo en el eje Y. `smArc2` está posicionado en (160,0) que está justo en el eje X. `smCircle` se coloca a la misma distancia que `smArc1` y `smArc2`, pero en un ángulo de 45 grados.

```java
Arc largeArc = new Arc(0, 0, 100, 100, 270, 90);
largeArc.setType(ArcType.ROUND);

Arc backgroundArc = new Arc(0, 0, 160, 160, 270, 90 );
backgroundArc.setType( ArcType.ROUND );

Arc smArc1 = new Arc( 0, 160, 30, 30, 270, 180);
smArc1.setType(ArcType.ROUND);

Circle smCircle = new Circle(160/Math.sqrt(2.0), 160/Math.sqrt(2.0), 30,Color.web("0xF2A444"));

Arc smArc2 = new Arc( 160, 0, 30, 30, 180, 180);
smArc2.setType(ArcType.ROUND);
```

En la parte inferior derecha el `Arc ` se coloca en función de la altura total del archivo `Stage`. Los 20 restados de la altura son los 10 píxeles de `Insets` (Margen) de `VBox` (10 para la izquierda + 10 para la derecha).

```java
Arc medArc = new Arc(568-20, 320-20, 60, 60, 90, 90);
medArc.setType(ArcType.ROUND);

primaryStage.setWidth(568);
primaryStage.setHeight(320);
```

#### El hipervínculo

El `Hyperlink` está posicionado compensado el centro (284,160) que es el ancho y alto de `Stage` ambos dividido por dos. Esto coloca el texto del `Hyperlink`en el cuadrante inferior derecho de la pantalla, por lo que se necesita un desplazamiento basado en el ancho y el alto de `Hyperlink`. Las dimensiones del `Hyperlink` no están disponibles hasta que se muestra la pantalla, por lo que se realiza un ajuste posterior a la visualización de la posición.

```java
Hyperlink hyperlink = new Hyperlink("About this App");

primaryStage.setOnShown( (evt) -> {
     hyperlink.setLayoutX( 284 - (hyperlink.getWidth()/3) );
     hyperlink.setLayoutY( 160 - hyperlink.getHeight() );
});
```

El `Hyperlink`no está colocado en el verdadero centro de la pantalla. El valor de `layoutX` se basa en una operación de división por tres que lo aleja de las formas de la esquina superior izquierda.

#### Orden Z

Como se mencionó anteriormente, `Pane` admite la superposición de los hijos. Esta imagen muestra la vista *Acerca de* con profundidad.

![paneapp zorder](https://fxdocs.github.io/docs/html5/images/layout/paneapp_zorder.png){width=500}

El orden z en este ejemplo está determinado por el orden en que se agregan los elementos secundarios al archivo `Pane`. `backgroundArc` está oscurecido por elementos agregados más tarde, más notablemente `largeArc`. Para reorganizar los elementos secundarios, use los métodos `toFront()` y `toBack()` después de agregar los elementos al archivo `Pane`.

```java
p.getChildren().addAll( backgroundArc, largeArc, smArc1, smCircle, smArc2, hyperlink, medArc );
vbox.getChildren().add( p );
```

!!! warning "Recomendación"
    Al comenzar con JavaFX, es tentador construir un diseño absoluto. Tenga en cuenta que los diseños absolutos son frágiles y, a menudo, se rompen cuando se cambia el tamaño de la pantalla (como en este caso) o cuando se agregan elementos durante la fase de mantenimiento del software. Sin embargo, existen buenas razones para utilizar el posicionamiento absoluto. El juego es uno de esos usos. En un juego, puede ajustar la coordenada (x,y) de una `Shape` para mover una pieza del juego por la pantalla.

#### Código completo

Esta es la aplicación JavaFX completa y principal.

**`PaneApp.java`**

```java
package UD09._04_Pane;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Hyperlink;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.Border;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Circle;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class PaneApp extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        VBox vbox = new VBox();
        vbox.setPadding( new Insets( 10 ) );
        vbox.setBackground(
            new Background(
                new BackgroundFill(Color.BLACK, new CornerRadii(0), new Insets(0))
                ));

        Pane p = new Pane();

        Arc largeArc = new Arc(0, 0, 100, 100, 270, 90);
        largeArc.setFill(Color.web("0x59291E"));
        largeArc.setType(ArcType.ROUND);

        Arc backgroundArc = new Arc(0, 0, 160, 160, 270, 90 );
        backgroundArc.setFill( Color.web("0xD96F32") );
        backgroundArc.setType( ArcType.ROUND );

        Arc smArc1 = new Arc( 0, 160, 30, 30, 270, 180);
        smArc1.setFill(Color.web("0xF2A444"));
        smArc1.setType(ArcType.ROUND);

        Circle smCircle = new Circle(
            160/Math.sqrt(2.0), 160/Math.sqrt(2.0), 30,Color.web("0xF2A444")
            );

        Arc smArc2 = new Arc( 160, 0, 30, 30, 180, 180);
        smArc2.setFill(Color.web("0xF2A444"));
        smArc2.setType(ArcType.ROUND);

        Hyperlink hyperlink = new Hyperlink("Acerca de esta App");
        hyperlink.setFont( Font.font(36) );
        hyperlink.setTextFill( Color.web("0x3E6C93") );
        hyperlink.setBorder( Border.EMPTY );

        Arc medArc = new Arc(568-20, 320-20, 60, 60, 90, 90);
        medArc.setFill(Color.web("0xD9583B"));
        medArc.setType(ArcType.ROUND);

        p.getChildren().addAll( backgroundArc, largeArc, smArc1, smCircle,
            smArc2, hyperlink, medArc );

        vbox.getChildren().add( p );

        Scene scene = new Scene(vbox);
        scene.setFill(Color.BLACK);

        primaryStage.setTitle("Aplicación Pane");
        primaryStage.setScene( scene );
        primaryStage.setWidth( 568 );
        primaryStage.setHeight( 320 );
        primaryStage.setOnShown( (evt) -> {
             hyperlink.setLayoutX( 284 - (hyperlink.getWidth()/3) );
             hyperlink.setLayoutY( 160 - hyperlink.getHeight() );
        });
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### GridPane

Los formularios en las aplicaciones comerciales a menudo usan un diseño que imita un registro de base de datos. Para cada columna de una tabla, se agrega un encabezado en el lado izquierdo que coincide con un valor de fila en el lado derecho. JavaFX tiene un control de propósito especial llamado `GridPane` para este tipo de diseño que mantiene los contenidos alineados por fila y columna. `GridPane` también admite expansión para diseños más complejos.

La siguiente captura de pantalla muestra un diseño básico de `GridPane`. En el lado izquierdo del formulario, hay una columna de nombres de campo: Correo-e, Prioridad, Problema, Descripción. En el lado derecho del formulario, hay una columna de controles que mostrará el valor del campo correspondiente. Los nombres de campo son de tipo `Label` y los controles de valor son una mezcla que incluye `TextField`, `TextArea` y `ComboBox`.

![Ejemplo de GridPane](assets/GridPane01.png){width=800}

El siguiente código muestra los objetos creados para el formulario. "vbox" es la raíz del `Scene`y también contendrá el `ButtonBar` en la base del formulario.

```java
VBox vbox = new VBox();
GridPane gp = new GridPane();

Label lblTitle = new Label("Tiquet de soporte");

Label lblEmail = new Label("Correo-e");
TextField tfEmail = new TextField();

Label lblPriority = new Label("Prioridad");
ObservableList<String> priorities = FXCollections.observableArrayList("Media", "Alta", "Baja");
ComboBox<String> cbPriority = new ComboBox<>(priorities);

Label lblProblem = new Label("Problema");
TextField tfProblem = new TextField();

Label lblDescription = new Label("Descripción");
TextArea taDescription = new TextArea();
```

GridPane tiene un método útil `setGridLinesVisible()` que muestra la estructura de la cuadrícula y los espacios. Es especialmente útil en diseños más complejos donde se involucra la expansión porque los espacios en las asignaciones de filas/columnas pueden causar cambios en el diseño.

![Lineas de estructura](assets/GridPane02.png){width=800}

#### Espaciado

Como contenedor, `GridPane` tiene una propiedad de relleno que se puede configurar para rodear el contenedor `GridPane` con espacios en blanco. `setPadding()` tomará un objeto `Inset` como parámetro. En este ejemplo, se aplican 10 píxeles de espacio en blanco a todos los lados, por lo que se usa un constructor de formato corto para `Inset`.

Dentro de `GridPane`, `vgap` y `hgap` controlan los espacios. El `hgap` se establece en 4 para mantener los campos cerca de sus valores. `vgap` es un poco más grande para ayudar con la navegación del mouse.

```java
gp.setPadding( new Insets(10) );
gp.setHgap( 4 );
gp.setVgap( 8 );
```

Para mantener consistente la parte inferior del formulario, `Priority.ALWAYS` se establece a en la clase VBox sobre el `GridPane` (recuerda que es estático). Sin embargo, esto no cambiará el tamaño de las filas individuales. Para especificaciones de cambio de tamaño individuales, debes usar `ColumnConstraints` y `RowConstraints`.

```java
VBox.setVgrow(gp, Priority.ALWAYS );
```

#### Adición de elementos

A diferencia de los contenedores como `BorderPane` o `HBox`, los nodos deben especificar su posición dentro del contenedor `GridPane`. Esto se hace con el método `add()` en `GridPane` y no con el método `add()` en una propiedad secundaria del contenedor. El método `add()` de `GridPane` recibe una posición de columna de base cero y una posición de fila de base cero. En este código ponemos dos declaraciones en la misma línea para facilitar la lectura.

```java
gp.add( lblTitle,       1, 1);  // empty item at 0,0
gp.add( lblEmail,       0, 2); gp.add(tfEmail,        1, 2);
gp.add( lblPriority,    0, 3); gp.add( cbPriority,    1, 3);
gp.add( lblProblem,     0, 4); gp.add( tfProblem,     1, 4);
gp.add( lblDescription, 0, 5); gp.add( taDescription, 1, 5);
```

`lblTitle` se coloca en la segunda columna de la primera fila. No hay ninguna entrada en la primera columna de la primera fila.

Las adiciones posteriores se presentan por parejas. Los objetos de nombre de campo `Label` se colocan en la primera columna (índice de columna=0) y los controles de valor se colocan en la segunda columna (índice de columna=1). Las filas se agregan por el segundo valor incrementado. Por ejemplo, `lblPriority` se coloca en la cuarta fila junto con su `ComboBox`.

`GridPane` es un contenedor importante en el diseño de aplicaciones empresariales JavaFX. Cuando tenga un requisito de pares de nombre/valor, `GridPane `será una manera más fácil de organizar la estructura del formulario.

#### Código completo

La siguiente clase es el código completo del ejemplo. Esto incluye la definición de la `ButtonBar`que no se presentó en las secciones anteriores enfocadas en `GridPane`.

**`GridPaneApp.java`**

```java
package UD09._05_GridPane;

import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonBar;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.Separator;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class GridPaneApp extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        VBox vbox = new VBox();

        GridPane gp = new GridPane();
        gp.setPadding(new Insets(10));
        gp.setHgap(4);
        gp.setVgap(8);

        VBox.setVgrow(gp, Priority.ALWAYS);

        Label lblTitle = new Label("Tiquet de soporte");

        Label lblEmail = new Label("Correo-e");
        TextField tfEmail = new TextField();

        Label lblPriority = new Label("Prioridad");
        ObservableList<String> priorities
                = FXCollections.observableArrayList("Media", "Alta", "Baja");
        ComboBox<String> cbPriority = new ComboBox<>(priorities);

        Label lblProblem = new Label("Problema");
        TextField tfProblem = new TextField();

        Label lblDescription = new Label("Descripción");
        TextArea taDescription = new TextArea();

        gp.add(lblTitle, 1, 1);  // empty item at 0,0
        gp.add(lblEmail, 0, 2);
        gp.add(tfEmail, 1, 2);
        gp.add(lblPriority, 0, 3);
        gp.add(cbPriority, 1, 3);
        gp.add(lblProblem, 0, 4);
        gp.add(tfProblem, 1, 4);
        gp.add(lblDescription, 0, 5);
        gp.add(taDescription, 1, 5);

        Separator sep = new Separator(); // hr

        ButtonBar buttonBar = new ButtonBar();
        buttonBar.setPadding(new Insets(10));

        Button saveButton = new Button("Guardar");
        Button cancelButton = new Button("Cancelar");

        buttonBar.setButtonData(saveButton, ButtonBar.ButtonData.OK_DONE);
        buttonBar.setButtonData(cancelButton, ButtonBar.ButtonData.CANCEL_CLOSE);

        buttonBar.getButtons().addAll(saveButton, cancelButton);

        vbox.getChildren().addAll(gp, sep, buttonBar);

        //para mostrar las lineas de estructura descomenta la siguiente linea
        //gp.setGridLinesVisible(true);
        
        Scene scene = new Scene(vbox);

        primaryStage.setTitle("Grid Pane App");
        primaryStage.setScene(scene);
        primaryStage.setWidth(736);
        primaryStage.setHeight(414);
        primaryStage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

### GridPane Spanning (expansión)

Para formularios más complejos implementados con `GridPane`, se admite la expansión. La expansión permite que un control reclame el espacio de columnas vecinas (`colspan`) y filas vecinas (`rowspan`). Esta captura de pantalla muestra un formulario que amplía el ejemplo de la sección anterior. El diseño de dos columnas de la versión anterior se reemplazó por un diseño de varias columnas. Los campos como Problema y Descripción conservan la estructura original. Pero se agregaron controles a las filas que anteriormente contenían solo Correo electrónico y Prioridad.

![Aplicación GridaPanev2](assets/GridPane03.png){width=800}

Al activar las líneas de la cuadrícula, observe que la cuadrícula anterior de dos columnas se reemplaza con una cuadrícula de seis columnas. La tercera fila que contiene seis elementos (3 pares de nombre de campo/valor) dicta la estructura. El resto del formulario utilizará la expansión para completar el espacio en blanco.

![Lineas de estructura para GridPanev2](assets/GridPane04.png){width=800}

Hay un poco más de Vgap para ayudar al usuario a seleccionar los controles `ComboBox`. Como en la versión anterior, los controles se agregan al `GridPane` con el método `add()`. Se especifica una columna y una fila. Repasa los índices ya que no es evidente, ya que se espera que se llenen los vacíos mediante el contenido expandido.

Las definiciones de expansión se establecen mediante un método estático en `GridPane`. Hay un método similar para hacer la expansión de filas. El título ocupará 5 columnas, al igual que el problema y la descripción. El correo electrónico comparte una fila con el contrato, pero ocupará más columnas. La tercera fila de ComboBoxes es un conjunto de tres pares de campo/valor, cada uno de los cuales ocupa una columna.

```java
GridPane.setColumnSpan( lblTitle, 5 );
GridPane.setColumnSpan( tfEmail, 3 );
GridPane.setColumnSpan( tfProblem, 5 );
GridPane.setColumnSpan( taDescription, 5 );
```

Alternativamente, una variación del método add() tendrá argumentos columnSpan y rowSpan para evitar la subsiguiente llamada al método estático.

Este ejemplo ampliado `GridPane`demostró la expansión de columnas. La misma capacidad está disponible para la expansión de filas, lo que permitiría que un control reclame espacio vertical adicional. La expansión mantiene los controles alineados incluso en los casos en que varía el número de elementos en una fila (o columna) determinada. 

#### Código completo

El siguiente es el código completo para el ejemplo de GridPane de expansión.

**`GridPaneAppv2.java`**

```java
Package UD09._05_GridPane;

import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonBar;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.Separator;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class GridPaneAppv2 extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        VBox vbox = new VBox();

        GridPane gp = new GridPane();
        gp.setPadding(new Insets(10));
        gp.setHgap(4);
        gp.setVgap(10);

        VBox.setVgrow(gp, Priority.ALWAYS);

        Label lblTitle = new Label("Tiquet de soporte");

        Label lblEmail = new Label("Correo-e");
        TextField tfEmail = new TextField();

        Label lblContract = new Label("Contrato");
        TextField tfContract = new TextField();

        Label lblPriority = new Label("Prioridad");
        ObservableList<String> priorities
                = FXCollections.observableArrayList("Media", "Alta", "Baja");
        ComboBox<String> cbPriority = new ComboBox<>(priorities);

        Label lblSeverity = new Label("Severidad");
        ObservableList<String> severities
                = FXCollections.observableArrayList("Bloqueante", "Salvable", "No importa");
        ComboBox<String> cbSeverity = new ComboBox<>(severities);

        Label lblCategory = new Label("Categoria");
        ObservableList<String> categories
                = FXCollections.observableArrayList("Defecto", "Nueva funcionalidad");
        ComboBox<String> cbCategory = new ComboBox<>(categories);

        Label lblProblem = new Label("Problema");
        TextField tfProblem = new TextField();

        Label lblDescription = new Label("Descripción");
        TextArea taDescription = new TextArea();

        gp.add(lblTitle, 1, 0);  // empty item at 0,0

        gp.add(lblEmail, 0, 1);
        gp.add(tfEmail, 1, 1);
        gp.add(lblContract, 4, 1);
        gp.add(tfContract, 5, 1);

        gp.add(lblPriority, 0, 2);
        gp.add(cbPriority, 1, 2);
        gp.add(lblSeverity, 2, 2);
        gp.add(cbSeverity, 3, 2);
        gp.add(lblCategory, 4, 2);
        gp.add(cbCategory, 5, 2);

        gp.add(lblProblem, 0, 3);
        gp.add(tfProblem, 1, 3);
        gp.add(lblDescription, 0, 4);
        gp.add(taDescription, 1, 4);
```
```java
        //Expansiones
        GridPane.setColumnSpan(lblTitle, 5);
        GridPane.setColumnSpan(tfEmail, 3);
        GridPane.setColumnSpan(tfProblem, 5);
        GridPane.setColumnSpan(taDescription, 5);

        Separator sep = new Separator(); // hr

        ButtonBar buttonBar = new ButtonBar();
        buttonBar.setPadding(new Insets(10));

        Button saveButton = new Button("Guardar");
        Button cancelButton = new Button("Cancelar");

        buttonBar.setButtonData(saveButton, ButtonBar.ButtonData.OK_DONE);
        buttonBar.setButtonData(cancelButton, ButtonBar.ButtonData.CANCEL_CLOSE);

        buttonBar.getButtons().addAll(saveButton, cancelButton);

        vbox.getChildren().addAll(gp, sep, buttonBar);

        //para mostrar las lineas de estructura descomenta la siguiente linea
        gp.setGridLinesVisible(true);
        
        Scene scene = new Scene(vbox);

        primaryStage.setTitle("Grid Pane App");
        primaryStage.setScene(scene);
        primaryStage.setWidth(736);
        primaryStage.setHeight(414);
        primaryStage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

## Estructura de la aplicación

### El patrón MVC

**Modelo-vista-controlador** (**MVC**) es un patrón de arquitectura de software, que separa los datos y principalmente lo que es la lógica de negocio de una aplicación de su representación y el módulo encargado de  gestionar los eventos y las comunicaciones. Para ello MVC propone la  construcción de tres componentes distintos que son el **modelo**, la **vista** y el **controlador**, es decir, por un lado define componentes para la representación de la  información, y por otro lado para la interacción del usuario. Este patrón de arquitectura de software se basa en las ideas de reutilización de código y la separación de conceptos, características que buscan facilitar la tarea de desarrollo de aplicaciones y su posterior mantenimiento.

De manera genérica, los componentes de MVC se podrían definir como sigue:

- El **Modelo**: Es la representación de la información con la  cual el sistema opera, por lo tanto gestiona todos los accesos a dicha  información, tanto consultas como actualizaciones, implementando también los privilegios de acceso que se hayan descrito en las especificaciones de la aplicación (lógica de negocio). Envía a la &apos;vista&apos; aquella parte de la información que en cada momento  se le solicita para que sea mostrada (típicamente a un usuario). Las  peticiones de acceso o manipulación de información llegan al &apos;modelo&apos; a  través del &apos;controlador&apos;.
- El **Controlador**: Responde a eventos (usualmente acciones del  usuario) e invoca peticiones al &apos;modelo&apos; cuando se hace alguna solicitud sobre la información (por ejemplo, editar un documento o un registro en una base de datos). También puede enviar comandos a su &apos;vista&apos; asociada si se solicita un cambio en la forma en que se presenta el &apos;modelo&apos;  (por ejemplo, desplazamiento o scroll por un documento o por los  diferentes registros de una base de datos), por tanto se podría decir  que el &apos;controlador&apos; hace de intermediario entre la &apos;vista&apos; y el  &apos;modelo&apos; (véase ***[Middleware](https://es.wikipedia.org/wiki/Middleware)***).
- La **Vista**: Presenta el &apos;modelo&apos; (información y *lógica de negocio*) en un formato adecuado para interactuar (usualmente la interfaz de usuario), por tanto requiere de dicho &apos;modelo&apos; la información que debe representar como salida.

![](assets/MVC-Process.png){width=400}

## Píldoras informáticas relacionadas

<p><iframe  width="100%" height="315" src="https://www.youtube.com/embed/videoseries?si=AEnj5v1FyQu9y8-V&amp;list=PLU8oAlHdN5BktAXdEVCLUYzvDyqRQJ2lk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></p>
