from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,
                               label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                               }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                               }))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150,
                               label='Username',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                               }))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                             }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150,
                              label='Тема',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                              }))
    mail_body = forms.CharField(label='Текст',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'rows': 5
                                }))
    captcha = CaptchaField(label='Каптча')
