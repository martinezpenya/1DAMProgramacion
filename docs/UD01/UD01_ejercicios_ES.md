# Ejercicios de la UD01

## Retos

1. (Reto1) Haga un programa que evalúe una expresión que contenga literales de los cuatro tipos de datos  (booleano, entero, real y carácter) y la muestre por pantalla.

2. (Reto2) En su entorno de trabajo, cree el programa siguiente. Obsérvese que  pasa exactamente. Entonces, intente arreglar el problema.

    ```java
    // Un programa que usa un entero muuuuy grande
    public class TresMilMilions {
    	public static void main (String [] args) {
    		System.out.println (3000000000);
    	}
    }
    ```

3. (Reto3) 3. Reto 3: Haga un programa con dos variables que, sin usar ningún literal ninguna parte excepto para  inicializar estas variables, vaya estimando e imprimiendo sucesivamente  los 5 primeros valores de la tabla de multiplicar del 4. Puede usar  operadores aritméticos y de asignación, si desea.

4. (Reto4) 4. Reto 4: Haga dos programas, uno que muestre por pantalla la tabla de multiplicar del 3, y otro, la del 5. Los dos deben ser exactamente  iguales, letra por letra, excepto en un único literal dentro de todo el  código.

5. (Reto5) 5. Reto 5:  Experimente qué pasa si en el siguiente programa inicializa la variable  realLargo con un valor con varios decimales. El programa continúa  compilando? ¿Qué resultado da? Después inténtelo asignando un valor  superior al rango de los enteros (por ejemplo, 3000000000.0).

    ```java
    public class ConversionExplicita {
    public static void main (String [] args) {
    double realLlarg = 3000000000.0;
    // Asignación incorrecta. ¿Un real tiene decimales, no?
    long enterLlarg = (long) realLlarg;
    // Asignación incorrecta. ¿Un entero largo tiene un rango mayor que un entero, no?
    int enter = (int) enterLlarg;
    System.out.println (enter);
    }
    }
    ```

6. (Reto6) 6. Reto 6: Haga un programa que muestre en pantalla de forma tabulada la tabla de verdad de una  expresión de disyunción entre dos variables booleanas.

7. (Reto7) 7. Reto 7: Haga un programa que muestre por pantalla la multiplicación de tres números reales entrados por teclado.

## Ejercicios

 Solo se puede usar en esta actividad ya que no se a explicado en profundidad en este tema y lo pueden confundir con el  `System.console().readLine()`; 

1. (EJS1) Probar la E/S elemental: Escribe el pequeño programa que aparece a continuación.

    ```java
    import java.util.*;
    public class EntradaSalida {
        public static void main (String [] arg) {
            Scanner tec = new Scanner(System.in);
            int a, b;
            System.out.println("Introduce un número entero");
            a = tec.nextInt();
            System.out.println("Introduce otro número entero");
            b = tec.nextInt();
            System.out.println("Los números introducidos son " + a + " y " + b);
        }
    }
    ```

    Ejecútalo para ver como se comporta el programa.

    ¿Qué ocurre si cuando nos pide un número entero le damos un número real? ¿Y si le damos un carácter no numérico?

    ¿Qué ocurre si eliminamos la instrucción `import java.util.*`;

2. (EJS2) 2. Averigua mediante pruebas:

    1. ¿Es posible escribir dos instrucciones en la misma línea de un programa?
    2. ¿Se puede "romper" una instrucción entre varias líneas?
    3. Algunos lenguajes de programación dan un valor por defecto a las variables cuando las declaramos sin inicializarlas. Otros no permiten usar el contenido de una variable que no haya sido previamente inicializada. ¿Cuál es comportamiento de Java? 

3. (EJS3) 3. ¿Cuáles de los siguientes identificadores son válidos y cuales no? Pruébalos cuando tengas duda
    1. `n`
    2. `MiProblema`
    3. `MiJuego`
    4. `Mi Juego`
    5. `Int`
    6. `Jose&Co`
    7. `A b`
    8. `1rApellido`
    9. `aaaaaaaaaaaa`
    10. `NombreApellidos` 
    11. `Saldo-actual` 
    12. `Universidad Alicante`
    13. `Juan=Rubio`
    14. `Edad5`
    15. `_5Java`
    16. `true`
    17. `_false`
    18. `f_alse`

