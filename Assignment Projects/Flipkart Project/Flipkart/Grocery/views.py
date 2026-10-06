from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Rice_Grains(request):
    return HttpResponse("Rice & Grains Section !")

def Pulses(request):
    return HttpResponse("Pulses Section !")

def Oil(request):
    return HttpResponse("Oil Section !")

def Beverages(request):
    return HttpResponse("Beverages Section !")

def Spices(request):
    return HttpResponse("Spices Section !")