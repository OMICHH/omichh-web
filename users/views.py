# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse

from .utils import account_activation_token

#Views
from django.views import View

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
            try:
                user = User.objects.get(username=username)
                if user.is_active == False:
                    return render(request,'users/login.html',{'error':'Verify your email to activate your account'})

                return render(request,'users/login.html',{'error':'Invalid username and password'})
            except:
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
            if User.objects.get(email = request.POST['email']):
                return render(request, 'users/singup.html', {'error': 'Email has alredy taken'})
        except:
            pass

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/singup.html',{'error':'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        email_subject = 'Activación de cuenta'
        email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
        }

        link = reverse('activate', kwargs={'uidb64': email_body['uid'], 'token': email_body['token']})
        activate_url = 'http://'+current_site.domain+link


        email = EmailMessage(
            email_subject,
            'Hola '+ user.get_full_name() + ', Por favor da click en el siguiente enlace para activar tu cuenta. \n'+activate_url,
            'no_reply@omichh.org',
            [user.email],
        )

        email.send(fail_silently=False)

        type_of_user = request.POST['type']
        if type_of_user == 'coach':
            profile = Coach(coach_user=user)
            profile.save()
        else:
            profile = Student(student_user=user)
            profile.save()

        messages.success(request,'La cuenta se creo con exito revisa tu bandeja de entrada para activarla')
        return redirect('login')

    return render(request,'users/singup.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Tu cuenta se ha activado con exito')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


@login_required
def dashboard(request):
    """ Dashboard URL """
    return render(request,'users/dashboard.html')


def landing_view(request):
    return render(request, 'base/landing.html')

@login_required
def contact_view(request):
    return render(request, 'index/contact.html')

@login_required
def complete_profile_view(request):
    """ Complete a user profile """
    user_is_coach=hasattr(request.user, "coach")
    if request.method == 'POST':
        if user_is_coach:
            profile=request.user.coach
            return redirect('landing')
        else:
            profile=request.user.student
            return redirect('landing')
    if user_is_coach:
        return render(request,'users/complete_profile_coach.html')
    else:
        return render(request,'users/complete_profile_student.html')

@login_required
def info_profile_view(request):
    """ Look at a info user """
    user=request.user
    user_is_coach=hasattr(request.user, "coach")
    if request.method == 'POST':
        if user_is_coach:
            profile=request.user.coach
            return redirect('landing')
        else:
            profile=request.user.student
            return redirect('landing')
    if user_is_coach:
        return render(request,'users/info_profile_coach.html')
    elif user.student.category == "OMI":
        return render(request,'users/info_profile_omi.html')
    else:
        return render(request,'users/info_profile_omips.html')