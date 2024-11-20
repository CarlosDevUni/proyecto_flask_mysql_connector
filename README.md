# Proyecto Flask

Repositorio de ejemplo para desarrollar una API RESTful usando Flask con conexion a base de datos

## Requisitos

Se requieren los siguientes programas para la ejecución del proyecto:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## Instalación

### 1. Clonar el repositorio

Abrir una terminal y ejecutar el comando:

```bash
git clone https://github.com/CarlosDevUni/proyecto_flask_mysql_connector
```

### 2. Navegar al directorio del proyecto

```bash
cd proyecto_flask_mysql
```

### 3. Crear un entorno virtual

En **Windows**:

```bash
py -3 -m venv .venv
```

NOTA: Si se produce un error al ejecutar el comando anterior, puede utilizarse alternativamente otra herramienta para la creación del entorno virtual, siguiendo estos pasos:
```bash
# sólo si el comando anterior produce un error
pip install virtualenv
virtualenv .venv
```


En **macOS/Linux**:

```bash
python3 -m venv .venv
```

### 4. Activar el entorno virtual

En **Windows**:

```bash
.venv\Scripts\activate
```

NOTA: Si se produce un error al ejecutar el comando anterior, abrir VSC en modo Administrador y ejecutar el siguiente comando para activar los permisos en Windows:
```bash
# sólo si el comando anterior produce un error
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```

En **macOS/Linux**:

```bash
source .venv/bin/activate
```

### 5. Instalar las dependencias

Las dependencias necesarias se encuentran en el archivo `requirements.txt` dentro de la carpeta settings:

```bash
pip install -r .\settings\requirements.txt
```


### 6. Inicializar la base de datos (estructura, usuario, datos de prueba)

Los archivos de inicialización de la base de datos se encuentran en la carpeta settings

```
├── settings/
│       └── create_db.sql
│       └── create_user.sql
│       └── test_seeder.sql
```
- `create_db.sql/`: Contiene las sentencias SQL necesarias para la creación de la base de datos y las tablas.
- `create_user.sql/`: Contiene las sentencias SQL necesarias para la creación de un usuario que tenga acceso a la base de datos del proyecto.
- `test_seeder.sql/`: Contiene las sentencias SQL necesarias para insertar datos de prueba en la base de datos (se usa opcionalmente para testing).

Para realizar la inicialización, se puede copiar el contenido de cada archivo y ejecutarlo directamente en la pestaña SQL de phpMyAdmin (o una herramienta similar que se utilice). Los archivos de creación se deben ejecutar desde la pestaña SQL dentro del servidor, mientras que el archivo de insersión de datos de prueba se debe ejecutar desde la pestaña SQL de la base de datos ya creada.  

Alternativamente, se pueden ejecutar los scripts desde la línea de comandos:

```bash
cd settings
mysql --default-character-set=utf8mb4   -u root -p -e  "source create_db.sql"
mysql --default-character-set=utf8mb4   -u root -p -e  "source create_user.sql"
mysql --default-character-set=utf8mb4   -u root -p -e  "source test_seeder.sql"
```
Explicación del comando:
- `mysql`: Corresponde al ejecutable mysql.exe. Debe estar configurado correctamente como variable de entorno del sistema, de lo contrario no será reconocido. (Equipo->Propiedades->Configuración Avanzada del Sistema->Variables de entorno, agregar a la variable Path la ruta donde se ubica el archivo, ej: C:\xampp\mysql\bin\mysql.exe).
- `--default-character-set=utf8mb4`: especifica el juego de caracteres (necesario para evitar errores al insertar datos de prueba con caracteres especiales).
- `-u root`: el flag -u indica que a continuación se encuentra el nombre de usuario que debe utilizarse para la operación. En este ejemplo, el usuario es root. 
- `-p`: flag para indicar que el usuario tiene contraseña. Se debe completar luego de ejecutar el comando.
- `-e "source nombre_archivo.sql"`: indica el archivo que se desea ejecutar (ruta relativa al directorio settings).

NOTA: se requiere contar con un usuario `root` para ejecutar correctamente los comandos anteriores.

### 7. Crear un archivo con las variables de entorno

En la raíz del proyecto, crear un archivo `.env` con el siguiente contenido

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=flask_user_name
DB_PASSWORD=flask_user_password
DB_NAME=flask_app_db
PORT=5000
HOST=localhost
```

La configuración en este archivo debe coincidir con la utilizada para crear la base de datos y el usuario. Los valores del ejemplo son los mismos que se definen en los scripts de inicialización en SQL. Cuando el proyecto se despliegue en un servicio en la nube, se definirán valores específicos para esta configuración y el proyecto ya queda preparado para actualizar dichos valores.

### 8. Ejecutar el proyecto

```bash
python main.py
```

Una vez iniciada la aplicación, acceder desde un navegador a la ruta `http://127.0.0.1:5000/`, y debe observarse la respuesta `{"message": "test ok"}`
## Estructura del Proyecto

```
├── api/
│   ├── __init__.py
│   ├── db/
│       └── db_config.py
|   ├── models/
│       └── person.py
|   ├── routes/
│       └── person.py
|   ├── settings/
│       └── create_db.sql
│       └── create_user.sql
│       └── requirements.txt
│       └── test_seeder.sql
├── main.py
├── .venv/
├── requirements.txt
└── README.md
```

- `api/`: Carpeta principal del código fuente de la aplicación.
- `db/`: Carpeta de configuración de la conexión a la base de datos. Implementa la función get_db_connection(), que debe importarse en cada archivo que requiera realizar una consulta a la base de datos.
- `models/`: Carpeta de definición de modelos. Habitualmente cada archivo en esta carpeta se nombra de la misma forma que el recurso correspondiente. Implementa una clase con el nombre del recurso, con todas las operaciones asociadas al mismo, incluyendo la interacción con la base de datos.
- `routes/`: Carpeta de definición de rutas. Habitualmente cada archivo en esta carpeta se nombra de la misma forma que el recurso correspondiente. Debe importar el modelo al que hace referencia (y los relacionados, si es necesario). Define las rutas asociadas al recurso e invoca los métodos implementados en la clase asociada. Se utilizan bloques try-except para gestionar las posibles excepciones y evitar que se detenga el servidor.
- `settings/`: Carpeta de configuraciones y archivos de inicialización del proyecto. Puede incluir, por ejemplo, un archivo requirements.txt para la instalación de dependencias de python, archivos de scripts SQL para la inicialización de bases de datos, inserción de registros de prueba, etc. 
- `main.py`: Archivo de inicio de la aplicación
- `requirements.txt`: Archivo que contiene las dependencias del proyecto.
- `.venv/`: Entorno virtual (esta carpeta está en `.gitignore` y no debe ser incluida en el repositorio).
