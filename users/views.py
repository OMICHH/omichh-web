# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Coach, Student


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


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login')


def sing_up_view(request):
    """ Sing Up View """
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password_confirmation = request.POST['password_confirm']

        if password != password_confirmation:
            return render(request, 'users/singup.html', {'error': 'Password do not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/singup.html',{'error':'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        type_of_user = request.POST['type']
        if type_of_user == 'coach':
            profile = Coach(coach_user=user)
            profile.save()
        else:
            profile = Student(student_user=user)
            profile.save()

        return redirect('login')

    return render(request,'users/singup.html')

@login_required
def dashboard(request):
    """ Dashboard URL """
    return render(request,'users/dashboard.html')


def landing_view(request):
    return render(request, 'base/landing.html')

