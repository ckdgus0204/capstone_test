from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
# from .forms import CreateUserForm


def signup(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect("home")
    elif request.method=="GET":
        userform = UserCreationForm()

    return render(request,'registration/signup.html',{"userform":userform})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html')
    else:
        return render(request,'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
    