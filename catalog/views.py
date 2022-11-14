from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from catalog.models import Book, BookInstance, Author, Genre, Language
from django.views.generic import ListView, DetailView
import datetime
from catalog.forms import RenewBookForm
from django.urls import reverse

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
        context['ahora'] = datetime.datetime.now()
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

## Búsqueda
class SearchResultsListView(ListView):
    model = Book
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        # voy a guardar query para el contexto
        if query:
            self.query = query
            return Book.objects.filter(title__icontains=query)
        else:
            return []
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['busqueda'] = self.query
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        return context

# Libros prestados
class LoanedBooksByUserListView(ListView):
    '''Vista generica para el listado de libros prestados por usuario'''
    model = BookInstance
    template_name = 'catalog/book_borrowed.html'
    paginate_by = 15
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('-due_back')

# Renovar libro
def renovar_libro(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('libros-prestados') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/renovacion_fecha.html', context)