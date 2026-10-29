from django.shortcuts import render, redirect, get_object_or_404
from .models import vehicleModel
from .forms import vehicleModelForm

# Create your views here.
def create(request):
        form = vehicleModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('read')
        return render(request,'create.html', {'form':form})
    
def read(request):
    records = vehicleModel.objects.all()
    return render(request, 'read.html',{'context':records})


def update(request, vid):
    record = get_object_or_404(vehicleModel, id=vid)
    form = vehicleModelForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request,'update.html', {'form':form})


def delete(request, vid):
    record = get_object_or_404(vehicleModel, id = vid)
    if request.method == 'POST':
        record.delete()
        return redirect('read')
    return render(request,'delete.html', {'context':record})