from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieModel, UsersModel
from .forms import MovieModelForm, UsersModelForm

# Create your views here.
def create_mov(request):
    form = MovieModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_mov')
    return render(request, 'create_mov.html', {'form':form})


def read_mov(request):
    records = MovieModel.objects.all()
    return render(request, 'read_mov.html',{'context':records})

def update_mov(request,mid):
    record = get_object_or_404(MovieModel, id=mid)
    form = MovieModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read_mov')
    return render(request,'update_mov.html', {'form':form})

def delete_mov(request, mid):  
    record = get_object_or_404(MovieModel, id = mid)
    if request.method == 'POST':
        record.delete()
        return redirect('read_mov')

    return render(request,'delete_mov.html', {'context':record})

# UsersModel CRUD

def create_users(request):
    form = UsersModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_u')
    return render(request, 'create_users.html', {'form':form})

def read_users(request):
    records = MovieModel.objects.all()
    return render(request,'read_users.html',{'context':records})

def update_users(request, uid):
    record = get_object_or_404(UsersModel, id = uid)
    form = UsersModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read_u')
    return render(request,'update_users.html', {'form':form})

def delete_users(request, uid):
    record = get_object_or_404(UsersModel, id = uid)
    if request.method == 'POST':
        record.delete()
        return redirect('read_u')
    return render(request,'delete_users.html')