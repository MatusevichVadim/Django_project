from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket


# контроллеры = views = функции

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)

def basket_delete(request, product_id):
    basket = Basket.objects.get(id=product_id)
    if basket.quantity == 1:
        basket.delete()
    else:
        basket.quantity -= 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
