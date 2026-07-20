from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserAccount(AbstractUser):
    USER_TYPE_CHOICES= {
        'admin':'admin',
        'student':'student',
        'library':'library',
        'teacher':'teacher',
    }
    students_id = models.IntegerField(null=True,blank=True)
    Admission_number=models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=22,null=True,blank=True)
    user_type=models.CharField(null=True,blank=True,choices=USER_TYPE_CHOICES)