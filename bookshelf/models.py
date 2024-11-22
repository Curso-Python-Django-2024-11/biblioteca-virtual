from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=80)

GENEROS = [
    ('aventuras', 'Aventuras'),
    ('ciencia_ficcion', 'Ciencia ficción'),
    ('fantasia', 'Fantasía'),
    ('epica', 'Épica'),
    ('ensayo', 'Ensayo'),
    ('terror', 'Terror'),
    ('misterio', 'Misterio'),
    ('romance', 'Romance'),
    ('drama', 'Drama'),
    ('comedia', 'Comedia'),
    ('infantil', 'Infantil'),
    ('juvenil', 'Juvenil'),
    ('poesia', 'Poesía'),
    ('historia', 'Historia'),
    ('biografia', 'Biografía'),
]


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=50, choices=GENEROS)
    fecha_pub = models.DateField()
    bibliotecario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)                     


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    