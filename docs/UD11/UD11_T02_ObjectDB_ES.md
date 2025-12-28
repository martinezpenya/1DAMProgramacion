---
title: Taller UD11_1: Añadir ObjectDB a un proyecto IntelliJ (Maven)
language: ES
author: David Martínez Peña [www.martinezpenya.es]
subject: Programación
keywords: [PRG, 2025, Programacion, Java]
IES: IES Eduardo Primo Marqués (Carlet)
header: ${title} - ${subject} (ver. ${today}) 
footer:${currentFileName}.pdf - ${author} - ${IES} - ${pageNo}/${pageCount}
typora-root-url:${filename}/../
typora-copy-images-to:${filename}/../assets
---


[toc]

# Que es ObjectDB

**ObjectDB** es un potente sistema de gestión de bases de datos orientado a objetos (`ODBMS`). Es compacto, fiable, fácil de usar y extremadamente rápido. **ObjectDB** proporciona todos los servicios estándar de administración de bases de datos (almacenamiento y recuperación, transacciones, administración de bloqueos, procesamiento de consultas, etc.), pero de una manera que facilita el desarrollo y acelera las aplicaciones.

## Características clave de la base de datos **ObjectDB**

- Sistema de gestión de bases de datos orientado a objetos (ODBMS) 100% puro Java.
- Sin API propietaria - administrado únicamente por API de Java estándar (JPA 2 / JDO 2).
- Extremadamente rápido: más rápido que cualquier otro producto JPA/JDO.
- Adecuado para archivos de bases de datos que van desde kilobytes hasta terabytes.
- Admite tanto el modo Cliente-Servidor como el modo Integrado.
- JAR único sin dependencias externas.
- La base de datos se almacena como un único archivo.
- Capacidades avanzadas de consulta e indexación.
- Efectivo en entornos multiusuario con mucha carga.
- Puede integrarse fácilmente en aplicaciones de cualquier tipo y tamaño.
- Probado con Tomcat, Jetty, GlassFish, JBoss y Spring.

