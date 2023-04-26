from django.urls import path

from .views import api_v1


urlpatterns = [
    path('', api_v1, name='api_v1'),

]
