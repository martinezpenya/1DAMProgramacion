public class EjemploUD01 {

    // variable de clase precisa static para poder usarse dentro de la funcion
    // main()
    static double dto = 0.25;

    public static void main(String[] args) {

        // Declaración y asignación de valores a variables
        byte a;
        a = 127;
        short c = 3;
        int d = -30;
        int e = 0xC125;
        long l = 5L;
        char car1 = 99; // car1 es la letra "c" equivale al ascii 99
        char letra = '\u0061'; // código unicode del carácter "a"
        double b = 5F;
        double f = 1e6;
        float g = 1 / 2F;
        boolean par = false;

        // Declaración y asignación constantes y literales
        final double IVA = 0.21;
        System.out.println("1a linea\n2a linea\n3a \"linea\"");

        // Muestra por pantalla literales y contenidos de variables.
        System.out.println("Hola Mundo");
        System.out.println("a vale " + a);
        System.out.println("b vale " + b);
        System.out.println("c vale " + c);
        System.out.println("d vale " + d);
        System.out.println("e vale " + e);
        System.out.println("f vale " + f);
        System.out.println("g vale " + g);
        System.out.println("l vale " + l);
        System.out.println("car1 vale " + car1);
        System.out.println("letra vale " + letra);
        System.out.println("par vale " + par);

        // uso de la constante
        double precio = 430;
        double preciofinal = precio - (precio * dto) + ((precio - (precio * dto)) * IVA);
        System.out.println(IVA);
        System.out.println(preciofinal);

        // Operadores aritméticos
        double num1, num2, suma, resta, producto, division, resto;
        num1 = 8;
        num2 = 5;
        suma = num1 + num2; // 13
        resta = num1 - num2; // 3
        producto = num1 * num2; // 40
        division = num1 / num2; // 1.6
        resto = num1 % num2; // 3
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Producto: " + producto);
        System.out.println("División: " + division);
        System.out.println("Resto: " + resto);

        // Operadores Relacionales
        int valor1 = 10;
        int valor2 = 3;
        boolean compara;
        compara = valor1 > valor2; // true
        System.out.println("Mayor:" + compara);
        compara = valor1 < valor2; // false
        System.out.println("Menor:" + compara);
        compara = valor1 >= valor2; // true
        System.out.println("Mayor o igual: " + compara);
        compara = valor1 <= valor2; // false
        System.out.println("Menor o igual: " + compara);
        compara = valor1 == valor2; // false
        System.out.println("Igual: " + compara);
        compara = valor1 != valor2; // true
        System.out.println("Distinto: " + compara);

        // Operadores Lógicos
        double sueldo = 1400;
        int edad = 34;
        boolean logica;
        logica = (sueldo > 1000 & edad < 40); // true
        System.out.println("AND: " + logica);
        logica = (sueldo > 1000 && edad > 40); // false
        System.out.println("AND: " + logica);
        logica = (sueldo > 1000 | edad > 40); // true
        System.out.println("OR: " + logica);
        logica = (sueldo < 1000 || edad > 40); // false
        System.out.println("OR: " + logica);
        logica = !(edad < 40); // false
        System.out.println("NOT: " + logica);
        logica = (sueldo > 1000 ^ edad > 40); // true
        System.out.println("XOR: " + logica);
        logica = (sueldo < 1000 ^ edad > 40); // false
        System.out.println("XOR: " + logica);

        // Operadores Unarios o Unitarios
        int m = 5, n = 3;
        m++; // 6
        n--; // 2
        System.out.println("Incremento: " + m);
        System.out.println("Decremento: " + n);

        int A = 1, B;
        B = ++A; // A vale 2 y B vale 2
        System.out.println("A vale: " + A + " B vale: " + B);
        B = A++; // A vale 3 y B vale 2
        System.out.println("A vale: " + A + " B vale: " + B);

        // Operadores de Asignación
        int dato1 = 10, dato2 = 2, dato;
        dato = dato1; // dato vale 10
        System.out.println("= : " + dato);
        dato2 *= dato1; // dato2 vale20
        System.out.println("*= : " + dato2);
        dato2 /= dato1; // datos2 vale 2
        System.out.println("/= : " + dato2);
        dato2 += dato1; // dato2 vale 12
        System.out.println("+= : " + dato2);
        dato2 -= dato1; // dato2 vale 2
        System.out.println("-= : " + dato2);
        dato1 %= dato2; // dato1 vale 0
        System.out.println("%= : " + dato1);

        // Operadores de desplazamiento
        int j = 33;
        int k = j << 2;
        // 00000000000000000000000000100001 : j = 33
        // 00000000000000000000000010000100 : k = 33 << 2 ; k = 132
        System.out.println("k= : " + k);
        int o = 132;
        int p = o >> 2;
        // 00000000000000000000000010000100 : o = 132
        // 00000000000000000000000000100001 : p = 132 >> 2 ; p = 33
        System.out.println("p= : " + p);
        int x = -1;
        int y = x >>> 2;
        // 11111111111111111111111111111111 : x = -1
        // 00111111111111111111111111111111 : y = x >>> 2; y = 1073741823
        System.out.println("y= : " + y);
        int q = 132; // q: 00000000000000000000000010000100
        int r = 144; // r: 00000000000000000000000010010000
        int s = q & r; // s: 00000000000000000000000010000000
        // El resultado da 128
        System.out.println("s= : " + s);
        int t = q | r; // t: 00000000000000000000000010010100
        // El resultado da 148
        System.out.println("t= : " + t);
        int u = q ^ r; // u: 00000000000000000000000000010100
        // El resultado da 20
        System.out.println("u= : " + u);
        int v = ~q; // v: 11111111111111111111111101111011
        // El resultado da -133
        System.out.println("v= : " + v);

        // Operador condicional
        int mayor, exp1 = 15, exp2 = 25;
        mayor = (exp1 > exp2) ? exp1 : exp2;
        // mayor valdrá 25
        System.out.println("mayor= : " + mayor);

        // Prioridad de los operadores
        int x1, y1 = 6, y2 = 2, y3 = 8;
        x1 = y1 + y2 * y3; // 22
        System.out.println("Sin paréntesis: " + x);
        x1 = (y1 + y2) * y3; // 64
        System.out.println("Con paréntesis: " + x);

        // Conversión Implícita
        byte origen = 5;
        short destino;
        destino = origen; // 5
        System.out.println("Implícita: " + destino);

        // Conversión Explícita
        byte destino2;
        short origen2 = 3;
        destino2 = (byte) origen2; // 3
        System.out.println("Explícito: " + destino2);

        // comentario de una sola línea

        /*
         * Esto es un comentario
         * de varias líneas
         */

        /**
         * Comentario de documentación.
         * Javadoc extrae los comentarios del código y
         * genera un archivo html a partir de este tipo de comentarios
         */

        // Generar número aleatorios
        double numero;
        int entero;
        numero = Math.random();
        System.out.println("El número es: " + numero);
        numero = Math.random() * 100;
        System.out.println("El número es: " + numero);
        entero = (int) (Math.random() * 100);
        System.out.println("El número sin decimales es: " + entero);

        // Introducir texto desde teclado
        String texto;
        System.out.print("Introduce un texto: ");
        texto = System.console().readLine();
        System.out.println("El texto introducido es: " + texto);

        // Introducir un número entero desde teclado
        String texto2;
        int entero2;
        System.out.print("Introduce un número: ");
        texto2 = System.console().readLine();
        entero2 = Integer.parseInt(texto2);
        System.out.println("El número introducido es:" + entero2);

        // Introducir un número decimal desde teclado
        String texto3;
        double doble3;
        System.out.print("Introduce un número decimal: ");
        texto3 = System.console().readLine();
        doble3 = Double.parseDouble(texto3); // convertimos texto a doble
        System.out.println("Número decimal introducido es: " + doble3);
    }
}
