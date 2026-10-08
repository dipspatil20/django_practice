from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Cricket(request):
    return HttpResponse("Cricket")

def Football(request):
    return HttpResponse("Football")

def Basketball(request):
    return HttpResponse("Basketball")

def Chess(request):
    return HttpResponse("Chess")

def Volleyball(request):
    return HttpResponse("Volleyball")

