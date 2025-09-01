# Ejercicios de la UD05

## Ejercicios

### Paquete: `UD05._1.gestionEmpleados`

Una empresa quiere hacer una gestión informatizada básica de sus empleados. Para ello, de cada empleado le interesa:

- Nombre (String)
- DNI (String)
- Año de ingreso (número entero)
- Sueldo bruto anual (número real)

2. Diseñar una clase Java `Empleado`, que contenga los atributos (privados) que caracterizan a un empleado e implemente los métodos adecuados para:

   - Crear objetos de la clase: **Constructor** que reciba todos los datos del empleado a crear.

   - Consultar el valor de cada uno de sus atributos. (**Consultores** o **getters**)

   - `public int antiguedad()`. Devuelve el número de años transcurridos desde el ingreso del empleado en la empresa. Si el año de ingreso fuera posterior al de la fecha actual, devolverá 0. Para obtener el año actual puedes usar:

     - ```java
       int anyoActual = Calendar.getInstance().get(Calendar.YEAR);
       ```

   - `public void incrementarSueldo(double porcentaje)`. Incrementa el sueldo del empleado en un porcentaje dado (expresado como una cantidad real entre 0 y 100).

   - `public String toString()`. Devuelve un `String` con los datos del empleado, de la siguiente forma:  

     ```sh
     Nombre: Juan González
     Dni: 545646556K
     Año de ingreso: 1998
     Sueldo bruto anual: 20000 €
     ```

   - `public boolean equals(Object o)`. Método para comprobar si dos empleados son iguales. Dos empleados se consideran iguales si tienen el mismo DNI.
   
   - `public int compareTo(Empleado o)`. Se considera menor o mayor el empleado que tiene menor o mayor DNI (el mismo criterio que al comparar dos strings).
   
   - Método estático `public static double calcularIRPF(double salario)`. Determina el % de  IRPF que corresponde a un salario (mensual) determinado, según la siguiente tabla:
     | Desde salario (incluido) | Hasta salario (no incluido) | % IRPF |
     | :----------------------- | --------------------------- | -----: |
     | 0                      | 800                       | 3    |
     | 800                    | 1000                      | 10   |
     | 1000                   | 1500                      | 15   |
     | 1500                   | 2100                      | 20   |
     | 2100                   | infinito | 30   |

2. Diseñar una clase Java `TestEmpleado` que permita probar la clase `Empleado` y sus métodos. Para ello se desarrollará el método `main` en el que:

   - Se crearán dos empleados utilizando los datos que introduzca el usuario.
   - Se incrementará el sueldo un 20 % al empleado que menos cobre.
   - Se incrementará el sueldo un 10% al empleando más antiguo.
   - Muestra el IRPF que correspondería a cada empleado. 
   - Para comprobar que las operaciones se realizan correctamente, muestra los datos de los empleados tras cada operación.

3. Diseñar una clase `Empresa`, que permita almacenar el nombre de la empresa y la información de los empleados de la misma (máximo 10 empleados) en un array. Para ello, se utilizarán tres atributos: `nombre`, `plantilla` (array de empleados) y `numEmpleados` (número de empleados que tiene la empresa). En esta clase, se deben implementar los métodos:

   - `public Empresa (String nombre)`. Constructor de la clase. Crea la empresa con el nombre indicado y sin empleados.

   - `public void contratar(Empleado e) throws PlantillaCompletaException`. Añade el empleado indicado a la plantilla de la empresa, siempre que quepa en el array. Si no cabe, se lanzará la excepción `PlantillaCompletaException`.

   - `public void despedir(Empleado e) throws ElementoNoEncontradoException`. Elimina el empleado indicado de la plantilla. Si no existe en la empresa, se lanza `ElementoNoEncontradoException`.

   - `public void subirTrienio (double porcentaje)` Subir el sueldo, en el porcentaje indicado, a todos los empleados cuya antigüedad sea exactamente tres años.

   - `public String toString()`. Devuelve un `String` con el nombre de la empresa y la información de todos los empleados. La información de los distintos empleados debe estar separada por saltos de línea.

