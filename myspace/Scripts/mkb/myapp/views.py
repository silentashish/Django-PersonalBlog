from django.shortcuts import render

def index(request):
    return render(request,"myapp/home.html")

def contact(request):
    return render(request,'myapp/contact.html',{'contact':['This is my basic info about the different stuff i do in my personal life','my mail is ashish.gm74@gmail.com']})

# Create your views here.
