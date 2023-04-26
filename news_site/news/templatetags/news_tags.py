from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category

register = template.Library()


@register.simple_tag(name='list_categories')
def get_categories():
    return Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='first_argument', arg2='second_argument'):
    # categories = cache.get('categories')
    categories = cache.get_or_set('categories',
                                  Category.objects.annotate(
                                      cnt=Count('get_news',
                                                filter=F('get_news__is_published')
                                                )
                                  ).filter(cnt__gt=0), 100)
    # if not categories:
    # # categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
    #     categories = Category.objects.annotate(
    #         cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 150)
    context = {
        'categories': categories,
        'arg1': arg1,
        'arg2': arg2,
    }
    return context
