from django.shortcuts import render

from .forms import JsonInputDateForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = JsonInputDateForm(request.POST)
    else:
        form = JsonInputDateForm()
    context = {
        'form': form,
    }
    return render(request, template_name='API/index.html', context=context)
