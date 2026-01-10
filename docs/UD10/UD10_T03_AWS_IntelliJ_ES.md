# Taller UD10_03: BBDD en la nube (AWS) con IntelliJ

## Introducción

La intención de este documento es la de dar una perspectiva más realista del uso del acceso a datos, ya que en lugar de usar la misma máquina del alumno como servidor de BBDD, vamos a desplegar el servidor MariaDB en una máquina alojada en la nube de Amazon (AWS).

## Requisitos

Para realizar esta práctica guiada necesitamos:

- Acceso al Learner Lab proporcionado por el profesor. (https://awsacademy.instructure.com)
- Conocimientos sobre las BBDD, IP's y puertos.
- Un dispositivo local con capacidad de ejecutar un cliente de BBDD, con acceso a los puertos e Ip's de AWS (Ojo con la red de conselleria)

## Guía paso a paso

### Preparar el entorno de la nube

#### Iniciar Laboratorio

Lo primero que necesitamos es arrancar el laboratorio, para ello Accedemos al LMS del awsacademy, buscamos el Curso facilitado por el docente, accedemos a sus contenidos y a continuación al Learner Lab. (Si es la primera vez que accedemos debemos aceptar los términos de uso).

Inicialmente el laboratorio está en rojo:

![Estado inicial del laboratorio](assets/LAB01.png)

Elegimos la opción `Start Lab` y esperamos a que aparezca el laboratorio en verde:

![Laboratorio iniciado correctamente](assets/LAB02.png)

Por defecto el Learner Lab nos proporciona 100 dolares de saldo, y un tiempo de 4 horas, tras el cual se detendrán la mayoría de servicios que tengamos en marcha. Pero mientras quede saldo podemos volver a iniciar el Laboratorio y dispondremos de 4 horas más.

Una vez aparece en verde podemos hacer click sobre las letras AWS y aparecerá el Dashboard de AWS (debemos permitir las ventanas emergentes):

![Dashboard AWS](assets/LAB03.png)

#### Crear una BD en AWS

Debemos buscar el apartado Amazon RDS (ahora se llama Aurora y RDS):

![Buscar RDS](assets/RDS01.png)

Una vez aquí debemos pulsar el botón `[Crear base de datos]`:

![Screenshot_20230404_113411](assets/RDS02.png)

Ahora debemos elegir las opciones para nuestra base de datos:

Al `Crear base de datos` dejamos la `Creación estándar` por defecto:

![Método de creación](assets/RDS03a.png)

En `Opciones del motor` elegimos `MariaDB` (Como versión puedes elegir la más moderna que aparezca):

![Opciones del motor](assets/RDS03b.png)

En `Plantillas` elegimos la `Capa gratuita`:

![Plantillas](assets/RDS03c.png)

A continuación, en `Configuración`:

Elegimos el `Identificador de instancias de bases de datos`, podemos poner el que más nos guste, en mi caso `databaseDMP`, también debemos indicar el `username`, en mi caso `admin`, y por último la `Contraseña maestra` y su confirmación, que deberá tener más de 8 carácteres ASCII imprimibles, en mi caso `123456Ab$`. 

> ### Anota todos estos datos en un lugar seguro, los necesitarás más adelante.

![Apartado Configuración](assets/RDS04.png)

En la `Configuración de la instancia` dejamos todo por defecto (ahora db.t4g.micro):

![Screenshot_20230404_114838](assets/RDS05.png)

En `Almacenamiento` dejamos el Almacenamiento asignado en 20GiB y deshabilitamos el escalado automático del almacenamiento:

![Screenshot_20230404_114929](assets/RDS06.png)

Dejamos `Disponibilidad y durabilidad` por defecto.

![Disponibilidad y durabilidad](assets/RDS07.png)

En el apartado `Conectividad` dejamos todo por defecto excepto la opción de `Acceso público` que debemos indicar que `Sí`:

![Conectividad](assets/RDS08.png)

En la parte baja elegiremos crear un nuevo `Grupo de seguridad de VPC` y el puerto `3306`, el resto de opciones por defecto:

![Grupo de seguridad](assets/RDS08b.png)

> ### OJo! aunque el puerto 3306 debería estar abierto el la red del instituto, he encontrado ocasiones en las que no ha funcionado correctamente, si te sucede esto, puedes cambiar al puerto 6000 o alguno de los que te sugiera tu profesor.

En el apartado `Configuración adicional` indicamos `starwars` como nombre de la base de datos inicial y cambiamos el periodo de retención de copias a `1 dia`:

![Configuración adicional](assets/RDS08c.png)

dejamos el resto de opciones por defecto y pulsaremos el botón del final `[Crear base de datos]`:

![Crear base de datos](assets/RDS09.png)

Si todo ha ido bien AWS nos indica que se está creando la BD y puede tardar varios minutos:

![Creando BD](assets/RDS10.png)

Una vez aparezca el estado en `Disponible`, podremos pasar al siguiente paso:

![Screenshot_20230404_120627](assets/RDS11.png)

#### Abrir puertos para el acceso público

Ahora abriremos el puerto necesario para la que la BD sea accesible desde el exterior, para ello haremos clic sobre el nombre de la base de datos:

![Clic en el nombre de la BD](assets/RDS12.png)

Y en la siguiente ventana hacemos click sobre el `Grupo de seguridad de la VPC` :

![Grupo de seguridad](assets/RDS13bis.png)

Una vez estamos en el apartado de Grupos de seguridad, debemos elegir la pestaña `Reglas de entrada`, y el botón `Editar reglas de entrada`:

![Editar reglas de entrada](assets/RDS14.png)

Si hemos seguido correctamente la guia debería aparecer el puerto 3306 abierto, pero solo para la ip pública desde la que estamos accediendo, así que deberemos pulsar la x para eliminar esa ip:

![Puerto 3306](assets/RDS15.png)

Y por último agrega la ip 0.0.0.0 para que sea acesible desde cualquier lugar:

![ip 0.0.0.0](assets/RDS16.png)

#### Dirección pública de la BBDD

Ahora necesitamos la URL de acceso a la BD desde el exterior, primero volvemos al apartado RDS:

![Buscar RDS](assets/RDS01.png)

y a continuación haremos clic sobre el nombre de la base de datos:

![Clic en el nombre de la BD](assets/RDS12.png)

Y en la siguiente ventana encontraremos los datos que necesitamos, por un lado el `Punto de enlace` (`databasedmp.cm6pc9b4jil5.us-east-1.rds.amazonaws.com`) y por otro el `Puerto` (`3306`):

![Punto de enlace y puerto](assets/RDS13.png)

Con toda esta información podemos realizar conexiones desde el exterior.

### Carga de datos desde IntelliJ

#### Instalar MySQL WorkBench

Dependiendo de nuestro sistema operativo deberemos usar un procedimiento u otro, lo mejor es consultar la página web y seguir sus instrucciones:

https://www.mysql.com/products/workbench/

#### Conexión de prueba

Una vez instalado nuestro cliente configuraremos una nueva conexión con los datos que hemos guardado en pasos anteriores, indicaremos el `Connection Name` (nombre de la conexión), `Hostname` (URL de la base de datos), y `username` (usuario de la base de datos). Al pulsar el botón `Test Connection`, nos permite probar la conexión y nos pedirá el `password`, y si pulsamos `OK` se guardará.

![Crear conexión](assets/WB01.png)

Es posible que nos indique que puede haber problemas de compatibilidad, pero podemos dar a `Continue anyway` sin preocuparnos.

![Continue anyway](assets/WB02.png)

Y deberíamos ver nuestro entorno de modo similar a este:

![Entorno](assets/WB03.png)

#### Importar datos de muestra

Para no trabajar con una base de datos vacía partiremos de una base de datos con información que podemos encontrar en el siguiente enlace: https://github.com/miguelmarti/FreakDataBases

En concreto usaremos la de [StarWars.sql](https://github.com/miguelmarti/FreakDataBases/blob/main/StarWars.sql), la descargaremos de github, abriremos el archivo con nuestro editor preferido, copiaremos todo su contenido y lo pegaremos en la ventana blanca del entorno. A continuación pulsamos el rayo para ejecutar el script, y por último el botón para refrescar el contenido de las tablas:

![Pegar starwars.sql](assets/WB04.png)

Una vez hecho todo esto debería tener al menos 7 tablas:

![Screenshot_20230404_163800](assets/WB05.png)



Cuando comprobemos que tenemos la 7 tablas, podemos seguir.

### Preparar el cliente local

#### Descargar MySQL connector

Tal y como vimos en el taller [UD10_T02_Conectores_ES](UD10_T02_Conectores_ES.md), añade el conector a tu proyecto (mediante jar o maven, como prefieras.)


#### Código del cliente

En nuestro IDE preferido creamos un nuevo archivo `AWSTest.java` con el siguiente código:

```java
package UD10.AWS;

import java.sql.*;
import java.util.Scanner;

/**
 *
 * @author David Martínez (wwww.martinezpenya.es|ieseduardoprimo.es)
 */
public class AWSTest {

    private static final String AWSDNS = "databasedmp.cm6pc9b4jil5.us-east-1.rds.amazonaws.com";
    private static final String DBNAME = "starwars";
    private static final int PUERTO = 3306;
    private static final String USERNAME = "admin";
    private static final String PASSWORD = "123456Ab$";

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        try (Connection con = DriverManager.getConnection("jdbc:mysql://" + AWSDNS + ":" + PUERTO + "/" + DBNAME, USERNAME, PASSWORD);) {
            Statement stmt = con.createStatement();
            //Query sin parámetros
            ResultSet rs = stmt.executeQuery("select * from films");
            System.out.println("Estas son las películas de Star Wars");
            while (rs.next()) {
                System.out.println(rs.getInt(1) + "  " + rs.getString(2) + "  " + rs.getString(3));
            }
            System.out.print("Elige un número de película y te mostraré los personajes que aparecen en ella: ");
            String numPelicula = sc.nextLine();
            PreparedStatement pStmt = con.prepareStatement("SELECT C.id, name, C.height, C.mass, C.hair_color, C.skin_color "
                    + "FROM starwars.characters C, starwars.character_films CF, starwars.films F "
                    + "WHERE F.id=CF.id_film AND CF.id_character=C.id "
                    + "AND CF.id_film = ?;");
            pStmt.setString(1, numPelicula);
            //Query con parámetros
            ResultSet rs2 = pStmt.executeQuery();
            while (rs2.next()) {
                System.out.println(rs2.getInt(1) + "  " + rs2.getString(2) + "  " + rs2.getInt(3) + "  " + rs2.getFloat(4) + "  " + rs2.getString(5) + "  " + rs2.getString(6));
            }
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

> ### Recuerda cambiar la constante `AWSDNS`, `DBNAME`, `PUERTO`, `USERNAME` y `PASSWORD` por el `String` o `int` que corresponda con tu configuración.

### Ejecución de prueba

#### Desde el punto de vista del cliente

Una vez ejecutado el cliente debe aparecer algo similar a esto:

```sh
Estas son las películas de Star Wars
1  Episode I  The Phantom Menace
2  Episode II  Attack of the Clones
3  Episode III  Revenge of the Sith
4  Episode IV  A New Hope
5  Episode V  The Empire Strikes Back
6  Episode VI  Return of the Jedi
Elige un número de película y te mostraré los personajes que aparecen en ella: 
```

Y si a continuación elegimos por ejemplo la película 4:

```sh
Elige un número de película y te mostraré los personajes que aparecen en ella: 4
1  Luke Skywalker  172  77.0  blond  fair
2  C-3PO  167  75.0  n/a  gold
3  R2-D2  96  32.0  n/a  white, blue
4  Darth Vader  202  136.0  none  white
5  Leia Organa  150  49.0  brown  light
6  Owen Lars  178  120.0  brown, grey  light
7  Whitesun lars  165  75.0  brown  light
8  R5-D4  97  32.0  n/a  white, red
9  Biggs Darklighter  183  84.0  black  light
10  Obi-Wan Kenobi  182  77.0  auburn, white  fair
12  Wilhuff Tarkin  180  0.0  auburn, grey  fair
13  Chewbacca  228  112.0  brown  null
14  Han Solo  180  80.0  brown  fair
15  Greedo  173  74.0  n/a  green
18  Wedge Antilles  170  77.0  brown  fair
19  Jek Tono Porkins  180  110.0  brown  fair
81  Raymus Antilles  188  79.0  brown  light
89  Cornelius Evazan  0  0.0  null  null
90  Ponda Baba  0  0.0  null  null
```

> ## **Warning SLF4J**
>
> Si te aparece el mensaje siguiente:
>
> ```
> SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
> SLF4J: Defaulting to no-operation (NOP) logger implementation
> SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
> ```
>
> Aunque es un **warning** y no debe afectar al funcionamiento de tus programas, resolver el error es tan sencillo como añadir una dependencia más:
>
> ```xml
> <!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-api -->
> <dependency>
>     <groupId>org.slf4j</groupId>
>     <artifactId>slf4j-simple</artifactId>
>     <version>2.0.17</version>
> </dependency>
> ```

## Tarea

Ahora que has visto como crear una BBDD en AWS:

1. Genera una nueva BBDD con el motor que prefieras (MySQL, MariaDB, Oracle, etc...)
2. Carga una Base de Datos que puedas conseguir por tu cuenta, que crees desde cero, o a partir de las que te proporciona el profesor. La condición es que debe tener al menos 3 tablas, al menos dos de ellas deben estar relacionadas, y debes tener al menos 10 registros (información) en cada una de las tablas.

   Comenta con el profesor  (por correo electrónico) la BBDD que usaras para evitar que dos alumnos usen la misma (en caso que uses una que encuentres por Internet).
3. Esta nueva Base de Datos será la que usaras para completar la [siguiente tarea](UD10_T04_DAO_ES.md), así que quizá deberías echarle un ojo antes de tomar la decisión.

Envía una memoria en fichero **pdf** explicando los pasos seguidos (con capturas) a la tarea de **Aules** correspondiente.