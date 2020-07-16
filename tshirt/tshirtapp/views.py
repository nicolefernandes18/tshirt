from django.shortcuts import render,redirect
from .models import Tshirt

# Create your views here.
def index(request):
    
    context = {
        
    }
    return render(request, 'tshirtapp/index.html', context)

def signup(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        tshirt_obj = Tshirt(FirstName = firstname, LastName=lastname, Email=email , Password=password , ConfirmPassword=cpassword )

        if password==cpassword:
            if Tshirt.objects.filter(Email=email).exists():
                print("Email taken")

            else:
                tshirt_obj.save()
                print('CREATED')
            
            

        else:
            print("Password not matching..")

        return redirect('index')

    else:
        context1 = {

        }
        return render(request,'tshirtapp/signup.html',context1 )

def login(request):

    context2 = {

    }
    return render(request,'tshirtapp/login.html',context2)