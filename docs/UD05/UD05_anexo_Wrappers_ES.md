# Anexo Wrappers

## Wrappers (Envoltorios)

Los wrappers permiten "envolver" datos primitivos en objetos, también se llaman clases contenedoras. La diferencia entre un tipo primitivo y un wrapper es que este último es una clase y por tanto, cuando trabajamos con wrappers estamos trabajando con objetos. 

!!! tip "Recuerda"
    Como son objetos debemos tener cuidado en el paso como parámetro en métodos ya que en el wrapper se realiza por referencia.

Una de las principales ventajas del uso de wrappers son la facilidad de conversión entre tipos primitivos y cadenas.

Hay una clase contenedora por cada uno de los tipos primitivos de Java. Los datos primitivos se escriben en minúsculas y los wrappers se escriben con la primera letra en mayúsculas.

| Tipo primitivo | Wrapper asociado |
| -------------- | ---------------- |
| byte           | Byte             |
| short          | Short            |
| int            | Integer          |
| long           | Long             |
| float          | Float            |
| double         | Double           |
| char           | Char             |
| boolean        | Boolean          |

Cada clase wrapper tiene dos constructores, uno se le pasa por parámetro el dato de tipo primitivo y otro se le pasa un `String`.

Para wrapper `Integer`:

```java
Integer(int)
Integer(String)
```

Ejemplo:

```java
Integer i1 = new Integer(42);
Integer i2 = new Integer ("42");
Float f1 = new Float(3.14f);
Float f2 = new Float ("3.14f");
```

Antiguamente, una vez asignado un valor a un objeto o wrapper `Integer`, este no podía cambiarse. Actualmente e internamente se apoyan en variables y wrapers internos para poder variar el valor de un wrapper.

Ejemplo:

```java
Integer y = new Integer(567);		//Crea el objeto
y++;								//Lo desenvuelve, incrementa y lo vuelve a envolver 
System.out.println("Valor: " + y); 	//Imprime el valor del Objeto y
```

Los wrapper disponen de una serie de métodos que permiten realizar funciones de conversión de datos. Por ejemplo, el wrapper `Integer` dispone de los siguientes métodos:

| Método                                                       | Descripción                                  |
| ------------------------------------------------------------ | -------------------------------------------- |
| `Integer(int)`<br/>`Integer(String)`                         | Constructores                                |
| `byteValue()`<br/>`shortValue()`<br/>`intValue()`<br/>`longValue()`<br/>`doubleValue()`<br/>`floatValue()` | Funciones de conversión con datos primitivos |
| `Integer decode(String)`<br/>`Integer parseInt(String)`<br/>`Integer parseInt(String, int)`<br/>`Integer valueOf(String)`<br/>`String toString()` | Conversión a String                          |
| `String toBinaryString(int)`<br/>`String toHexString(int)`<br/>`String toOctalString(int)` | Conversión a otros sistemas de numeración    |
| `MAX_VALUE`, `MIN_VALUE`, `TYPE`                             | Constantes                                   |

### Métodos `valueOf()`

El método `valueOf()` permite crear objetos wrapper y se le pasa un parámetro `String` y opcionalmente otro parámetro que indica la base en la que será representado el primer parámetro.

Ejemplo:

```java
// Convierte el 101011 (base 2) a 43 y le asigna el valor al objeto Integer i3 
Integer i3 = Integer.valueOf("101011", 2);
System.out.println(i3);

// Asigna 3.14 al objeto Float f3 
Float f3 = Float.valueOf("3.14f");
System.out.println(f3);
```

### Métodos `xxxValue()`.

Los métodos `xxxValue()` permiten convertir un wrapper en un dato de tipo primitivo y no necesitan argumentos.

Ejemplo:

```java
Integer i4 = 120; // Crea un nuevo objeto wrapper
byte b = i4.byteValue(); // Convierte el valor de i4 a un primitivo byte 
short s1 = i4.shortValue(); // Otro de los métodos de Integer
double d = i4.doubleValue(); // Otro de los métodos xxxValue de Integer 
System.out.println(s1); // Muestra 120 como resultado

Float f4 = 3.14f; // Crea un nuevo objeto wrapper
short s2 = f4.shortValue(); // Convierte el valor de f4 en un primitivo short
System.out.println(s2); // El resultado es 3 (truncado, no redondeado)
```

### Métodos `parseXxxx()`

Los métodos `parseXxxx()` permiten convertir un wrapper en un dato de tipo primitivo y le pasamos como parámetro el `String` con el valor que deseamos convertir y opcionalmente la base a la que convertiremos el valor (2, 8, 10 o 16).

Ejemplo:

```java
double d4 = Double.parseDouble("3.14"); // Convierte un String a primitivo 
System.out.println("d4 = " + d4);	// El resultado será d4 = 3.14 
long l2 = Long.parseLong("101010", 2);	// un String binario a primitivo
System.out.println("l2 = " + l2);	// El resultado es l2 = 42
```

