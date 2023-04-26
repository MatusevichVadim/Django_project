from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .forms import UserRegistrationForm, UserLoginForm, ContactForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('home')
        else:
            messages.error(request, "Validation failed")
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            pass
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def send_mail_for_registrations(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['mail_body'],
                             'vadeggenstachil1@gmail.com',
                             ['Matusevichgizika@yandex.ru'],
                             fail_silently=True,
                             )
            if mail:
                messages.success(request, "Mail has been sent check your email")
                return redirect('mail')
            else:
                messages.error(request, "Mail hasn't been sent")
        else:
            messages.error(request, "Registration failed")
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'users/mail.html', context)
# class UsersLogin(User):
#     pass
#
#
# class UsersRegister(User):
#     pass
#
#
# class UsersLogout():
#     pass
