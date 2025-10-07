package es.martinezpenya.ejemplos.UD02;

import java.util.Scanner;

public class EjemploUD02 {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        //Introducir texto desde teclado
        String texto;
        System.out.print("Introduce un texto: ");
        texto = teclado.nextLine();
        System.out.println("El texto introducido es: " + texto);

        //Introducir un número entero desde teclado
        String texto2;
        int entero2;
        System.out.print("Introduce un número: ");
        texto2 = teclado.nextLine();
        entero2 = Integer.parseInt(texto2);
        System.out.println("El número introducido es:" + entero2);

        //Introducir un número decimal desde teclado
        String texto3;
        double doble3;
        System.out.print("Introduce un número decimal: ");
        texto3 = teclado.nextLine();
        doble3 = Double.parseDouble(texto3); // convertimos texto a doble
        System.out.println("Número decimal introducido es: " + doble3);

        System.out.println("La clase String");
        String nombre = "Javier "; //Observa que hay un espacio final
        System.out.println(nombre.toUpperCase()); //JAVIER 
        System.out.println(nombre.charAt(4)); //E
        System.out.println(nombre.indexOf("i"));//3
        System.out.println(nombre.substring(0, 3));//JAVI
        System.out.println(nombre.toLowerCase());//javier
        System.out.println(nombre.trim());//Javier sin espacios finales
        System.out.println(nombre.toUpperCase().substring(0, 4).indexOf("i"));
        System.out.printf("%,.2f\n", 12345.1684);
        
        System.out.format("El valor de la variable float es %f"
                + ", mientras que el valor del entero es %d"
                + " y el string contiene %s", doble3, entero2, texto);
        
        System.err.println("Salida de error por pantalla");
    }
}
