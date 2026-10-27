# Ejercicios de la UD02

## Actividades

!!! tip "Cómo leer los recuadros «Para pasar los tests»"
    Cada ejercicio que se corrige automáticamente indica el nombre exacto de la clase (con su prefijo `_NN_`), los constructores y los métodos que comprueban los tests, si son `static` o no y qué tipo devuelven. Si un nombre, un tipo o un formato no coincide exactamente, el test falla y te dice qué esperaba.

1. (Temperatura) Crear una clase llamada Temperatura con dos métodos:
    - `celsiusToFahrenheit`. Convierte grados *Celsius* a *Fahrenheit*.

    $$
    F=(1,8*C)+32
    $$

    - `fahrenheitToCelsius`. Convierte grados *Fahrenheit* a *Celsius*.
    
    $$
    C=\frac{F-32}{1,8}
    $$

    !!! info "Para pasar los tests"
        - Clase `_01_Temperatura`.
        - `public static double celsiusToFahrenheit(double celsius)`
        - `public static double fahrenheitToCelsius(double fahrenheit)`

2. (Moto) A partir de la siguiente clase:

    ```java
    public class Moto {
        
        private int velocidad;
        
        public Moto() {
    	    velocidad=0;
        }
    }
    ```

    Añade los siguientes métodos:

    - `int getVelocidad()`. Devuelve la velocidad del objeto moto.
    - `void acelera(int mas)`. Permite aumentar la velocidad del objeto moto.
    - `void frena(int menos)`. Permite reducir la velocidad del objeto moto.

    !!! info "Para pasar los tests"
        - Clase `_02_Moto`, con constructor sin parámetros.
        - Métodos de instancia (sin `static`): `int getVelocidad()`, `void acelera(int mas)` y `void frena(int menos)`.

4. (Rebajas) Crea una clase `Rebajas` con un método `descubrePorcentaje()` que descubra el descuento aplicado en un producto. El método recibe el precio original del producto y el rebajado y devuelve el porcentaje aplicado. Podemos calcular el descuento realizando la operación:
    $$
    porcentajeDescuento = \frac{precioOriginal-precioRebajado}{precioOriginal}
    $$

    !!! info "Para pasar los tests"
        - Clase `_03_Rebajas`.
        - `public static double descubrePorcentaje(double precioOriginal, double precioRebajado)`
        - Devuelve el descuento **como fracción**, no multiplicado por 100: `descubrePorcentaje(150, 123)` devuelve `0.18`.

5. (Finanzas) Realiza una clase `Finanzas` que convierta dólares a euros y viceversa. Codifica los métodos `dolaresToEuros` y `eurosToDolares`. Prueba que dicha clase funciona correctamente haciendo conversiones entre euros y dólares. La clase tiene que tener:
      - Un constructor `Finanzas()` por defecto el cual establece el cambio Dólar-Euro en 1.36.
      - Un constructor `Finanzas(double cambio)`, el cual permitirá configurar el cambio Dólar-euro a una cantidad personalizada.

    El cambio Dólar-Euro indica **cuántos euros vale 1 dólar**. Con el cambio por defecto, 1 $ = 1,36 €; por tanto, para pasar de dólares a euros se multiplica por el cambio y para pasar de euros a dólares se divide.

    !!! info "Para pasar los tests"
        - Clase `_04_Finanzas`, con los constructores `_04_Finanzas()` y `_04_Finanzas(double cambio)`.
        - Métodos de instancia: `double dolaresToEuros(double dolares)` y `double eurosToDolares(double euros)`.
        - Con el cambio por defecto (1 $ = 1,36 €): `dolaresToEuros(5)` devuelve `6.8` y `eurosToDolares(5)` devuelve `3.68` (aprox.).

6. (MiNumero) Realiza una clase `MiNumero` que proporcione el doble, triple y cuádruple de un número (que puede contener decimales) proporcionado en su constructor (realiza un método para `doble`, otro para `triple` y otro para `cuadruple`). 

    *(Opcional, no hay puntos)* Haz que la clase tenga un método `main` y comprueba los distintos métodos.

    !!! info "Para pasar los tests"
        - Clase `_05_MiNumero`, con constructor `_05_MiNumero(double numero)`.
        - Métodos de instancia: `double doble()`, `double triple()` y `double cuadruple()`.

