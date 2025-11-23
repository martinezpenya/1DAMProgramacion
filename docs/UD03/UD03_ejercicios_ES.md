# Ejercicios de la UD03

## Retos

1. (Descuento) modifique el programa para que, en lugar de realizar un descuento del 8% si la compra es de 100 € o más, aplique una penalización de 2 € si el precio es inferior a 30 €.

    ```java
    import java.util.Scanner;
    //Un programa que calcula descuentos.
    
    public class _1_Descuento{
        public static final float DESCUENTO= 8;
        public static final float COMPRA_MIN = 100;
    
        public static void main(String[] args) {
            Scanner lector = new Scanner(System.in);
            System.out.print("¿Cuál es el precio del producto, en euros?");
            float precio= lector.nextFloat();
            lector.nextLine();
            if (precio>= COMPRA_MIN) {
                float descuentoHecho= precio * DESCUENTO / 100;
                precio = precio - descuentoHecho;
            }
            System.out.println("El precio final a pagar es de "+ precio +" euros.");
        }
    }
    ```

2. (Adivina) modifique el programa para que, en lugar de un único valor secreto, haya dos. Para ganar, basta con acertar uno de los dos. La condición lógica que necesitará ya no se puede resolver con una expresión compuesta por una única comparación. Será más compleja.

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, la variable `VALOR_SECRETO` debe ser renombrada a `VALOR_SECRETO1`, y la nueva debe llamarse `VALOR_SECRETO2` (deberá generarse aleatoriamente) y aunque el nombre sea de constante, no puede ser final.

    ```java
    import java.util.Scanner;
    
    public class Adivina{
    
        public static final int VALOR_SECRETO = 4;
    
        public static void main(String[] args) {
            Scanner lector = new Scanner(System.in);
            System.out.println("Empecemos el juego.");
            System.out.print("Adivina el valor entero, entre 0 y 10: ");
            int valorUsuario = lector.nextInt();
            lector.nextLine();
            if (VALOR_SECRETO == valorUsuario) {
                System.out.println("¡Exactamente! Era " + VALOR_SECRETO + ".");
            } else {
                System.out.println("¡Te has equivocado!");
            }
            System.out.println("Hemos terminado el juego.");
        }
    }
    ```

3. (AdivinaCorrecto) modifique el ejemplo anterior (Adivina) para que comprueben que el valor que ha introducido el usuario se encuentra dentro del rango de valores correcto (entre 0 y 10).

4. (AdivinaControlErroresEntrada) aplique el mismo tipo de control sobre los datos de la entrada del ejemplo siguiente al ejercicio del reto 1.

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, el mensaje de error cuando no se introduzca un entero debe contener la palabra "ERROR"

    ```java
    import java.util.Scanner;
    
    public class AdivinaControlErroresEntrada{
    
        public static final int VALOR_SECRETO = 4;
    
        public static void main(String[] args) {
            Scanner lector = new Scanner(System.in);
            System.out.println("Empecemos el juego.");
            System.out.print("Adivina el valor entero, entre 0 y 10: ");
            boolean tipoCorrecto = lector.hasNextInt();
            if (tipoCorrecto) {
                //Se ha escrito un entero correctamente. Ya puede leerse.
                int valorUsuario = lector.nextInt();
                lector.nextLine();
                if (VALOR_SECRETO == valorUsuario) {
                    System.out.println("Exacto! Era " + VALOR_SECRETO + ".");
                } else {
                    System.out.println("Te has equivocado!");
                }
                System.out.println("Hemos terminado el juego.");
            } else {
                //No se ha escrito un entero.
                System.out.println("El valor introducido no es un entero.");
            }
        }
    }
    ```

5. (Linea) Modifique el ejemplo para que primero pregunte al usuario cuántos caracteres "-" quiere escribir por pantalla, y entonces los escriba. Cuando pruebe el programa, no introduzca un número muy alto!

    ```java
    //Un programa que escribe una línea con 100 caracteres '−'.
    
    public class Linea {
    
        public static void main(String[] args) {
            //Inicializamos un contador
        
            int i = 0;
            //¿Ya hemos hecho esto 100 veces?
            while (i < 100) {
                System.out.print("−");
                //Lo hemos hecho una vez, sumamos 1 al contador
        
                i = i + 1;
            }
            //Forzamos un salto de línea
            System.out.println();
        }
    }
    ```

6. (TablaMultiplicar) un contador tanto puede empezar a contar desde 0 e ir subiendo, como desde el final e ir disminuyendo como una cuenta atrás. Modifique este programa para que la tabla de multiplicar comience mostrando el valor para 10 y vaya bajando hasta el 1.

    ```java
    import java.util.Scanner;
    public class TablaMultiplicar{
    
        public static void main(String[] args) {
            Scanner lector = new Scanner(System.in);
            System.out.print("¿Qué tabla de multiplicar quieres? ");
            int tabla = lector.nextInt();
            lector.nextLine();
            int i = 1;
            while (i <= 10) {
                int resultado = tabla * i;
                System.out.println(tabla + " * " + i + " = " + resultado);
                i = i + 1;
            }
            System.out.println("Ésta ha sido la tabla del " + tabla);
        }
    }
    ```

7. (Modulo) el uso de contadores y acumuladores no es excluyente, sino que puede ser complementario. Piense cómo se podría modificar el programa para calcular el resultado del módulo y la división entera a la vez. Recuerde que la división entera simplemente sería contar cuántas veces se ha podido restar el divisor.

    ```java
    import java.util.Scanner;
    
    public class Modulo{
    
        public static void main(String[] args) {
             Scanner lector = new Scanner(System.in);
            System.out.print("¿Cuál es el dividendo? ");
            int dividendo = lector.nextInt();
            lector.nextLine();
            System.out.print("¿Cuál es el divisor? ");
            int divisor = lector.nextInt();
            lector.nextLine();
            while (dividendo >= divisor) {
                dividendo = dividendo - divisor;
                System.out.println("Bucle: por ahora el dividendo vale " + dividendo + ".");
            }
            System.out.println("El resultado final es" + dividendo + ".");
        }
    }
    ```

## Ejercicios

### `if else`

1. (MenorDeDos) Escribir un método (`menorDeDos`) que devuelva el menor de dos números enteros introducidos por teclado.

2. (MenorDeTres) Escribir dos métodos que devuelve el menor de tres números recibidos por parámetros. Haz dos versiones:
    - `menorDeTresV1`: utilizando los operadores de comparación (<, >, ==) y lógicos (&&,||, ...) necesarios
    - `menorDeTresV2`: sin utilizar ninguno de los operadores lógicos (habrá que usar sentencias if else anidadas)

3. (IntermedioDeTres) Escribir un método (`intermedioDeTres`) que devuelva el intermedio de tres números recibidos por parámetros.

4. (NotasTexto) Escribir un método (`notas2Texto`) que recibe un valor numérico (se supone entre 1 y 10 y puede contener decimales) y devuelva el literal correspondiente a dicha nota según ("insuficiente", "suficiente", "bien", "notable", "sobresaliente" y "matricula de honor").

5. (Division) Escribir un método (`division`) que reciba dos números enteros e imprima el resultado de la división. Tener en cuenta que si dividimos un número por cero se producirá un error de ejecución y debemos evitarlo. Ejemplos de ejecución:
    ```sh
    Vamos a dividir dos números.
    Introduce el valor del dividendo: 15
    Introduce el valor del divisor: 3
    La división es: 5.0
    
    Vamos a dividir dos números.
    Introduce el valor del dividendo: 4
    Introduce el valor del divisor: 0
    No se puede realizar la división porque el divisor es 0
    ```

6. (Raiz) Se desea calcular la raíz cuadrada real de un número real cualquiera pedido inicialmente al usuario. Como dicha operación no está definida para los números negativos es necesario tratar, de algún modo, dicho posible error sin que el programa detenga su ejecución. Debes escribir un método `raiz` que recibe un entero. Ejemplos de ejecución:

    ```sh
    Vamos a calcular la raíz cuadrada de un número.
    Introduce el valor del número: 81
    La raíz es: 9.0
    
    Vamos a calcular la raíz cuadrada de un número.
    Introduce el valor del número: -52
    No se puede realizar la raíz porque el número es negativo
    ```

7. (Hora12) Escribir un método (`formatoDoce`) que recibe dos enteros (hora y minutos) en notación de 24 horas y la devuelve como `String` en notación de 12 horas. Por ejemplo, si la entrada es 13 horas 45 minutos, la salida será "`1:45 PM`". La hora y los minutos se leerán de teclado de forma separada, primero la hora y luego los minutos. Si la hora pasada al método no es correcta devolverá: "Error de conversión"

    ```sh
    Vamos a convertir una hora a formato 12H.
    Introduce el valor para la hora: 51
    Introduce el valor para los minutos: 6
    Error de conversión.
    
    Vamos a convertir una hora a formato 12H.
    Introduce el valor para la hora: 13
    Introduce el valor para los minutos: 45
    01:45 PM
    
    Vamos a convertir una hora a formato 12H.
    Introduce el valor para la hora: 4
    Introduce el valor para los minutos: 53
    04:53 AM
    ```

8. (Bisiesto) Escribir un método (`esBisiesto`) que devuelva si un año introducido por teclado es o no bisiesto. Un año es bisiesto si es múltiplo de 4 (por ejemplo 1984). Sin embargo, los años múltiplos de 100 no son bisiestos, salvo que sean múltiplos de 400, en cuyo caso si lo son (por ejemplo 1800 no es bisiesto y 2000 si lo es). Para hacer el programa, implementa un método dentro de la clase que reciba un año y devuelva true si el año es bisiesto y false en caso de que no lo sea.

9. (Fechas) Escribir un método (`imprimeMenor`) que reciba dos fechas (día, mes y año) (6 parámetros en total), que se suponen correctas, y le muestre la menor de ellas. La fecha se mostrará en formato dd/mm/año. Utiliza un método `mostrarFecha`, para mostrar la fecha por pantalla. La fecha se mostrará siempre con dos dígitos para el día, dos para el mes y cuatro para el año.

    ```sh
    Vamos a ver que fecha es menor.
    Introduce el valor para el Fecha1. 
    	- Dia: 4
    	- Mes: 5
    	- Año: 1999
    
    Introduce el valor para el Fecha2. 
    	- Dia: 3
    	- Mes: 5
    	- Año: 1999
    
    La fecha menor es:
    03/05/1999
    ```

