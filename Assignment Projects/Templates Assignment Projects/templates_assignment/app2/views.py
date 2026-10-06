from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Electronics(request):
    return render(request,'electronics.html')

def Fashion(request):
    return render(request,'fashion.html')

def Groceries(request):
    return render(request,'groceries.html')