4. (Por2) Escribir un programa que lea un entero desde teclado, lo multiplique por 2, y a continuación escriba el resultado en la pantalla:

    Ejemplo de ejecución:

    ```sh
    Escribe un número:
    3
    El doble de 3 es 6
    ```

5. (Intercambio) Escribir un programa que …

    1. Lea desde teclado dos valores enteros. Llama a las variables v1 y v2.
    2. Muestre los valores introducidos por el usuario
    3. Intercambie el valor de v1 y v2 (v1 pasa a  valer lo que valía v2 y viceversa)
    4. Muestre de nuevo los valores, ahora con su valor intercambiado

    Ejemplo de ejecución:

    ```sh
    Escribe un número para v1: 2
    Escribe un número para v2: 9
    Antes de intercambiar	 v1: 2   y	 v2: 9
    Después de intercambiar	 v1: 9	 y	 v2: 2
    ```

6. (ExpresionesMatematicas) 6. Escribir las siguientes expresiones siguiendo la sintaxis de Java.
    1. $\frac{x}{y}+1$
    2. $\frac{x+y}{x-y}$
    3. $[ \frac{b}{c+d}]$
    4. $(a+b)²$
    5. $\frac{x+\frac{y}{2}}{x-\frac{y}{z}}$
    6. $\frac{xy}{1-4Zx}$
    7. $(a+b)\frac{c}{d}$
    8. $\frac{xy}{mn}$

7. (Superficie) Escribir un programa que solicite al usuario la longitud y la anchura de una habitación y a continuación muestre su superficie (longitud por anchura).

8. (Medidas) Escribir un programa que convierta una medida dada en pies a sus equivalentes en yardas, pulgadas, centímetros  y metros, sabiendo que 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 cm, 1 m = 100 cm.

9. (Segundos) Escribir un programa que, dada una cantidad de segundos, introducida por teclado, la desglose en días, horas, minutos y segundos.  

    Ejemplo de ejecución: 

    ```sh
    Introduce cantidad de segundos: 3661
    3661 segundos son:
    0 dias
    1 horas
    1 minutos
    1 segundos
    ```

10. (Fuerza) La fuerza de atracción entre dos masas m1 y m2 separadas por una distancia d, está dada por la fórmula:
    $$
    F= \frac{(G · m1 · m2)}{d^2}
    $$

    *donde G es la constante de gravitación universal G= 6.67430 · 10 ^–11^.* 

    Escribir un programa que lea la masa de dos cuerpos y la distancia entre ellos y a continuación obtenga su fuerza de atracción.

11. (Círculo) Escribir un programa que calcule la longitud de la circunferencia y el área del círculo para un valor del radio introducido por teclado.

12. (Dados) Escribir un programa que simula el lanzamiento de dos dados.

    ```sh
    Dado 1 : 5
    Dado 2: 4
    Puntuación total: 9
    ```

13. (UltimaCifra) Escribir un programa que muestre la última cifra de un número entero que introduce el usuario por teclado. *Pista: ¿Qué devuelve a%10 ?*

    ```sh
    Introduce un número entero: 3761
    La última cifra de 3761 es 1
    ```
    
14. (PenultimaCifra) Escribir un programa que muestre la penúltima cifra de un número entero que introduce el usuario por teclado.

    ```sh
    Introduce un número entero: 3761
    La penúltima cifra de 3761 es 6
    ```
    
    Una vez hayas comprobado que el programa funciona correctamente, prueba qué ocurre si el usuario introduce un valor de una sola cifra (por ejemlo 4). Explica el resultado mostrado por el programa.
    
15. (Redondear1) `Math.round(x)` redondea x de manera que este queda sin decimales. (*`Math.round(35.5289)` da como resultado `36`)*

    Trata de escribir un programa en el que el usuario introduzca un número real y a continuación se muestre redondeado a un decimal. *Pista : combinar productos, divisiones y Math.round()*

    Ejemplo de ejecución:

    ```sh
    Introduce un número real: 35.5289
    El número 35.5289, redondeado a un decimal es 35.5
    ```

