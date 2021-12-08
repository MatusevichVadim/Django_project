from django.shortcuts import render

# Create your views here.
# контроллеры = views = функции

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог'
    }
    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'title': 'Store',
        'header': 'DRUUUUUUUG',
        'username': 'IVAN',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ],
        'product_of_promotion': [
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00},
        ]
    }

    return render(request, 'products/test-context.html', context)
