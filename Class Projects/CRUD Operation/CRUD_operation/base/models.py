from django.db import models

# Create your models here.
class Employee(models.Model):
    empname = models.CharField(max_length=100)
    empsal = models.IntegerField()
    dept = models.CharField(max_length=50)
    loc = models.CharField(max_length=10)
    avail = models.BooleanField(default=True)


"""
    Username: dipalee
    Email address: dipalee515@gmail.com  
    password : 123
"""