4. Diseñar una clase Java `TestEmpresa` que permita probar la clase `Empresa` y sus métodos. Para ello, desarrolla el método `main` y en él …:

   - Crea una empresa, de nombre "DAMCarlet".
   - Contrata a varios empleados (con el nombre, DNI, etc. que quieras).
   - Usa el método `subirTrienio` para subir un 10% el salario de los empleados que cumplen un trienio en el año actual.
   - Despide a alguno de los empleados.
   - Trata de despedir a algún empleado que no exista en la empresa.
   - Muestra los datos de la empresa siempre que sea necesario para comprobar que las operaciones se realizan de forma correcta.

### Paquete: `UD05._2.gestionHospital`

Se desea realizar una aplicación para gestionar el ingreso y el alta de pacientes de un hospital. Una de las clases que participará en la aplicación será la clase `Paciente`, que se detalla a continuación :

1. La clase `Paciente` permite representar un paciente mediante los atributos: `nombre` (cadena), `edad` (entero), `estado` (entero entre 1 -más grave- y 5 -menos grave-, 6 si está curado), y con las siguientes operaciones:

   - `public Paciente (String n, int e)`. Constructor de un objeto `Paciente` de nombre `n`, de `e` años y cuyo estado es un valor aleatorio entre 1 y 5.

   - `public int getEdad()`. Consultor que devuelve edad.

   - `public int getEstado()`. Consultor que devuelve estado.

   - `public void mejorar()`. Modificador que incrementa en uno el estado del paciente (mejora al paciente)

   - `public void empeorar()`. Modificador que decrementa en uno el estado del paciente (empeora al paciente)

   - `public String toString()`. Transforma el paciente en un `String`. Por ejemplo,

     ```sh
     Pepe Pérez 46 5
     ```

   - `public int compareTo(Paciente o)`. Permite comparar dos pacientes. Se considera menor el paciente más leve. A igual gravedad, se considera menor el paciente más joven. Ejemplo:

     - Teniendo a `David 40 3`, `Pepe 25 3` y `Juan 35 5`:

       ```sh
       David.compareTo(Juan) = 2
       Juan.compareTo(Pepe) = -2
       David.compareTo(Pepe) = 15
       ```

1. Diseñar una clase Java `TestPaciente` que permita probar la clase `Paciente` y sus métodos. Para ello se desarrollará el método `main` en el que:

   - Se crearán dos pacientes: "Antonio" de 20 años y "Miguel" de 30 años.
   - Imprimir el estado inicial de los dos pacientes.
   - Mostrar los datos del que se considere menor (según el criterio de `compareTo` de la clase `Paciente`).
   - Aplicar "mejoras" al paciente más grave hasta que los dos pacientes tengan el mismo estado.
   - Imprimir el estado final de los dos pacientes.

1. La clase **Hospital** contiene la información de las camas de un hospital, así como de los pacientes que las ocupan. Un Hospital tiene un número máximo de camas `MAXC` = 200 y para representarlas se utilizará un array (llamado `listaCamas`) de objetos de tipo Paciente junto con un atributo (`numLibres`) que indique el número de camas libres del hospital en un momento dado. El número de cada cama coincide con su posición en el array de pacientes (la posición 0 no se utiliza), de manera que `listaCamas[i]` es el Paciente que ocupa la cama `i` o es `null` si la cama está libre. Las operaciones de esta clase son:

   - `public Hospital()`. Constructor de un hospital. Cuando se crea un hospital, todas las camas están libres.

   - `public int getNumLibres()`. Consultor del número de camas libres.

   - `public boolean hayLibres()`. Devuelve true si en el hospital hay camas libres y devuelve false en caso contrario.

   - `public int primeraLibre()`. Devuelve el número de la primera cama libre del array `listaCamas` si hay camas libres o devuelve un 0 si no las hay.

   - `public void ingresarPaciente(String n, int e) throws HospitalLlenoException` Si hay camas libres, la primera de ellas (la de número menor) pasa a estar ocupada por el paciente de nombre `n` y edad `e`. Si no hay camas libres, lanza una excepción.

   - `private void darAltaPaciente(int i)`. La cama `i` del hospital pasa a estar libre. (Afectará al número de camas libres)

   - `public void darAltas()`. Se mejora el estado (método `mejorar()` de `Paciente`) de cada uno de los pacientes del hospital y a aquellos pacientes sanos (cuyo estado es 6) se les da el alta médica (invocando al método `darAltaPaciente`).

   - `public String toString()`. Devuelve un `String` con la información de las camas del hospital. Por ejemplo,

     ```sh
     1 María Medina 30 4
     2 Pepe Pérez 46 5
     3 libre
     4 Juan López 50 1
     5 libre
     ...
     199 Andrés Sánchez 29 3
     ```