10. (DiasDelMes) Escribir un método (`diasMes`) que recibe el número de un mes (1 a 12) y devuelve el número de días que tiene el mes. Hacerlo utilizando sentencias `if else`. Si el mes recibido no es correcto, debe devolver 0.

    ```sh
    Vamos a ver cuantos días tiene un mes.
    Introduce el valor para el mes: 8
    Este mes tiene 31 días.
    
    Vamos a ver cuantos días tiene un mes.
    Introduce el valor para el mes: 54
    Este mes tiene 0 días.
    ```

11. (NombreDelMes) Escribir un programa que lea de teclado el número de un mes (1 a 12) y visualice el nombre del més (enero, febrero, etc). Hacerlo utilizando sentencias `if else`. Para hacer un programa, implementa un método en la clase que reciba un número de mes y devuelva el nombre del mes

12. (Salario) Escribir un método (`salario`) que recibe las horas trabajadas por un empleado en una semana y calcula y devuelve su salario neto semanal, sabiendo que:

    - Las horas ordinarias se pagan a 6 €.
    - Las horas extraordinarias se pagan a 10 €.
    - Los impuestos a deducir son:
        - Un 2 % si el salario bruto semanal es menor o igual a 350 €
        - Un 10 % si el salario bruto semanal es superior a 350 €
    - La jornada semanal ordinaria son 40 horas. El resto de horas trabajadas se considerarán horas extra.

13. (Signo) Dados dos números enteros, num1 y num2, realizar un programa que escriba uno de los dos
     mensajes:

     - "el producto de los dos números es positivo o nulo" o bien
     - "el producto de los dos números es negativo".

     Resolverlo sin calcular el producto, sino teniendo en cuenta únicamente el signo de los números a multiplicar.

14. (Calculadora) Escribir un programa para simular una calculadora. Considera que los cálculos posibles son del tipo num1 operado num2, donde num1 y num2 son dos números reales cualesquiera y operador es una de entre: +, -, * y /. El programa pedirá al usuario en primer lugar el valor num1, a continuación el operador y finalmente el valor num2. Resolver utilizando instrucciones `if else`

15. (Comercio) Un comercio aplica un descuento del 8% por compras superiores a 40 euros. El descuento máximo será de 12 euros. Escribir un programa que solicite al usuario el importe de la compra y muestre un mensaje similar al siguiente:

     - Importe de la compra 100 €
     - Porcentaje de descuento aplicado: 8%
     - Descuento aplicado: 8 €
     - Cantidad a pagar: 92 €

16. (Editorial) Una compañía editorial dispone de 2 tipos de publicaciones: libros y revistas. El precio de cada pedido depende del número de elementos solicitados al cual se le aplica un determinado descuento, que es diferente para libros y para revistas. La siguiente tabla muestra los descuentos a aplicar en función del número de unidades y del tipo de producto:

    | Cantidad pedida         | Libros            | Revistas          |
    | ----------------------- | ----------------- | ----------------- |
    | Hasta 5 unidades        | 0 % de descuento  | 0 % de descuento  |
    | De 6 a 10 unidades      | 10 % de descuento | 15 % de descuento |
    | De 11 a 20 unidades     | 15 % de descuento | 20 % de descuento |
    | A partir de 20 unidades | 20 % de descuento | 25 % de descuento |

    Escribe un método `calcularCoste` que, recibiendo el tipo de publicación (`String`), que puede ser "libro" o "revista", el precio individual (`double`) y el número de unidades solicitado (`int`), devuelva el coste del pedido (aplicando el descuento correspondiente).
    Escribe un programa en el que el usuario deba introducir cantidad y precio de revistas y cantidad y precio de libros que incluye un pedido, y muestre el coste del pedido.

    Si el tipo especificado es diferente de "libro" o "revista", el método devolverá -1.

    ```sh
    Vamos a calcular el coste del pedido.
    
    Introduce los datos respecto a LIBROS.
    	Precio unitario: 12,3
    	Cantidad: 4
    
    Introduce los datos respecto a REVISTAS.
    	Precio unitario: 2,6
    	Cantidad: 5
    
    El coste total de pedido será de 62,20€.
    ```

17. (Taxi) Se desea calcular el coste del trayecto realizado en taxi en función de los kilómetros recorridos en las carreras metropolitanas de Valencia. Según las tarifas vigentes para el 2012, el coste se calcula de la siguiente manera:

    - Días laborables en horario diurno (de 6:00 a antes de las 22:00h): 0.73 €/km.
    - Días laborables en horario nocturno: 0.84 €/km.
    - Sábados y domingos: 0.93 €/km.
    - Además, la tarifa mínima diurna es de 2.95€ y la mínima nocturna de 4€.

    Escribir un método que recibe:

    - La hora (`hora` y `minutos`) en que se realizó el trayecto.
    - El `día de la semana` (se supone que el usuario introduce un valor entre 1 para lunes y 7 para domingo)
    - Los `kilómetros` recorridos.

    El método devuelve el coste del trayecto.
    Escribe un método `main` que solicite al usuario la introducción de los datos y llamando al método muestre el resultado:

    ```sh
    Vamos a calcular el coste del trayecto.
    Introduce la hora: 15
    Introduce los minutos: 20
    Introduce el dia de la semana (1 para lunes y 7 para domingo): 6
    Introduce los kilometros recorridos: 3,5
    
    El coste total del trayecto es de 3,26€.
    ```

18. (Nombre) Escribir un método (`coincidenPrimeraYUltima`) que recibe una cadena de texto. El método devolverá si la primera y la última letra del nombre coinciden o no. 

    Haz que funcione aunque las letras tengan diferente CASE (pista: lowercase i uppercase).

    Escribe el método `main` que solicite al usuario un nombre de persona y llamando al método diga si coinciden o no, pruébalo con "Ana", "ana", "Angel", "Amanda" y "David":

    ```sh
    Vamos a ver si la primera y la última letra de tu nombre son iguales.
    Introduce un nombre: Ana
    Si coinciden.
    
    Vamos a ver si la primera y la última letra de tu nombre son iguales.
    Introduce un nombre: Angel
    No coinciden.
    ```
19. (Validar) Se desea implementar un programa que determine si dos datos `x` e `y` de entrada son válidos. Un par de datos es válido si es uno de los que aparecen en la siguiente tabla:

    | x :  | a    | a    | a    | a    | a    | b    | b    | b    | b    | b    |
    | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
    | y :  | 1    | 3    | 5    | 7    | 9    | 2    | 4    | 6    | 8    | 10   |

    Se pide implementar un método (`esValido`) que recibe los dos valores (`x` e `y`), que devuelva si la combinación es válida o no. 
    
    Escribe también un método `main` que lea de teclado el valor de `x` y el valor de `y`, e indique por pantalla "VALIDOS" o "NO VALIDOS". Se pide hacerlo de forma que no se utilice ninguna estructura condicional (if, switch,...), es decir, se calculará una expresión booleana que determine si `x` e `y` son válidos. Se procurará que la expresión booleana propuesta sea breve y concisa.

### Bucles simples

1. (SencillosWhile) Crear una clase llamada `SencillosWhile` y crear en él métodos que realicen las siguientes tareas.
    1. (imparesHastaN) Recibe un nº entero `n`, devuelve los números impares que hay entre 1 y `n`. Por ejemplo, si `n` es 8 devolverá `"1 3 5 7 "`
    2. (nImpares) Recibe un nº entero `n`, devuelve los `n` primeros números impares. Por ejemplo, si `n` es 3 devolverá `"1 3 5"` (3 primeros impares)
    3. (cuentaAtras) Recibe un entero `n` , devuelve una cuenta atrás partiendo de `n`: `n`, `n-1`, …. Por ejemplo, si `n` es 5 devolverá `"5 4 3 2 1 0 "`
    4. (sumaNPrimeros) Recibe un entero `n`, devuelve la suma de los números entre 1 y `n`. Por ejemplo, si `n` es 5 devolverá `15`
    5. (mostrarDivisoresN) Recibe un entero `n`, devuelve todos sus divisores, incluidos el 1 y el mismo `n`. Por ejemplo, si `n` es 12 mostraría `"1 2 3 4 6 12 "`
    6. (sumaDivisoresN) Recibe un entero `n`, devuelve la suma de todos sus divisores, sin incluir al propio `n`. Por ejemplo, si `n` es 12 sumará 1, 2, 3, 4 y 6 = `16`

    Ejemplo de ejecución con todos los métodos:

    ```sh
    Esta realiza varios While sencillos:
    Introduce un número: 15
    Imprimimos:
    	Todos los números impares menores que 15: 1 3 5 7 9 11 13 15 
    	Los primeros 15 números impares: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 
    	Cuenta atrás desde 15: 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 
    	La suma de los 15 primeros números resulta: 120
    	Los divisores del número 15 son: 1 3 5 15 
    	La suma de todos los divisores del número 15 (sin él mismo) son: 9
    ```

2. (SencillosFor) Crear una clase llamada "SencillosFor" y crear en él los mismos métodos que en el ejercicio anterior, pero utilizando la sentencia `for` en lugar de `while`:

    ```sh
    Esta realiza varios For sencillos:
    Introduce un número: 15
    Imprimimos:
    	Todos los números impares menores que 15: 1 3 5 7 9 11 13 15 
    	Los primeros 15 números impares: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 
    	Cuenta atrás desde 15: 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 
    	La suma de los 15 primeros números resulta: 120
    	Los divisores del número 15 son: 1 3 5 15 
    	La suma de todos los divisores del número 15 (sin él mismo) son: 9
    ```