7. (Numero) Realiza una clase `Numero` que almacene un número entero y tenga las siguientes características:
    - Constructor por defecto que inicializa a 0 el número interno.
    - Constructor que inicializa el número interno.
    - Método `anade` que permite sumarle un número al valor interno.
    - Método `resta` que resta un número al valor interno.
    - Método `getValor`. Devuelve el valor interno.
    - Método `getDoble`. Devuelve el doble del valor interno.
    - Método `getTriple`. Devuelve el triple del valor interno.
    - Método `setNumero`. Inicializa de nuevo el valor interno.

    !!! info "Para pasar los tests"
        - Clase `_06_Numero`, con los constructores `_06_Numero()` y `_06_Numero(int numero)`.
        - Métodos de instancia: `void anade(int n)`, `void resta(int n)`, `void setNumero(int n)`, `int getValor()`, `int getDoble()` y `int getTriple()`.

8. (Peso) Crea la clase `Peso`, la cual tendrá las siguientes características:
    - Deberá tener un atributo donde se almacene el peso de un objeto en kilogramos.
      En el constructor se le pasará el peso y la medida en la que se ha tomado ("Lb" para libras, "Li" para lingotes, "Oz" para onzas, "P" para peniques, "K" para kilos, "G" para gramos y "Q" para quintales).
    - Deberá de tener los siguientes métodos:
      - `getLibras`. Devuelve el peso en libras.
      - `getLingotes`. Devuelve el peso en lingotes.
      - `getPeso`. Devuelve el peso en la medida que se pase como parámetro ("Lb" para libras, "Li" para lingotes, "Oz" para onzas, "P" para peniques, "K" para kilos, "G" para gramos y "Q" para quintales).
    - Para la realización del ejercicio toma como referencia los siguientes datos:
      - 1 Libra = 16 onzas = 453 gramos.
      - 1 Lingote = 32,17 libras = 14,59 kg.
      - 1 Onza = 0,0625 libras = 28,35 gramos.
      - 1 Penique = 0,05 onzas = 1,55 gramos.
      - 1 Quintal = 100 libras = 43,3 kg.

    *(Opcional, no hay puntos)* Crea además un método `main` para testear y verificar los métodos de esta clase.

    !!! info "Para pasar los tests"
        - Clase `_07_Peso`, con constructor `_07_Peso(double peso, String medida)`.
        - Métodos de instancia: `double getLibras()`, `double getLingotes()` y `double getPeso(String medida)`.
        - Compara la medida con `equals` (`medida.equals("Lb")`), no con `==`: el test usa textos que no son literales y con `==` no los reconoce.

9. (Millas) Crea una clase con un método `millasAMetros()` que toma como parámetro de entrada un valor en millas marinas y las convierte a metros. Una vez tengas este método escribe otro `millasAKilometros()` que realice la misma conversión, pero esta vez exprese el resultado en kilómetros.

    *Nota: 1 milla marina equivale a 1852 metros.*

    !!! info "Para pasar los tests"
        - Clase `_08_Millas`.
        - `public static double millasAMetros(double millas)` y `public static double millasAKilometros(double millas)`.

10. (Coche) Crea la clase `Coche` con dos constructores. Uno no toma parámetros y el otro sí. Los dos constructores inicializarán los atributos `marca` y `modelo` de la clase.  El constructor por defecto (sin parametros) crea el coche "Ford" modelo "C-MAX". 

    *(Opcional, no hay puntos)*  Crea dos objetos (cada objeto llama a un constructor distinto) y verifica que todo funciona correctamente.

    !!! info "Para pasar los tests"
        - Clase `_09_Coche`, con los constructores `_09_Coche()` y `_09_Coche(String marca, String modelo)`.
        - Atributos `String marca` y `String modelo` (con esos nombres; pueden ser `private`). No hace falta ningún getter.

