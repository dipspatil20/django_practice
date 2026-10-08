from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Mens_cloths(request):
    return HttpResponse("Mens Clothing Section !")

def Womens_cloths(request):
    return HttpResponse("Womens Clothing Section !")

def Kids_cloths(request):
    return HttpResponse("Kids Clothing Section !")

def Footware(request):
    return HttpResponse("Footware Section !")

def Accessories(request):
    return HttpResponse("Accessories Section !")

