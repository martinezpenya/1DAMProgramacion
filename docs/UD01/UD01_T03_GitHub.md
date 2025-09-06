# Taller UD01_03: Como usar el VSCode integrado en GitHub

## `VsCode` integrado en `GitHub`

### Localizar repositorio.

Primero localizamos el repositorio con el que queremos colaborar (Por favor, busca uno del año actual, la imagen es solo un ejemplo):

1. Buscamos al usuario (En todo `GitHub`):

<img src="assets/vscode_01_localizar_repositorio.png" alt="Localizar repositorio" style="zoom:50%;" />

2. Elegimos la pestaña `Repositorios`:

<img src="assets/vscode_02_localizar_repositorio.png" alt="Localizar repositorio 2" style="zoom:50%;" />

3. Elegimos el que nos interesa modificar, en nuestro caso `PRG-CFGS-2324`:

<img src="assets/vscode_03_repositorio_elegido.png" alt="Repositorio elegido" style="zoom:50%;" />



### Abrir `VSCode` integrado.

Github cuenta con un editor online muy potente basado en `VSCode`.

Una vez visualizamos el código del repositorio en cuestión:

<img src="assets/vscode_04_codigo.png" alt="Screenshot_20220106_171327" alt="Código" style="zoom:50%;" />

Para abrir el editor solo debemos pulsar la tecla "." (punto) de nuestro teclado:

<img src="assets/vscode_05_vscode1.png" alt="editor VSCode" style="zoom:50%;" />

Visualizaremos la estructura de carpetas y archivos en un editor `VSCode` integrado en el navegador Web.

### Modificar un archivo.

Una vez detectada la errata dentro del código [markdown](https://markdown.es/) que es muy fácil de interpretar (a poco que le dediquéis unos minutos) podemos modificar el archivo en cuestión, y a su lado aparecerá una **M** porqué el archivo está modificado.

<img src="assets/vscode_06_vscode2.png" alt="Screenshot_20220106_172048" style="zoom:50%;" />

### Git integrado

VSCode lleva integrado un gestor de GIT, el tercer icono de la barra lateral: ![Screenshot_20220106_172635](assets/vscode_07_git.png)

1. Verificamos los archivos cambiados:
<img src="assets/vscode_07_git1.png" alt="Verificar cambios" style="zoom: 80%;" />

2. Los pasamos al area "staged" con el símbolo "+":
<img src="assets/vscode_07_git2.png" alt="pasar a staged" style="zoom:80%;" />

4. Añadimos el comentario del commit:
<img src="assets/vscode_07_git3.png" alt="comentario commit" style="zoom:80%;" />

4. Realizamos el commit:
    <img src="assets/vscode_07_git4.png" alt="Screenshot_20220106_173720" style="zoom:80%;" />

Como el repositorio no es nuestro mostrará este mensaje:

![Screenshot_20220106_173836](assets/vscode_07_git5.png)

En realidad podemos hacer el fork antes o después, aquí tienes un pequeño [vídeo](https://www.youtube.com/watch?v=zyT0sl3-kxE) que explica que es un fork.

A continuación nos pide el nombre de la rama que se creará y que luego podremos solicitar se incluya en el proyecto original:

<img src="assets/vscode_07_git6.png" alt="branch" style="zoom:80%;" />

Ahora nos pregunta si ya que hemos creado un fork, queremos cambiar el repositorio, y trabajar sobre nuestro fork en lugar de sobre el proyecto original, pulsamos sobre [Switch to Fork]:

<img src="assets/vscode_07_git7.png" alt="cambiar al fork" style="zoom:80%;" />

Ahora ya podemos salir del editor VSCode pulsando sobre el botón de las tres lineas horizontales y elegir la opción "Go to Repository":
<img src="assets/vscode_07_git8.png" alt="Volver al repositorio" style="zoom:80%;" />

### Pull request

Una vez volvemos a nuestro repositorio (nuestro fork), detectará que hay cambios respecto al repositorio original y nos propone que realicemos un pull request (una petición al usuario propietario del repositorio original para que incluya nuestra modificación).

<img src="assets/vscode_08_pullrequest.png" alt="Screenshot_20220106_175237" style="zoom:80%;" />

Una vez pulsado el botón [Compare & pull request] nos aparece la siguiente pantalla:

![Screenshot_20220106_175639](assets/vscode_09_pullrequest2.png)

Debemos asegurarnos de que la modificación se puede agregar al repositorio original "Able to merge", y que indicamos en los comentarios nuestro nombre completo para que el profesor nos identifique. Fíjate que el nombre del pull request es el nombre del commit que hicimos desde VSCode.

Ahora debemos pulsar el botón [Create pull request].

## Tarea

Sigue los pasos de este taller guiado para sugerir una modificación de cualquiera de los archivos de los repositorios del profesor [martinezpenya](https://github.com/martinezpenya) (Preferiblemente del curso 24-25). Adjunta a la tarea de AULES un `.pdf` con la **captura** de pantalla similar a esta donde se vé que has solicitado el **pull request** y que estás esperando a que se integre en el repositorio original. Además, **explica** que significan cada uno de los **5 apartados** señalados en la captura:
![Screenshot_20220106_180847](assets/vscode_10_pullrequest3.png)
