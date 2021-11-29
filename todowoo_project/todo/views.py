from django.shortcuts import render, redirect, get_object_or_404 # рендеh-создание страницы, редирект-переход на другую страницу,get для поиска ключа в бд
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #формы для создания и аутентификации юзера
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate #методы аутентификации
from .forms import TodoForm #форма для создания туду
from .models import Todo #модель туду
from django.utils import timezone #для заполнения поля datecomplete, для выполнения туду в функции completetodo

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
    todos = Todo.objects.filter(user=request.user, datecomplited__isnull=True) #обект словаря из моделей filter(user=request.user)-
    # -для вывода записей пользователя. datecomplited__isnull=True для отображения выполненных туду, если поле заполнено, отображать не будет
    return render(request, 'todo/currenttodo.html', {'todos': todos})

def viewtodo(request, todo_pk): #ключ записи для отображении на странице
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user) #класс и ключ
    if request.method == 'GET':
        form = TodoForm(instance=todo)  # форма для изменения уже сущевствующей туду
        return render(request, 'todo/viewtodo.html',
                      {'todo': todo, 'form': form})  # передаем ещё и форму для возможного изменения
    else:
        try:
            form = TodoForm(request.POST, instance=todo) #без instance=туду бд будет думать что мы создаем новую запись а не изменяем существующуючё
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/viewtodo.html',
                          {'todo': todo, 'form': form, 'error': 'плохая информация'})

def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST': #запрос на выполнение
        todo.datecomplited = timezone.now() #заполенение поля временем для отметки выполнено
        todo.save()
        return redirect('currenttodo')

def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST': #запрос на удаление
        todo.delete()
        return redirect('currenttodo')
