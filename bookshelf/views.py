from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from bookshelf.forms import FiltroLibrosForm, ResenaForm
from bookshelf.models import Autor, Libro, Resena
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

from bookshelf.serializers import AutorSerializer, LibroSerializer, UserSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.
class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'bookshelf/libro_list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltroLibrosForm(self.request.GET)
        return context

    def get_queryset(self):
        form = FiltroLibrosForm(self.request.GET)
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            autor = form.cleaned_data.get('autor')
            # pag = form.cleaned_data.get('pag')
            libros = Libro.objects.prefetch_related('autores').order_by('-fecha_pub') #queryset original
            if titulo:
                libros = libros.filter(titulo__icontains=titulo) #filtrar por titulo si se especifica
            if autor:
                libros = libros.filter(Q(autores__nombre__icontains=autor) | Q(autores__apellidos__icontains=autor)) # filtrar por autor si se especifica
            # if pag:
            #     pag = int(self.request.GET.get('pag', 1))
            #     offset = (pag - 1) * 5
            #     libros = libros[offset:offset+5] #paginar
            return libros
        else:
            return Libro.objects.none()
    

class LibroView(LoginRequiredMixin, View):
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
        

# Vistas de la API

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.bibliotecario == request.user
    


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @extend_schema(
        summary="Registra un nuevo libro",
        description="""Registra un nuevo libro en la base de datos,
        asignando el bibliotecario que lo registra.
        """,
        tags=['Libros']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(bibliotecario=self.request.user)
        else:
            raise PermissionDenied()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

