# Ejercicios de la UD11

## Actividades

### Definición de clases mediante ODL

El objetivo de esta actividad es ver cómo especificar clases usando el lenguaje ODL.

Genere la declaración ODL de las clases del diagrama siguiente:




![img](assets/wdamm03u5_12.png)

#### Solución


```java
class Zona(key nom) {
    attribute String nom;
    attribute integer habitants;
    attribute float extensió;
}
 
class Ciutat extends Zona {
    attribute string pais;
    relationship set<Districte> districtes;
}
 
class Districte extends Zona {
    attribute integer numDistricte;
    relationship set<Carrer> carrers;
}
 
class Coordenada {
    attribute String longitud;
    attribute String latitud;
}
 
class Carrer {
    attribute String nom;
    attribute float longitud;
    relationship <Coordenada> inici;
    relationship <Coordenada> fi;
    relationship Set<Intersecció> interseccions;
}
 
class Intersecció {
    attribute boolean semàfor;
    relationship <Carrer> carrerIntersectat;
    relationship <Coordenada> ubicació;
}
```

### Instalación y uso de db4o

El objetivo de esta actividad es ver cómo usar las librerías de *db4o* para trabajar con BDOO mediante su IDE.

Vaya a la página de [db4o](http://www.db4o.com/) y descargue sus bibliotecas y la documentación. Lea la documentación para ver cómo puede utilizar las bibliotecas para generar programas mediante su IDE. Una vez hecho, ejecute el siguiente código para ver que todo está correcto:


```java
import com.db4o.*;
 
public class ProvaDB4O {
 
  private class Data {
    private int dia;
    private int mes;
    private int any;
 
    public Data(int d, int m, int a) {
      dia = d;
      mes = m;
      any = a;
    }
 
    @Override
    public String toString() {
      return dia + "-" + mes + "-" + any;
    }
  }
 
  public void start() throws Exception {
    ObjectContainer db = Db4oEmbedded.openFile("BDOOClients.db4o");
    try {
      Data d = new Data(23, 11, 2011);
      db.store(d);
      d = new Data(5, 9, 1975);
      db.store(d);
      d = new Data(4, 9, 1978);
      db.store(d);
 
      System.out.println("Les dates del setembre són:");
      d = new Data(0,9,0);
      ObjectSet<Data> res = db.queryByExample(d);
      while (res.hasNext()) {
        System.out.println(res.next());
      }
 
    } finally {
      db.close();
    }
  }
 
  public static void main (String[] args) throws Exception {
    ProvaDB4O prova = new ProvaDB4O();
    prova.start();
  }
 
}
```

### Gestión de grupos de trabajo de estudiantes mediante db4o

El objetivo de esta actividad es ver cómo gestionar la persistencia de objetos usando la BDOO *db4o*.

Se dispone de las dos clases `Estudiant` y `GrupTreball`, cuyo código se muestra a continuación. A partir de este código, se desea crear una aplicación que, mediante una BDOO db4o gestione a qué grupos de trabajo pertenecen diferentes estudiantes dentro de una escuela. Dado un grupo de trabajo, éste puede tener asignados varios estudiantes, pero todo estudiante sólo tiene un (pero siempre uno) único grupo de trabajo. La aplicación debe poder hacer lo siguiente:

- Dar de alta a un nuevo estudiante. A la hora de asignarle un grupo, si el nombre indicado no existe, se crea un grupo nuevo. Si existe, al estudiante se le asigna ese grupo.
- Reasignar un estudiante a otro grupo de trabajo. Este grupo ya debe existir. Si, al hacerlo, el grupo antiguo queda sin miembros, debe borrarse de la BDOO.
- Listar a todos los grupos existentes.
- Listar a todos los estudiantes (ya qué grupo pertenecen).

Se considera que los nombres de los grupos y estudiantes son únicos en el sistema. No puede haber nombres repetidos. En base a la descripción, también hay que remarcar que la única forma de crear grupos nuevos es añadiendo nuevos estudiantes.

Para realizar esta tarea, el código fuente de estas dos clases no puede modificarse en absoluto.


```java
public class Estudiant {
  private String nom;
  private GrupTreball grup;
 
  public Estudiant (String n, GrupTreball gt) {
    nom = n;
    grup = gt;
    grup.sumaEstudiant();
  }
 
  public String getNom() {
    return nom;
  }
 
  public GrupTreball getGrupTreball() {
    return grup;
  }
 
  public void reassignaGrup(GrupTreball gt) {
    if (grup != gt) {
      grup.restaEstudiant();      
      grup = gt;
      grup.sumaEstudiant();
    }
 
  }
 
  @Override
  public String toString() {
    return nom + " -> " + grup;
  }
 
}
public class GrupTreball {
  private String nom;
  private String tema;
  private int numEstudiants = 0;
 
  public GrupTreball(String n, String tm) {
    nom = n;
    tema = tm;
  }
 
  public void sumaEstudiant() {
    numEstudiants++;
  }
 
  public void restaEstudiant() {
    numEstudiants--;
  }
 
  public int getNumEstudiants() {
    return numEstudiants;
  }
 
  @Override
  public String toString() {
    return nom + " - " + tema;
  }
 
}
```



#### Solución


```java
import java.util.*;
import com.db4o.*;
import com.db4o.config.EmbeddedConfiguration;
import com.db4o.query.Predicate;
 
public class GestionarTreballs {
 
  public void start() {
    EmbeddedConfiguration config = Db4oEmbedded.newConfiguration();
    config.common().objectClass(Estudiant.class).cascadeOnUpdate(true);
    ObjectContainer db = Db4oEmbedded.openFile("BDOOClientsEx3.db4o");
 
    boolean executar = true;
 
    while (executar) {
      System.out.println("[1] Alta de nou estudiant.");
      System.out.println("[2] Reassignar el grup d'un estudiant.");
      System.out.println("[3] Llistar Estudiants.");
      System.out.println("[4] Llistar Grups.");
      System.out.println("[0] Sortir.");
      switch(llegirEnter("Tria una opció")) {
        case 0:
          executar = false;
          break;
        case 1:
          altaEstudiant(db);
          break;
        case 2:
          reassignaGrup(db);
          break;
        case 3:
          llistaEstudiants(db);
          break;
        case 4:
          llistaGrups(db);
          break;
        default:
          System.out.println("Opció incorrecta.");
      }
    }
 
    db.close();
  }
 
  public void altaEstudiant(ObjectContainer db) {
    final String nom = llegirText("Nom del nou estudiant");    
 
    Predicate p = new Predicate<Estudiant>() {
      @Override
      public boolean match(Estudiant e) {
        //Codi per al criteri de cerca
        return nom.equals(e.getNom());
      }
    };
 
    ObjectSet<Estudiant> estudiants = db.query(p);
 
    if (estudiants.size() > 0) {
      System.out.println("Aquest estudiant ja existeix.");
    } else {
      String nomGrup = llegirText("Nom del seu grup");
      GrupTreball tr = new GrupTreball(nomGrup, null);
      ObjectSet<GrupTreball> grups = db.queryByExample(tr);
      GrupTreball nouGrup = null;
      if (grups.size() > 0) {
        nouGrup = grups.next();
        System.out.println("El nou estudiant s'ha afegit a un grup ja existent");
      } else {
        String tema = llegirText("Aquest grup és nou. Temàtica del grup? ");
        nouGrup = new GrupTreball(nomGrup, tema);
      }
      Estudiant estudiant = new Estudiant(nom, nouGrup);
      db.store(estudiant);
    }
  }
 
  public void reassignaGrup(ObjectContainer db) {
    final String nom = llegirText("Nom del nou estudiant");
 
    Predicate p = new Predicate<Estudiant>() {
      @Override
      public boolean match(Estudiant e) {
        //Codi per al criteri de cerca
        return nom.equals(e.getNom());
      }
    };
 
```
```java
    ObjectSet<Estudiant> estudiants = db.query(p);
 
 
    if (estudiants.size() == 0) {
      System.out.println("Aquest estudiant no existeix.");
    } else {
      Estudiant estudiant = estudiants.next();
      String nomGrup = llegirText("Nom del seu nou grup");
      GrupTreball tr = new GrupTreball(nomGrup, null);
      ObjectSet<GrupTreball> grups = db.queryByExample(tr);
      if (grups.size() == 0) {
        System.out.println("Aquest grup no existeix.");
      } else {
        GrupTreball nouGrup = grups.next();
        GrupTreball anticGrup = estudiant.getGrupTreball();
        estudiant.reassignaGrup(nouGrup);
        //Queda algú a l'antic grup?
        if (anticGrup.getNumEstudiants() == 0) {
          db.delete(anticGrup);
        }
        db.store(estudiant);
      }
    }
  }
 
  public void llistaEstudiants(ObjectContainer db) {
    Predicate p = new Predicate<Estudiant>() {
      @Override
      public boolean match(Estudiant e) {
        //Codi pel criteri de cerca
        return true;
      }
    };
 
    ObjectSet<Estudiant> estudiants = db.query(p);
 
    while (estudiants.hasNext()) {
      System.out.println(estudiants.next());
    }
  }
 
  public void llistaGrups(ObjectContainer db) {
    GrupTreball e = new GrupTreball(null, null);
    ObjectSet<GrupTreball> grups = db.queryByExample(e);
    while (grups.hasNext()) {
      System.out.println(grups.next());
    }
  }
 
  public String llegirText(String pregunta) {
    Scanner in = new Scanner(System.in);
    String res = null;
    while (res == null) {
      System.out.print(pregunta + ": ");
      res = in.next();
      if ("".equals(res))
        res = null;
      in.nextLine();
    }
    return res;
  }
 
 public int llegirEnter(String pregunta) {
    Scanner in = new Scanner(System.in);
    int res = -1;
    while (res == -1) {
      System.out.print(pregunta + ": ");
      try {
        res = in.nextInt();
      } catch (Exception ex) {
        System.out.println("Entrada invàlida.");
      }
      in.nextLine();
    }
    return res;
  }
 
  public static void main (String[] args) {
    GestionarTreballs programa = new GestionarTreballs();
    programa.start();
  }
}
```

### Gestión de clientes y encargos mediante db4o

El objetivo de esta actividad es ver cómo gestionar la persistencia de objetos usando la BDOO *db4o*.

Haga un programa que gestione los objetos de una base de datos de clientes de acuerdo al siguiente diagrama:



El programa debe poder dar las siguientes opciones:

- Añadir un nuevo tipo de producto.
- Añadir un nuevo cliente.
- Añadir un nuevo encargo a un cliente; el encargo puede contener más de un tipo de producto asociado.
- Listar todos los tipos de producto en el sistema.
- Listar los datos de un cliente y todos sus encargos hasta ahora.

Los tipos de producto y los clientes se identifican de forma única por el nombre (sólo puede haber un único objeto con un nombre dado). Para este ejercicio no es necesario gestionar la persistencia de actualizaciones entre diferentes ejecuciones.

#### Solución

```java
public class TipusProducte {
  private String nom;
  private float preu;
 
  public TipusProducte(String n, float p) {
    nom = n;
    preu = p;
  }
 
  @Override
  public String toString() {
    return  nom + ":" + preu;
  }
}
```
```java
public class Quantitat {
  private TipusProducte tipusProducte;
  private int nre;

  public Quantitat(TipusProducte tp, int n) {
    tipusProducte = tp;
    nre = n;
  }

  @Override
  public String toString() {
    return tipusProducte.toString() + " - " + nre;
  }
}
```
```java
import java.util.*;
 
public class Client {
  private String nom;
  private String aPostal;
  private String aMail;
  private String telefon;
  private List<Encarrec> liComandes = new LinkedList<Encarrec>();
 
  public Client(String n, String ap, String am, String t) {
    nom = n;
    aPostal = ap;
    aMail = am;
    telefon = t;
  }
 
  public String getNom() {
    return nom;
  }
 
  public String getAPostal() {
    return aPostal;
  }
 
  public String getAMail() {
    return aMail;
  }
 
  public String getTelefon() {
    return telefon;
  }
 
  public int getNreComandes() {
    return liComandes.size();
  }
 
  public void addComanda(Encarrec e) {
    liComandes.add(e);
  }
 
  public List<Encarrec> getComandes() {
    return liComandes;
  }
 
  @Override
  public String toString() {
    String res = nom + " : " + aPostal + " : (" + aMail +
           ", " + telefon + ")\n";
    Iterator<Encarrec> it = liComandes.iterator();
    while (it.hasNext()) {
      Encarrec e = it.next();
      res += e.toString() + "\n";
     }
    return res;
  }
}
```
```java
import java.util.*;
 
public class Encarrec {
 
  private Date data;
  private List<Quantitat> productes = new LinkedList();
 
  public Encarrec () {
    data = new Date();
  }
 
  public void addProductes(TipusProducte tp, int n) {
    productes.add(new Quantitat(tp, n));
  }
 
  @Override
  public String toString() {
    String res = "Data = " + data + ":\n" ;
    Iterator<Quantitat> it = productes.iterator();
    while (it.hasNext()) {
      res += it.next().toString() + "\n";
    }
    return res;
  }
}
```
```java
import java.util.*;
import com.db4o.*;
import com.db4o.config.EmbeddedConfiguration;
 
public class GestionarClients {
 
  public void start() {
    EmbeddedConfiguration config = Db4oEmbedded.newConfiguration();
    config.common().objectClass(Client.class).cascadeOnUpdate(true);
    config.common().objectClass(Encarrec.class).cascadeOnUpdate(true);
    config.common().objectClass(Quantitat.class).cascadeOnUpdate(true);
    config.common().objectClass(TipusProducte.class).cascadeOnUpdate(true);
    ObjectContainer db = Db4oEmbedded.openFile("BDOOClientsEx4.db4o");
 
    boolean executar = true;
 
    while (executar) {
      System.out.println("[1] Afegir Tipus de Producte.");
      System.out.println("[2] Afegir Client.");
      System.out.println("[3] Afegir Encàrrec.");
      System.out.println("[4] Llistar tipus de productes a la BDOO.");
      System.out.println("[5] Mostrar client i els seus encàrrecs.");
      System.out.println("[0] Sortir.");
      switch(llegirEnter("Tria una opció")) {
        case 0:
          executar = false;
          break;
        case 1:
          afegirProducte(db);
          break;
        case 2:
          afegirClient(db);
          break;
        case 3:
          afegirEncarrec(db);
          break;
        case 4:
          llistarProductes(db);
          break;
        case 5:
          llistarClient(db);
          break;
        default:
          System.out.println("Opció incorrecta.");
      }
    }
    db.close();
  }
 
  public void afegirProducte(ObjectContainer db) {
    String nom = llegirText("Nom del Producte");
    //Cal cercar primer si ja existeix a la BDOO, o se'n crearà una còpia!
    TipusProducte p = new TipusProducte(nom, 0);
    ObjectSet<TipusProducte> prods = db.queryByExample(p);
    if (prods.size() > 0) {
      System.out.println("Aquest tipus de producte ja existeix.");  
    } else {    
      float preu = llegirReal("Preu");
      p = new TipusProducte(nom, preu);
      db.store(p);
      System.out.println("Producte emmagatzemat");
    }
  }
 
  public void afegirClient(ObjectContainer db) {
    String nom = llegirText("Nom del Client");
    //Cal cercar primer si ja existeix a la BDOO, o es crearà una còpia!
    Client c = new Client(nom, null, null, null);
    ObjectSet<Client> clis = db.queryByExample(c);
    if (clis.size() > 0) {
      System.out.println("Aquest client ja existeix.");
    } else {
      String ap = llegirText("Adreça");
      String am = llegirText("E-Mail");
      String tl = llegirText("Telefon");
      c = new Client(nom, ap, am, tl);
      db.store(c);
      System.out.println("Client emmagatzemat");
    }
  }
```
```java
  public void afegirEncarrec(ObjectContainer db) {
    String nom = llegirText("Nom del Client");
    //Cal cercar si el client existeix
    Client c = new Client(nom, null, null, null);
    ObjectSet<Client> clis = db.queryByExample(c);
    if (clis.size() == 0) {
      System.out.println("Aquest client no existeix.");
    } else {
      Client client = clis.next();
      boolean afegir = true;
      Encarrec encarrec = new Encarrec();
      while (afegir) {        
        nom = llegirText("Nom del Producte (escriu \"fi\" per acabar)");
        if ("fi".equals(nom)) {
          afegir = false;
        } else {
          TipusProducte p = new TipusProducte(nom, 0);
          ObjectSet<TipusProducte> prods = db.queryByExample(p);
          if (prods.size() == 0) {
            System.out.println("Aquest producte no existeix.");
          } else {
            TipusProducte prod = prods.next();
            int nre = llegirEnter("Quantiat");
            encarrec.addProductes(prod, nre);
          }
        }
      }
      client.addComanda(encarrec);
      db.store(client);
      System.out.println("Encàrrec emmagatzemat");
    }
  }
 
  public void llistarProductes(ObjectContainer db) {
    TipusProducte p = new TipusProducte(null, 0);
    ObjectSet<TipusProducte> prods = db.queryByExample(p);
    System.out.println("Llista de tipus de productes:");
    while (prods.hasNext()) {
      System.out.println(prods.next());  
    }
  }
 
  public void llistarClient(ObjectContainer db) {
    String nom = llegirText("Nom del Client");
    //Cal cercar si el client existeix
    Client c = new Client(nom, null, null, null);
    ObjectSet<Client> clis = db.queryByExample(c);
    if (clis.size() == 0) {
      System.out.println("Aquest client no existeix.");
    } else {
      Client client = clis.next();
      System.out.println(client);
    }
  }
 
  public String llegirText(String pregunta) {
    Scanner in = new Scanner(System.in);
    String res = null;
    while (res == null) {
      System.out.print(pregunta + ": ");
      res = in.next();
      if ("".equals(res))
        res = null;
      in.nextLine();
    }
    return res;
  }
 
 public int llegirEnter(String pregunta) {
    Scanner in = new Scanner(System.in);
    int res = -1;
    while (res == -1) {
      System.out.print(pregunta + ": ");
      try {
        res = in.nextInt();
      } catch (Exception ex) {
        System.out.println("Entrada invàlida.");
      }
      in.nextLine();
    }
    return res;
  }
```
```java
 public float llegirReal(String pregunta) {
    Scanner in = new Scanner(System.in);
    float res = -1;
    while (res == -1) {
      System.out.print(pregunta + ": ");
      try {
        res = in.nextFloat();
      } catch (Exception ex) {
        System.out.println("Entrada invàlida.");
      }
      in.nextLine();
    }
    return res;
  }
 
  public static void main (String[] args) {
    GestionarClients programa = new GestionarClients();
    programa.start();
  }
}
```

### Instalación y uso de JDO

El objetivo de esta actividad es ver cómo usar una BDDOO basada en JDO mediante su IDE.

Vaya a la página de BDOO [JDOInstruments](http://sourceforge.net/projects/jdoinstruments/develop) y descargue sus bibliotecas y la documentación. Lea la documentación para ver cómo puede utilizar las bibliotecas para generar programas mediante su IDE. Una vez hecho, ejecute correctamente el ejemplo proporcionado con las librerías (en la carpeta “linuxexample” o “windiowsexample”, según su sistema operativo).

## Ejercicios

### Ejercicio 1

A partir del siguiente fragmento de ODL, que describe en términos generales un juego donde jugadores se desplazan por un laberinto:


```
class Jugador {
  attribute string nom;
  relationship Bag<Item> items;
  relationship <Sala> ubicació;
}
 
class Item (key nom) {
  attribute string nom;
  attribute float pes;
}
 
class Sala {
  attribute string nom;
  attribute string descripció;
  relationship Set<Sortida> sortides; 
}
 
class Sortida {
  attribute string nom;
  attribute string descripció;
  relationship <Sortida> onVa; 
}
```

Marque si son verdaderas (V) o falsas (F) las siguientes opciones. Siguiendo estrictamente las definiciones…

| Núm  | Pregunta                                                     | V    | F    |
| ---- | ------------------------------------------------------------ | ---- | ---- |
| 1    | Un jugador puede tener varios elementos con el mismo nombre. |      | f    |
| 2    | Un jugador puede tener varios ítems con el mismo peso.       | v    |      |
| 3    | Una sala puede tener distintas salidas con el mismo nombre.  |      | f    |
| 4    | Una salida puede ir a parar a varias salas, pero nunca repetidas. |      | f    |
| 5    | En el programa puede haber salas con el mismo nombre.        | v    |      |
| 6    | En el programa puede haber salas con la misma descripción.   | v    |      |
| 7    | En el programa puede haber jugadores con el mismo nombre.    | v    |      |
| 8    | En el programa puede haber jugadores con un mismo ítem.      | v    |      |
| 9    | En el programa puede haber jugadores con la misma ubicación. | v    |      |
| 10   | No puede haber ningún ítem en ninguna sala.                  | v    |      |

### Ejercicio 2

Dada la consulta OQL siguiente:

```
SELECT c.adreçaPostal, c.telefon 
DE Clientes c
DONDE c.nom = "Cliente1"
```

Elija la opción correcta. Si se desea obtener estrictamente los mismos datos resultantes…


| Núm  | Pregunta                                                     |      |
| ---- | ------------------------------------------------------------ | ---- |
| 1    | En una BDOO *db4o*, es posible hacerlo usando una búsqueda por ejemplo. |      |
| 2    | En una BDOO *db4o*, es posible hacerlo usando una búsqueda nativa. |      |
| 3    | En una BDOO basada en JDO, es posible hacerlo usando una búsqueda `query.execute(…)`. |      |
| 4    | Ninguna de las anteriores afirmaciones es cierta.            | esta |

### Ejercicio 3

Se dispone de la siguiente clase, cuyos objetos están almacenados en una BDOO *db4o*. Para gestionarlos, sólo se desea utilizar búsquedas por ejemplo (*Queries-By-Example*).


```
public class Assignatura {
  private String nom;
  private String tematica;
  private int credits;
  private int nreCopsOberta;
  private List<Estudiants> estudiantsMatriculatsActualment; 
}
```

Marque si son verdaderas (V) o falsas (F) las siguientes opciones:

| Núm  | Pregunta                                                     | V    | F    |
| ---- | ------------------------------------------------------------ | ---- | ---- |
| 1    | Es posible buscar la asignatura que tiene un nombre concreto. |      | f    |
| 2    | Es posible buscar las asignaturas con una temática concreta. | v    |      |
| 3    | Es posible buscar las asignaturas de seis créditos.          | v    |      |
| 4    | Es posible buscar la asignatura con menos créditos.          |      | f    |
| 5    | Es posible buscar las asignaturas que nunca se han abierto.  |      | f    |
| 6    | Es posible buscar las asignaturas abiertas al menos una vez. |      | f    |
| 7    | Es posible buscar la asignatura con más estudiantes en la actualidad. |      | f    |
| 8    | Es posible buscar las asignaturas sin estudiantes en la actualidad. |      | f    |

### Ejercicio 4

Complete las afirmaciones con la palabra que considere más adecuada:

| Núm  | Pregunta                                | Respuesta |
| ---- | --------------------------------------- | --------- |
| 1    | Al abrir una BDOO *db4o* se obtiene un… |           |

| 2    | Al abrir una BDOO JDO se obtiene un…                         |      |
| ---- | ------------------------------------------------------------ | ---- |
| 3    | Para realizar búsquedas simples en una BDOO *db4o* se usa el método… |      |
| 4    | Para realizar búsquedas complejas en una BDOO *db4o* se usa el método… |      |
| 5    | Para realizar búsquedas en una BDOO JDO se usa el método…    |      |
| 6    | Para almacenar objetos en una BDOO *db4o* se usa el método…  |      |
| 7    | Para almacenar objetos en una BDOO JDO se usa el método…     |      |

### Ejercicio 5

Dado el siguiente diagrama de clases y fragmento de código de una BDOO *db4o*:

Figura![img](https://ioc.xtec.cat/materials/FP/Recursos/fp_dam_m03_/web/fp_dam_m03_htmlindex/WebContent/u5/media/u5.a3.ex5.png)

```
private ObjectContainer db = ...;
...
 
public void eliminaA(ClasseA a) {
  db.delete(a);
  Iterator<ClasseC> it = a.getC().iterator(); 
  while (it.hasNext()) {
    ClasseC c = it.next();
    db.delete(c);
  }
}
```

Elija la opción correcta:

| Núm  | Pregunta                                                     |      |
| ---- | ------------------------------------------------------------ | ---- |
| 1    | Este código es correcto y no crea ninguna inconsistencia en BDOO. |      |
| 2    | Este código es incorrecto; siempre habrá inconsistencias en la BDOO. |      |
| 3    | Este código es incorrecto, pero no siempre creará inconsistencias en BDOO. | ESTA |
| 4    | Este código es redundante, ya que no es necesario el bucle.  |      |

## Ejercicios propuestos

1. Investiga la sintaxis de uso de la API Criteria y propón algún ejemplo.
2. ¿Es posible mezclar parámetros por nombre y parámetros posicionales en una query?
3. Investiga sobre el marcado de clases con la etiqueta @Mapped. ¿Qué significado tiene?
4. ¿Para qué se utilizan los scripts enhancer.bat y enhancer.sh?
5. Indica qué significado tiene marcar un campo persistente con alguna de las siguientes marcas: @OneToO0ne, @ManyToOne, @OnetoMany, @ManyToMany, Basic. Propón ejemplos ilustrativos.

## Supuestos prácticos

1. Se necesita implementar un programa que administre la información de los vehículos y personas que los conducen cuando entran en un recinto privado. De los vehículos se desea almacenar su identificador (número entero), la matrícula (cadena de caracteres), la fecha de matriculación (fecha) y la persona que lo conduce (clase persona). De los vehículos que sean coches, además, se desea almacenar el tipo de energía que lo propulsa (enumerado: GASOLINA, DIÉSEL, ELÉCTRICO, HÍBRIDO). De las personas que conducen los vehículos se desea almacenar su nombre (cadena de caracteres) y su DNI (cadena de caracteres). De aquellas personas que además sean trabajadores se desea almacenar su número de registro personal (número entero). Implementa las clases entidad que permitan manejar y volcar esta información a una base de datos denominada control, así como un programa que añada los datos de 4 vehículos (2 de ellos coches) y 4 conductores (2 de ellos trabajadores). Utiliza el explorador ObJjectDB Explorer para comprobar que se han introducido correctamente.

2. Sobre el supuesto práctico anterior, añade al programa principal un menú que ofrezca al usuario la posibilidad de dar de alta nuevos vehículos y personas, consultar los datos de los vehículos almacenados en el sistema, modificar los mismos datos y eliminar los datos de determinados vehículos, incluidos coches, a partir de su identificador.

3. Crea un programa que permita migrar los datos de los trabajadores de una empresa contenidos en un fichero de texto a una base de datos ObjectDB. Los campos contenidos en el fichero de texto vienen separados por el carácter 4 y son los siguientes: DNI, Apellido1, Apellido2, Nombre, FechaNacimiento, Fechalncorporación, Puesto. Selecciona el tipo de dato persistente que mejor se adapte a la información a almacenar.

4. A partir de la base de datos del supuesto práctico anterior, escribe un programa que permita recuperar los datos de los trabajadores según determinados parámetros que serán introducidos por teclado conforme a la opción elegida en un menú de opciones. El menú constará de 3 opciones:

   - “Filtrar mayores de edad”: Devolverá únicamente los datos de los trabajadores de más de 18 años a fecha actual.
   - “Filtrar por DNI igual a...”: Devolverá únicamente los datos del trabajador cuyo DNI coincida con el leído.
   - “Filtrar por antigúedad mayor a...”: Devolverá los datos de los trabajadores cuya antigúedad en el puesto sea superior a la leída por teclado.

   Emplea @NamedQuery para una de ellas y querys dinámicas con parámetros por nombre para las otras dos.

5. Modifica el programa del supuesto práctico anterior para que añada la opción “Alta trabajador” al menú y permita leer los datos desde teclado para almacenarlos en la base de datos.

## Auto evaluación

1. ¿Cuál de las siguientes no es una declaración de tipo persistente?

   a) `java.sql.Date` fecha.

   b) `@Temporal(TemporalType.DATE) java.util.Date fecha`.

   c) `@Temporal(TemporalType.DATE) java.util.Calendar fecha`.

   d) Todas las opciones anteriores son declaraciones de tipo persistente.

