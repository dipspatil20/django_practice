from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Cycling(request):
    return HttpResponse("Cycling Section !")

def Swimming(request):
    return HttpResponse("Swimming Section !")

def Yoga(request):
    return HttpResponse("Yoga Section !")

def Fitness_Equipment(request):
    return HttpResponse("Fitness Equipment Section !")

def Badminton(request):
    return HttpResponse("Badminton Section !")