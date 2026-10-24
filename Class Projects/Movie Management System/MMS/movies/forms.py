from django import forms
from .models import MovieModel, UsersModel

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ['mname', 'director','rating', 'genre','price','avail']

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = UsersModel
        fields = ['name','contact','email', 'addr']
        