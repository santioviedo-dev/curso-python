from django import forms
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'artista', 'popularidad']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la canción'}),
            'artista': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del artista'}),
            'popularidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
        }