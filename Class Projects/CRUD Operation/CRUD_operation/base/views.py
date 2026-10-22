from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

# Create your views here.
def create(request):
    if request.method=="POST":
        name = request.POST.get('name')
        sal = request.POST.get('sal')
        dept = request.POST.get('dept')
        loc = request.POST.get('loc')
        avail = request.POST.get('avail')

        Employee.objects.create(empname = name, empsal=sal, dept = dept, loc=loc, avail=avail)

    return render(request,'create.html')

def read(request):
    data = Employee.objects.all()
    return render(request, 'read.html', {'context':data})

def update(request, eid):
    data = get_object_or_404(Employee,id = eid)
    if request.method == 'POST':
        data.empname = request.POST.get('name')
        data.empsal = request.POST.get('sal')
        data.dept = request.POST.get('dept')
        data.loc = request.POST.get('loc')
        data.avail = request.POST.get('avail')
        data.save()
        return redirect('read')

    return render(request,'update.html', {'context':data})


def delete(request,eid):
    data = get_object_or_404(Employee,id = eid)
    if request.method == 'POST':
        data.delete()
        return redirect('read')
    
    return render(request,'delete.html')