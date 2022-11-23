from django.contrib import admin
from .models import Book, Author, Genre, Language, BookInstance
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(BookInstance)

admin.site.site_header = _("Local Library Admin Site")
admin.site.site_title = _("Local Library Portal")
admin.site.index_title = _("Welcome to Local Library Admin Site")

# decorador para registrar el modelo
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('language', 'genre')
    search_fields = ('title', 'author__first_name', 'author__last_name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status_color', 'img_image')
    list_filter = ('status', 'due_back')
    search_fields = ('book__title', 'book__author__first_name', 'book__author__last_name')

@admin.register(Language)
class LanguageInstanceAdmin(admin.ModelAdmin):
    pass
