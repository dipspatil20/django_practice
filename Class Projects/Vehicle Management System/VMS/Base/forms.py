from django import forms
from .models import vehicleModel

class vehicleModelForm(forms.ModelForm):
    class Meta:
        model = vehicleModel
        fields = ['license_plate', 'make_model', 'daily_rate', 'color','is_rented']