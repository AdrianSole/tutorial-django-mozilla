from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, BookInstance, Author, Genre, Language
from django.views.generic import ListView, DetailView

# Create your views here.
def index_general(request):
    
    return render(request, 'index-general.html')



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

    ultimos = Book.objects.all().order_by('-id')[:10]

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits':num_visits,
            'ultimos':ultimos,},
    )

# Listas_genéricas

class BookListView(ListView):
    ''''Vista generica para el listado de libros'''
    model = Book
    paginate_by = 15
    def get_queryset(self):
        return Book.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = '2º DAW'
        return context

class BookDetailView(DetailView):
    '''Vista generica para el detalle de un libro'''
    model = Book    

class AuthorListView(ListView):
    '''Vista generica para el listado de autores'''
    model = Author
    paginate_by = 15

class AuthorDetailView(DetailView):
    '''Vista generica para el detalle de un autor'''
    model = Author

##Busqueda
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        # Voy a guardar query para el contexto
        self.query = query
        return Book.objects.filter(title__icontains=query)
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['query'] = self.query
        return context