from django import forms



class JsonInputDateForm(forms.Form):
    input_date = forms.CharField(empty_label=None, label='Вводимая информация',
                                 widget=forms.Textarea(attrs={
                                     'class': 'form-control'
                                 }))
