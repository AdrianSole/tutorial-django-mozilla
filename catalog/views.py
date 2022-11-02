from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book

# Create your views here.
def index(request):
    texto = '''<h1>Librería Local</h1>
    <p>Este es el sitio web de la biblioteca local</p>'''
    #texto = Página de inicio de la librería local
    lista = "<h2>mi lista de últimos libros</h2>"
    
    for libro in Book.objects.all()[274:]:
       lista += f'<li>{libro.title}</li>' # Otra manera de print()
    lista += '</ul>'

    return HttpResponse(texto + lista)

def acerca_de(request):
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pagina de acerca de de la librerÃ­a local.</p>
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python logo">
    
    '''
    return HttpResponse(texto)



