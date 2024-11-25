from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


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

    def __str__(self):
        return f"{self.autores.first()} - {self.titulo}"

         


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.libro} - {self.titulo}"
    