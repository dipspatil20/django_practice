from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Mobile(request):
    return HttpResponse("Electronics - Mobile Category !")

def Laptop(request):
    return HttpResponse("Electronics - Laptop Category !")

def TV(request):
    return HttpResponse("Electronics - TV Category !")

def Earbuds(request):
    return HttpResponse("Electronics - Earbuds Category !")

def Watches(request):
    return HttpResponse("Electronics - Watches Category !")
