from django.shortcuts import render

name = 'Dipalee'

# Create your views here.

def home(request):
    return render(request, 'home.html', {'context':name})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def help(request):
    return render(request, 'help.html')
