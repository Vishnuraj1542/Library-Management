from django.shortcuts import render,redirect
from .models import UserAccount
from django import views

# Create your views here.
def user_creation(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')


