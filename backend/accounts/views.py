from django.shortcuts import render,redirect
from .models import UserAccount
from django import views
from .forms import UsercreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')

def user_creation(request):
    if request.method == "POST":
        form = UsercreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            print(form.errors) 
    else:
        form = UsercreationForm()

    return render(request, "user_creation.html", {"form": form})

def login_view(request):
    if request.method =="POST":
        username=request.POST.get('username')
        name=UserAccount.objects.filter(username)
        if name :
            print(name)
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('user logged in sucessfully')
            return redirect('home')
        else:
            print('not correct')
            return render(request,'login.html',{'error':'invalid credential'})
    return render(request,'login.html')
        
    
        


