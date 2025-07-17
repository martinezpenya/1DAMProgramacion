/*
 * Here comes the text of your license
 * Each line should be prefixed with  *
 */
package UD05._3.contrarreloj;

import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author David Martínez (wwww.martinezpenya.es|iesmre.com)
 */
public class ContraReloj {

    static ListaCorredores hanSalido = new ListaCorredores();
    static ListaCorredores hanLlegado = new ListaCorredores();

    public static String generarMenu() {
        String resultado = "";
        resultado += "**********************************\n";
        resultado += "*     C O N T R A R R E L O J    *\n";
        resultado += "**********************************\n";
        resultado += "* 1=> Salida                     *\n";
        resultado += "* 2=> Llegada                    *\n";
        resultado += "* 3=> Clasificación              *\n";
        resultado += "* 4=> Salir                      *\n";
        resultado += "**********************************\n";
        resultado += "Elige una opción (1-4): ";
        return resultado;
    }

    public static void menuSalida() {
        Scanner teclado = new Scanner(System.in);
        System.out.println("REGISTRO DE SALIDA:");
        System.out.print("Introduzca el nombre del corredor: ");
        String nombre = teclado.next();
        System.out.printf("Introduzca el dorsal de %s: ", nombre);
        int dorsal = teclado.nextInt();
        try {
            hanSalido.añadir(new Corredor(dorsal, nombre));
        } catch (ElementoDuplicadoException ex) {
            System.out.println(
                    "ERROR: Ese dorsal ya ha sido registrado en la salida");
        }
    }

    public static void menuLlegada() {
        Scanner teclado = new Scanner(System.in);
        System.out.println("REGISTRO DE LLEGADA:");
        System.out.print("Introduzca el dorsal del corredor: ");
        int dorsal = teclado.nextInt();
        System.out.printf(
                "Introduzca el tiempo de llegada para el dorsal %d en segundos: ",
                dorsal);
        double tiempo = teclado.nextDouble();
        try {
            Corredor c = hanSalido.quitar(dorsal);
            c.setTiempo(tiempo);
            hanLlegado.insertarOrdenado(c);
        } catch (ListaCorredores.ElementoNoEncontradoException ex) {
            System.out.println(
                    "ERROR: El corredor no esta en la lista de salida");
        }
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int opcion;
        System.out.print(generarMenu());
        while ((opcion = teclado.nextInt()) != 4) {
            switch (opcion) {
                case 1:
                    menuSalida();
                    System.out.println(generarMenu());
                    break;
                case 2:
                    menuLlegada();
                    System.out.println(generarMenu());
                    break;
                case 3:
                    System.out.println(hanLlegado.toString());
                    System.out.println(generarMenu());
                    break;
                case 9:
                    System.out.println(hanSalido.toString());
                    System.out.println(generarMenu());
                    break;
                default:
                    System.out.println("Opción incorrecta, intentelo de nuevo");
                    System.out.print(generarMenu());
            }
        }
        System.out.println("Ha seleccionado Salir, que pase buen dia!");
    }
}
