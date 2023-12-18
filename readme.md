# Configuración del proyecto Josefa Computación (Django-MySQL)

## 1. Instalar Django

```bash
pip install Django
```

## 2. Crear el Proyecto y la Aplicación
```bash
django-admin startproject mysite
cd mysite
python3.9 manage.py startapp useradmin
```

## 3. Configurar la Base de Datos MySQL
### 3.1 Instalar el controlador para MySQL

```bash
pip install mysqlclient
```

### 3.2 Configurar la conexión en mysite/settings.py

```python
# En el archivo mysite/settings.py

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

## 4. Crear el Modelo en useradmin/models.py

```python
# En el archivo useradmin/models.py

from django.db import models

class UserAdminModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
```

## 5. Crear el Formulario en useradmin/forms.py

```python
# En el archivo useradmin/forms.py

from django import forms
from .models import UserAdminModel

class UserAdminModelForm(forms.ModelForm):
    class Meta:
        model = UserAdminModel
        fields = ['name', 'description']
```

## 6. Configurar las URLs en useradmin/urls.py
```python
# En el archivo useradmin/urls.py

from django.urls import path
from .views import index, create_item

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_item, name='create_item'),
]
```

## 7. Incluir las URLs de la Aplicación en mysite/urls.py
```python
# En el archivo mysite/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useradmin/', include('useradmin.urls')),
]
```

## 8. Ejecutar Migraciones
```bash
python3.9 manage.py makemigrations
python3.9 manage.py migrate
```

## 9. Iniciar el Servidor de Desarrollo
```bash
python3.9 manage.py runserver
```

El servidor se ejecutará en http://127.0.0.1:8000/