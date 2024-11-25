from django.forms import ModelForm
from bookshelf.models import Resena

class ResenaForm(ModelForm):
    class Meta:
        model = Resena
        fields = ['titulo', 'contenido']
        