3. (PotenciasDe2) Crea un método (`potencias`) que recibe un entero `n` positivo y devuelve las `n` primeras potencias de 2. Es decir, 2^0^, 2^1^, 2^2^, 2^3^, …, 2^n^. Crea un método `main` que solicite un número al usuario y muestre por pantalla todas las potencias de 2. Soluciona el ejercicio sin utilizar `Math.pow`. Ten en cuenta que, por ejemplo, 2^3^ = 1* 2 * 2 * 2 o que 2^4^ = 1* 2 * 2 * 2 * 2:

    ```sh
    Dime n: 20
    1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 
    ```

4. (Etapas) El ser humano pasa por una serie de etapas en su vida que, con carácter general se asocian a las edades que aparecen en la tabla siguiente.  

    | Infancia     | Hasta los 10 años|
    | :----------- | ----------------------------------- |
    | Pubertad     | De 11 a 14 años         |
    | Adolescencia | De 15 a 21 años         |
    | Adultez      | De 22 a 54 años         |
    | Vejez        | De 55 a 70 años         |
    | Ancianidad   | A partir de los 71 años |

    Escribe un método `main` en el que el usuario introduzca las edades de una serie de personas y calcule y muestre que porcentaje de personas que se encuentran en cada etapa. En primer lugar el programa pedirá el número de personas que participan en la muestra y a continuación solicitará la edad de cada una de ellas. El resultado será similar al siguiente:

    ```sh
    ¿Cuantas personas hay en la muestra?: 5
    Introduce la edad de la persona 1 de 5 : 17
     --> adolescencia
    Introduce la edad de la persona 2 de 5 : 21
     --> adolescencia
    Introduce la edad de la persona 3 de 5 : 53
     --> adultez
    Introduce la edad de la persona 4 de 5 : 62
     --> vejez
    Introduce la edad de la persona 5 de 5 : 78
     --> ancianidad
    Etapa 		Número	%
    Infancia: 	0	0.0%
    Pubertad: 	0	0.0%
    Adolescencia: 	2	40.0%
    Adultez: 	1	20.0%
    Vejez: 		1	20.0%
    Ancianidad: 	1	20.0%
    
    ¿Cuantas personas hay en la muestra?: 3
    Introduce la edad de la persona 1 de 3 : 1
     --> infancia
    Introduce la edad de la persona 2 de 3 : 2
     --> infancia
    Introduce la edad de la persona 3 de 3 : 25
     --> adultez
    Etapa 		Número	%
    Infancia: 	2	66.66666666666667%
    Pubertad: 	0	0.0%
    Adolescencia: 	0	0.0%
    Adultez: 	1	33.333333333333336%
    Vejez: 		0	0.0%
    Ancianidad: 	0	0.0%
    ```

5. (Primo) Escribir un método `esPrimo` que recibe un entero y devuelve si es primo o no. Escribe un método `main` en el que el usuario escriba un número entero y se le diga si se trata o no de un número primo, usando el método `esPrimo`. Recuerda que un nº primo es aquel que solo es divisible por 1 y por sí mismo (Es decir tiene SOLO y EXCLUSIVAMENTE dos divisores cuyo resto sea cero).

     ```sh 
     Este te dice si un número es primo:
     Introduce un número: 15
     El número es primo?: false
     
     Este te dice si un número es primo:
     Introduce un número: 7
     El número es primo?: true
     ```

