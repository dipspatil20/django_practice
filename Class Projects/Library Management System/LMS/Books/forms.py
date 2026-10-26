from django import forms
from .models import BooksModel

class BooksModelForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = ['bname', 'author', 'genre','avail']