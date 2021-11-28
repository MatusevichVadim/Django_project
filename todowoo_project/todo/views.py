from django.shortcuts import render, redirect # рендесоздание страницы, редирект-переход на другую страницу
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #формы для создания и аутентификации юзера
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate #методы аутентификации
from .forms import TodoForm #форма для создания туду

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #при совпадении пароля, смотрим есть ли такой пользователь и если нету
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #создаем
                user.save() #сохраняем
                login(request, user) # логинимся этим пользователем
                return redirect('currenttodo') #и переходим на страницу при удачной аутентификации
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Такое имя пользователя уже используется'})
                #ловим исключение если имя пользователя есть в базе
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
            #ловим несовпадение паролей


def logoutuser(request):
    """ при нажатии кнопки Logout сюда прилегает GET запрос, нужно переделать тег а в кнопке logout"""
    if request.method == 'POST': #post Для того чтобы автозагрузка браузера не выкидывала пользователя во время подгрузки ссылок на страницы
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])#при удаче возвращает обьект юзера или None
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Имя порльзователя или пароль не верны'})
            #если метод authenticate не находит изера или неправельный пароль возвращаем страницу с описанием ошибки
        else:
            login(request, user)  # логинимся этим пользователем
            return redirect('currenttodo')  # и переходим на страницу при удачной аутентификации


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()}) #нужно создать форму для создания туду, создаем файл формс.пу
    else:
        try:
            #если пользователь ввел какую-то инфу и отправил запрос на размещение
            form = TodoForm(request.POST) #джанго форма сама разобьет пост запрос на части
            newtodo = form.save(commit=False) #сохраним запрос в бд. commit=False дает объект модели с ним можно работать,
            #будем сохранять только после привязки объекта к пользователю
            newtodo.user = request.user #привязка пользователя
            newtodo.save() #сохраняем в базу данных
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error': 'error переданы не верные данные'} )

def currenttodo(request):
    return render(request, 'todo/currenttodo.html')