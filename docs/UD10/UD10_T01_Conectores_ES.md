# Taller UD10_02: Conectores


## Controlador MySql (Manualmente - Jar)

1. El primer paso es descargar desde https://www.mysql.com/products/connector/ el conector apropiado.

![jdbc download](assets/jdbc_1_download.png)

2. Elegiremos la opción independiente de la Plataforma, que nos provee del archivo jar necesario (comprimido en tar.gz o zip, según nos interese):

<img src="assets/jdbc_2_version.png" alt="Descargar conector" style="zoom: 33%;" />

3. Haz clic en **Donwload** y selecciona la opción: **No thanks, just start download**

![aceptar jdbc](assets/jdbc_2_accept.png)

4. Ahora descomprimimos el archivo descargado, que contendrá el archivo jar que nos interesa:

   `mysql-connector-j-9.0.0.jar`

 5. Ahora deberemos añadir la librería JDBC a nuestro proyecto. Este punto dependerá del IDE que estemos usando, en mi caso con IntelliJ seria en `File/Project Structure (Ctrl+Alt+Shift+S)` , y pulsar el botón `+` para añadir la libreria.

    <img src="assets/addLibraryIntelliJ.png" alt="Añadir Libreria a IntelliJ" style="zoom:50%;" />

 6. Busca en la carpeta descomprimida el archivo `jar` y selecciónalo, te informará de que la librería se añadirá a tu proyecto (pulsa OK) y debería quedar algo así:

    <img src="assets/addedJarToIntelliJ.png" alt="Jar añadido al proyecto" style="zoom:50%;" />

## Controlador MySql (IntelliJ - Maven)

**1. Crear un Nuevo Proyecto con Maven:**

- Al crear un nuevo proyecto en IntelliJ, selecciona "Maven" como sistema de construcción.

  <img src="assets/MavenIntelliJProject.png" alt="Nuevo Proyecto Maven IntelliJ" style="zoom: 50%;" />

- IntelliJ generará la estructura del proyecto y el archivo `pom.xml`.

**2. Importar un Proyecto Existente con Maven:**

- Si ya tienes un proyecto con un `pom.xml`, simplemente importa el proyecto en IntelliJ y selecciona el archivo `pom.xml`. IntelliJ configurará el proyecto automáticamente.

**3. Agregar Dependencias:**

- Abre el archivo `pom.xml` y agrega las dependencias necesarias dentro de la sección `<dependencies> ` (Aquí se muestran dos, MySQL y MariaDB, por ejemplo, agrega solo una!). IntelliJ descargará y configurará automáticamente las dependencias.

```xml
[...]
	<dependencies>
        <!-- Dependencia de MySQL -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.33</version>
        </dependency>
        <!-- Dependencia de MariaDB -->
        <dependency>
            <groupId>org.mariadb.jdbc</groupId>
            <artifactId>mariadb-java-client</artifactId>
            <version>3.5.2</version>
        </dependency>        
    </dependencies>
[...]
```

4. Actualizar Dependencias:

- Si cambias el archivo `pom.xml`, IntelliJ mostrará un botón para cargar los cambios:

<img src="assets/LoadMavenChanges.png" alt="Cargar cambios de Maven" style="zoom:50%;" />

## Tarea

Ahora que conoces las diferencias entre agregar una libreria manualmente o mediante Maven, genera un documento pdf con el siguiente contenido:

1. Después de haber probado las dos maneras de agregar el conector `MySQL` a tu proyecto, explica que método te ha resultado más difícil. Luego, investiga si en el repositorio de central de Maven, siempre está disponible la última versión del controlador `MySQL`, crees que esto puede llegar a ser un problema?
2. Explica en tu documento como agregar los controladores (mediante Maven) para bases de datos Oracle (explica las diferencias entre el `Ojdbc8` y el `Ojdbc11`) y `SQLite`. (Capturas de pantalla y explicaciones, y capturas que demuestren que el proyecto tiene las librerías agregadas).

Envia tu fichero pdf a la tarea de Aules.