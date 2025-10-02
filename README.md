# ProyectoTPOO
Este es el proyecto final del equipo 1 del grupo 004 de Taller de programación orientada a objetos.

El objetivo de este proyecto es simplificar la gestión y manejo de las pólizas de seguro. Los usuarios del proyecto podrán ver y editar las pólizas y usuarios del sistema, así como también ver una lista completa de los agentes y aseguradoras que se encuentran en el sistema. Además, podrán tener acceso a reportes detallados de las pólizas de seguro y las relaciones de los agentes con las aseguradoras, así como de las aseguradoras con los tipos de póliza que maneja cada una. Los usuarios podrán también crear una póliza desde cero pudiendo escoger o crear un usuario para esta y manejar fácilmente los campos requeridos para la creación de esta.

## Instalación y ejecución del servidor de prueba
Si se desea descargar el proyecto para ejecutarlo localmente en un servidor de pruebas es necesario seguir los siguientes pasos:
### 1. Instalar Python.
Es necesario tener instalada la versión 3.13.2 de Python, si no se tienen instalado Python puede descargarlo [aquí.](https://www.python.org/downloads/) Es importante que verifique que Python y pip estén agregados al path y puedan ejecutarse desde consola.
### 2. Crear un entorno virtual.
Para crear el entorno virtual puede utilizar cualquier herramienta de Python, como pipenv. Para instalarlo solo hay que ejecutar `pip install pipenv`. Una vez instalado pipenv, se debe de ejecutar `pipenv --python 3.13.2` en la carpeta que se desea instalar el proyecto para crear el entorno virtual.
### 3. Instalar el proyecto.
Para instalar el proyecto puede descargarse directamente en un archivo `.zip` o ejecutando en el entorno virtual desde git Bash `git clone https://github.com/DarkGhost74/ProyectoTPOO.git`.
### 4. Instalar requerimientos.
Para instalar los requerimientos basta con ir a la carpeta del proyecto recién instalado y ejecutar `pipenv install requirements.txt`
### 5. Ejecutar el servidor de pruebas.
Para correr el servidor local se debe de ejecutar desde CMD (no PowerShell) en la carpeta del proyecto el comando `python manage.py runserver`
### 6. Editar el código del proyecto.
Si se desea modificar el código se debe se asegurar que sea con el intérprete de Python del entorno virtual. En VS Code por ejemplo, puede hacerse presionando F1, seleccionar interprete de Python, y seleccionar el interprete local. Si se va a trabajar en VS Code se debe de asegurar tener instaladas las extensiones de Python de Microsoft.