11. (Consumo) Implementa una clase `Consumo`, la cual forma parte del "ordenador de a bordo" de un coche y tiene las siguientes características:

    - Atributos:
        - kilometros.
        - litros. Litros de combustible consumido.
        - vmed. Velocidad media.
        - pgas. Precio de la gasolina.
    - Métodos:
        - `getTiempo`. Indicará el tiempo empleado en realizar el viaje.
        - `consumoMedio`. Consumo medio del vehículo (en litros cada 100 kilómetros).
        - `consumoEuros`. Consumo medio del vehículo (en euros cada 100 kilómetros).

    No olvides crear un constructor para la clase que establezca el valor de los atributos. Elige el tipo de datos más apropiado para cada atributo.

    !!! info "Para pasar los tests"
        - Clase `_10_Consumo`, con constructor `_10_Consumo(double kilometros, double litros, double vmed, double pgas)` (en ese orden).
        - Métodos de instancia: `double getTiempo()` (en horas), `double consumoMedio()` y `double consumoEuros()`.
        - Ejemplo: 100 km, 8 l, 50 km/h y 1,5 €/l → tiempo `2.0`, consumo medio `8.0`, consumo en euros `12.0`.

13. (ConsumoModificadores) Para la clase anterior implementa los siguientes métodos, los cuales podrán modificar los valores de los atributos de la clase:
      - `setKilometros`
      -  `setLitros`
      - `setVmed`
      - `setPgas`

    !!! info "Para pasar los tests"
        - Clase `_11_ConsumoModificadores`: la del ejercicio anterior (mismo constructor y métodos) más los cuatro métodos de instancia `void setKilometros(double)`, `void setLitros(double)`, `void setVmed(double)` y `void setPgas(double)`.

14. (Restaurante) Un restaurante cuya especialidad son las patatas con carne nos pide diseñar un método (`calcularClientes`) con el que se pueda saber cuántos clientes pueden atender con la materia prima que tienen en el almacén. El método recibe la cantidad de patatas y carne en kilos y devuelve el número de clientes que puede atender el restaurante teniendo en cuenta que por cada tres personas, utilizan un dos kilos de patatas y un kilo de carne.

    !!! info "Para pasar los tests"
        - Clase `_12_Restaurante`.
        - `public static int calcularClientes(double kilosPatatas, double kilosCarne)`: primero las patatas y después la carne. El resultado se trunca (no se redondea).
        - Ejemplos: `calcularClientes(2, 1)` → `3`; `calcularClientes(3, 2)` → `4`; `calcularClientes(10, 2)` → `6`.

15. (RestauranteClase) Modifica el programa anterior creando una clase que permita almacenar los kilos de patatas y carne del restaurante. Implementa los siguientes métodos:

     - `public void addCarne(int x)`. Añade x kilos de carne a los ya existentes.
     - `public void addPatatas(int x)`. Añade x kilos de patatas a los ya existentes.
     - `public int getComensales()`. Devuelve el número de clientes que puede atender el restaurante (este es el método del ejercicio anterior).
     - `public double getKilosCarne()`. Devuelve los kilos de carne que hay en el almacén.
     - `public double getKilosPatatas()`. Devuelve los kilos de patatas que hay en el almacén.

    !!! info "Para pasar los tests"
        - Clase `_13_RestauranteClase`, con constructor sin parámetros (almacén vacío).
        - Todos los métodos de la lista son de instancia, con esos nombres y tipos exactos.

