from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Tshirt(AbstractBaseUser):

    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Email =  models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['Password']
    USERNAME_FIELD = 'Email'

    