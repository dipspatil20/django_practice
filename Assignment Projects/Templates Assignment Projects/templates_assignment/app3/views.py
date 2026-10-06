from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Add_item(request):
    return render(request,'add_items.html')

def Items(request):
    return render(request,'items.html')

def Remove_item(request):
    return render(request,'remove_items.html')
