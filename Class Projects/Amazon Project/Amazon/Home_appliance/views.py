from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Grinder(request):
    return HttpResponse("Grinder")

def Cooker(request):
    return HttpResponse("Coocker")

def Mixer(request):
    return HttpResponse("Mixer")

def Stove(request):
    return HttpResponse("stove")

def Microwave(request):
    return HttpResponse("Microwave")

