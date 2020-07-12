from django.db import models

# Create your models here.
class Tshirt(models.Model):

    FirstName = models.CharField(max_length=100)
    LastName =  models.CharField(max_length=100)
    Email =  models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)