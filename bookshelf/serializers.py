from rest_framework import serializers
from django.contrib.auth.models import User
from bookshelf.models import Autor, Libro

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'is_staff', 'first_name', 'last_name', 'email']
        read_only_fields = ['username', 'is_staff']

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['url', 'id', 'nombre', 'apellidos']

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['url', 'id', 'titulo', 'genero', 'fecha_pub', 'autores', 'bibliotecario']
        read_only_fields = ['bibliotecario']
