# Taller UD01_01: Instalación de Veyon en Linux

Este manual instala en tu portátil el componente **Veyon Service**, que permite que el profesor vea y controle tu pantalla durante la clase. No necesitas instalar el "Master" (esa parte solo la usa el profesor).

## Qué necesitas

- Tu portátil con Linux conectado a la red del aula.
- El fichero de **clave pública** que te ha entregado el profesor (por ejemplo `veyon-aula-profesor.pem`), descargado desde AULES o recibido por USB.

## 1. Instalar Veyon

### Ubuntu / Debian / Lliurex

```bash
wget -qO- https://download.veyon.io/apt/veyon.gpg | sudo gpg --dearmor -o /usr/share/keyrings/veyon-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/veyon-archive-keyring.gpg] https://download.veyon.io/apt/ ./" | \
  sudo tee /etc/apt/sources.list.d/veyon.list
sudo apt update
sudo apt install veyon
```

### Fedora / openSUSE / otras distros

Consulta las instrucciones específicas para tu distribución en [https://veyon.io/download](https://veyon.io/download). Si no hay repositorio para tu distro, descarga el paquete `.rpm`/`.deb` correspondiente desde [https://github.com/veyon/veyon/releases](https://github.com/veyon/veyon/releases).

## 2. Configurar la autenticación por clave

1. Abre el Configurador de Veyon:
   ```bash
   veyon-configurator
   ```
2. Ve a la página **"Autenticación" (Authentication)** y en **Método** selecciona **"Autenticación mediante fichero de clave" (Key file authentication)**.
3. Ve a la página **"Claves de autenticación" (Authentication keys)**, pulsa **"Importar" (Import)**, ponle el mismo nombre que usó el profesor (`Docent`), y elige el fichero de clave pública que te ha dado el profesor (`veyon-aula-profesor.pem`).

## 3. Comprobar que el servicio está activo

El servicio arranca solo al iniciar sesión. Compruébalo con:

```bash
pgrep -fa veyon-service
```

Si no aparece, ejecútalo manualmente:

```bash
veyon-service start &
```

## 4. Firewall

Si tienes `ufw` activo, permite el puerto que usa Veyon:

```bash
sudo ufw allow 11100/tcp
```

## 5. Comprobación final

Avisa al profesor: tu equipo debería aparecer automáticamente en su consola en unos segundos, dentro del aula. Si no aparece o pide autenticación repetidamente, revisa la guía de [Resolución de problemas](UD01_T01_Veyon_Problemas.md) o avisa al profesor.

[⬅ Volver al taller T01](UD01_T01_Veyon.md)
