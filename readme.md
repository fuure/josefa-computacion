# Configuración del proyecto Josefa Computación (Django-MySQL)

## 1. Instalar Django

```bash
pip install Django
```

## 2. Configurar la base de datos MySQL
### 2.1 Instalar el controlador para MySQL

```bash
pip install mysqlclient
```
### 2.2 Crear un abase de datos vacía llamada "josefa"


### 2.3 Configurar la conexión en josefasite/settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'josefa',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 3. Ejecutar Migraciones e iniciar el Servidor de Desarrollo
Ejecutar dentro de la carpeta josefasite
```bash
sh run.sh
```

El servidor se ejecutará en http://127.0.0.1:8000/