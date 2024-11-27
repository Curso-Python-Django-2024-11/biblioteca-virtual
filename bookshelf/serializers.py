from rest_framework import serializers

from bookshelf.models import Libro

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['titulo', 'genero', 'fecha_pub']
