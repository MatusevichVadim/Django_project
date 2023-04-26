from django.contrib import admin
from .models import Todo #импорт модели туду


class TodoAdmin(admin.ModelAdmin):
    #класс нужен для отображения полей ридонли,и для этого создаем поле created для отображения в админке
    #admin.ModelAdmin нужен для костомизации интерфейса администратора
    readonly_fields = ('created', )


admin.site.register(Todo, TodoAdmin) #наследуем от класса TodoAdmin
