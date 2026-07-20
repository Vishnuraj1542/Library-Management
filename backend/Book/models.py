from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Book(models.Model):
    Language_Choices = [
        ('Eng','English'),('Mal','Malayalam'),('Hni','Hindi')
    ]
    book_name=models.CharField(max_length=100,null=True,blank=True)
    author_name=models.ForeignKey('Author',null=True,blank=True,on_delete=models.CASCADE)
    language=models.CharField(max_length=20,null=True,blank=True,choices=Language_Choices)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    total_copies=models.PositiveIntegerField(null=True,blank=True,default=0)
    publish_date=models.DateField(max_length=100,null=True,blank=True)
    added_by=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True,blank=True)

class Author(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True),
    dob=models.DateField(),
    Email=models.EmailField(null=True,blank=True)
    
class Category(models.Model):
    name=models.CharField(max_length=33,null=True,blank=True)