1. En la clase `GestorHospital` se probará el comportamiento de las clases anteriores. El programa deberá:

   - Crear un hospital.
   - Ingresar a cinco pacientes con los datos simulados introducidos directamente en el programa.
   - Realizar el proceso de `darAltas` mientras que el número de habitaciones libres del hospital no llegue a una cantidad (por ejemplo 198).
   - Mostrar los datos del hospital cuando se considere oportuno para comprobar la corrección de las operaciones que se hacen.

### Paquete: `UD05._3.contrarreloj`

Se quiere realizar una aplicación para registrar las posiciones y tiempos de llegada en una carrera ciclista contrarreloj. 

1. La clase `Corredor` representa a un participante en la carrera. Sus atributos son el dorsal (entero), el nombre (String) y el tiempo en segundos (double) que le ha costado completar el recorrido. Los métodos con los que cuenta son:

   - `public Corredor(int d, String n)`. Constructor a partir del dorsal y el nombre. Por defecto el tiempo tardado es 0

   - `public double getTiempo()`. Devuelve el tiempo tardado por el corredor

   - `public int getDorsal()`. Devuelve el dorsal del corredor

   - `public String getNombre()`. Devuelve el nombre del corredor

   - `public void setTiempo(double t) throws IllegalArgumentException`. Establece el tiempo tardado por el corredor. Lanzará la excepción si el tiempo indicado es negativo.

   - `public void setTiempo(double t1, double t2) throws IllegalArgumentException`. Establece el tiempo tardado por el corredor. 

     `t1` indica la hora de comienzo y `t2` la hora de finalización (expresadas en segundos). La diferencia en segundos entre los dos datos servirá para establecer el tiempo tardado por el `Corredor`.

     Lanzará la excepción si el tiempo resultante es negativo

   - `public String toString()`. Devuelve un String con los datos del corredor, de la forma:

     ```sh
     (234) - Juan Ramirez - 2597 segundos
     ```

   - `public boolean equals(Object o)`. Devuelve true si los corredores tienen el mismo dorsal y false en caso contrario

   - `public int compareTo (Corredor o)`. Un corredor es menor que otro si tiene menor dorsal. 

   - `public static int generarDorsal()`. Devuelve un número de dorsal generado secuencialmente. Para ello la clase hará uso de un atributo `static int siguienteDorsal` que incrementará cada vez que se genere un nuevo dorsal.

2. Diseñar una clase Java `TestCorredor` que permita probar la clase Corredor y sus métodos. Para ello se desarrollará el método `main` en el que:

   - Se crearán dos corredores: El nombre lo indicará el usuario mientras que el dorsal se generará utilizando el método `generarDorsal()` de la clase.
   - Se establecerá el tiempo de llegada del primer corredor a 300 segundos y el del segundo a 400. 
   - Se mostrarán los datos de ambos corredores (`toString`)

