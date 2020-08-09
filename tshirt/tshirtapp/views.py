from django.shortcuts import render,redirect
from .models import Men
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.
def index(request):
    
    context = {
        
    }
    return render(request, 'tshirtapp/index.html', context)

def signup(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=firstname,last_name=lastname,email=email, password=password)
                user.save()
                print('CREATED')
                return redirect('login')
        else:
            messages.info(request,'Password not matching..')

        return redirect('signup')

    else:
    
        context1 = {

        }   
        return render(request,'tshirtapp/signup.html',context1 )

def login(request):

    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            print('Invalid credentials')
            return redirect('login')
    else:
    
        context2 = {
        }
        return render(request,'tshirtapp/login.html',context2)

def mencategory(request):

    menobjs = Men.objects.all()

    return render(request, 'mencategory.html', {'menobjs': menobjs})