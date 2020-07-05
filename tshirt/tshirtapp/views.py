from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
        
    }
    return render(request, 'tshirtapp/index.html', context)

def signup(request):

    context1 = {

    }
    return render(request,'tshirtapp/signup.html',context1 )

def login(request):

    context2 = {

    }
    return render(request,'tshirtapp/login.html',context2)