from django.urls import path

from .views import register, user_login, user_logout, send_mail_for_registrations

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('mail/', send_mail_for_registrations, name='mail'),
]

