from django.db import models

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name



    def __repr__(self):
        ...
    