from django.contrib import admin
from bookshelf.models import Autor, Libro, Resena

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Resena)