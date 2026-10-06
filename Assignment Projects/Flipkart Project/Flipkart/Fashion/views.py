from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Sarees(request):
    return HttpResponse("Sarees Section !")

def Kurtas(request):
    return HttpResponse("Kurtas Section !")

def Jeans(request):
    return HttpResponse("Jeans Section !")

def Shirts(request):
    return HttpResponse("Shirts Section !")

def Handbags(request):
    return HttpResponse("Handbags Section !")