from django.shortcuts import render

# Create your views here.
def create_profile(request):
    return render(request,'create_profile.html')

def display_profile(request):
    return render(request,'display_profile.html')

def update_profile(request):
    return render(request,'update_profile.html')
