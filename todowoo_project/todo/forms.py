from django.forms import ModelForm #импортируем формы джанго
from .models import Todo

class TodoForm(ModelForm):
    #параметры а атрибуты которые мы хотим разместить там
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important'] #то что будет отображатся

