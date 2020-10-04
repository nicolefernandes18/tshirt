from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    
    context = {
        
    }
    return render(request, 'tshirtapp/index.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'tshirtapp/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'tshirtapp/checkout.html', context)

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

    menobjs = Product.objects.filter(Gender = 'M')

    return render(request, 'tshirtapp/mencategory.html', {'menobjs': menobjs})

def women(request):

    womenobjs = Product.objects.filter(Gender = 'F')
    return render(request, 'tshirtapp/women.html', {'womenobjs': womenobjs})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('Product: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)