16. (ExpresionesAritmeticas) 16. Cuál es el valor resultante de dada una de las siguientes expresiones
    1. `5 * 4 – 3 * 6`
    2. `4 * 5 * 2`
    3. `(24 + 2 * 6) / 4`
    4. `8 / 2 / 2 * 5`
    5. `3 + 4 * (8  * (4 –  (9 + 3) /  6 ))`
    6. `4 * 3 * 5 + 8 * 4 * 2`
    7. `4 – 40 % 5`
    8. `4 * 3 / 2`
    9. `4 / 2 * 3`
    10. `213 /100`

17. (Einstein) La famosa ecuación de Einstein para la conversión de una masa m en energía viene dada por la fórmula E=mc^2^, donde c es la velocidad de la luz que vale 2.997925 · 10^8^ m/s. Escribir un programa que lea el valor de la masa y obtenga la energía correspondiente según la anterior fórmula.

18. (FragmentosCodigo) Indica cuales serán los valores de las variables después de ejecutar cada uno de los siguientes fragmentos de código. Resuelve el ejercicio sin escribir los programas correspondientes y probarlos.

    1. ```java
       int a=3, b = 2;
       a = b + b;
       b = a + a;
       ```

    2. ```java
       int a=3,b=0;
       b = b - 1;
       a = a + b;
       ```

    3. ```java
       int a, b=5;
       b++;
       ++b;
       a= b+1;
       ```

    4. ```java
       int a = 5,b;
       b = a++;
       ```

    5. ```java
       int a = 5,b;
       b = ++a;
       ```

    6. ```java
       int a=2, b=3;
       b+=a;
       ```

    7. ```java
       int a=2, b=3;
       b-=a;
       a=-b;
       ```

    8. ```java
       int a=2, b=3;
       b%=a;
       ```

    9. ```java
       int a=2,b=3,c=4;
       a = --b + c++;
       b+=a;
       ```

## Expresiones Lógicas

1. Sean 4 variables enteras:

    ```java
    int m, j, p, v ;
    ```
    
    que contienen respectivamente la edad de Miguel, Julio, Pablo y Vicente. 
    
    Expresar las siguientes afirmaciones utilizando operadores lógicos y relacionales
    
    *Ejemplo*: `Miguel es mayor de edad.`
    
    *Solución*: `m >= 18`

    1. (Logica1) 1. Miguel es menor de edad.
    2. (Logica2) 2. Miguel es mayor que Julio
    3. (Logica3) 3. Miguel es el más viejo.
    4. (Logica4) 4. Miguel es el más joven.
    5. (Logica5) 5. Miguel no es el más joven.
    6. (Logica6) 6. Miguel no es el más viejo.
    7. (Logica7) 7. Alguno de ellos es mayor de edad.
    8. (Logica8) 8. Miguel y Julio son los más jóvenes.
    9. (Logica9) 9. Entre todos tienen más de 100 años.
    10. (Logica10) 10. Entre Miguel y Julio suman más edad que Pablo.
    11. (Logica11) 11. Entre Miguel y Julio suman más edad que Pablo y Vicente juntos.
    12. (Logica12) 12. Si los ordenamos por edades de menor a mayor, Julio es el segundo.
    13. (Logica13) 13. Si los ordenamos por edades de menor a mayor, Julio es el segundo y Pablo el tercero.
    14. (Logica14) 14. Al menos uno de ellos es menor de edad.
    15. (Logica15) 15. Al menos dos de ellos son menores de edad.
    16. (Logica16) 16. Todos son menores de edad.
    17. (Logica17) 17. Solo dos de ellos son menores de edad.
    18. (Logica18) 18. Al menos dos de ellos nacieron el mismo año.
    19. (Logica19) 19. Solo dos de ellos nacieron el mismo año.
    20. (Logica20) 20. Al menos uno de ellos es menor que Julio
    21. (Logica21) 21. Solo uno de ellos es menor que Julio
    22. (Logica22) 22. Miguel es mayor de edad y alguno de los otros es menor de edad.

## Actividades

1. (Actividad1) 1. Realiza un conversor de euros a pesetas. La cantidad de euros que se quiere convertir debe ser  introducida por teclado.

