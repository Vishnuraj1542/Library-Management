from django.db import models
from django.conf import settings
from Book.models import Book
class Lended(models.Model):
    STATUS_CHOICES=[('Issued','issued'),('Returned','returned'),('Due','due'),('Lost','lost')]
    book_name = models.ForeignKey(Book,null=True,blank=True,on_delete=models.CASCADE)
    lended_user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='taken_user')
    issued_officer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={
        'user_type':'library'
    })
    alloted_date=models.DateField(null=True,blank=True)
    return_date=models.DateField(null=True,blank=True)
    due_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=22,null=True,blank=True,choices=STATUS_CHOICES)