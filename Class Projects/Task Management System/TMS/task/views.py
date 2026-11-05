from django.shortcuts import render,redirect,get_object_or_404
from .models import TasksModel, UserTaskModel, CategoryModel
from .forms import TaskModelForm, UserTaskModelForm, CategoryModelForm


# Create your views here.
def create(request):
    form = TaskModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request,'create.html',{'form':form})


def read(request):
    records=TasksModel.objects.all()
    return render(request,'read.html',{'context':records})


def update(request, tid):
    record = get_object_or_404(TasksModel,id=tid)
    form = TaskModelForm(request.POST or None,instance=record)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request,'update.html',{'form':form})

def delete(request,tid):
    record = get_object_or_404(TasksModel,id=tid)
    if request.method=='POST':
        record.delete()
        return redirect('read')
    return render(request,'delete.html')

# -------------------------------------------------------

def create_rec(request):
    form = UserTaskModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_rec')
    return render(request, 'create.html', {'form':form})

def read_rec(request):
    record = UserTaskModel.objects.all()
    return render(request, 'read_rec.html',{'context':record})

def update_rec(request,tid):
    record = get_object_or_404(UserTaskModel,id = tid)
    form = UserTaskModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read_rec')
    return render(request,'update_rec.html',{'form':form})

def delete_rec(request,tid):
    record = get_object_or_404(UserTaskModel,id = tid)
    if request.method == 'POST':
        record.delete()
        return redirect('delete_rec')
    return render(request,'delete_rec.html',{'context':record})

# ----------------------------------------------------------------------

def create_cat(request):
    form = CategoryModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_cat')
    return render(request,'create_cat.html',{'form':form})


def read_cat(request):
    record = CategoryModel.objects.all()
    return render(request, 'read_cat.html',{'context':record})

def update_cat(request,tid):
    record = get_object_or_404(CategoryModel,id = tid)
    form = CategoryModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read_cat')
    return render(request,'update_cat.html',{'form':form})

def delete_cat(request,tid):
    record = get_object_or_404(CategoryModel,id = tid)
    if request.method == 'POST':
        record.delete()
        return redirect('delete_cat')
    return render(request,'delete_cat.html',{'context':record})
