from django.shortcuts import render, redirect, get_object_or_404
from .models import BooksModel
from .forms import BooksModelForm


# Create your views here.
def create(request):
    form = BooksModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read') #urlname - name in views.py
    return render(request,'create.html',{'form':form})

def read(request):
    records = BooksModel.objects.all()
    return render(request,'read.html', {'context':records})

def update(request,bid):
    record = get_object_or_404(BooksModel,id=bid)
    form = BooksModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request,'update.html',{'form':form})

def delete(request, bid):
    record = get_object_or_404(BooksModel, id = bid)
    if request.method == 'POST':
        record.delete()
        return redirect('read')
    return render(request,'delete.html')