3. La clase `ListaCorredores` permite representar a un conjunto de corredores. En la lista, como máximo habrá 200 corredores, aunque puede haber menos de ese número. Se utilizará un array, llamado lista, de 200 elementos junto con una propiedad `numCorredores` que permita saber cuantos corredores hay realmente. Métodos:

   - `public ListaCorredores()`. Constructor. Crea la lista de corredores, incicialmente vacía.

   - `public void anyadir(Corredor c) throws ElementoDuplicadoException`. Añade un corredor al final de la lista de corredores (pero lo más al principio posible del array), siempre y cuando el corredor no esté ya en la lista, en cuyo caso se lanzará `ElementoDuplicadoException`

   - `public void insertarOrdenado(Corredor c)`. Inserta un corredor en la posición adecuada de la lista de manera que esta se mantenga ordenada crecientemente por el tiempo de llegada. Para poder realizar la inserción debe averiguarse la posición que debe ocupar el nuevo elemento y, antes de añadirlo al array, desplazar el elemento que ocupa esa posición y todos los posteriores, una posición a la derecha.

   - `public Corredor quitar(int dorsal) throws ElementoNoEncontradoException`. Quita de la lista al corredor cuyo dorsal se indica. El array debe mantenerse compacto, es decir, todos los elementos posteriores al eliminado deben desplazarse una posición a la izquierda. El método devuelve el Corredor quitado de la lista. Si no se encuentra se lanza `ElementoNoEncontradoException`. 

   - `public String toString()` Devuelve un `String` con la información de la lista de corredores. Los minutos apareceran formateados con 2 decimales. Por ejemplo:

     ```sh
     Posición: 0
      Dorsal: 234
      Nombre: Juan Ramirez
      Tiempo: 25.97 minutos
     
     Posición: 1
      Dorsal: 26
      Nombre: José González
      Tiempo: 29.70 minutos
     ```


(Clase `Contrarreloj`) Realizar un programa que simule una contrarreloj. Para llevar el control de una carrera contrarreloj se mantienen dos listas de corredores (dos objetos de tipo `ListaCorredores`):

- (`hanSalido`) Una con los que han salido, que tiene a los corredores por orden de salida. El atributo tiempo de estos corredores será 0. Para que los corredores se mantengan por orden de salida, se añadiran a la lista utilizando el método añadir.
- (`hanLlegado`) Otra con los corredores que hay llegado a la meta. A medida que los corredores llegan a la meta se les extrae de la primera lista, se les asigna un tiempo y se les inserta ordenadamente en esta segunda lista.

En el método `main` realizar un programa que muestre un menú con las siguientes opciones:

1. `Salida`: Para registrar que una corredor ha comenzado la contrarreloj y sale de la línea de salida. Solicita al usuario el nombre de un corredor y su dorsal, y lo añade a la lista de corredores que han salido.
2. `Llegada`: Para registrar que un corredor ha llegado a la meta. Solicita al usuario el dorsal de un corredor y el tiempo de llegada (en segundos). Quita al corredor de la lista de corredores que `hanSalido`, le asigna el tiempo que ha tardado y lo inserta (ordenadamente) en la lista de corredores que `hanLlegado`
3. `Clasificación`: Muestra la lista de corredores que `hanLlegado`. Dado que esta lista está ordenada por tiempo, mostrarla por pantalla nos da la clasificación.
4. `Salir`: Sale del programa

### Paquete: `UD05._4.reservasLibreria`

Una librería quiere proporcionar a sus clientes el siguiente servicio:

Cuando un cliente pide un libro y la librería no lo tiene, el cliente puede hacer una reserva de manera que cuando lo reciban en la librería le avisen por teléfono. 

De cada reserva se almacena:

- `Nif` del cliente (`String`)
- `Nombre` del cliente (`String`)
- `Teléfono` del cliente (`String`)
- `Código` del libro reservado. (`entero`)
- Numero de `ejemplares` (`entero`)

1. Diseñar la clase `Reserva`, de manera que contemple la información descrita e implementar:
   - `public Reserva(String nif, String nombre, String tel, int codigo, int ejemplares)`. Constructor que recibe todos los datos de la reserva.
   - `public Reserva(String nif, String nombre, String tel, int codigo)`. Constructor que recibe los datos del cliente y el código del libro. Establece el número de ejemplares a uno. 
   - Consultores de todos los atributos.
   - `public void setEjemplares(int ejemplares)`. Modificador del número de ejemplares. Establece el número de ejemplares al valor indicado como parámetro. 
   - `public String toString()` que devuelva un `String` con los datos de la reserva
   - `public boolean equals(Object o)`. Dos reservas son iguales si son del mismo cliente y reservan el mismo libro.
   - `public int compareTo(Object o)`. Es menor la reserva cuyo código de libro es menor. El parámetro es de tipo `Object` así que revisa si debes hacer alguna "adaptación".