6. (Primos) Escribir un programa en el que el usuario escriba un número entero y se le diga todos los números primos entre 1 y el número introducido (Puedes usar el método `esPrimo` que has escrito en el ejercicio anterior.

7. (EsPrimoMejorada) Haz una nueva versión del programa del ejercicio anterior teniendo en cuenta lo siguiente:  
     - El único número par que es primo es el 2.
     - Un número *n* no puede tener divisores mayores que n/2 (o mayores que Math.sqrt(n))

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests de rendimiento, debes tener el ejercicio 6 (Primos) y 7 (EsPrimoMejorada) y el rendimiento del 7 debe ser un 20% mejor (más rápido) que el del 6

8. (Divisores) Escribir un programa que muestre los tres primeros divisores de un número n introducido por el usuario. Por ejemplo, si el usuario introduce el número 45, el programa mostrará los divisores 1, 3 y 5. Ten en cuenta que la posibilidad de que el número n tenga menos de 3 divisores. Prueba qué pasa si el usuario pide, por ejemplo, los tres primeros divisores de 7.  

9. (SumaSerie) Dado un número `n`, introducido por el usuario, calcula y muestra por pantalla la siguiente suma 1/1+1/2+1/3+ ··· + 1/`n` 

10. (Cifras) Escribir un método (`cifras`) que recibe un número entero cualquiera (positivo, negativo o cero) y devuelve cuantas cifras tiene. Pistas: ¿Cuantas cifras tiene el nº 25688? ¿Cuántas veces podemos dividir el nº 25688 por 10 hasta que se hace cero? Cuidado, el nº 0 tiene una cifra.

     ```sh
     Vamos a decirte cuantas cifras tiene un número:
     Introduce un número: 0
     El número tiene 1 cifras.
     
     Vamos a decirte cuantas cifras tiene un número:
     Introduce un número: 25688
     El número tiene 5 cifras.
     
     Vamos a decirte cuantas cifras tiene un número:
     Introduce un número: -14
     El número tiene 2 cifras.
     ```

11. (Transportes) Una empresa de transportes cobra 30€ por cada bulto que transporta. Además, si el peso total de todos los bultos supera los 300 kilos, cobra 0.9€ por cada kg extra. Por último si el trasporte debe realizarse en sábado, cobra un plus de 60€. La empresa no realiza el pedido si hay que transportar más de 30 bultos, si el peso total supera los 1000 kg o si se solicita hacerlo en domingo. Realizar un método `main` que solicite el número de bultos, el día de la semana (valor entre 1 y 7) y el peso de cada uno de los bultos y muestre el coste del transporte en caso de que pueda realizarse o un mensaje adecuado en caso contrario:

       ```sh
       ¿Cuantos bultos debes enviar?: 3
       ¿Qué dia de la semana se realiza el envio (entre 1=lunes y 7=domingo)?: 7
       No se puede realizar el envio por superar los 30 bultos o ser domingo
       
       ¿Cuantos bultos debes enviar?: 4
       ¿Qué dia de la semana se realiza el envio (entre 1=lunes y 7=domingo)?: 6
       Cuanto pesa el bulto 1 de 4 : 25
       Cuanto pesa el bulto 2 de 4 : 120
       Cuanto pesa el bulto 3 de 4 : 35
       Cuanto pesa el bulto 4 de 4 : 78
       El coste del envio será de: 180.0
       
       ¿Cuantos bultos debes enviar?: 2
       ¿Qué dia de la semana se realiza el envio (entre 1=lunes y 7=domingo)?: 1
       Cuanto pesa el bulto 1 de 2 : 700
       Cuanto pesa el bulto 2 de 2 : 400
       No se puede realizar el envio por superar los 1000Kg
       ```

12. (Containers) La capacidad de un buque que transporta containers está limitada tanto por la cantidad de containers como por el peso, pudiendo transportar un máximo de 100 containers y un máximo de 700 toneladas. Hacer un programa en el que se vaya introduciendo el peso de los containers (en toneladas) a medida que se cargan en el barco, hasta que se llegue al máximo de capacidad. Mostrar al final la cantidad de containers cargados y el peso total. En el momento en que se desee cargar un container que haga que la carga total supere las 700 toneladas, se dará por finalizada la carga, aunque pudieran existir containers menos pesados con posibilidad de ser cargados.

13. (Notas) Realizar un método `main` que permita introducir las notas de varios examenes de un alumno de un curso. El usuario irá introduciendo las notas una tras otra. Se considerará finalizado el proceso de introducción de notas cuando el usuario introduzca una nota negativa. Al final, el programa le dirá:
        - El número de notas introducidas.
        - El número de aprobados (mayor o igual a 5 puntos)
        - La nota media

       ```sh
       Vamos a darte información sobre tus notas, introduce una nota tras otra. Para finalizar escribe una nota negativa:
       Introduce la nota 1: 5,5
       Introduce la nota 2: 6,7
       Introduce la nota 3: 8,4
       Introduce la nota 4: 3,2
       Introduce la nota 5: 1,5
       Introduce la nota 6: -3
       Has introducido un total de 5 notas,
       de las cuales has aprobado 3,
       con una media de 4.
       ```

14. (NotasExtremas) Modificar el ejercicio anterior para que además calcule la nota máxima y la nota mínima.

### Bucles anidados

1. (Edades) Programa que pida al usuario la edad de cinco personas. Si la suma de las edades es inferior a 200, el programa volverá a solicitar las 5 edades.

    ```sh
    Introduce la edad de la persona 1: 80
    Introduce la edad de la persona 2: 42
    Introduce la edad de la persona 3: 15
    Introduce la edad de la persona 4: 56
    Introduce la edad de la persona 5: 34
    ```
    ```sh
    Introduce la edad de la persona 1: 15
    Introduce la edad de la persona 2: 12
    Introduce la edad de la persona 3: 43
    Introduce la edad de la persona 4: 5
    Introduce la edad de la persona 5: 4
    La suma de edades debe ser superior a 200
    
    Introduce la edad de la persona 1: 48
    Introduce la edad de la persona 2: 54
    Introduce la edad de la persona 3: 35
    Introduce la edad de la persona 4: 12
    Introduce la edad de la persona 5: 89
    ```

2. (NotasPorAlumno) Programa que pida al usuario las notas de `A` alumnos en `S` asignaturas, alumno por alumno. `A` y `S` se definirán en el programa como `CONSTANTES`.

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, la variable `A` debe ser 3 y  `S` debe ser 5.

    ```sh
    Alumno 1
    	Introduce la nota de la asignatura 1: 5
    	Introduce la nota de la asignatura 2: 4
    	Introduce la nota de la asignatura 3: 3
    	Introduce la nota de la asignatura 4: 5
    	Introduce la nota de la asignatura 5: 0
    Alumno 2
    	Introduce la nota de la asignatura 1: 6
    	Introduce la nota de la asignatura 2: 8
    	Introduce la nota de la asignatura 3: 9
    	Introduce la nota de la asignatura 4: 8
    	Introduce la nota de la asignatura 5: 7
    Alumno 3
    	Introduce la nota de la asignatura 1: 0
    	Introduce la nota de la asignatura 2: 0
    	Introduce la nota de la asignatura 3: 2
    	Introduce la nota de la asignatura 4: 4
    	Introduce la nota de la asignatura 5: 5
    ```

3. (NotasPorAsignatura) Programa que pida al usuario las notas de `A` alumnos en `S` asignaturas, asignatura por asignatura. `A` y `S` se definirán en el programa como `CONSTANTES`. 

    ```sh
    Asignatura 1
    Introduce nota del alumno 1: 
    Introduce nota del alumno 2:
    ...
    Asignatura 2
    Introduce nota del alumno 1:
    ...
    ```

4. (MediasPorAsignatura) Repite el ejercicio anterior haciendo que se muestre la media de cada asignatura

    ```sh
    Asignatura 1
    Introduce nota del alumno 1: 
    Introduce nota del alumno 2:
    ...
    Media asignatura 1: 8.5 puntos
    
    Asignatura 2
    Introduce nota del alumno 1:
    ...
    Media asignatura 2: 6.5 puntos
    ...
    ```

5. (TablaMult) Escribir un programa que permita al usuario introducir un número `N` e imprima la tabla de multiplicar (del 0 al 10) de todos los números entre 1 y `N`. Ejemplo: Si el usuario introduce en número 5, el programa imprimiria

    ```
    Tabla del 1:
    1 por 0, 0
    1 por 1, 1
    1 por 2, 2
    ...
    1 por 10, 10
    
    Tabla del 2:
    2 por 0, 0
    2 por 1, 2
    ....
    2 por 10, 20
    
    Tabla del 3:
    ...
    
    Tabla del 5:
    ...
    5 por 10, 50
    ```

6. (PrimosHastaN) Programa que solicite al usuario un numero `n` y muestre todos los números primos menores o iguales que `n`. (IGUAL AL 27!!)

7. (CombinarLetras2) Escribir un programa que muestre todas las palabras de dos letras que se pueden formar con los cuatro primeros caracteres del alfabeto en minúsculas ('a', 'b', 'c', 'd'):

    ```sh
    aa
    ab
    ac
    ad
    ba
    bb
    bc
    bd
    ...
    da
    db
    dc
    dd
    ```

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, en lugar de usar `System.out.println`, debes usar `System.out.print` con un `\n` al final de la cadena a imprimir.

8. (CombinarLetras3) Repite el ejercicio anterior mostrando palabras de tres letras

    ```sh
    aaa
    aab
    ...
    ddc
    ddd
    ```

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, en lugar de usar `System.out.println`, debes usar `System.out.print` con un `\n` al final de la cadena a imprimir.

9. (LetraALetra) Escribe un programa en el que se solicite al usuario un texto de forma repetida hasta que el usuario introduzca la cadena vacía. Con cada texto que introduzca el usuario se le mostrará carácter a carácter, cada carácter en una línea

    ```sh
    Vamos a escribir textos letra a letra
    Introduce texto: Hola
    H
    o
    l
    a
    Introduce texto: Casa
    C
    a
    s
    a
    Introduce texto: 
    Fin del programa
    ```

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, en lugar de usar `System.out.println`, debes usar `System.out.print` con un `\n` al final de la cadena a imprimir.

10. (DibujarFiguras1) Escribe una clase que contenga los métodos que se indican a continuación. En el método `main` solicita al usuario las dimensiones de las figuras necesarias en cada caso y llama al método correspondiente para que se muestre por pantalla

    1. (`void dibRecAsteriscos (int ancho, int alto)` dibuja un rectángulo utilizando asteriscos, como el siguiente. En el ejemplo ancho es 7 y alto es 3

        ```sh
        * * * * * * *
        * * * * * * *
        * * * * * * *
        ```

        ```sh
        Vamos a dibujar figuras.
        Introduce el ancho: 8
        Introduce el alto: 4
        * * * * * * * * 
        * * * * * * * * 
        * * * * * * * * 
        * * * * * * * * 
        ```

    2. (`void dibRecNumeros1 (int ancho, int alto)` dibuja un rectángulo utilizando números, como el siguiente. En el ejemplo ancho es 7 y alto es 3

        ```sh
        1 2 3 4 5 6 7
        1 2 3 4 5 6 7
        1 2 3 4 5 6 7
        ```

    3. (`void dibRecNumeros2 (int ancho, int alto)` dibuja un rectángulo utilizando números, como el siguiente. En el ejemplo ancho es 7 y alto es 3

        ```sh
        7 6 5 4 3 2 1
        7 6 5 4 3 2 1
        7 6 5 4 3 2 1
        ```

    4. (`void dibRecNumeros3 (int ancho, int alto)` dibuja un rectángulo utilizando números, como el siguiente. En el ejemplo ancho es 7 y alto es 3

        ```sh
        01 02 03 04 05 06 07
        08 09 10 11 12 13 14
        15 16 17 18 19 20 21
        ```

    5. (`void dibDiagonal (int ancho, int alto)` dibuja un rectángulo con ceros y unos. Los 1 están en las posiciones en las que fila y columna coinciden. En el ejemplo ancho es 7 y alto es 3

        ```java
        1 0 0 0 0 0 0
        0 1 0 0 0 0 0
        0 0 1 0 0 0 0
        ```

    6. 
       (`void dibRecLetras (int ancho, int alto)` dibuja un rectángulo letras sucesivas comenzando por la "a". En el ejemplo ancho es 7 y alto es 3

       ```sh
       a a a a a a a
       b b b b b b b
       c c c c c c c
       ```

    7. 
       (`void dibRecLetras2 (int ancho, int alto)` dibuja un rectángulo letras sucesivas terminando por la "a". En el ejemplo ancho es 7 y alto es 3

       ```sh
       c c c c c c c
       b b b b b b b
       a a a a a a a
       ```

    8. 
       (`void dibRecLetras3 (int ancho, int alto)` dibuja un rectángulo letras sucesivas comenzando por la "a". En el ejemplo ancho es 7 y alto es 3

       ```sh
       a b c d e f g
       h i j k l m n
       o p q r s t u
       ```

11. (dibujarFiguras2) Escribe una clase que contenga los métodos que se indican a continuación. En el método main solicita al usuario las dimensiones de las figuras necesarias en cada caso y llama al método correspondiente para que se muestre por pantalla

       1. `void dibRectNumeros3 (int ancho, int alto)` dibuja un rectángulo 	utilizando números, como el siguiente. En el ejemplo ancho es 7 y alto es 3

          ```sh
          1 2 3 4 5 6 7 7 6 5 4 3 2 1
          1 2 3 4 5 6 7 7 6 5 4 3 2 1
          1 2 3 4 5 6 7 7 6 5 4 3 2 1
          ```

       2. 
          `void dibRectAsteriscos1 (int ancho, int alto)` dibuja un rectángulo utilizando asteriscos (*) y espacios en blanco, como el siguiente. En el ejemplo ancho es 7 y alto es 3

          ```sh
          * * * * * * *
          * * * * * * *
          * * * * * * *
          ```

       3. 
          `void dibRectAsteriscos2 (int ancho, int alto)` dibuja un rectángulo utilizando asteriscos (*), espacios en blanco y el carácter ‘+’, como el siguiente. En el ejemplo ancho es 7 y alto es 3

          ```yaml
          * + * + * + *
          * + * + * + *
          * + * + * + *
          ```

       4. 
          `void dibRectAsteriscos3 (int ancho, int alto)` dibuja un rectángulo utilizando asteriscos (*) y espacios en blanco, como el siguiente. En el ejemplo ancho es 7 y alto es 3

          ```sh
          * * * * * * *
          *           *
          * * * * * * *
          ```

       5. 
          `void dibTriangulo1 (int base)` dibuja un triángulo utilizando asteriscos (*) y espacios en blanco, como el siguiente. En el ejemplo base es 5

          ```sh
          *
          * *
          * * * 
          * * * * 
          * * * * *
          ```

       6. 
          `void dibTriangulo2 (int altura)` dibuja un triángulo utilizando asteriscos (*) y espacios en blanco, como el siguiente. En el ejemplo altura es 5

          ```sh
                  *
                * *
              * * * 
            * * * * 
          * * * * *
          ```

       7. 
          `void dibTriangulo3 (int altura)` dibuja un triángulo utilizando asteriscos (*) y espacios en blanco, como el siguiente. En el ejemplo altura es 5

          ```sh
                  *
                * * *
              * * * * *
            * * * * * * *
          * * * * * * * * *
          ```

### `switch`

1. (NotasTexto2) Escribir un método (`nota2TextoSwitch`) que reciba la nota de un examen (valor numérico entero entre 1 y 10) y muestre el literal correspondiente a dicha nota según (insuficiente, suficiente, bien, notable, sobresaliente, matrícula de honor). Hacerlo utilizando la sentencias switch.

2. (DiasDelMes2) Escribir un método que recibe un número de mes (1 a 12) y devuelva el número de días que tiene el mes. Resolver utilizando la sentencias switch. Si el mes es erroneo, devolverá 0.

    ```sh
    Vamos a calcular el número de dias que tiene un mes.
    Introduce el número del mes (1-12): 8
    31
    
    Vamos a calcular el número de dias que tiene un mes.
    Introduce el número del mes (1-12): 2
    28
    
    Vamos a calcular el número de dias que tiene un mes.
    Introduce el número del mes (1-12): 15
    0
    ```

3. (NombreDelMes2) Escribir un método (`nombreMes`) que recibe el número de un mes (1 a 12) y devuelve el nombre del mes ("enero", "febrero", etc). Resolver utilizando la sentencias switch. Si el mes no es válido, devolverá la cadena vacía "".
4. (Calculadora2) Escribir un método (`calculadora`) para simular una calculadora. Considera que los cálculos posibles son del tipo `num1, operador, num2`, donde `num1` y `num2` son dos números reales cualesquiera y operador es una de entre: `'+', '-', '*'` y `'/'`. El método recibirá los tres parámetros y devolverá el resultado de la operación. Resolver utilizando la sentencias switch. Si el `operador` no es ninguno de la lista, devuelve el `num1`.

### en papel...

1. (Valor) ¿Qué valor se asignará a consumo en la sentencia `if` siguiente si velocidad es 120?

    ```java
    if (velocidad > 80)
    	consumo = 10;
    else if (velocidad > 100)
    	consumo = 12;
    else if (velocidad > 120)
    	consumo = 15;
    ```

2. (Errores) Encuentra y corrige los errores de los siguientes fragmentos de programa.

    1.  fragmento a

        ```java
        if (x > 25)
            y = x
        else
            y = z;
        ```

    2. fragmento b

        ```java
        if (x<0)
            System.out.println("El valor de x es" +x);
            System.out.println ("x es negativo");
        else
            System.out.println ("El valor de x es"+x);
            System.out.println ("x es positivo");
        ```

    3. fragmento c

        ```java
        if (x = 0) System.out.println ("x igual a cero");
        else System.out.println ("x distinto de cero");
        ```

3. (SalidaExacta) Cuál es la salida exacta por pantalla del siguiente fragmento de programa

    ```java
    int x = 20;
    System.out.println("Comenzamos");
    if (x>= 20)
    	if (x>50) System.out.println("Muy grande");
    	else {
    		if (x%2 != 0) System.out.println("Impar");
    	}
    else if (x<=20) System.out.println("Pequeño");
    System.out.println("Terminamos");
    ```

28. (Descuentos) En una tienda, por liquidación, se aplican distintos descuentos en función del total de las compras realizadas:

    - Si total < 500 €, no se aplica descuento.
    - Si 500 € <= total <= 2000 €, se aplica un descuento del 30 %.
    - Si total > 2000 €, entonces se aplica un descuento del 50 %

    ¿Cuál de los siguientes fragmentos de programa asigna a la variable `desc` el descuento correcto? Indica "Si" o "NO" al lado de cada fragmento

    1. fragmento a

        ```java
        double desc = 0.0;
        if (total <= 500)
            if (total >= 2000) desc = 30.0;
            else desc = 50.0;
        total = total * desc / 100.0;
        ```

    2. fragmento b

        ```java
        double desc = 0.0;
        if (total >= 500)
            if (total <= 2000) desc = 30.0;
            else desc = 50.0;
        total = total * desc / 100.0;
        ```

    3. fragmento c

        ```java
        double desc = 0.0;
        if (total <= 2000){
            if (total >= 500) desc = 30.0;
            } else desc = 50.0;
        total = total * desc / 100.0;
        ```

    4. fragmento d

        ```java
        double desc = 0.0;
        if (total > 500)
            if (total < 2000) desc = 30.0;
            else desc = 50.0;
        total = total * desc /100.0;
        ```

29. (Salida) ¿Qué salida producirá el siguiente fragmento de programa si la variable entera platos vale 1? ¿Y si
    vale 3? ¿Y si vale 0?

    ```java
    switch (platos) {
        case 1: System.out.println("\nPrimer plato");
        case 2: System.out.println ("\nSegundo plato");
        case 3: System.out.println ("\nBebida");
        		System.out.println ("\nPostre");
        		break;
        default: System.out.println("\nCafé");
    }
    ```

30. (ValorP) Dados tres enteros a, b y c, y un booleano p, el siguiente análisis por casos establece el valor de p en función de los valores de a, b y c:

    ```java
    si a > b entonces p = cierto;
    si a < b entonces p = falso;
    si a = b entonces 
        si a > c entonces p = cierto;
    	si a < c entonces p = falso;
    	si a = c entonces p = falso;
    ```

    Se pide la traducción de dicho análisis por casos a Java mediante:

    - Una única instrucción `if` sin anidamientos.
    - Una única instrucción, de la forma `p = ...`, que utilice el operador ternario.
    - Una única instrucción, de la forma `p = ...` , sin sentencias `if` ni utilizar el operador ternario.

### Trazas

Indica cual será la salida producida por los siguientes programas, teniendo en cuenta los datos de entrada:

1. (Traza1) **Datos de entrada: 2, 5**

    a.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x+y;
        System.out.println(a);
    }
    ```
    
    b.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,a;
        x = tec.nextInt();
        x = tec.nextInt();
        a= x+x;
        System.out.println(a);
    }
    ```

    c.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x+y;
        a = x*y;
        System.out.println(a);
    }
    ```
    
    d.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x+y;
        System.out.println(a);
        a = x*y;
        System.out.println(a);
    }
    ```
    
    e.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x+y;
        a = a+x+y;
        a = a+a;
        System.out.println(a);
    }
    ```

    f.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x;
        a = doble(x);
        System.out.format ("%d%n%d%n%d",x,y,a);
    }
    public static int doble(int num){
        return 2*num;
    }
    ```
    
    g.

    ```java
    public static void main (String[] args) {
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = x;
        doble(a);
        System.out.format("%d%n%d%n%d%n",x,y,a);
    }
    public static void doble(int x){
        x = 2*x;
    }
    ```
    
    h.

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        a = calcular(y,x);
        System.out.format("%d%n%d%n%d%n",x,y,a);
    }
    public static int calcular (int x, int y){
        return x-y;
    }
    ```
    
    i. 

    ```java
    public static void main (String[] args){
        Scanner tec = new Scanner(System.in);
        int x,y,a;
        x = tec.nextInt();
        y = tec.nextInt();
        y = calcular(x);
        a = calcular(y);
        System.out.format("%d%n%d%n%d%n",x,y,a);
    }
    public static int calcular (int x){
        return x*x;
    }
    ```

2. (Traza2) **Datos de entrada: 2, 5, 7**

    ```java
    public static void main (String[] args){
        int k,l,m,x,y,z;
        k = tec.nextInt();
        l = tec.nextInt();
        m = tec.nextInt();
        x = k+l;
        if (x != m) {
            y = k*l;
            z = 0;
        } else {
            y = 0;
            z = k-l;
        }
        if (z < 0) z = -z;
            System.out.format("%d%n%d%n%d%n",x,y,z);
    }
    ```

3. (Traza3) **Datos de entrada: 2, 5, 7, 9, -9, -7, -5, -2**

    a.

    ```java
    public static void main (String[] args){
        int x,y;
        x = 0;
        y = tec.nextInt();
        while(!(y<0)) {
            x+=-y;
            y = tec.nextInt();
            System.out.format("%d, %d",x,y);
        }
    }
    ```
    
    b.

    ```java
    public static void main (String[] args){
        int x,y,z,a;
        x = y = z = a = 0;
        x = tec.nextInt();
        while(x>0) {
            if (y < z) y = tec.nextInt();
            else z= tec.nextInt();
            a = a-x+y*z;
            x = tec.nextInt();
            System.out.format("%d, %d, %d, %d",a,x,y,z);
        }
    }
    ```

4. (Traza4) **Datos de entrada: 5, 5, 7, -5, -4, 2**

    a.

    ```java
    public static void main (String[] args){
        int x, y, a=0;
        x = 0;
        y = 99;
        while (x >= 0) {
            x = tec.nextInt();
            y = tec.nextInt();
            a = a + x*y;
        }
        System.out.println(a);
    }
    ```

    b.

    ```java
    public static void main (String[] args){
        int x, y, a=0;
        x = 0;
        y = 99;
        while (x >= 0 && y >= 0) {
            x = tec.nextInt();
            y = tec.nextInt();
            a = a + x*y;
        }
        System.out.println(a);
    }
    ```

    c.

    ```java
    public static void main (String[] args){
        int x, y, a=0;
        x = 0;
        y = 99;
        while (x >= 0 && y <= 0) {
            x = tec.nextInt();
            y = tec.nextInt();
            a = a + x*y;
        }
        System.out.println(a);
    }
    ```

    d.

    ```java
    public static void main (String[] args){
        int x, y, a=0;
        x = 0;
        y = 99;
        while (x >= 0 || y >= 0) {
            x = tec.nextInt();
            y = tec.nextInt();
            a = a + x*y;
        }
        System.out.println(a);
    }
    ```

5. (Traza5) **Datos de entrada: 5, 5, 7, -5, -4, 2**

    ```java
        public static void main(String[] args) {
            int x, y;
    
            x = 2;
            y = 3;
            while (x + y > 0) {
                x = tec.nextInt();
                y = tec.nextInt();
                x += y;
                y = x - y;
                System.out.format("%d, %d", x, y);
            }
        }
    ```

6. (Traza6) **Datos de entrada: 2, 4, 7, 5, -6, -3, 6, 6**

    a.

    ```java
    public static void main (String[] args){
        int a,b;
        do{
            a = tec.nextInt();
            b = tec.nextInt();
            for (int i=a ; i<=b ; i++)
            System.out.println(i);
        } while (a!=b)
    }
    ```

    b.

    ```java
    public static void main (String[] args){
        int a,b;
        a=5;
        b=5;
        do {
            for (int i=a ; i<=b ; i++)
            System.out.println(i);
            a = tec.nextInt();
            b = tec.nextInt();
        } while (a!=b);
    }
    ```

7. (Traza7) **Datos de entrada: 3, 3, 5, 5, -3, -7, 2, 2**

    ```java
    public static void main (String[] args){
        int x,y;
        do {
            x = tec.nextInt();
            b = tec.nextInt();
        } while (x==y);
        if (x>y) {
            x=y;
            y=x;
        }
        System.out.format("%d %d %n",x,y);
    }
    ```

8. (Traza8) **Datos de entrada: 3, 2, 1, 4**

    ```java
    public static void main (String[] args){
        int a=0,b;
        b = tec.nextInt();
        for(int i=1;i<=b,i++) a=(a+i)*i;
        System.out.println(a);
    }
    ```

9. (Traza9) **Datos de entrada:** No aplica

    ```java
    public static void main (String[] args){
        int x,y;
        for (x=3;x>=1;x--){
            for(y=1;y<=x;y++) System.out.println(x);
            System.out.println();
        }
    }
    ```

10. (Traza10) **Datos de entrada:** No aplica

    ```java
    public static void main (String[] args){
        int x,y;
        x=0;
        y=0;
        for (int i=1;i<=2;i++) {
            for (int j=1;j<=3;j++) x=(x+i)*j;
            	y+=x;
        }
        System.out.println("%d %d %n",x,y);
    }
    ```

11. (Traza11) **Datos de entrada: 4, 5, 6, 7, 8, 9**

    ```java
    public static void main (String[] args){
        int x,y;
        do x = tec.nextInt();
        while (x<=5);
        y=0;
        for (int i=12;i>=x;i-=2) y+=(x*i);
        System.out.println(y);
    }
    ```

### Excepciones

1. (Edades) Escribe un programa que solicite al usuario la edad de cinco personas y calcule la media. La edad  de una persona debe ser un valor entero comprendido en el rango [0,110]. Realiza tres versiones:
    1. (Edades_1) Si se introduce mal la edad de una persona se vuelve a pedir la edad de esa persona.

       ```sh
       Introduce una edad entre 0 y 110 para la persona 1: 55
       Introduce una edad entre 0 y 110 para la persona 2: 125
       Introduce una edad entre 0 y 110 para la persona 2: -4
       Introduce una edad entre 0 y 110 para la persona 2: 34
       Introduce una edad entre 0 y 110 para la persona 3: 45
       Introduce una edad entre 0 y 110 para la persona 4: 12
       Introduce una edad entre 0 y 110 para la persona 5: 5
       La media de las 5 edades introducidas es: 30,20
       ```

    2. (Edades_2) Si se introduce mal la edad de una persona, el programa muestra un mensaje de error, no calcula la media y termina.

       ```sh
       Introduce una edad entre 0 y 110 para la persona 1: 55
       Introduce una edad entre 0 y 110 para la persona 2: 125
       java.lang.Exception: La edad introducida debe estar entre 0 y 110.
       ```

    3. (Edades_3) Si se introduce mal la edad de una persona, el programa vuelve a solicitar la edad de las cinco personas (comienza el proceso).

2. (PosicionLetra) Escribe los programas que se indican a continuación. Ejecuta cada programa haciendo que la entrada del usuario provoque una excepción. Anota el nombre de la excepción que se produce y cuál es la jerarquía de objetos de la que desciende:

    1. Programa que solicita dos números enteros (a y b) y muestra el resultado de su división (a/b).

        1. El usuario introduce 0 como valor de b.
        2. El usuario introduce letras cuando el programa espera números enteros.
        3. El usuario introduce un número real cuando el programa espera un entero.

    2. Programa que solicita al usuario su nombre y una posición dentro del nombre. Se muestra al usuario la letra del nombre cuya posición se ha indicado. Por ejemplo:

        ```sh
        Introduce nombre: Javi
        Introduce posición: 2
        En la posición 2 de Javi está la letra a
        ```

        1. El usuario introduce una posición inválida.

3. (PosicionLetraMain) Repite el ejercicio anterior utilizando métodos y llamándolos desde el método `main`:
    1. Un método `dividir` que devuelva el cociente de dos números que recibe como parámetro
    2. Un método `letraNombre` que, dados un String `nombre` y un entero `pos`, devuelva el carácter del nombre que ocupa la posición indicada.
    Ejecuta los programas provocando errores (como en el ejercicio anterior) y observa los mensajes que se generan.

4. (DividirArgs) Escribir un programa que divida dos números que se reciben en main en `args[0]` y `args[1]`. 

    Ejemplo:

    ```sh
    $ java dividir 10 5
    10/5 es igual a 2
    ```

    Donde 10 y 5 son `args[0]` y `args[1]` respectivamente, es decir los parámetros con que llamamos al programa dividir.

5. (PorqueError) Justifica por qué se produce error en el siguiente fragmento de código

    ```java
    try {
        System.out.println("Introduce edad: ");
        int edad = tec.nextInt();
        if (edad >= 18) {
            System.out.println("Mayor edad");
        } else {
            System.out.println("Menor edad");
        }
        System.out.println("Introduce nif");
        String nif = tec.next();
        int numero = Integer.parseInt(nif.substring(0, nif.length() - 1));
        char letra = nif.charAt(nif.length() - 1);
        System.out.println("Numero: " + numero);
        System.out.println("Letra: " + letra);
    } catch (Exception e){  
        System.out.println("Debías introducir un número");
    } catch (NumberFormatException e) {
        System.out.println("El nif es incorrecto");
    }
    ```

6. (SalidaPantalla) Indica qué se mostrará por pantalla cuando se ejecute esta clase y por qué:

    ```java
    public class Uno {
          private static int metodo()  {
                int valor=0;
                try  {
                      valor = valor + 1;
                      valor = valor + Integer.parseInt("42") ;
                      valor = valor + 1;
                      System.out.println("Valor al final del try: " + valor);
                } catch(NumberFormatException e)  {
                      valor = valor + Integer.parseInt ("42");
                      System.out.println("Valor al final del catch: " + valor) ;
                }
                finally  {
                      valor = valor + 1;
                      System.out.println("Valor al final de finally: " + valor) ;
                }
                valor = valor + 1;
                System.out.println ("Valor antes del return: " + valor) ;
                return valor;
          }
          
          public static void main(String[] args)  {
                try {
                      System.out.println (metodo());
                }  catch (Exception e)  {
                      System.err.println("Excepcion en metodo()") ;
                      e.printStackTrace();
                }
          }
    }
    ```

7. (SalidaPantalla2) Indica qué se mostrará por pantalla cuando se ejecute esta clase y por qué:

    ```java
    public class Dos {
          private static int metodo()  {
                int valor=0;
                try   {
                      valor = valor+1;
                      valor = valor + Integer.parseInt("W");
                      valor = valor + 1;
                      System.out.println("Valor al final del try: " + valor);
                } catch(NumberFormatException e) {
                      valor = valor + Integer.parseInt("42");
                      System.out.println("Valor al final del catch: " + valor) ;
                } finally {
                      valor = valor + 1;
                      System.out.println("Valor al final de finally: " + valor) ;
                }
                valor = valor + 1;
                System.out.println ("Valor antes del return: " + valor) ;
                return valor ;
          }
          
          public static void main (String[] args)  {
                try  {
                    System .out.println(metodo());
                }  catch (Exception e) {
                      System.err.println("Excepcion en metodo() ");
                      e.printStackTrace();
                }
          }
    }
    ```

8. (SalidaPantalla3) Indica qué se mostrará por pantalla cuando se ejecute esta clase y por qué:

    ```java
    public class Tres {
          private static int metodo()  {
                int valor = 0;
                try {
                      valor = valor +1;
                      valor = valor + Integer.parseInt("W");
                      valor = valor + 1;
                      System.out.println("Valor al final del try : " + valor);
                } catch (NumberFormatException e) {
                      valor = valor + Integer.parseInt("W");
                      System.out.println("Valor al final del catch : " + valor);
                } finally {
                      valor = valor + 1;
                      System.out.println("Valor al final de finally: " + valor);
                }
                valor = valor + 1;
                System.out.println ("Valor antes del return: " + valor);
                return valor ;
          }
    
          public static void main (String[ ] args)
          {
                try {
                      System.out.println(metodo ());
                } catch (Exception e) {
                      System.err.println("Excepcion en metodo()") ;
                      e.printStackTrace();
                }
          }
    }
    ```

9. (SalidaPantalla4) Indica qué se mostrará por pantalla cuando se ejecute esta clase y por qué:

    ```java
    import java.io.*;
    
    public class Cuatro
    {
          private static int metodo()  {
                int valor = 0;
                try {
                      valor = valor+1;
                      valor = valor + Integer.parseInt("W");
                      valor = valor + 1;
                      System.out.println("Valor al final del try : " + valor) ;
                      throw new IOException();
                } catch (IOException e)  {
                      valor = valor + Integer.parseInt("42");
                      System.out.println("Valor al final del catch : " + valor);
                } finally {
                      valor = valor + 1;
                      System.out.println("Valor al final de finally: " + valor);
                }
                valor = valor + 1;
                System.out.println ("Valor antes del return: " + valor) ;
                return valor ;
          }
    
          public static void main(String[] args)  {
                try {
                      System.out.println(metodo());
                } catch (Exception e) {
                      System.err.println("Excepcion en metodo()");
                      e.printStackTrace();
                }
          }
    }
    ```

10. (SalidaPantalla5) Indica qué se mostrará por pantalla cuando se ejecute esta clase:

    1. Si se ejecuta con `java Cinco casa`
    2. Si se ejecuta con `java Cinco 0`
    3. Si se ejecuta con `java Cinco 7`

    ```java
    public class Cinco {
       public static void main(String args[])  {
          try  {
             	int a = Integer.parseInt(args[0]);
             	System.out.println("a = " + a);
             	int b=42/a;
    			String c = "hola";
                char d = c.charAt(50);
          }  catch (ArithmeticException e) {
             System.out.println("div por 0: " + e);
          }  catch (IndexOutOfBoundsException e) {
             System.out.println("Índice del String fuera de límites: " + e);
          }  finally {
              System.out.println("Ejecución de finally");
          }
       }
    }
    ```

11. (SalidaPantalla6) Indica cuál será la salida del siguiente programa y por qué

      ```java
      public class Seis {
         public static void procA()  {
             try {
                 System.out.println("dentro del procA"); 2
                 throw new RuntimeException("demo"); 3
             } finally {
                 System.out.println("Finally del procA"); 4
             }
          }
      
         public static void procB() {
             try  {
                 System.out.println("dentro del procB"); 6
                 return; 7
             } finally {
                 System.out.println("finally del procB"); 8
             }
          }
      
          public static void main(String args[])  {
              try  {
                  procA(); 1
              } catch(Exception e) {
                  procB(); 5
              }
           }
      }
      ```

12. (SalidaPantalla7) Indica cuál será la salida del siguiente programa y por qué

      ```java
      public class Siete {
         public static void metodo() {
             try  {
                 throw new NullPointerException("demo"); 2
             } catch (NullPointerException e) {
                 System.out.println("capturada en método"); 3
                 throw e; 4
             }
          }
      
          public static void main (String args[])  {
              try   {
                  metodo(); 1
              }  catch(NullPointerException e)  {
                 System.out.println("capturada en main " + e); 5
              }
          }
      }
      ```

13. (DivisionPorCero)  Crea un programa que intente dividir dos números enteros ingresados por  el usuario y maneja la excepción de división por cero. [Aquí](https://stackoverflow.com/questions/2381544/why-doesnt-java-throw-an-exception-when-dividing-by-0-0) tienes la explicación de porqué la división entre 0 no provoca excepciones para `double` y `float`.

      ```sh
      Introduce el dividendo (entero): 85
      Introduce el divisor (entero): 4
      El resultado de 85/4 es: 21
      
      Introduce el dividendo (entero): 5
      Introduce el divisor (entero): 0
      Error: División por cero no permitida.
      ```

14. (CalculadoraExcepcion) Crea una clase `CalculadoraExcepcion` con un método `dividir` que acepte dos números con decimales como argumentos, devuelva su resultado o lance una excepción  personalizada (`DivisionPorCeroException`) si el divisor es cero. Captura la excepción en el método  `main` y muestra un mensaje de error.

      ```sh
      Introduce el dividendo: 15,5
      Introduce el divisor: 4
      El resultado de 15.5/4.0 es: 3.875
      
      Introduce el dividendo: 3,5
      Introduce el divisor: 0
      Error: División por cero no permitida.
      ```

15. (EntradaNoNumerica) Escribe un programa que lea un número entero desde el teclado. Si el  usuario ingresa algo que no es un número entero, maneja la excepción y  muestra un mensaje de error.

16. (RangoNumerico) Escribe un programa que solicite al usuario ingresar un número entre 1 y 100. Si el número está fuera de ese rango, lanza una excepción  personalizada (`NumeroFueraDeRangoException`) y muestra un mensaje de error.

     ```sh
     Introduce un número entre 1 y 100: 5
     Número válido: 5
     
     Introduce un número entre 1 y 100: 500
     Error: Número fuera de rango: 500
     ```

17. (NumeroNegativo) Crea un método que reciba dos números como argumentos y lance una excepción personalizada si uno de los números es negativo. Captura esa excepción en el método principal y muestra un mensaje de error.

     ```sh
     Introduce el primer número: 5
     Introduce el segundo número: 4
     Ambos números son positivos.
     
     Introduce el primer número: -4
     Introduce el segundo número: 5
     Error: Uno de los números es negativo.
     ```

18. (LongitudCadena) Diseña un programa que lea una cadena de caracteres desde el teclado y, si la longitud de la cadena es mayor de 10 caracteres, lance una  excepción personalizada. Captura esa excepción y muestra un mensaje de  error.

19. (TemperaturaInvalida) Implementa una clase `ConversorTemperatura` que tenga un método para convertir grados Celsius a Fahrenheit. Si el  valor en grados Celsius es inferior a -273.15, lanza una excepción  personalizada. Captura la excepción y muestra un mensaje de error en el  método principal.

20. (EdadInvalida) Diseña una clase `ValidadorEdad` que tenga un método para validar si una persona tiene una edad válida  (por ejemplo, entre 0 y 120 años). Si la edad no es válida, lanza una  excepción personalizada y muestra un mensaje de error en el método  principal.

### Aserciones

1. (Aserciones1) A partir del siguiente fragmento de código, añade una linea debajo del comentario de la linea 4 que haga lo que se solicita:

    ```java
    class Main {
        public static void main(String args[]) {
            String[] finde = {"viernes", "sabado", "domingo"};
            //Añade una aserción que compruebe que solo hay dos dias en el fin de semana.

            System.out.println("Solo hay " + weekends.length + "  dias en el fin de semana");
        }
    }
    ```

2. (Aserciones2) Escribe un método llamado `validarEdad(int edad)` que acepte como parámetro la edad de una persona. Usa una aserción para verificar que la edad sea un valor positivo y menor que 150. Si la edad es negativa o extremadamente alta, la aserción debería fallar. Dispones del siguiente `main`:

    ```java
    public static void main(String[] args) {
        // Caso que debe pasar la aserción
        validarEdad(25);
        // Caso que debe fallar la aserción (edad negativa)
        validarEdad(-5);
    }
    ```

3. (Aserciones3) Crea un método llamado `esPar(int numero)` que devuelva `true` si el número es par y `false` en caso contrario. Luego, escribe una aserción para verificar que el resultado es `true` cuando el número proporcionado es efectivamente par. Dispones del siguiente `main`:

    ```java
    public static void main(String[] args) {
        // Caso que debe devolver true
        assert esPar(4) : "El número 4 debería ser par";
        // Caso que debe devolver false
        assert !esPar(3) : "El número 3 no debería ser par";
        // Hace saltar la excepción si las aserciones están activadas y alguna falla
        assert esPar(5) : "Hará saltar la excepción";
    }
    ```

4. (Aserciones4) Implementa un método llamado `dentroDeRango(int numero, int min, int max)` que devuelva `true` si el número está en el rango `[min, max]` y `false` en caso contrario. Usa aserciones para probar que el método devuelve `true` para un número dentro del rango y `false` para uno fuera.

    ```java
    // Ejemplo de uso:
    assert dentroDeRango(5, 1, 10) : "El número 5 debería estar en el rango [1, 10]";
    assert !dentroDeRango(15, 1, 10) : "El número 15 no debería estar en el rango [1, 10]";
    ```

## Actividades

1. (TransformarBucle) Transforma el siguiente bucle for en un bucle while:

    ```java
    for (i=5; i<15; i++) { 
        System.out.println(i);
    }
    ```

2. (NumerosPares) Escribe un método (`nPares`) que recibe un número `n` y que devuelve un `String` con los `n` primeros números pares. Escribe un método `main` que pida un número al usuario y use el método `nPares` para mostrarlos en pantalla.

    ```sh
    Introduce un número entero positivo: 15
    2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 
    ```

3. (Rango) Escribe un método (`rango`) que recibe dos enteros y que devuelve un `String` que comience con el primero y termine en el segundo. Se asume que el primero será menor que el segundo. Escribe un método `main` que pida los dos números al usuario y muestre el rango de números usando el método `rango`:

    ```sh
    Introduce el primer número del rango: 200
    Introduce el segundo número del rango: 250
    200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 
    ```

4. (TablasMultiplicar) Escribe un método (`tabla`) que recibe un número entero positivo y devuelve un String con la tabla de múltiplicar de dicho número con el siguiente formato:
    ```sh
    Tabla del 2
    2 x 1 = 2
    2 x 2 = 4
    ...
    2 x 10 = 20    
    ```
    Escribe un método main, que usando el método tabla imprima por pantalla las tablas del 1 al 10.

5. (SinMultiplos5) Programa que muestre los números del 1 al 100 sin mostrar los múltiplos de 5.

    ```sh
    ...
    28
    29
    31
    32
    33
    34
    36
    37
    38
    39
    41
    42
    43
    ...
    ```

    !!! warning "Atención"
        Para pasar satisfactoriamente los tests, en lugar de usar `System.out.println`, debes usar `System.out.print` con un `\n` al final de la cadena a imprimir.

6. (CuadradoHastaNegativo) Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo.

7. (PositivoNegativo) Leer un número e indicar si es positivo o negativo. El proceso se repetirá hasta que se introduzca un 0.

8. (ParImpar) Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar.

9. (ContarNumeros) Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido.

10. (AdivinarNumero) Realizar un juego para adivinar un número `X`. Para ello pedir un número `N`, y luego ir pidiendo números indicando "mayor" o "menor" según sea mayor o menor con respecto a `X`. El proceso termina cuando el usuario acierta.

    ```sh
    Voy a pensar un número menor que 1000 para que lo adivines...
    
    Introduce que número crees que he pensado: 500
    El número que he pensado es menor que 500
    Introduce que número crees que he pensado: 250
    El número que he pensado es menor que 250
    Introduce que número crees que he pensado: 125
    El número que he pensado es mayor que 125
    Introduce que número crees que he pensado: 187
    El número que he pensado es mayor que 187
    Introduce que número crees que he pensado: 210
    El número que he pensado es mayor que 210
    Introduce que número crees que he pensado: 230
    El número que he pensado es mayor que 230
    Introduce que número crees que he pensado: 240
    El número que he pensado es mayor que 240
    Introduce que número crees que he pensado: 245
    Enhorabuena has acertado, el número que había pensado es el 245
    ```

11. (SumaNumeros) Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos.

12. (MediaNumeros) Pedir números hasta que se introduzca uno negativo, y calcular la media.

13. (NumerosHastaN) Pedir un número `N`, y mostrar todos los números del 1 al `N`.

14. (De100a0) Escribir todos los números del 100 al 0 de 7 en 7.

15. (Suma15Numeros) Pedir 15 números y escribir la suma total.

16. (ProductoImpares) Diseñar un programa que muestre el producto de los 10 primeros números impares.

17. (Factorial) Pedir un número y calcular su factorial (el factorial se representa con el simbolo  `!`).

         Aquí tienes el factorial de los 5 primeros números enteros:
         
         ```shell
         1! = 1
         2! = 2 * 1 = 2
         3! = 3 * 2 * 1 = 6
         4! = 4 * 3 * 2 * 1 = 24
         5! = 5 * 4 * 3 * 2 * 1 = 120
         ```
         
         Ejemplo de ejecución del programa:
         
         ```shell
         Dime el número para calcular su factorial: 6
         6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
         ```

18. (MediaPosNeg) Pedir 10 números. Mostrar la media de los números positivos, la media  de los números negativos y la cantidad de ceros.

19. (Sueldos1000) Pedir 10 sueldos. Mostrar su suma y cuantos hay mayores de 1000€.

20. (AlumnosEdadAltura) Dadas las edades y alturas de 5 alumnos, mostrar la edad y la estatura  media, la cantidad de alumnos mayores de 18 años, y la cantidad de  alumnos que miden más de 1.75.

21. (TablaMultiplicar) Pide un número (que debe estar entre 0 y 10) y mostrar la tabla de multiplicar de dicho número.

22. (AprobadosSuspensos) Dadas 6 notas, escribir la cantidad de alumnos aprobados y suspensos.

23. (SueldoMaximo) Pedir un número `N`, introducir `N` sueldos, y mostrar el sueldo máximo.

24. (HayNegativo) Pedir 10 números, y mostrar al final si se ha introducido alguno negativo.

25. (HaySuspenso) Pedir 5 calificaciones de alumnos y decir al final si hay algún suspenso.

26. (Multiplo3) Pedir 5 números e indicar si alguno es múltiplo de 3.

27. (SaludoHorario) Realiza un programa que pida una hora por teclado y que muestre luego  buenos días, buenas tardes o buenas noches según la hora. Se utilizarán  los tramos de 6 a 12, de 13 a 20 y de 21 a 5. respectivamente. Sólo se  tienen en cuenta las horas, los minutos no se deben introducir por  teclado.

28. (DiaSemana) Escribe un programa en que dado un número del 1 a 7 escriba el correspondiente nombre del día de la semana.

29. (SalarioHorasExtras) Escribe un programa que calcule el salario semanal de un trabajador  teniendo en cuenta que las horas ordinarias (40 primeras horas de  trabajo) se pagan a 12 euros la hora. A partir de la hora 41, se pagan a 16 euros la hora.

30. (MediaTresNotas) Realiza un programa que calcule la media de tres notas.

31. (BoletinNotas) Amplía el programa anterior para que diga la nota del boletín  (insuficiente, suficiente, bien, notable o sobresaliente).

32. (Horoscopo) Escribe un programa que nos diga el horóscopo a partir del día y el mes de nacimiento.

33. (Cuestionario) Realiza un minicuestionario con 4 preguntas tipo test sobre las  asignaturas que se imparten en el curso. Cada pregunta acertada sumará  un punto. El programa mostrará al final la calificación obtenida.

34. (NotaProgramacion) Calcula la nota de un trimestre de la asignatura Programación. El  programa pedirá las dos notas que ha sacado el alumno en los dos  primeros controles. Si la media de los dos controles da un número mayor o igual a 5, el alumno está aprobado y se mostrará la media. En caso de  que la media sea un número menor que 5, el alumno habrá tenido que hacer el examen de recuperación que se califica como apto o no apto, por  tanto se debe preguntar al usuario ¿Cuál ha sido el resultado de la  recuperación? (apto/no apto). Si el resultado de la recuperación es  apto, la nota será un 5; en caso contrario, la nota será 1.

         Ejemplo 1:
         
         ```sh
         Nota del primer control: 7 Nota del segundo control: 10
         Tu nota de Programación es 8.5
         ```
         
         Ejemplo 2:
         
         ```sh
         Nota del primer control: 6 Nota del segundo control: 3
         ¿Cuál ha sido el resultado de la recuperación? (apto/no apto): apto
         Tu nota de Programación es 5
         ```
         
         Ejemplo 3:
         
         ```sh
         Nota del primer control: 6 Nota del segundo control: 3
         ¿Cuál ha sido el resultado de la recuperación? (apto/no apto): no apto
         Tu nota de Programación es 1
         ```

35. (Multiplos5For) Muestra los números múltiplos de 5 entre el 0 y el 100 utilizando un bucle `for`.

36. (Multiplos5While) Muestra los números múltiplos de 5 entre el 0 y el 100 utilizando un bucle `while`.

37. (Multiplos5DoWhile) Muestra los números múltiplos de 5 entre el 0 y el 100 utilizando un bucle `do while`.

38. (ContarAtrasFor) Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando un bucle `for`.

39. (ContarAtrasWhile) Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando un bucle `while`.

40. (ContarAtrasDoWhile) Muestra los números del 320 al 160, contando de 20 en 20 utilizando un bucle `do-while`.

41. (CajaFuerte) Realiza el control de  acceso a una caja fuerte. La combinación será un número de 4 cifras. El  programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje "**Esa no es la combinación correcta**" y si acertamos se nos dirá "**La caja se ha abierto correctamente**". Tendremos cuatro oportunidades para abrir la caja fuerte, si lo sobrepasamos nos dirá "**Has sobrepasado el número de intentos permitido**".

     !!! warning "Atención"
         Para pasar satisfactoriamente los tests, la combinación de apertura debe estar configurada en "1234"

42. (CuadradoCubo) Escribe un programa que muestre en tres columnas, el cuadrado y el cubo de los 5 primeros números enteros a partir de uno que se introduce por  teclado.

43. (Potencia) Escribe un método (`potencia`) que reciba una base y un exponente (enteros positivos) y que calcule la potencia (sin usar `Math`). Escribe un método `main` para pedir los datos al usuario y usando el método `potencia` mostrar el resultado.

       ```sh
       Vamos a calcular una potencia.
       Introduce la BASE: 6
       Introduce el EXPONENTE: 5
       El resultado de elevar la BASE: 6 al EXPONENTE: 5 resulta en: 7776
       ```

44. (Suma100Siguientes) Realiza un programa que sume los 100 números siguientes a un número  entero y positivo introducido por teclado. Se debe comprobar que el dato introducido es correcto (que es un número positivo).

45. (NumerosEntre7) Escribe un programa que imprima por pantalla los números enteros comprendidos entre  dos números introducidos por teclado y validados como distintos, el  programa debe empezar por el menor de los enteros introducidos e ir incrementando de 7 en 7.

        ```sh
        Introduce dos números DIFERENTES!
        Introduce el primer número: 8
        Introduce el segundo número: 8
        Los números no son DIFERENTES!
        
        Introduce dos números DIFERENTES!
        Introduce el primer número: 6
        Introduce el segundo número: 50
        6
        13
        20
        27
        34
        41
        48
        ```

46. (EstadisticasNumeros) Realiza un programa que vaya pidiendo números hasta que se introduzca  un numero negativo y nos diga cuantos números se han introducido, la  media de los impares y el mayor de los pares. El número negativo sólo se utiliza para indicar el final de la introducción de datos pero no se  incluye en el cómputo.

47. (SumaHasta10000) Escribe un programa que permita ir introduciendo una serie  indeterminada de números mientras su suma no supere el valor 10000.  Cuando esto último ocurra, se debe mostrar el total acumulado, el  contador de los números introducidos y la media.

48. (Multiplos3) Escribe un programa que muestre, cuente y sume los múltiplos de 3 que hay entre 1 y un número leído por teclado.

49. (PrecioFinal) Escribe un programa que calcule el precio final de un producto según su base imponible (precio antes de impuestos), el tipo de IVA aplicado  (general, reducido o superreducido) y el código promocional. Los tipos  de IVA general, reducido y superreducido son del 21%, 10% y 4%  respectivamente. Los códigos promocionales pueden ser nopro, mitad,  meno5 o 5porc que significan respectivamente que no se aplica promoción, el precio se reduce a la mitad, se descuentan 5 euros o se descuenta el 5%.

         Ejemplo:
         
         ```sh
         Introduzca la base imponible: 25
         Introduzca el tipo de IVA (general, reducido o superreducido): reducido
         Introduzca el código promocional (nopro, mitad, meno5 o 5porc): mitad
         Base imponible 25.00
         Cód. promo. (mitad): -12.50
         IVA (10%) 1.25
         Precio con IVA 13.75
         TOTAL 13.75
         ```

50. (AnioBisiesto) Pedir un año e indicar  si es bisiesto, teniendo en cuenta que son bisiestos todos los años  divisibles por 4, excluyendo los que sean divisibles por 100, pero no  los que sean divisibles por 400.

         En pseudocódigo se calcularía así:
         
         ```pseudocode
         SI ((año divisible por 4) Y ((año no divisible por 100) O (año divisible por 400)))ENTONCES
         	es bisiesto
         SINO
         	no es bisiesto
         FIN_SI
         ```

51. (NumeroALetras) Pedir un número de 20 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y seis.

52. (VehiculoIVA) Introducir datos de un vehículo (marca, modelo y precio). Devolver el  precio con IVA del vehículo. Controlar con Excepciones que el precio del vehículo introducido son números y que el cálculo de Precio Final con  IVA no devuelva error.

53. (NotaMediaAlumnos) Introducir códigos de alumnos, nombre y nota hasta que se introduzca un código de alumno negativo. Devolver la nota media de los alumnos la  clase. Controlar con Excepciones que las notas introducidas son números y que si no se introducen alumnos el cálculo de la media no devuelva  error.

54. (ImporteFinal) Crear una función o método llamado `impFinal`, que calcule el importe final de una compra. Los parámetros que se le pasarán a la función son el `precio` del producto, las `cantidad de unidades` compradas, el `porcentaje de iva` y el `porcentaje de descuento`. El método principal debe pedir por teclado el precio del producto, las  unidades adquiridas, el porcentaje de IVA y el porcentaje de descuento y devolver el `Importe final` de la Factura.

55. (CapacidadDisco) Crear una función que calcule la capacidad de un disco. La capacidad se calcula multiplicando los Cabezales o pistas del disco por los  Cilindros por los Sectores por Tamaño de Sector. El método principal  debe pedir por teclado los Cabezales o Pistas del disco, los Cilindros,  Sectores y Tamaño de Sector y devolver la Capacidad del disco en  Gigabytes.

         Por ejemplo: Calcular la  capacidad de un disco teniendo en cuenta que dispone de 10 Cabezales o  Pistas, 65535 Cilindros, 1024 Sectores/pista y un Tamaño de 512  bytes/sector:
         
         Capacidad del disco = 10 * 65535 * 1024 * 512 = 343597383680 bytes
         
         343597383680 bytes / 1024 / 1024 / 1024 = 320 Gbytes

56. (MayorDeTres) Función que devuelva el mayor de tres números. El método principal debe pedir por teclado los tres números introducidos por el teclado. La  función debe recibir como parámetros los tres números y devolver el  mayor.