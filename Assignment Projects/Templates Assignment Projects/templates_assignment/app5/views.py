from django.shortcuts import render

# Create your views here.
def ai_help(request):
    return render(request,'ai_help.html')
def chat_help(request):
    return render(request,'chat_help.html')
def faq(request):
    return render(request,'faq.html')