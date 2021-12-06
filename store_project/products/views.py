from django.shortcuts import render

# Create your views here.
# контроллеры = views = функции

def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'Store',
        'header': 'DRUUUUUUUG',
        'username': 'IVAN',

    }

    return render(request, 'products/test-context.html', context)