**ObjectDB** se puede descargar y utilizar **sin coste (incluso comercialmente)** con la restricción de un máximo de **10 clases de entidad** y **un millón de objetos de entidad** por archivo de base de datos. Esto podría ser útil para proyectos pequeños, tareas académicas, evaluación y aprendizaje. **ObjectDB** es un software comercial y su uso sin estas restricciones [requiere la compra de una licencia](https://www.objectdb.com/database/license).

Se recomienda probar **ObjectDB** antes de comprar una licencia.

Más información sobre tipos de licencias: https://www.objectdb.com/database/purchase

# Añadir ObjectDB mediante Maven

**1. Crear un Nuevo Proyecto con Maven:**

- Al crear un nuevo proyecto en IntelliJ, selecciona "Maven" como sistema de construcción.

  <img src="/assets/T1_crea_proyecto_maven.png" alt="Craer proyecto Maven de Java" style="zoom: 67%;" />

- IntelliJ generará la estructura del proyecto y el archivo `pom.xml`.

<img src="/assets/T1_nuevo_proyecto_pomxml.png" alt="image-20250501110018265" style="zoom:67%;" />

**2. Agregar Dependencias:**

- Abre el archivo `pom.xml` y agrega el repositorio y las dependencias necesarias. 

```xml
[...]
	<repositories>
		<repository>
			<id>objectdb</id>
			<name>ObjectDB Repository</name>
			<url>https://m2.objectdb.com</url>
		</repository>
	</repositories>

	<dependencies>
		<dependency>
			<groupId>com.objectdb</groupId>
			<artifactId>objectdb</artifactId>
			<version>2.8.1</version>
		</dependency>
	</dependencies>
[...]
```

**3. Actualizar Dependencias:**

- Si cambias el archivo `pom.xml`, IntelliJ mostrará un botón para cargar los cambios:

![image-20250501110419123](/assets/T1_boton_pom.png)

# Tu primer proyecto con ObjectDB

En la web del proyecto ObjectDB puedes descargar un tutorial con un proyecto ya creado para ver como funciona, pero nosotros lo vamos a crear desde cero.

1. Código fuente de la clase `Punto.java`

   Dentro de la carpeta `src/main/java` crea una nueva clase llamada `Punto.java` con el siguiente contenido:

   ```java
   import javax.persistence.Entity;
   import javax.persistence.GeneratedValue;
   import javax.persistence.Id;
   
   @Entity
   public class Punto {
       @Id
       @GeneratedValue
       private long id;
   
       private int x;
       private int y;
   
       public Punto() {
       }
   
       Punto(int x, int y) {
           this.x = x;
           this.y = y;
       }
   
       public Long getId() {
           return id;
       }
       public int getX() {
           return x;
       }
       public int getY() {
           return y;
       }
       public void setId(long id) {
           this.id = id;
       }
       public void setX(int x) {
           this.x = x;
       }
       public void setY(int y) {
           this.y = y;
       }
   
       @Override
       public String toString() {
           return String.format("(%d, %d)", this.x, this.y);
       }
   }
   ```

2. En la misma ruta, crea la clase `TestPunto.java`:

   ```java
   import javax.persistence.*;
   import java.util.List;
   
   public class TestPunto {
       public static void main(String[] args) {
           // Abre una conexión a la base de datos
           // Se crea un EntityManagerFactory con la configuración especificada en el archivo de persistencia
           EntityManagerFactory emf = Persistence.createEntityManagerFactory("src/main/java/DB/puntos.odb");
           // Se crea un EntityManager para interactuar con la base de datos
           EntityManager em = emf.createEntityManager();
   
           // Almacena 1000 objetos Punto en la base de datos
           // Inicia una transacción
           em.getTransaction().begin();
           for (int i = 0; i < 1000; i++) {
               // Crea un nuevo objeto Punto con coordenadas aleatorias entre 0 y 99
               Punto p = new Punto((int) (Math.random() * 100), (int) (Math.random() * 100));
               // Persiste el objeto Punto en la base de datos
               em.persist(p);
           }
           // Confirma la transacción para guardar los cambios
           em.getTransaction().commit();
   
           // Consulta para contar los objetos Punto
           Query q1 = em.createQuery("SELECT COUNT(p) FROM Punto p");
           // Imprime el resultado de la consulta
           System.out.println("Número total de Puntos: " + q1.getSingleResult());
   
           // Consulta para calcular el promedio de X
           Query q2 = em.createQuery("SELECT AVG(p.x) FROM Punto p");
           // Imprime el resultado de la consulta
           System.out.println("Media de los puntos X: " + q2.getSingleResult());
   
           // Consulta para obtener todos los objetos Punto
           TypedQuery<Punto> query = em.createQuery("SELECT p FROM Punto p", Punto.class);
           // Obtiene la lista de resultados
           List<Punto> results = query.getResultList();
           System.out.println("Resultados de la consulta query:");
           for (Punto p : results) {
               // Imprime cada objeto Punto
               System.out.println(p);
           }
   
           // Cierra la conexión a la base de datos
           // Cierra el EntityManager
           em.close();
           // Cierra el EntityManagerFactory
           emf.close(); 
       }
   }
   ```

3. Crea la BDOO:

   Una vez creado todo el proyecto, y comprobado que no tenga errores de compilación, ejecuta el método `main` de la clase `TestPunto` y veras aparecer una carpeta llamada `DB` en la ruta que contiene un único fichero `puntos.odb`.

   <img src="/assets/T1_ruta_DB.png" alt="image-20250501113351121" style="zoom:67%;" />

   

4. El resultado en pantalla debe ser similar a este:

   ```sh
   Número total de Puntos: 1000
   Media de los puntos X: 49.05433333333333
   (96, 19)
   (40, 65)
   (87, 97)
   (24, 26)
   (46, 19)
   (28, 79)
   (32, 18)
   (51, 18)
   (64, 22)
   ...
   ```

> ### Puede que hayas observado que la palabra Punto dentro de las consultas SQL aparece subrayado en rojo. Eso es porque IntelliJ no detecta la clase Punto como una entidad JPA:
>
> ![image-20250501114711764](/assets/T1_Punto_not_JPA.png)
>
> La solución es tan simple como hacer clic en la bombilla roja que aparece, y elegir la opción de que IntelliJ nos añada el complemento necesario de JPA para "entender" la persistencia de datos.
>
> ![image-20250501114846651](/assets/T1_add_JPA_facet.png)

Ten en cuenta que cada vez que ejecutas el código se añaden 1000 puntos más a la BDOO, así que si lo ejecutas un par de veces más tendras 3000 puntos en la base de datos.

Si quieres volver a empezar solo debes borrar el fichero `*.odb` y al volver a ejecutar el código se generará de nuevo el fichero con 1000 puntos.

# Actividades

Ahora genera un documento `pdf` con el siguiente contenido:

1. Explica para que sirven las etiquetas (`@Entity`, `@Id`, `@GeneratedValue` y `@Override`) que aparecen en la clase `Punto`.
1. Modifica la clase `TestPunto.java` para que la base de datos se cree en la ruta `bdoo` en luga de `DB` y el fichero `.odb` tenga tu nombre (en mi caso `david.odb`).
3. Modifica el método `main` y añade dos consultas más `q3`, `q4` y `q5` que muestren:
   1. `q3`: La media de los puntos Y.
   2. `q4`: consulte los puntos en los que la X o la Y sean superiores a 50.
   3. `q5`: consulta los puntos ordenando primero descendientemente por la X, y en caso de empate ascendentemente por la Y.


Envía tu fichero `pdf` con explicaciones detallas sobre los cambios requeridos, adjuntando fragmentos del código añadido (con capturas de pantalla o recortes de código fuente) a la tarea de Aules.

# Fuentes de información

- [Wikipedia](https://es.wikipedia.org)
- [Programación (Grado Superior) - Juan Carlos Moreno Pérez (Ed. Ra-ma)](https://www.ra-ma.es/libro/programacion-grado-superior_48302/)
- Apuntes IES Henri Matisse (Javi García Jimenez?)
- Apuntes AulaCampus
- [Apuntes José Luis Comesaña](https://www.sitiolibre.com/)
- [Apuntes IOC Programació bàsica (Joan Arnedo Moreno)](https://ioc.xtec.cat/materials/FP/Recursos/fp_asx_m03_/web/fp_asx_m03_htmlindex/index.html)
- [Apuntes IOC Programació Orientada a Objectes (Joan Arnedo Moreno)](https://ioc.xtec.cat/materials/FP/Recursos/fp_dam_m03_/web/fp_dam_m03_htmlindex/index.html)
- [FXDocs](https://github.com/FXDocs/docs)
- https://openjfx.io/openjfx-docs/
- https://arturoblasco.github.io/pr
