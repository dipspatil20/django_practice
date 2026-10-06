from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ACs(request):
    return HttpResponse("AC Section !")

def Fans(request):
    return HttpResponse("Fans Section !")

def Irons(request):
    return HttpResponse("Irons Section !")

def Fridge(request):
    return HttpResponse("Fridge Section !")

def Washing_Machines(request):
    return HttpResponse("Washing Machines Section !")