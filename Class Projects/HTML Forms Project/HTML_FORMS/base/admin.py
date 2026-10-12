from django.contrib import admin
from .models import Sample

# Register your models here.

class AdminSample(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact', 'email', 'password']

admin.site.register(Sample, AdminSample)

'''
username = dipalee
email = dipalee515@gmail.com
password = 123
'''