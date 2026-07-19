from django.db import models

# Create your models here.
class books(models.Model):
    book_name=models.CharField(max_length=100,null=True,blank=True)
    publishdate=models.CharField(max_length=100,null=True,blank=True)
    
