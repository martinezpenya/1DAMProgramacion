# Taller UD01_01: Instalar NoMachine para el control remoto

## ¿Qué es `NoMachine`?
 
Conéctese a cualquier computadora de forma remota a la velocidad de la luz. Gracias a nuestra tecnología NX, NoMachine es el escritorio remoto más rápido y de mayor calidad que jamás haya probado. Conecta con tu ordenador al otro lado del mundo con solo unos pocos clics. Vé donde esté tu escritorio, podrás acceder a él desde cualquier otro dispositivo y compartirlo con quien quieras. `NoMachine` es tu servidor personal, privado y seguro. Además, es gratis.

https://www.nomachine.com/

### Descarga e instala la aplicación

Desde la página de descargas:

https://downloads.nomachine.com/

E instala la aplicación en tu PC.

## Permisos al profesor

Debemos conceder permisos para que el profesor se pueda conectar a nuestro PC mientras estemos en el instituto sin necesidad de contraseña. Esto solo será posible cuando estemos conectados a la red del instituto, y el profesor no podrá acceder cuando estemos en casa.

Agrega la clave SSH pública (es un fichero `authorized.crt` que te proporcionará el profesor a través de AULES) en tu ordenador

- Debes colocarla en la carpeta `<Inicio del usuario>/.nx/config`.

- Cree este directorio si no existe.
  - En Linux y macOS, ejecute en una terminal:`mkdir $HOME/.nx/config`
  - En Windows, créelo en (`C:\Users\username\.nx\config`) usando las herramientas del sistema (Explorador de archivos).

- Si la carpeta de configuración ya existe, copia el fichero `authorized.crt` en ella.

  > Ten en cuenta que los navegadores pueden cambiar las extensiones de los archivos, es conveniente tener las opciones de "ver extensiones de archivos" y "ver archivos ocultos" en nuestro gestor de archivos habitual

## Tarea

Debes enviar un archivo `*.pdf` a la plataforma de AULES con una simple captura que demuestre que el profesor se ha podido conectar a tu PC.

> Debes mantener `NoMachine` instalado y permitir las conexiones automáticas por parte del profesor para pedir ayuda y consultar dudas en clase, para corregir las tareas diarias, y para realizar los exámenes.
