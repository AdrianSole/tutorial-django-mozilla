## creamos urls.py en catalog

from django.urls import path
from .views import index , acerca_de, BookListView, BookDetailView, AuthorListView, AuthorDetailView, \
     SearchResultsListView, LoanedBooksByUserListView, renovar_libro

urlpatterns = [
    path ('', index, name='index'),
    path('acercade/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),
    path('autores/', AuthorListView.as_view(), name='autores'),
    path('autores/<int:pk>', AuthorDetailView.as_view(), name='detalle-autor'),
    path('busqueda/', SearchResultsListView.as_view(), name='buscar'),
    path('libros-prestados/', LoanedBooksByUserListView.as_view(), name='libros-prestados'),
    path('libro/<uuid:pk>/renovar/', renovar_libro, name='renovar-fecha'),
]