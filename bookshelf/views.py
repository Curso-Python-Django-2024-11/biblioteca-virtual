from django.shortcuts import render
from django.views.generic import ListView
from bookshelf.models import Libro

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = 'bookshelf/libro_list.html'

    def get_queryset(self):
        return Libro.objects.prefetch_related('autores').all()