16. (Proveedor) Crear un clase llamada `Proveedor` con las siguientes propiedades:
       - `cif`
       - `nombreEmpresa`
       - `descripcion`
       - `sector`
       - `direccion`
       - `telefono`
       - `poblacion`
       - `codPostal`
       - `correo`

     Crear para la clase `Proveedor` los métodos:

     - Constructor que permite crear una instancia con los datos de un proveedor.
     - Métodos get (*getters*).
     - Métodos set (*setters*).
     - Método `verificaCorreo` que devuelve true si la dirección de correo contiene `@`.
     - Método `toString` que devuelva todos los datos del proveedor.

     Crear un método principal `main` ejecutable que:

     - Cree una instancia del objeto `Proveedor` llamado `proveedor`.
     - Cambie el sector del `proveedor`.
     - Muestre el sector del `proveedor`.
     - Verifique si el correo es válido.
     - Muestre todos los datos del `proveedor`.

    !!! info "Para pasar los tests"
        - Clase `_14_Proveedor`, con constructor `_14_Proveedor(String cif, String nombreEmpresa, String descripcion, String sector, String direccion, long telefono, String poblacion, long codPostal, String correo)` (en ese orden).
        - Getters de instancia: `getCif()`, `getNombreEmpresa()`… (`telefono` y `codPostal` son `long`; el resto, `String`). Setters `setSector(String)` y `setCorreo(String)`, y `boolean verificaCorreo()`.
        - `toString()` devuelve exactamente este formato (ejemplo):

            ```
            _14_Proveedor{cif=B12345678, nombreEmpresa=Empresa Test, descripcion=Descripción de prueba, sector=Tecnología, direccion=Calle Test 123, telefono=91234567, poblacion=Madrid, codPostal=28001, correo=info@test.com}
            ```

17. (Producto) Crear una clase llamada `Producto` con las siguientes propiedades:
     - `codProducto`
     - `nombreProducto`
     - `descripcion`
     - `categoria`
     - `peso`
     - `precio`
     - `stock`

     Crear para la clase `Producto` los siguiente métodos:

     - `Producto`: Permite crear una instancia con los datos de un producto.
     - Getters y Setters para todas las propiedades.
     - `aumentaStock`: Permite aumentar el stock de unidades del producto. Se le pasa el dato de unidades que aumentamos.
     - `disminuyeStock`: Permite disminuir el stock de unidades del producto. Se le pasa el dato de unidades que disminuimos.
     - `ivaProducto`: Permite calcular el IVA aplicado al precio del producto. Se le pasa el dato del porcentaje de IVA.
     - `mostrarDatos`: Muestra los datos del producto. (No tiene test)
    
     Crear un método principal `main` ejecutable que:
    
     - Crear dos instancias de la clase `Producto` llamadas `productoHardware` y `productoSoftware`.
     - Mostrar los datos de los dos objetos `Producto` que hemos creado.
     - Aumenta el stock de unidades del `productoHardware` en 12 unidades.
     - Disminuir el stock de unidades del `productoSoftware` en 5 unidades.
     - Calcula el IVA de los dos objetos `Producto` que hemos creado.
     - Mostrar los datos de los dos objetos `Producto`, así como sus importes de IVA y los precios finales de cada una de las instancias.

    !!! info "Para pasar los tests"
        - Clase `_15_Producto`, con constructor `_15_Producto(long codProducto, String nombreProducto, String descripcion, String categoria, double peso, double precio, long stock)` (en ese orden).
        - Getters de instancia con esos tipos (`long getCodProducto()`, `double getPeso()`, `long getStock()`…).
        - `void aumentaStock(long unidades)`, `void disminuyeStock(long unidades)` y `double ivaProducto(double porcentaje)`, que devuelve **el importe del IVA** (no el precio final): con precio 49.99 e IVA 21 devuelve `10.4979`.
    
