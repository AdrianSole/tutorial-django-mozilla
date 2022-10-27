# Tutorial-django-mozilla

## Crear un env en python


## Crear proyecto libreria local y configurarlo

> mkdir libreria local

> pip install django

- activar el (activate .bat (diferente en windows y linux))

> pip freeze > requirements.txt (redirecciona la colección de librerias)

> pip freeze (version de las librerias instaladas en el entorno)

> PS1 = "C:\>"

> django-admin 

> django-admin startproject locallibrary

> pip install ipython (coleccion de librerias)

> py manage.py (activa las migraciones)

- Migracion -> Tienen que adaptar la base de datos a lo que nosotros tenemos en el sistema definido.

> py manage.py createsuperuser (pedira correo y contraseña)

> py manage.py runserver (activa el server, puerto 8000 pordefecto)

## Catalog 

> django-admin startproject catalog

---
settings.py

INSTALLED_APPS = [
        'catalog.apps.CatalogConfig',
        ---snip---
]

---
**sqlite** (base de datos que va en un fichero)

setting.py

DATABASES = [

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
]

---

LANGUAGE_CODE = 'en-us' -> 'es-es'

TIME_ZONE = -> 'Europe/Madrid'

USE_I18N = True (internalizacion)

USE_TZ = True (uso time zones)

---
**locallibrary/urls.py**

urlpatterns = [

    path('admin/'), admin.site.urls),
    path('catalog',include('catalog.urls')) 
]

**catalog/urls.py**

from django.urls import path

urlpatterns = [

    path ('', views.index, name='index'),
]

--- views no esta definida
 views.py 

'''

from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    
    texto = '''<h1>Librería Local</h1>
    <p>Este es el sitio web de la biblioteca local</p>'''
    return HttpResponse(texto)

'''

**acercade.py**

---
#### En catalog/urls.py

Nos dara error porque no hay acercade.py (no esta definido)

- from .views import index, acerca_de

- path('acercade/', acerca_de, name='acercade'),

---
En **views.py** añadiremos este def->

**def acerca_de(request):**
    
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pÃ¡gina de acerca de de la librerÃ­a local.</p>
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python logo">
    
    '''
    return HttpResponse(texto)

En **locallibrary/urls.py**

cambiamos a ->

#importamos la vista de nuestra app catalog
from catalog.views import index

urlpatterns = [

    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    ## para el index general
    path('', index, name='index_general'),
]


makemigrations, migrate