### Métodos `toString()`

El método `toString()` permite retornar un `String` con el valor primitivo que se encuentra en el objeto contenedor. Se le pasa un parámetro que es el wrapper y opcionalmente para `Integer` y `Long` un parámetro con la base a la que convertiremos el valor (2, 8, 10 o 16).

Ejemplo:

```java
Double d1 = new Double("3.14");
System.out.println("d1 = " + d1.toString() ); // El resultado es d = 3.14 
String d2 = Double.toString(3.14); // d2 = "3.14"
System.out.println("d2 = " + d2); // El resultado es d = 3.14 
String s3 = "hex = " + Long.toString(254, 16); // s3 = "hex = fe" 
System.out.println("s3 = " + s3); // El resultado es s3 = hex = fe
```

### Métodos `toXxxxxString()` (Binario, Hexadecimal y Octal)

Los métodos `toXxxxxString()` permiten a las clases contenedoras `Integer` y `Long` convertir números en base 10 a otras bases, retornando un `String` con el valor primitivo que se encuentra en el objeto contenedor.

Ejemplo:

```java
String s4 = Integer.toHexString(254); // Convierte 254 a hex 
System.out.println("254 es " + s4); // Resultado: "254 es fe" 
String s5 = Long.toOctalString(254); // Convierte 254 a octal
System.out.println("254(oct) = " + s5); // Resultado: "254(oct) = 376"
```

!!! info "Resumen"
    Para resumir, los métodos esenciales para las conversiones son:

    - **`primitive xxxValue()`** – Para convertir de `Wrapper` a `primitive`
    - **`primitive parseXxx(String)`** – Para convertir un `String` en `primitive`
    - **`Wrapper valueOf(String)`** – Para convertir `String` en `Wrapper`


## Ejemplo Anexo UD05

### `Anexo1Wrappers`

```java
package es.martinezpenya.ejemplos.UD05;

public class Anexo1Wrappers {

    public static void main(String[] args) {

        // WRAPPERS
        //Integer i1 = new Integer(42); // Obsoleto (deprecated)
        Integer i1 = Integer.valueOf(42);
        //Integer i2 = new Integer("42");// Obsoleto (deprecated)
        Integer i2 = Integer.valueOf("42");
        //Float f1 = new Float(3.14f);// Obsoleto (deprecated)
        Float f1 = Float.valueOf(3.14f);
        //Float f2 = new Float("3.14f");// Obsoleto (deprecated)
        Float f2 = Float.valueOf("3.14f");

        Integer y = Integer.valueOf(567);	   //Crea el objeto
        y++;				   //Lo desenvuelve, incrementa y lo vuelve a envolver 
        System.out.println("Valor: " + y); //Imprime el valor del Objeto y     

        // VALUEOF
        // Convierte el 101011 (base 2) a 43 y le asigna el valor al objeto Integer i1 
        Integer i3 = Integer.valueOf("101011", 2);
        System.out.println(i3);

        // Asigna 3.14 al objeto Float f3 
        Float f3 = Float.valueOf("3.14f");
        System.out.println(f3);

        // XXXVALUE
        Integer i4 = 120; // Crea un nuevo objeto wrapper
        byte b = i4.byteValue(); // Convierte el valor de i2 a un primitivo byte 
        short s1 = i4.shortValue(); // Otro de los métodos de Integer
        double d = i4.doubleValue(); // Otro de los métodos xxxValue de Integer 
        System.out.println(s1); // Muestra 120 como resultado

        Float f4 = 3.14f; // Crea un nuevo objeto wrapper
        short s2 = f4.shortValue(); // Convierte el valor de f2 en un primitivo short
        System.out.println(s2); // El resultado es 3 (truncado, no redondeado)

        // PARSEXXXX
        double d4 = Double.parseDouble("3.14"); // Convierte un String a primitivo 
        System.out.println("d4 = " + d4);	// El resultado será d4 = 3.14 
        long l2 = Long.parseLong("101010", 2);	// un String binario a primitivo
        System.out.println("l2 = " + l2);	// El resultado es L2 42

        // TOSTRING
        Double d1 = Double.valueOf("3.14");
        System.out.println("d1 = " + d1.toString()); // El resultado es d = 3.14 
        String d2 = Double.toString(3.14); // d2 = "3.14"
        System.out.println("d2 = " + d2); // El resultado es d = 3.14 
        String s3 = "hex = " + Long.toString(254, 16); // s = "hex = fe" 
        System.out.println("s3 = " + s3); // El resultado es d = 3.14

        // TOXXXSTRING
        String s4 = Integer.toHexString(254); // Convierte 254 a hex 
        System.out.println("254 es " + s4); // Resultado: "254 es fe" 
        String s5 = Long.toOctalString(254); // Convierte 254 a octal
        System.out.println("254(oct) = " + s5); // Resultado: "254(oct) = 376"
    }
}
```
