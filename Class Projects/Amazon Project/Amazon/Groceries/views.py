from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Fruits(request):
    return HttpResponse("fruits")

def Vegetable(request):
    return HttpResponse("Vegetable")

def Dairy(request):
    return HttpResponse("Dairy")

def Dry_fruits(request):
    return HttpResponse("Dry-fruits")

def Snaks(request):
    return HttpResponse("Snacks")


