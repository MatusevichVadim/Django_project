from django import forms
from .models import News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название',
#                             widget=forms.TextInput(attrs={
#                                 'class': 'form-control'
#                             }))
#     content = forms.CharField(required=False, label='Текст',
#                               widget=forms.Textarea(attrs={
#                                   'class': 'form-control',
#                                   'rows': 5,
#                               }))
#     is_published = forms.BooleanField(initial=True, label='Опубликовано',
#                                       widget=forms.CheckboxInput(attrs={
#                                           'class': 'form-check-input'
#                                       }))
#     category = forms.ModelChoiceField(empty_label=None, queryset=Category.objects.all(),
#                                       label='Категория', widget=forms.Select(attrs={
#                                           'class': 'form-select'
#                                       }))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        # fields = '__all__'
