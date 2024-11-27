from django import forms
from bookshelf.models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['titulo', 'contenido']
        
class FiltroLibrosForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)
    autor = forms.CharField(max_length=100, required=False)
    pag = forms.IntegerField(min_value=1, required=False, widget=forms.HiddenInput())