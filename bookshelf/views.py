from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from bookshelf.forms import ResenaForm
from bookshelf.models import Libro, Resena

# Create your views here.
class LibroListView(ListView):
    model = Libro
    template_name = 'bookshelf/libro_list.html'

    def get_queryset(self):
        return Libro.objects.prefetch_related('autores').all()
    

class LibroView(View):
    def get(self, request, pk):
        libro = Libro.objects.prefetch_related('autores').get(pk=pk)
        if not libro:
            return render(request, '404.html', status=404)
        resenas = Resena.objects.filter(libro=libro, visible=True)
        form = ResenaForm()
        return render(request, 'bookshelf/libro_detail.html', {'libro': libro, 'resenas': resenas, 'form': form})

    def post(self, request, pk):
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.instance
            resena.libro = Libro.objects.get(pk=pk)
            resena.usuario = request.user
            resena.save()
            return redirect('libro_detail', pk=pk)
        else:
            libro = Libro.objects.prefetch_related('autores').get(pk=pk)
            resenas = Resena.objects.filter(libro=libro, visible=True)
            return render(request, 'bookshelf/libro_detail.html', {'libro': libro, 'resenas': resenas, 'form': form})