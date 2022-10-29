# Tutorial-django-mozilla

## Crear un env en python

_Crear un entorno virtual y activarlo_
> $ python3 -m venv env

> $ source venv/bin/activate

_*En windows*_

> C:\> env\Scripts\activate.bat

## Crear proyecto libreria local y configurarlo


1. mkdir libreria local

2. pip install django

* _- activar el (activate .bat (diferente en windows y linux))_

3. pip freeze > requirements.txt (redirecciona la colección de librerias)

4. pip freeze (version de las librerias instaladas en el entorno)

5. PS1 = "C:\>"

6. django-admin 

7. django-admin startproject locallibrary

8. pip install ipython (coleccion de librerias)

9. py manage.py (activa las migraciones)

- Migracion -> Tienen que adaptar la base de datos a lo que nosotros tenemos en el sistema definido.

10. py manage.py createsuperuser (pedira correo y contraseña)

11. py manage.py runserver (activa el server, puerto 8000 pordefecto)

## Catalog 

> django-admin startproject catalog

---
**_settings.py_**

```python
INSTALLED_APPS = [
        'catalog.apps.CatalogConfig',
        ---snip---
]
```
---
### sqlite (base de datos que va en un fichero)

**_setting.py_**

```python
DATABASES = [

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
]
```
---
### + cambios en locallibrary/settings.py

* LANGUAGE_CODE = 'en-us' -> 'es-es'

* TIME_ZONE = -> 'Europe/Madrid'

* USE_I18N = True (internalizacion)

* USE_TZ = True (uso time zones)

---
**_locallibrary/urls.py_**

* Añadimos url de catalog para que la encuentre

```python
urlpatterns = [

    path('admin/'), admin.site.urls),
    path('catalog/',include('catalog.urls')) 
]
```

**catalog/urls.py**

```python
from django.urls import path

urlpatterns = [

    path ('', views.index, name='index'),
]
```


**_views.py_** 

* views no esta definida

```python
from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    
    texto = '''<h1>Librería Local</h1>
    <p>Este es el sitio web de la biblioteca local</p>'''
    return HttpResponse(texto)
```
---

**_acercade.py_**

### En catalog/urls.py

Nos dara error porque no hay acercade.py (no esta definido)

- from .views import index, acerca_de

- path('acercade/', acerca_de, name='acercade'),

En **_views.py** añadiremos este def_->

```python
def acerca_de(request):
    
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pÃ¡gina de acerca de de la librerÃ­a local.</p>
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python logo">
    
    '''
    return HttpResponse(texto)
```

### En locallibrary/urls.py

cambiamos a ->

* importamos la vista de nuestra app catalog

```python
from catalog.views import index

urlpatterns = [

    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    ## para el index general
    path('', index, name='index_general'),
]
```

>makemigrations, migrate