2. Diseñar una clase Java `TestReservas` que permita probar la clase `Reserva` y sus métodos. Para ello se desarrollará el método `main` en el que:
   - Se creen dos reservas con los datos que introduce el usuario. Las reservas no pueden ser iguales (equals). Si la segunda reserva es igual a la primera se pedirá de nuevo los datos de la segunda al usuario.
   - Se incremente en uno el número de ejemplares de ambas reservas.
   - Se muestre la menor y a continuación la mayor.
   - Mostrar el listado de reservas cada vez que consideres oportuno.
3. Diseñar una clase `ListaReservas` que implemente una lista de reservas. Como máximo puede haber 100 reservas en la lista. Se utilizará un array de Reservas que ocuparemos a partir de la posición 0 y un atributo que indique el número de reservas. Las reservas existentes ocuparán las primeras posiciones del array (sin espacios en blanco). Implementar los siguientes métodos:
   - `public void reservar (String nif, String nombre, String telefono, int libro, int ejemplares) throws ListaLlenaException, ElementoDuplicadoException`: Crea una reserva y la añade a la lista. Lanza `ElementoDuplicadoException` si la reserva ya estaba en la lista. Lanza `ListaLlenaException` si la lista de reservas está llena.
   - `public void cancelar (String nif, int libro) throws ElementoNoEncontradoException`. Dado un nif de cliente y un código de libro, anular la reserva correspondiente. Lanzar `ElementoNoEncontradoException` si la reserva no existe.
   - `public String toString()`: Devuelve un `String` con los datos de todas las reservas de la lista.
   - `public int numEjemplaresReservadosLibro (int codigo)`: Devuelve el número de ejemplares que hay reservados en total de un libro determinado.
   - `public void reservasLibro (int codigo)`: Dado un código de libro, muestra el nombre y el teléfono de todos los clientes que han reservado el libro.
4. Realizar un programa `GestionReservas` que, utilizando un menú, permita:
   - Realizar reserva. Permite al usuario realizar una reserva.
   - Anular reserva: Se anula la reserva que indique el usuario (Nif de cliente y código de libro).
   - Pedido: El usuario introduce un código de libro y el programa muestra el nº de reservas que se han hecho del libro. Esta opción de menú le resultará útil al usuario para poder hacer el pedido de un libro determinado.
   - Recepción: Cuando el usuario recibe un libro quiere llamar por teléfono a los clientes que lo reservaron. Solicitar al usuario un código de libro y mostrar los datos (nombre y teléfono) de los clientes que lo tienen reservado.

### Paquete: `UD05._5.gestorCorreoElectronico`

Queremos realizar la parte de un programa de correo electrónico que gestiona la organización de los mensajes en distintas carpetas. Para ello desarrollaremos:

1. La clase `Mensaje`. De un mensaje conocemos:

   - `Codigo (int)` Número que permite identificar a los mensajes.
   - `Emisor (String)`: email del emisor.
   - `Destinatario (String)`: email del destinatario.
   - `Asunto (String)`
   - `Texto (String)`

   Desarrollar los siguientes métodos:

   - Constructor que reciba todos los datos, excepto el código, que se generará automáticamente (nº consecutivo. Ayuda: utiliza una variable de clase (`static`))
   - Consultores de todos los atributos.
   - `public boolean equals(Object o)`. Dos mensajes son iguales si tienen el mismo código.
   - `public static boolean validarEMail(String email)`: Método estático que devuelve true o false indicando si la dirección de correo indicada es válida o no. Una dirección es válida si tiene la forma `direccion@subdominio.dominio`
   - `public String toString()`

2. Con la clase `TestCorreo` probaremos las clases y métodos desarrollados.

   - Crea varios mensajes con los datos que introduzca el usuario y muéstralos por pantalla.
   - Prueba el método `validarEMail` de la clase Mensaje con las direcciones siguientes (solo la primera es correcta):
     - `tuCorreo@gmail.com`
     - `tuCorreogmail.com`
     - `tuCorreo@gmail`
     - `tuCorreo.com@gmail`	

