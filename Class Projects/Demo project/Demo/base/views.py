from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 1. class and object
# 2. Functions

def Home(request):
    return HttpResponse("Hello Django!!!!!")

