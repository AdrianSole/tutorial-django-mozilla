## creamos urls.py en catalog

from django.urls import path
from .views import SearchAuthorResultListView, index , acerca_de, BookListView, BookDetailView, AuthorListView, AuthorDetailView, \
     SearchResultsListView, LoanedBooksByUserListView, renovar_libro, AuthorCreate, AuthorUpdate, AuthorDelete, \
        SearchAuthorResultListView

urlpatterns = [
    path ('', index, name='index'),
    path('acercade/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),
    path('busqueda/', SearchResultsListView.as_view(), name='buscar'),
    path('libros-prestados/', LoanedBooksByUserListView.as_view(), name='libros-prestados'),
    path('libro/<uuid:pk>/renovar/', renovar_libro, name='renovar-fecha'),
    path('autores/', AuthorListView.as_view(), name='autores'),
    path('autores/<int:pk>', AuthorDetailView.as_view(), name='detalle-autor'),
    path('autores/crear/', AuthorCreate.as_view(), name='crear-autor'),
    path('autores/<int:pk>/renovar/', AuthorUpdate.as_view(), name='renovar-autor'),
    path('autores/<int:pk>/eliminar/', AuthorDelete.as_view(), name='eliminar-autor'),
    path('busqueda-autores/', SearchAuthorResultListView.as_view(), name='buscar-autores'),
]