3. La clase `Carpeta`, cada carpeta tiene un nombre y una lista de Mensajes. Para ello usaremos un array con capacidad para 100 mensajes y un atributo que indique el número de mensajes que contiene la carpeta. Además se implementarán los siguientes métodos:

   - `public Carpeta(String nombre)`: Constructor. Dado un nombre, crea la carpeta sin mensajes.
   - `public void anyadir(Mensaje m)`: Añade a la carpeta el mensaje indicado.
   - `public void borrar(Mensaje m) throws ElementoNoEncontradoException`: Borra de la carpeta el mensaje indicado. Lanza la excepción si el mensaje no existe.
   - `public Mensaje buscar(int codigo) throws ElementoNoEncontradoException`: Busca el mensaje cuyo código se indica. Si lo encuentra devuelve el mensaje, en caso contrario lanza la excepción.
   - `public String toString()` que devuelva un `String` con el nombre de la carpeta y sus mensajes
   - `public static void moverMensaje(Carpeta origen, Carpeta destino, int codigo) throws ElementoNoEncontradoException`: Método estático. Recibe dos Carpetas de correo y un código de mensaje y mueve el mensaje indicado de una carpeta a otra. Para ello buscará el mensaje en la carpeta origen. Si existe lo eliminará y lo añadirá a la carpeta de destino. Si el mensaje indicado no está en la carpeta de origen lanza `ElementoNoEncontradoException`.

4. Con la clase `TestCarpetas` probaremos las clases y métodos desarrollados:

   - Crea dos carpetas de correo de nombre `Mensajes recibidos` y `Mensajes eliminados` respectivamente.
   - Crea varios mensajes y añádelos a `Mensajes recibidos`.
   - Mueve el mensaje de código 1 desde la `Mensajes recibidos` a `Mensajes elimiminados`.
   - Muestra el contenido de las carpetas antes y después de cada operación (añadir, mover,...)

### Paquete: `UD05._6.juegoDeCartas`

Se está desarrollando una aplicación que usa una baraja de cartas. Para ello, se implementarán en Java las clases necesarias. 

1. Una de ellas es la clase `Carta` que permite representar una carta de la baraja española. La información requerida para identificar una `Carta` es:

   - su `palo` (oros, copas, espadas o bastos) y
   - su `valor` (un entero entre 1 y 12).

   Para dicha clase, se pide:

   - Definir 4 constantes, atributos de clase (estáticos) públicos enteros, para representar cada uno de los palos de la baraja (`OROS` será el valor 0, `COPAS` el 1, `ESPADAS` el 2 y `BASTOS` el 3). 
   - Definir los atributos (privados): `palo` y `valor`.
   - Escribir dos constructores: uno para construir una carta de forma aleatoria (sin parámetros) y otro para construir una carta de acuerdo a dos datos: su palo y su valor (si los datos son incorrectos se lanzará `IllegalArgumentException`)
   - Escribir los métodos `consultores` y `modificadores` de los valores de los atributos.
   - Escribir un método `compareTo` para comprobar si la carta actual es menor que otra carta dada. El criterio de ordenación es por palos (el menor es oros, después copas, a continuación espadas y, finalmente, bastos) y dentro de cada palo por valor (1, 2, ..., 12).
   - Escribir un método `equals` para comprobar la igualdad de dos cartas. Dos cartas son iguales si tienen el mismo palo y valor.
   - Escribir un método `sigPalo` para devolver una nueva carta con el mismo valor que el de la carta actual pero del palo siguiente, según la ordenación anterior y sabiendo que el siguiente al palo bastos es oros.
   - Escribir un método `toString` para transformar en `String` la carta actual, con el siguiente formato: "valor de palo"; por ejemplo, "4 de oros" o "1 de bastos" (sobrescritura del método `toString` de `Object`).

