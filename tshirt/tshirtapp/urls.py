from django.contrib import admin
from django.urls import path
from tshirtapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('mencategory', views.mencategory, name='mencategory'),
    path('women', views.women, name='women'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update_item', views.updateItem, name='update_item'),
]
