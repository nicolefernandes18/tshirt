from django.db import models


# Create your models here.

class Men(models.Model):


    Name = models.CharField(max_length=100)
    Brand =  models.CharField(max_length=100)
    Size = models.CharField(max_length=100)
    Price =  models.CharField(max_length=100)
    Image= models.ImageField(upload_to='pics')
    
class Women(models.Model):


    W_Name = models.CharField(max_length=100)
    W_Brand =  models.CharField(max_length=100)
    W_Size = models.CharField(max_length=100)
    W_Price =  models.CharField(max_length=100)
    W_Image= models.ImageField(upload_to='w_pics')
    


    