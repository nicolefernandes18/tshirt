from django.contrib import admin
from django.urls import path
from tshirtapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