2. ¿Cuál de los siguientes no es un requisito de una clase entidad?

   a) Tener un constructor parametrizado.

   b) Sus campos deben ser privados.

   c) Sus propiedades deben ser accesibles mediante métodos get y set que siguen una convención de nomenclatura estándar.

   d) Ser serializable.

3. ¿Cómo debe marcarse el campo de una clase entidad cuyo tipo sea una clase definida
   por el programador y del que no se desea que sea almacenado como clase entidad?

   a) `@Embedded`.

   b) `@Embeddable`.

   c) `@Serializable`,

   d) `@Entity`

4. De las siguientes estrategias de generación de clave primaria, ¿cuál es equivalente a `@GeneratedValue`?

   a) Omitir la marca es la equivalencia.

   b) `@GeneratedValue(strategy=GenerationType.IDENTITY)`.

   c) `@GeneratedValue(strategy=GenerationType.AUTO)`.

   d) `@GeneratedValue(strategy=GenerationType.SEQUENCE, generator="seq")`.

5. ¿En qué parte de una sentencia SELECT se pueden emplear las funciones agregadas?
   a) SELECT.

   b) FROM.

   c) AS.

   d) Todas las opciones son correctas.

6. ¿Cuál de los siguientes métodos propaga los cambios a la base de datos?
   a) `persist`.

   b) `begin`.

   c) `rollback`.

   d) `commit`.

