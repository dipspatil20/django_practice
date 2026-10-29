from django.contrib import admin
from .models import vehicleModel

# Register your models here.
class adminVehicleModel(admin.ModelAdmin):
    list_display = ['license_plate', 'make_model', 'daily_rate', 'color','is_rented']

admin.site.register(vehicleModel, adminVehicleModel)

# username = dipalee
# password = 1234