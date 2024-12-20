from django.contrib import admin
from bookshelf.models import Autor, Libro, Resena

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'fecha_pub', 'bibliotecario')
    list_filter = ('genero', 'fecha_pub')
    date_hierarchy = 'fecha_pub'
    ordering = ('-fecha_pub',)
    search_fields = ('titulo', 'autores__nombre', 'autores__apellidos')
    actions_on_top = True
    actions_on_bottom = False
    exclude = ('bibliotecario',)

    def save_model(self, request, obj, form, change):
        obj.bibliotecario = request.user
        super().save_model(request, obj, form, change)


@admin.action(description="Censurar reseñas seleccionadas")
def censurar(modeladmin, request, queryset):
    queryset.update(visible=False) # Este queryset contiene las reseñas seleccionadas


class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'usuario', 'titulo', 'visible')
    list_filter = ('visible', 'libro', 'usuario')
    actions = [censurar]


admin.site.register(Autor)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Resena, ResenaAdmin)