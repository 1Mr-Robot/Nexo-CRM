# Nexo CRM

Sistema de gestión de relaciones con clientes (CRM) diseñado para simplificar la administración y manejo de pólizas de seguro.

<p align="left">
    <img src="https://uziel.app/media/projects/nexo-crm/1.webp" alt="hero"  />&nbsp;
</p>

## Descripción

Nexo CRM permite a los usuarios visualizar, editar y gestionar pólizas de seguro, usuarios del sistema, agentes y aseguradoras. El sistema ofrece reportes detallados sobre las pólizas, relaciones entre agentes y aseguradoras, y las aseguradoras con los tipos de póliza que manejan. También incluye un asistente para crear pólizas desde cero, seleccionando o creando un usuario asociado.

## Arquitectura del Proyecto

El proyecto sigue una arquitectura MVT (Model-View-Template) implementada con el framework Django:

```
Nexo-CRM/
├── Nexo-CRM/           # Configuración principal del proyecto Django
│   ├── settings.py     # Configuración de la aplicación
│   ├── urls.py         # Rutas principales
│   ├── wsgi.py         # Punto de entrada WSGI
│   └── asgi.py         # Punto de entrada ASGI
├── agentes/            # App para gestión de agentes
├── aseguradoras/        # App para gestión de aseguradoras
├── clientes/           # App para gestión de clientes
├── crear/              # App para asistente de creación de pólizas
├── core/               # App con modelos de relaciones (DetalleAgAs, DetalleAsTP)
├── polizas/            # App para gestión de pólizas y catálogos
├── reportes/           # App para generación de reportes
└── manage.py           # Utilidad de administración Django
```

### Aplicaciones Django

| App | Descripción |
|-----|-------------|
| `agentes` | Gestión de agentes de seguro |
| `aseguradoras` | Gestión de aseguradoras |
| `clientes` | Gestión de clientes con datos personales y dirección |
| `crear` | Asistente paso a paso para crear pólizas |
| `core` | Modelos de relaciones entre entidades |
| `polizas` | Gestión de pólizas, tipos, formas y métodos de pago |
| `reportes` | Generación de reportes detallados |

## Tecnologías

### Framework y Lenguaje
- **Django 5.2** - Framework web Python
- **Python 3.13** - Lenguaje de programación

### Base de Datos
- **MySQL** - Sistema de gestión de base de datos
- **Clever Cloud** - Plataforma hosting para la base de datos remota

### Librerías y Dependencias
- **django-ckeditor 6.7.2** - Editor WYSIWYG para contenido enriquecido
- **mysqlclient 2.2.7** - Conector MySQL para Python
- **pillow 11.2.1** - Procesamiento de imágenes
- **python-dotenv 1.2.2** - Carga de variables de entorno
- **django-js-asset 3.1.2** - Soporte para JavaScript en formularios Django

### Frontend
- HTML5 / CSS3
- JavaScript vanilla
- Bootstrap
- Templates Django (Jinja2-like syntax)

## Modelos de Datos

### Entidades Principales

| Modelo | Tabla | Descripción |
|--------|-------|-------------|
| `Cliente` | `cliente` | Datos personales, contacto y dirección del cliente |
| `Agente` | `agente` | Agentes de seguro (nombre, apellidos) |
| `Aseguradora` | `aseguradora` | Compañías aseguradoras (nombre, logo) |
| `Poliza` | `poliza` | Pólizas de seguro con todos sus atributos |
| `TipoPoliza` | `tipoPoliza` | Tipos de póliza disponibles |
| `FormaPago` | `formaPago` | Formas de pago (mensual, semestral, anual) |
| `MetodoPago` | `metodoPago` | Métodos de pago (efectivo, transferencia, etc.) |
| `GeneroCliente` | `generoCliente` | Catálogo de géneros |

### Entidades de Relación

| Modelo | Tabla | Descripción |
|--------|-------|-------------|
| `DetalleAgAs` | `detalleAgAs` | Relación muchos a muchos Agente-Aseguradora |
| `DetalleAsTP` | `detalleAsTP` | Relación Aseguradora-TipoPoliza con comisión |

## Funcionalidades

### Gestión de Pólizas
- Visualizar lista de pólizas con información completa
- Editar pólizas existentes
- Crear nuevas pólizas mediante asistente
- Búsqueda flexible por múltiples campos

### Gestión de Usuarios
- Sistema de autenticación integrado
- Diferentes niveles de acceso (staff vs usuarios regulares)
- Redirección basada en rol después del login

### Reportes
- Reporte de pólizas con filtros de búsqueda
- Reporte de relaciones Agente-Aseguradora
- Reporte de relaciones Aseguradora-Tipo de Póliza

### Asistente de Creación de Pólizas
1. Selección o creación de cliente
2. Selección de agente
3. Filtrado de aseguradoras relacionadas al agente
4. Filtrado de tipos de póliza por aseguradora
5. Configuración de pago con cálculo automático de comisión

## Herramientas Recomendadas

### Desarrollo
- **Visual Studio Code** - Editor de código recomendado
- **Git / Git Bash** - Control de versiones
- **MySQL Workbench** - Cliente visual para base de datos

### Extensiones VS Code
- Python (Microsoft)
- Django (Baptiste Darthen)
- Djaneiro (Vivian")
- Pylint con pylint_django

## Configuración del Entorno

### Variables de Entorno (.env)

El proyecto utiliza variables de entorno para configuración sensible:

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=host_mysql
DB_PORT=3306
```

### Base de datos pública

Se ha cerado una base de datos pública alojada en Clever Cloud para que cualquiera pueda experimentar con ella. Para usarla solo hay que configurar el .env:

```env
DB_NAME=blbobicm5ybh67kjinxc
DB_USER=uxxuzbyn4sknuup3
DB_PASSWORD=HWnbIzeSH3zcsx97Bu3M
DB_HOST=blbobicm5ybh67kjinxc-mysql.services.clever-cloud.com
DB_PORT=3306
```

## Contribuir

Para instrucciones detalladas de instalación y configuración, consulta [CONTRIBUTING.md](CONTRIBUTING.md).
