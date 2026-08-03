from django.shortcuts import render,redirect
from .models import UserAccount
from django import views
from .forms import UsercreationForm

# Create your views here.
def user_creation(request):
    if request.method == 'POST':
       form= UsercreationForm(request.POST)
       if form.is_valid():
           user=form.save()
           return redirect('user_creation.html')
       else:
           form=UsercreationForm()
           return render(request,'user_creation.html',{'form':form})


        


