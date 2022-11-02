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

## Librerias

> pip freeze

> pip freeze > requirements.txt

> pip install -r requirements.txt

## Runserver

> python manage.py runserver

## Shell
*__ipython para un mejor manejo del shell__*

> python manage.py shell (Abre un entorno de py (con ipython en este caso))
- Nos permite acceder directamente a la base de datos
- Hacer consultas directas a la base de datos
> exit()
- Salir del editor de texto en la consola de comandos

```python
from catalog.models import Book

Book.objects.all() # Cuantos objetos tiene de tipo libro
```
---

> py manage.py loaddata catalogo

- Cargar datos

```python
from catalog.models import Book # Nos permite acceder al .json previamente instalado

Book.objects.all().count() # Cuenta los libros en la db

for l in Book.objects.all():
    print(l)

# P.E => Podemos imprimir solo los 5 primeros libros

for l in Book.objects.all()[:5]:
    print(l)

history # Comprobar lo introducido hasta el momento

Book.objects.filter(title="1984") # Buscar libro por título

for l in Book.objects.filter(title="1984"):
    print(l.author) # Método str que tiene el autor

for l in Book.objects.filter(title="1984"):
    print(f'{l.title}({l.author.last_name})') # Otra manera de print()

```

### Mostrar en inicio los 5 ultimos libros

- views.py es donde se encuentra la ruta de inicio *__index()__*.
- (podemos comprobarlo desde *__urls.py()__*)

```python
lista = "<h2>mi lista de últimos libros</h2>"
    
for libro in Book.objects.all()[274:]:
   lista += f'<li>{libro.title}</li>' 
lista += '</ul>'

return HttpResponse(lista)
```
```python
# Otra manera de hacerlo

lista = "<h2>mi lista de últimos libros</h2>"
    
for libro in Book.objects.all().order_by('id')[:5]:
       lista += f'<li>{libro.title}</li>' 
lista += '</ul>'

return HttpResponse(lista)
```

## Introducir nosotros un libro

### Desde el terminal

```python
from catalog.models import Author, Book

andres = Author()

andres.first_name = 'Andrés'

andres.last_name = 'Trapiello'

andres.save() # Insert y commit en la DB

# ---

libro = Book()

libro.title = "Don Quijote de la Mancha"

libro.author = andres

libro.isbn = '97884233496782'

# Si el texto ocupa + de una linea se usa ''' '''
libro.summary = ''' Descripcion '''

libro.save()
```
---
## Sitio administrativo

*__admins.py__*
```python
from .models import Book, Author, Genre, Language

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
```