2. (Actividad2) 2. Realiza un conversor de pesetas a euros. La cantidad de pesetas que  se quiere convertir debe ser introducida por teclado.

3. (Actividad3) 3. Escribe un programa que calcule el área de un rectángulo. (`area = base * altura`)

4. (Actividad4) 4. Escribe un programa que calcule el área de un triángulo. (`area = (base * altura) / 2`)

5. (Actividad5) 5. Escribe un programa que calcule el salario semanal de un empleado en base a las horas trabajadas, a razón de 12 euros la hora.

6. (Actividad6) 6. Realiza un conversor de MiB a KiB. [Ayuda](https://es.wikipedia.org/wiki/Prefijo_binario)

7. (Actividad7) 7. Realiza un conversor de Kib a Mib. [Ayuda](https://es.wikipedia.org/wiki/Prefijo_binario)

8. (Actividad8) 8. Realiza un programa en Java que genere letras de forma aleatoria.

9. (Actividad9) 9. Realiza un programa en Java que genere el número premiado del Cupón de la ONCE.

10. (Actividad10) 10. Modificar el siguiente programa para que compile y funcione:

    ```java
    public class Activ10 {
        public static void main(String[] args) {
            int n1 = 50, int n2 = 30,
            boolean suma = 0;
            suma = n1 + n2;
            System.out.println("LA SUMA ES: " + suma);
        }
    }
    ```

11. (Actividad11) Modificar el siguiente programa para que compile y funcione:

    ```java
    public class Activ11 {
    	public static void main(String[] args) { 
           	int numero = 2;
    		cuad = numero * número;
    		System.out.println("EL CUADRADO DE "+NUMERO+" ES: "+cuad);
    	}
    }
    ```

12. (Actividad12) Indicar que valor devolverá la ejecución del siguiente programa:

    ```java
    public class Activ12 {
    	public static void main(String[] args) {
        	int num = 5;
    		num += num - 1 * 4 + 1;
        	System.out.println(num);
    	}
    }
    ```

13. (Actividad13) Indicar que valor devolverá la ejecución del siguiente programa:

    ```java
    public class Activ13 {
    	public static void main(String[] args) {
           	int num = 4;
    		num %= 7 * num % 3 * 3;   
            System.out.println(num);
    	}
    }
    ```

14. (Actividad14) Realizar un programa que muestre por pantalla respetando los saltos de carro el siguiente texto (con un solo `println`):

    ```sh
    Me gusta la programación
    cada día más
    ```

15. (Actividad15) Realiza un programa en Java que tenga las variables edad, nivel de estudios e ingresos y almacene en una variable llamada jasp el valor verdadero si la edad es menor o igual a 28 y el nivel de estudios es mayor a 3, o bien la edad es menor de 30 y los ingresos superiores a 28000. En caso contrario almacenar el valor falso.

16. (Actividad16) Realizar un programa que realice el cálculo del precio de un producto teniendo en cuenta que el producto vale 120 €, tiene un descuento del 15% y el IVA que se le aplica es del 21%.

17. (Actividad17) Realiza un programa que calcule la nota que hace falta sacar en el segundo examen de la asignatura Programación para obtener la media deseada. Hay que tener en cuenta que la nota del primer examen cuenta el 40% y la del segundo examen un 60%.
    Ejemplo 1:

    ```sh
    Introduce la nota del primer examen: 7
    ¿Qué nota quieres sacar en el trimestre? 8.5
    Para tener un 8.5 en el trimestre necesitas sacar un 9.5 en el segundo examen.
    ```

    Ejemplo 2:

    ```sh
    Introduce la nota del primer examen: 8
    ¿Qué nota quieres sacar en el trimestre? 7
    Para tener un 7 en el trimestre necesitas sacar un 6.333333333 en el segundo examen.
    ```

18. (Actividad18) Realizar un programa que dado un importe en euros nos indique el mínimo número de billetes y la cantidad sobrante de euros. Debes usar el operador condicional `?:`

    ```java
    ¿Cuántos euros tienes?: 232
    1 billete de 200 €
    1 billete de 20 €
    1 billete de 10 €
    Sobran 2 €
    ```