18. (Cuenta) Crea una clase llamada `Cuenta` que tendrá los siguientes atributos: `titular` y `cantidad` (puede tener decimales).

     Al crear una instancia del objeto Cuenta, el titular será obligatorio y la cantidad es opcional. Crea dos constructores que cumplan lo anterior, es decir debemos crear dos métodos constructores con el mismo nombre que será el nombre del objeto.

     Crea sus métodos get, set y el método `mostrarDatos` que devuelva un `String` con los datos de la cuenta. Tendrá dos métodos especiales:

     - `ingresar(double cantidad)`: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
     - `retirar(double cantidad)`: se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0 retirando el importe máximo en función de la cantidad disponible en el objeto.

     Crear una método principal `main` ejecutable:

     - Crear una instancia del objeto Cuenta llamada `cuentaParticular1` con el nombre del titular.
     - Crear una instancia del objeto Cuenta llamada `cuentaEmpresa1` con el nombre del titular y una cantidad inicial de dinero.
     - Mostrar el titular de la instancia `cuentaParticular1`.
     - Mostrar el saldo de la instancia `cuentaEmpresa1`.
     - Ingresar 1000 € en la instancia `cuentaParticular1`.
     - Retirar 500 € en la instancia `cuentaEmpresa1`.
     - Mostrar los datos de las dos instancias del objeto `Cuenta`.

    !!! info "Para pasar los tests"
        - Clase `_16_Cuenta`, con los constructores `_16_Cuenta(String titular)` (cantidad 0) y `_16_Cuenta(String titular, double cantidad)`.
        - Métodos de instancia: `String getTitular()`, `double getCantidad()`, `void setTitular(String)`, `void setCantidad(double)`, `void ingresar(double)`, `void retirar(double)` y `String mostrarDatos()`.
        - `mostrarDatos()` **devuelve** (no imprime) un `String` que incluye el titular y la cantidad.

19. (Libro) Crea una clase llamada `Libro` que guarde la información de cada uno de los libros de una biblioteca. La clase debe guardar las siguientes propiedades:

     - `título`
     - `autor`
     - `editorial`
     - `número de ejemplares totales`
     - `número de prestados`

     La clase contendrá los siguientes métodos:

     - Constructor por defecto.
     - Constructor con parámetros.
     - Métodos Setters/getters.
     - Método `prestamo` que incremente el atributo correspondiente cada vez que se realice un préstamo del libro. No se podrán prestar libros de los que no queden ejemplares disponibles para prestar. Devuelve `true` si se ha podido realizar la operación y `false` en caso contrario.
     - Método `devolucion` que decremente el atributo correspondiente cuando se produzca la devolución de un libro. No se podrán devolver libros que no se hayan prestado. Devuelve `true` si se ha podido realizar la operación y `false` en caso contrario.
     - Método `perdido` que decremente el atributo número de ejemplares por perdida de ejemplar. Como el ejemplar perdido estaba prestado, también decrementa el número de prestados. No se podrán perder libros que no tengan ejemplares o no se hayan prestado. Devuelve `true` si se ha podido realizar la operación y `false` en caso contrario.
     - Método `mostrarDatos` que devuelva un `String` con los datos del libro.

     Crear un método principal `main` ejecutable:

     - Crear una instancia del objeto libro `libroInformatica1` con los datos de un libro.
     - Consultar el título de la instancia `libroInformatica1`.
     - Cambiar la editorial de la instancia `libroInformatica1` por Anaya.
     - Realiza el préstamo de la instancia `libroInformatica1`.
     - Realiza otro préstamo de la instancia `libroInformatica1`.
     - Muestra los prestamos de la instancia `libroInformatica1`.
     - Realiza la devolución de la instancia `libroInformatica1`.
     - Muestra los prestamos de la instancia `libroInformatica1`.
     - Gestiona la pérdida de un ejemplar de la instancia `libroInformatica1`.
     - Muestra los ejemplares de la instancia `libroInformatica1`.
     - Muestra todos los datos de la instancia `libroInformatica1`.

    !!! info "Para pasar los tests"
        - Clase `_17_Libro`, con los constructores `_17_Libro()` y `_17_Libro(String titulo, String autor, String editorial, int ejemplaresTotales)` (los prestados empiezan en 0).
        - El constructor por defecto crea el libro `"Sin titulo"`, `"Sin autor"`, `"Sin editorial"`, con 1 ejemplar y 0 prestados.
        - Getters y setters de instancia: `getTitulo`, `getAutor`, `getEditorial`, `int getEjemplaresTotales()`, `int getEjemplaresPrestados()`, y `setTitulo`, `setAutor`, `setEditorial`, `setEjemplaresTotales(int)`.
        - `boolean prestamo()`, `boolean devolucion()` y `boolean perdido()`.
        - `mostrarDatos()` **devuelve** (no imprime) exactamente este formato:

            ```
            Titulo: Aprende Java, Autor: David Martínez, Editorial: Marcombo, Ejemplares Totales: 3, Ejemplares Prestados: 0
            ```

