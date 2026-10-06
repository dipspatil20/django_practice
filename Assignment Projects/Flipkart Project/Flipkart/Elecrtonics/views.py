from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Cameras(request):
    return HttpResponse("Camera Section !")

def Tablets(request):
    return HttpResponse("Tablet Section !")

def Speakers(request):
    return HttpResponse("Speaker Section !")

def Printers(request):
    return HttpResponse("Printer Section !")

def Power_Banks(request):
    return HttpResponse("Power Bank Section !")
