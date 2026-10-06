from django.shortcuts import render

# Create your views here.
movies = [
    {
        'name':'robot',
        'dir':'shankar',
        'imdb':7.2,
        'hero':'rajnikant',
        'heroine':'aishwarya rai'
    },
    {
        'name':'ij',
        'dir':'sankar',
        'imdb':7.2,
        'hero':'vikram',
        'heroine':'amy'
    }
]

def sandal(request):
    return render(request, 'sandalwood.html', {'context':movies})

def molly(request):
    return render(request, 'mollyhood.html',{'context':movies})

def bolly(request):
    return render(request,'bollywood.html',{'context':movies})
