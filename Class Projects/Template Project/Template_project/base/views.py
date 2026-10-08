from django.shortcuts import render

trainers = [
    {
        'name':'Saurav Kumar Jha',
        'sub':'Python Libraries',
        'desc':'Kind, God Of Cricket, Sense of Humour'
    },
    {
        'name':'Sachin Kushwaha',
        'sub':'Data Analyst',
        'desc':'Strict, Funny, Dabba Fellows, Cartoon Lover'
    },
    {
        'name':'Rohit Bagadi',
        'sub':'Frontend Developer',
        'desc':'Short-Tempered, rider, fashion designer,'
    }
]

# Create your views here.
def index(request):
    return render(request, 'index.html', {'context':trainers})

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def help(request):
    return render(render, 'help.html')