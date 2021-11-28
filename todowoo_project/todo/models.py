from django.db import models
from django.contrib.auth.models import User #для привязки тудушек к юзерам

class Todo(models.Model):
    title = models.CharField(max_length=100) #ограничиваем заголовок в 100 символов
    memo = models.TextField(blank=True) #поле описания,blank=True необязательное для заполнения поле
    created = models.DateTimeField(auto_now_add=True) #автозаполнения даты времени, удобно для сортировки
    datecomplited = models.DateTimeField(null=True, blank=True) #null=True наличие не обязательно, blank=True для необязательного заполнения в админке
    important = models.BooleanField(default=False) #default=False необязательный для заполнения параметр
    user = models.ForeignKey(User, on_delete=models.CASCADE) #связь между пользователем и записью

    #при создании модели, нужно провести миграции, makemigrations migrate и сделать запись в admin.py чтобы появился
    #объект тодо в админке

    def __str__(self):
        #метод для показа названия туду в админке
        return self.title


