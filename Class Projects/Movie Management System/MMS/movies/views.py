from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieModel
from .forms import MovieModelForm

# Create your views here.
def create_mov(request):
    form = MovieModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_mov')
    return render(request, 'create_mov.html', {'form':form})


def read_mov(request):
    return render(request, 'read_mov.html')

def update_mov(request,mid):
    return render(request,'update_mov.html')

def delete_mov(request, mid):
    return render(request,'delete_mov.html')