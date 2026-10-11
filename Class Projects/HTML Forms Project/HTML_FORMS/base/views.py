from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':   # to check whether the form is submitted or not

        data = {}
        data['first_name'] = request.POST.get('fn')
        data['second_name'] = request.POST.get('sn')
        data['fno'] = request.POST.get('phno')
        data['email'] = request.POST.get('email')
        data['reason'] = request.POST.get('reason')

        return render(request, 'profile.html',{'context':data})

    return render(request, 'contact.html')


#---------------------------------------------------

        # fn = request.POST.get('fn')
        # sn = request.POST.get('sn')
        # phno = request.POST.get('phno')
        # email = request.POST.get('email')
        # reason = request.POST.get('reason')
        # return render(request, 'profile.html', {'context':[fn,sn,phno,email,reason]})
        
# ------------------------------------------------------------------

        # fn = request.POST["fn"]
        # sn = request.POST["sn"]
        # phno = request.POST["phno"]
        # email = request.POST['email']
        # reason = request.POST["reason"]
        # print(fn)
        # print(sn)
        # print(phno)
        # print(email)
        # print(reason)

        #another method
        #request.POST.get('key)


    return render(request, 'contact.html')