20. (Hospital) Crear una clase llamada `Hospital` con las siguientes propiedades y métodos: 

     - Propiedades:

         - `codHospital`
         - `nombreHospital`
         - `direccion`
         - `telefono`
         - `poblacion`
         - `codPostal`
         - `habitacionesTotales`
         - `habitacionesOcupadas`

     - Métodos:

         - `Hospital`: Permite crear una instancia con los datos de un hospital.
         - Métodos get.
         - Métodos set.
         - Método `ingreso` que incrementa las habitaciones ocupadas. No puede realizarse el ingreso si las habitaciones ocupadas son iguales a las habitaciones totales del hospital. Devuelve `true` si se ha podido realizar el ingreso.
         - Método `alta` que decrementa las habitaciones ocupadas. No puede realizarse el alta las habitaciones ocupadas son 0. Devuelve `true` si se ha podido realizar el alta.
         - Método `toString` que devuelva todos los datos del hospital.

     - Crear un método principal `main` ejecutable que:

         - Cree una instancia de la clase `Hospital` llamada `hospitalRibera`.
         - Cambie el número de habitaciones de la instancia `hospitalRibera`.
         - Muestre el número de habitaciones de la instancia `hospitalRibera`.
         - Realiza un ingreso de la instancia `hospitalRibera`.
         - Muestra las habitaciones ocupadas de la instancia `hospitalRibera`.
         - Realiza un alta de la instancia `hospitalRibera`.
         - Muestra las habitaciones ocupadas de la instancia `hospitalRibera`.
         - Muestre todos los datos de la instancia `hospitalRibera`.

    !!! info "Para pasar los tests"
        - Clase `_18_Hospital`, con constructor `_18_Hospital(int codHospital, String nombreHospital, String direccion, long telefono, String poblacion, long codPostal, int habitacionesTotales, int habitacionesOcupadas)` (en ese orden).
        - Getters y setters de instancia con esos tipos, `boolean ingreso()` y `boolean alta()`.
        - `toString()` devuelve un `String` que contiene todos los datos del hospital.

21. (Medico) Crear un clase llamada `Medico` con las siguientes propiedades y métodos:

     - Propiedades:

         - `codMedico`
         - `nombre`
         - `apellidos`
         - `dni`
         - `direccion`
         - `telefono`
         - `poblacion`
         - `codPostal`
         - `fechaNacimiento`
         - `especialidad`
         - `sueldo`

     - Métodos:

         - Medico: Permite crear una instancia con los datos de un médico.
         - Métodos get. Recuperan datos de la instancia del objeto.
         - Métodos set. Asignan datos a la instancia del objeto.
         - `retencionMedico`: Permite calcular la retención aplicada al sueldo del médico. Se le pasa el dato del porcentaje de retención.
         - `toString`: Devuelve los datos del médico.
         
     - Crear un método principal `main` ejecutable que:

         - Crear dos instancias de la clase `Medico` llamados `medicoDigestivo` y `medicoTraumatologo`.
         - Cambia el sueldo del `medicoTraumatologo`.
         - Muestra el sueldo del `medicoTraumatologo`.
         - Cambia el dni del `medicoDigestivo`.
         - Muestra el dni del `medicoDigestivo`.
         - Calcula la retención de las dos instancias de la clase `Medico` que hemos creado.
         - Mostrar los datos de las dos instancias de la clase `Medico` que hemos creado, así como las retenciones y los sueldos finales de cada una.

    !!! info "Para pasar los tests"
        - Clase `_19_Medico`, con constructor `_19_Medico(int codMedico, String nombre, String apellidos, String dni, String direccion, long telefono, String poblacion, long codPostal, String fechaNacimiento, String especialidad, double sueldo)` (en ese orden).
        - Getters y setters de instancia con esos tipos.
        - `double retencionMedico(double porcentaje)` devuelve sueldo × porcentaje / 100: con sueldo 3500 y 20 devuelve `700.0`.
        - `toString()` devuelve un `String` que contiene, al menos, el nombre, los apellidos, el DNI y el sueldo.
