# 📌 Documentación: Clonar y Sincronizar un Repositorio GitHub

## 🏗️ Clonar un Repositorio GitHub en tu PC

1. Abre una terminal y ejecuta:
   ```bash
   git clone https://github.com/mi_repositorio.git
   ```
   Esto descargará el código en una carpeta llamada `mi_repositorio`.

2. Accede al directorio del proyecto:
   ```bash
   cd mi_repositorio
   ```

## 🔐 Configurar Git (Si es Necesario)
Si es la primera vez que usas Git en este equipo, configura tu usuario:
   ```bash
   git config --global user.name "TuNombre"
   git config --global user.email "tuemail@example.com"
   ```

## 💾 Realizar Cambios y Confirmarlos
1. Edita los archivos que necesites y revisa los cambios:
   ```bash
   git status
   ```
2. Agrega los cambios al área de preparación:
   ```bash
   git add .
   ```
3. Confirma los cambios con un mensaje:
   ```bash
   git commit -m "Descripción de los cambios"
   ```

## 🚀 Subir los Cambios a GitHub
1. Para subir los cambios al repositorio remoto:
   ```bash
   git push origin main
   ```
   *(Si la rama principal es `master`, usa `git push origin master`).*

## 🔄 Obtener Últimos Cambios del Repositorio
Si en algún momento deseas traer los últimos cambios del repositorio remoto:
   ```bash
   git pull origin main
   ```

## 🌿 Crear y Subir Cambios desde una Nueva Rama (Opcional)
Si quieres trabajar en una nueva funcionalidad sin afectar la rama principal:
   ```bash
   git checkout -b nueva-rama
   git add .
   git commit -m "Cambios en nueva rama"
   git push origin nueva-rama
   ```
   Luego, en GitHub, puedes hacer un **Pull Request** para fusionarla con `main`.

## 🔐 Métodos de Autenticación en GitHub
Para hacer ```git push``` debes auyenticarte en la cuenta github del repositorio. Hay varios métodos:
### 1️⃣ Usar HTTPS con Token Personal de Acceso (Recomendado)
GitHub ya no permite autenticarse con usuario y contraseña por HTTPS, así que debes usar un **Personal Access Token (PAT)**.

#### ➤ **Crear un Token de Acceso Personal (PAT)**
1. Ve a [GitHub → Configuración de Tokens](https://github.com/settings/tokens).
2. Haz clic en **"Generate new token (classic)"**.
3. Selecciona la opción **repo** (para acceso a repositorios).
4. Copia el token generado (⚠️ solo lo verás una vez).

#### ➤ **Autenticarse con el Token**
Cuando hagas `git push`, te pedirá usuario y contraseña:
- **Usuario**: Tu usuario de GitHub.
- **Contraseña**: Usa el token en lugar de tu contraseña.

Si prefieres no ingresar el token cada vez, puedes guardarlo:
```bash
 git remote set-url origin https://<TOKEN>@github.com/mi_repositorio.git
```
Reemplaza `<TOKEN>` por tu token real.

---

### 2️⃣ Usar SSH (Método Alternativo)
Si no quieres usar tokens, puedes configurar **claves SSH** para autenticarte sin escribir contraseñas.

#### ➤ **Generar una clave SSH (si no tienes una)**
```bash
ssh-keygen -t ed25519 -C "tuemail@example.com"
```
Presiona **Enter** para aceptar la ubicación predeterminada.

#### ➤ **Agregar la clave a GitHub**
1. Copia la clave pública:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Ve a [GitHub → Configuración de SSH](https://github.com/settings/keys).
3. Haz clic en **"New SSH Key"**, pega la clave y guárdala.

#### ➤ **Cambiar la URL remota a SSH**
```bash
git remote set-url origin git@github.com:joseliza/mi_repositorio.git
```
Ahora, puedes hacer `git push` sin escribir credenciales cada vez.

---

## 🎯 **Resumen**:
- **Si usas HTTPS** → Necesitas un **token de acceso personal (PAT)**.
- **Si usas SSH** → Necesitas **configurar claves SSH**.

🔥 **Recomendación:** Usa SSH si trabajas desde un PC personal. Para entornos más seguros o compartidos, usa HTTPS con un token.

---
🚀 ¡Listo! Ya tienes el repositorio sincronizado con tu PC. 😊
