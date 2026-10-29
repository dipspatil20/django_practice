from django.db import models

# Create your models here.
class vehicleModel(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    make_model = models.CharField(max_length=100)
    daily_rate = models.DecimalField(max_digits=6,decimal_places=2)
    color = models.CharField(max_length=30)
    is_rented = models.BooleanField(default=False)


    def __str__(self):
        return self.license_plate