from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, BookInstance, Author, Genre, Language

# Create your views here.
def index_old(request):
    texto = '''<h1>Librería Local</h1>
    <p>Este es el sitio web de la biblioteca local</p>'''
    #texto = Página de inicio de la librería local
    lista = "<h2>mi lista de últimos libros</h2>"
    
    for libro in Book.objects.all()[274:]:
       lista += f'<li>{libro.title}</li>' # Otra manera de print()
    lista += '</ul>'

    lista_disponibles = "<h2>Libros disponibles</h2>"
    count_disponibles = BookInstance.objects.filter(status='a').count()
    lista_disponibles += "<p>Hay " + str(count_disponibles) + " libros disponibles</p>"

    return HttpResponse(texto + lista + lista_disponibles)

def acerca_de(request):
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pagina de acerca de de la librerÃ­a local.</p>
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python logo">
    
    '''
    return HttpResponse(texto)

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors},
    )

