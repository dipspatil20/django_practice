from django import forms
from .models import MovieModel

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ['mname', 'director','rating', 'genre','price','avail']