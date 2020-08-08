from django.db import models


# Create your models here.

class Men(models.Model):


    Name = models.CharField(max_length=100)
    Brand =  models.CharField(max_length=100)
    Size = models.CharField(max_length=100)
    Price =  models.CharField(max_length=100)
    Image= models.ImageField(upload_to='pics')
    

    


    