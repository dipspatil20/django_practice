from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        fn = request.POST["fn"]
        sn = request.POST["sn"]
        phno = request.POST["phno"]
        email = request.POST['email']
        reason = request.POST["reason"]
        print(fn)
        print(sn)
        print(phno)
        print(email)
        print(reason)
    return render(request, 'contact.html')