7. ¿Cuál de las siguientes query utiliza parámetros posicionales de forma correcta?
   a) `em.createQuery("SELECT e FROM Compra c WHERE p.precio = *1")`.

   b) `em.createQuery("SELECT € FROM Compra c WFIERE p.precio =? 1")`.

   c) `em.createQuery("SELECT e FROM Compra c WHERE p.precio = '*1'")`.

   d) `em.createQuery(“SELECT € FROM Compra c WHERE p.precio = '?1'”`).

8. ¿Qué operación del conjunto de operaciones CRUD no necesita de un commit?
   a) C (*Create*).

   b) R (*Read*).

   c) U (*Update*).

   d) D (*Delete*).

9. ¿Cuál de las siguientes no es una opción válida para establecer la ruta de la base de datos?

   a) Utilizar la variable `$objectdb`.

   b) Utilizar directamente el path de la base de datos (“`C:\ ...`”).

   c) Utilizar una URL.

   d) Todas las opciones anteriores son válidas para establecer la ruta de la base de datos.

10. ¿Qué métodos permiten establecer los cambios que se ejecutan como una transacción?

    a) `em.getTransaction().begin()`; y `em.getTransaction().end()`.
    b) `em.getTransaction().start()`; y `em.getTransaction().end()`.
    c) `em.getTransaction().begin()`; y `em.getTransaction().commit()`.
    d) `em.getTransaction().start()`; y `em.getTransaction().commit()`.

![image-20240903190856889](assets/image-20240903190856889.png)