from django.db import models
import uuid
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
# Create your models here.
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', 
        on_delete=models.SET_NULL, # que pasa si borramos el autor?
        null=True)  # puede ser nulo?
    summary = models.TextField(
        max_length=1000, 
        help_text='Enter a brief description of the book',
        blank=True)
    isbn = models.CharField(
        'ISBN', 
        max_length=13, 
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField('Genre', 
        help_text='Select a genre for this book')

    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object.""" 
        return self.title

    # display genre as a string
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, 
        help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        # ordering = ['-id']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, 
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class BookInstance(models.Model):
    """
    Modelo que representa una copia espec??fica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID ??nico para este libro particular en toda la biblioteca")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Disponibilidad del libro'
    )

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)

    @admin.display(description=_("Image"))
    def img_image(self):
        if self.image:
            return format_html(
                '<img src="{}" width="80" />'.format(
                    self.image.url)
            )
        else:
            return 'No foto'

    @admin.display(description=_('Status'))
    def status_color(self):
        return format_html(
            '<span style="color: {}; font-size:18px;">????</span>',
            'green' if self.status == 'a' else 'red',
        )