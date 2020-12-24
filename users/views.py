# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError


def login_view(request):
    """ Login View """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request, 'users/login.html')


def Sign_up_view(request):
    pass


def landing_view(request):
    return render(request, 'base/landing.html')


def dashboard(request):
    """ Dashboard URL """
    return render(request,'users/dashboard.html')