2. Implementar una clase `JuegoCartas` con los métodos siguientes:

   - Un método de clase (estático) `public static int ganadora( Carta c1, Carta c2, int triunfo)` que dados dos objetos `Carta` y un número entero representando el palo de triunfo (o palo ganador), determine cuál es la carta ganadora. El método debe devolver 0 si las dos cartas son iguales. En caso contrario, devolverá -1 cuando la primera carta es la ganadora y 1 si la segunda carta es la ganadora.

     Para determinar la carta ganadora se aplicarán las siguientes reglas:

     - Si las dos cartas son del mismo palo, la carta ganadora es el as (valor 1) y, en el resto de casos, la carta ganadora es la de valor más alto (por ejemplo, "1 de oros" gana a "7 de oros", "5 de copas" gana a "2 de copas", "11 de bastos" gana a "7 de bastos").
     - Si las dos cartas son de palos diferentes:
       - Si el palo de alguna carta es el palo de triunfo, dicha carta es la ganadora.
       - En otro caso, la primera carta siempre gana a la segunda.

   - Un método `main` en el que se debe:

     - Crear una `Carta` aleatoriamente y mostrar sus datos por pantalla.
     - Generar aleatoriamente un entero en el rango [0..3] representando el palo de triunfo, y mostrar por pantalla a qué palo corresponde.
     - Crear una `Carta` a partir de un palo y un valor dados (solicitados al usuario desde teclado), y mostrar sus datos por pantalla.
     - Mostrar por pantalla la carta ganadora (invocando al método del apartado anterior con el objeto `Carta` del usuario.

## Actividades

1. (WrapperDouble) Introducir por teclado un valor de tipo `double` , convertirlo en Wrapper e imprimirlo.

2. (StringAEntero) Introducir por teclado un valor numérico en un `String` y convertirlo en entero e imprimirlo.

3. (StringAWrapper) Introducir por teclado un valor numérico entero en un `String` y convertirlo en un `Wrapper` e imprimirlo.

4. (OperacionesBinarias) Introducir por teclado dos valores numéricos enteros y la operación que queremos realizar (`suma`, `resta` o `multiplicación`). Realizar la operación y mostrar el resultado en `Binario`, `Hexadecimal` y `Octal`.

   Ejemplo de ejecución:

   ```sh
   Introduce el primer valor numérico: 14
   Introduce el segundo valor numérico: 4
   Introduce la operación (suma, resta, multiplicacion): resta
   EL RESULTADO:
    en binario: 1010
    en octal: 12
    en hexadecimal: a
   ```

5. (SegundosDesde1970) Mostrar los segundos transcurridos desde el `1 de Enero de 1970 a las 0:00:00` hasta `hoy`.

6. (FormatosFechaHora) Mostrar la `fecha` y `hora` de hoy con los siguientes formatos (para todos los ejemplos se supone  que hoy es 26 de agosto de 2021 a las 17 horas 16 minutos y 8 segundos,  tu deberas mostrar la fecha y hora de tu sistema en el momento de  ejecución):

   a) `August 26, 2021, 5:16 pm`
   b) `08.26.21`
   c) `26, 8, 2021`
   d) `20210826`
   e) `05-16-08, 26-08-21`
   f) `Thu Aug 26 17:16:08`
   g) `17:16:08`

7. (ValidarFecha) Introducir un día, un mes y un año y verificar si es una fecha correcta.

   ```sh
   Introduce un dia para la fecha: 29
   Introduce un mes para la fecha: 2
   Introduce un año para la fecha: 2022
   LA FECHA ES INCORRECTA
   
   Introduce un dia para la fecha: 29
   Introduce un mes para la fecha: 2
   Introduce un año para la fecha: 2020
   LA FECHA ES CORRECTA
   ```

8. (DiasEntreFechas) Introducir dos fechas e indicar los días transcurridos entre las dos fechas.

   ```sh
   Introduce la fecha inicial con formato dd/mm/yyyy: 01/02/2021
   Introduce la fecha final con formato dd/mm/yyyy: 15/03/2022
   La fecha inicial es: 1/2/2021
   La fecha final es: 15/3/2022
   Entre la fecha inicial y la final hay un periodo de: P1Y1M14D
   dias: 14
   meses: 1
   años: 1
   ```

9. (PagosPlazos) Introducir una fecha y devolver las fecha de los pagos a 30, 60 y 90 días.

10. (CompararFechas) Introducir tres fechas e indicar la mayor y a menor.

