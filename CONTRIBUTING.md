# Guía de Contribución

Documentación técnica para desarrolladores que deseen instalar, configurar y trabajar con el proyecto Nexo CRM.

## Requisitos Previos

### Software Necesario

| Software | Versión Mínima | Propósito |
|----------|---------------|-----------|
| Python | 3.13 | Runtime del framework Django |
| Git | Latest | Control de versiones |
| MySQL | 8.0 | Sistema de gestión de base de datos |

### Plataformas Soportadas

- Windows 10/11 (PowerShell, CMD)
- Linux (bash)
- macOS (zsh, bash)

## Instalación Paso a Paso

### 1. Clonar o Descargar el Proyecto

**Opción A: Clonar con Git**
```bash
git clone https://github.com/1Mr-Robot/Nexo-CRM.git
cd Nexo-CRM
```

**Opción B: Descargar como ZIP**
1. Descarga el proyecto como archivo `.zip` desde el repositorio
2. Extrae el contenido en tu carpeta de preferencia
3. Abre una terminal en la carpeta del proyecto

### 2. Instalar Python 3.13

1. Descarga Python desde [python.org/downloads/](https://www.python.org/downloads/)
2. Ejecuta el instalador
3. **Importante**: Marca la opción "Add Python to PATH"
4. Verifica la instalación:
```bash
python --version
pip --version
```

### 3. Crear el Entorno Virtual

Los entornos virtuales permiten aislar las dependencias del proyecto.

**Usando venv (módulo estándar de Python)**

```bash
python -m venv venv
```

Esto crea una carpeta `venv/` con una copia independiente de Python.

### 4. Activar el Entorno Virtual

**Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

Si aparece un error de ejecución de scripts, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego intenta activar nuevamente.

**Windows CMD:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

Verás `(venv)` al inicio de tu terminal indicando que el entorno está activo.

### 5. Instalar Dependencias

Con el entorno virtual activo:

```bash
pip install -r requirements.txt
```

Dependencias de desarrollo:

```bash
pip install -r requirements-dev.txt
```

**Dependencias incluidas:**
- `Django==5.2` - Framework web principal
- `mysqlclient==2.2.7` - Conector MySQL
- `django-ckeditor==6.7.2` - Editor WYSIWYG
- `pillow==11.2.1` - Procesamiento de imágenes
- `python-dotenv==1.2.2` - Variables de entorno
- `asgiref==3.8.1` - Soporte ASGI
- `sqlparse==0.5.3` - Parser SQL
- `django-js-asset==3.1.2` - JavaScript en formularios
- `tzdata==2025.2` - Datos de zonas horarias

### 6. Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=nexocrm
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
```

**Generar SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 7. Configurar la Base de Datos

#### Opción A: Usar Base de Datos Remota (Clever Cloud)

Para poder la base de datos de pruebas, solo hay que configurar el .env:

```env
DB_NAME=blbobicm5ybh67kjinxc
DB_USER=uxxuzbyn4sknuup3
DB_PASSWORD=HWnbIzeSH3zcsx97Bu3M
DB_HOST=blbobicm5ybh67kjinxc-mysql.services.clever-cloud.com
DB_PORT=3306
```

Si se desea conectar mediante terminal, basta con ejecutar:

```bash
mysql -h blbobicm5ybh67kjinxc-mysql.services.clever-cloud.com -P 3306 -u uxxuzbyn4sknuup3 -p blbobicm5ybh67kjinxc
```

y escribir la contraseña:

```
HWnbIzeSH3zcsx97Bu3M
```

#### Opción B: Base de Datos Local

1. Crea una base de datos MySQL:
```sql
CREATE DATABASE nexocrm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Modifica el archivo `.env` con tus credenciales locales.

#### Tablas No Administradas por Django

Las siguientes tablas tienen `managed = False` en sus modelos, lo que significa que fueron creadas manualmente y Django no las modifica:

| Tabla | Modelo | Propósito |
|-------|--------|-----------|
| `agente` | `Agente` | Agentes de seguro |
| `aseguradora` | `Aseguradora` | Aseguradoras |
| `cliente` | `Cliente` | Clientes |
| `detalleAgAs` | `Detalleagas` | Relación Agente-Aseguradora |
| `detalleAsTP` | `Detalleastp` | Relación Aseguradora-TipoPóliza |
| `formaPago` | `Formapago` | Formas de pago |
| `generoCliente` | `Generocliente` | Géneros de cliente |
| `metodoPago` | `Metodopago` | Métodos de pago |
| `poliza` | `Poliza` | Pólizas |
| `tipoPoliza` | `Tipopoliza` | Tipos de póliza |

#### Crear Copia Local de la Base de Datos

Si deseas que Django tenga control total sobre las tablas:

1. Cambia `managed = False` a `managed = True` en todos los modelos
2. Actualiza las credenciales en `.env`
3. Ejecuta:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Ejecutar el Servidor

### Servidor de Desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

### Crear Superusuario

El acceso está limitado a usuarios autenticados:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear el usuario administrador.

## Configuración del Entorno de Desarrollo

### Visual Studio Code

1. **Extensiones recomendadas:**
   - Python (Microsoft)
   - Django (Baptiste Darthen)
   - Djaneiro (Vivian")
   - Pylint

2. **Seleccionar Intérprete de Python:**
   - Presiona `F1`
   - Busca "Python: Select Interpreter"
   - Selecciona el intérprete dentro de `venv/Scripts/python.exe`

3. **Configurar Pylint para Django:**
   - Ve a `File > Preferences > Settings`
   - Busca "pylint"
   - En "Args" agrega:
   ```
   --load-plugins,pylint_django
   ```

### Configuración Adicional

**Carpetas importantes:**
- `core/static/` - Archivos estáticos (CSS, JS, imágenes)
- `templates/` - Plantillas HTML base
- `media/` - Archivos subidos por usuarios

**Base URL del admin:**
- Admin Django: `/admin/`
- Login: `/home/login/`

## Comandos Django Útiles

| Comando | Descripción |
|---------|-------------|
| `python manage.py runserver` | Iniciar servidor de desarrollo |
| `python manage.py makemigrations` | Crear migraciones |
| `python manage.py migrate` | Aplicar migraciones |
| `python manage.py createsuperuser` | Crear superusuario |
| `python manage.py shell` | Abrir shell de Django |
| `python manage.py collectstatic` | Recolectar archivos estáticos |
| `python manage.py check` | Verificar problemas |

## Flujo de Trabajo para Modificar Código

1. Asegúrate de tener el entorno virtual activo
2. Verifica que el intérprete de Python sea el del entorno virtual
3. Realiza los cambios en el código
4. Prueba localmente con `python manage.py runserver`
5. Verifica que no haya errores con `python manage.py check`

## Estructura de URLs del Proyecto

| Ruta | Vista | Descripción |
|------|-------|-------------|
| `/admin/` | Django Admin | Panel de administración |
| `/home/login/` | `iniciar_sesion` | Página de login |
| `/home/logout/` | `cerrar_sesion` | Cerrar sesión |
| `/polizas/` | `polizas` | Lista de pólizas |
| `/reportes/` | `menu` | Menú de reportes |
| `/reportes/polizas/` | `reporte_polizas` | Reporte de pólizas |
| `/reportes/agas/` | `reporte_AgAs` | Reporte Agente-Aseguradora |
| `/reportes/astp/` | `reporte_AsTP` | Reporte Aseguradora-TipoPóliza |
| `/crear/` | `crear` | Crear cliente |
| `/crear/agente/<id>/` | `crear_agente` | Seleccionar agente |
| `/crear/aseguradora/<cliente>/<agente>/` | `crear_aseguradora` | Seleccionar aseguradora |
| `/crear/tipopoliza/<cliente>/<agente>/<aseguradora>/` | `crear_tipoPoliza` | Seleccionar tipo |
| `/crear/pago/<cliente>/<agente>/<aseguradora>/<tipopoliza>/` | `crear_pago` | Configurar pago |

## Notas Técnicas Adicionales

### Relación entre Entidades

- Un `Agente` puede trabajar con múltiples `Aseguradora` (many-to-many via `DetalleAgAs`)
- Una `Aseguradora` puede ofrecer múltiples `TipoPoliza` (many-to-many via `DetalleAsTP`)
- Una `Poliza` está vinculada a un `Cliente`, `Agente`, `Aseguradora`, `TipoPoliza`, `FormaPago` y `MetodoPago`

### Cálculo de Prima

La prima final se calcula automáticamente sumando la comisión del agente:
```python
prima_final = prima_base * (1 + comision / 100)
```

### Búsqueda Flexible

El sistema implementa búsqueda por múltiples términos separados por espacios, permitiendo buscar por nombre, apellidos o ID en cualquier combinación.