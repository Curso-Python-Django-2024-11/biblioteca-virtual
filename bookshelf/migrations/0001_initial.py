# Generated by Django 5.1.3 on 2024-11-22 12:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('aventuras', 'Aventuras'), ('ciencia_ficcion', 'Ciencia ficción'), ('fantasia', 'Fantasía'), ('epica', 'Épica'), ('ensayo', 'Ensayo'), ('terror', 'Terror'), ('misterio', 'Misterio'), ('romance', 'Romance'), ('drama', 'Drama'), ('comedia', 'Comedia'), ('infantil', 'Infantil'), ('juvenil', 'Juvenil'), ('poesia', 'Poesía'), ('historia', 'Historia'), ('biografia', 'Biografía')], max_length=50)),
                ('fecha_pub', models.DateField()),
                ('autores', models.ManyToManyField(to='bookshelf.autor')),
                ('bibliotecario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.libro')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