11. (FechaActualComparacion) Introducir el día, mes, año. Crear una fecha a partir de los datos  introducidos y comprobar e indicar si se trata de la fecha actual, si es una fecha pasada o una fecha futura.

12. (EdadEmpleado) Introducir una fecha de nacimiento de un empelado e indicar cuántos años tiene el empleado.

13. (ProductoCaducado) Introducir la fecha de caducidad de un producto e indicar si el  producto está o no caducado. El valor por defecto será la fecha actual y solo se podrán introducir fechas del año en curso.

14. (FormatoFechaCeros) Mostrar una fecha con formato dd/mm/aaaa utilizando 0 delante de los días o meses de 1 dígito.

15. (FormatoFechaExtendido) Mostrar una fecha con formato `DiaSemana`, `DiaMes` de `Mes` del `Año` a las `horas:minutos:segundos`. Por ejemplo: Miercoles, 9 de Diciembre del 2015 a las 18:45:32

16. (SumarFechaFutura) Suma 10 años, 4 meses y 5 días a la fecha actual.

    ```sh
    Hoy es: dijous, 03 de març del 2022
    Dentro de 10 años, 4 meses y 5 dias será: dijous, 08 de juliol del 2032
    ```

17. (RestarFechaPasada) Resta 5 años, 11 meses y 18 días a la fecha actual.

18. (PagoHorasExtra) Introducir el número de horas trabajadas por un empleado y la fecha en  las que las trabajo. Si el día fue sábado o domingo el precio hora  trabajada es 20€ en caso contrario 15€. Calcula la cantidad de dinero  que habrá que pagar al empleado por las horas trabajadas.

19. (CalculoNomina) Introducir la fecha inicial y final de una nómina y calcular lo que  debe cobrar el empleado sabiendo que cada día trabajado recibe 55 € y  tiene una retención del 12% sobre el sueldo.

20. (ClaseAlumno) Crear una clase `Alumno` con los atributos `codigo`, `nombre`, `apellidos`, `fecha_nacimiento`, `calificacion`. La fecha de nacimiento deberá introducirse como una fecha. Crear constructor, métodos `setter` y `getter` y `toString`. Crear una instancia con los siguientes valores `1`, `'Luis'`, `'Mas Ros'`, `05/10/1990`, `7.5`. Mostrar los datos del alumno además de su edad.

    ```sh
    Alumno{codigo=1, nombre=Luis, apellidos=Mas Ros, fecha=1990-10-05, calificacion=7.5, edad= 31}
    ```

21. (PlazoEntrega) Introducir la fecha de entrega de un documento y nos diga si está  dentro o fuera de plazo teniendo en cuenta que la fecha de entrega  límite es la fecha actual.

22. (RetencionesTrabajadores) Introducir en un array `nombre`, `apellidos` y `sueldo` de varios trabajadores y la `fecha de alta` en la empresa. Las fechas deberán introducirse como fechas. Recorrer el array y mostrar para cada trabajador la retención que debe aplicarse  sobre el sueldo teniendo en cuenta que los trabajadores incorporados  antes de 1980 tienen una retención del 20%, los trabajadores con fecha  entre 1980 y 2000 una retención del 15% y los trabajadores con fecha  posterior al 2000 la retención que aplicaremos será el 5% del sueldo.

23. (MayorEdad) Realiza un método estático que dada la `fecha de nacimiento` de una persona indique si es mayor de edad.

24. (ClaseConversor) Realiza una clase `Conversor` que tenga las siguientes características: Toma como parámetro en el constructor un valor entero. Tiene un método `getNumero` que dependiendo del parámetro devolverá el mismo número (String) en el siguiente sistema de numeración: `B Binario`, `H Hexadecimal`, `O Octal`. Realiza un método `main` en la clase para probar todo lo anterior.

25. (ConversorFechas) Realiza una clase `ConversorFechas` que tenga los siguientes métodos:

    - `String normalToAmericano(String fecha)`. Este método convierte una fecha en formato normal `dd/mm/yyyy` a formato americano `mm/dd/yyyy``
    - ``String americanoToNormal(String fecha)`. Este método realiza el paso contrario, convierte fechas en formato americano a formato normal.
