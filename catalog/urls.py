## creamos urls.py en catalog

from django.urls import path
from .views import index , acerca_de, BookListView

urlpatterns = [
    path ('', index, name='index'),
    path('acercade/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='libros'),
]