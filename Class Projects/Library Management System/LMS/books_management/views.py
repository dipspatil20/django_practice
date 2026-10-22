from django.shortcuts import render, redirect, get_object_or_404
from .models import BooksModel
from django.contrib.auth.models import User
from .forms import UsersModelForm

# Create your views here.

def create_users(request):
    form = UsersModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'create_users.html', {'form':form})

def profile(request):
    return render(request,'profile.html')

def update_users(request):
    return render(request, 'update_users.html')

def delete_users(request):
    return render(request, 'delete_users.html')

def create_books(request):
    if request.method == 'POST':
        BooksModel.objects.create(
            bname = request.POST.get('bname'),
            author = request.POST.get('author'),
            genre = request.POST.get('genre'),
            avail = request.POST.get('avail'))
        return redirect('read_b')
    return render(request,'create_books.html')

def read_books(request):
    records = BooksModel.objects.all()
    return render(request,'read_books.html', {'context':records})

def update_books(request, bid):
    record = get_object_or_404(BooksModel, id = bid)
    if request.method == 'POST':
        record.bname = request.POST.get('bname')
        record.author = request.POST.get('author')
        record.genre = request.POST.get('genre')
        record.avail = request.POST.get('avail')
        record.save()
        return redirect('read_b')
    return render(request,'update_books.html', {'context':record})

def delete_books(request, bid):
    record = get_object_or_404(BooksModel, id= bid)
    if request.method == 'POST':
        record.delete()
        return redirect('read_b')
    return render(request,'delete_books.html', {'context':record})