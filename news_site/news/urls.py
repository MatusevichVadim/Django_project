from django.urls import path
from django.views.decorators.cache import cache_page

from .views import HomeNews, NewsByCategory, ViewNews, CreateNews

urlpatterns = [
    # path('', index, name='home'),
    path('', cache_page(60)(HomeNews.as_view()), name='home'),
    # path('category/<int:category_id>/', get_category,  name='get_category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='get_category'),
    path('news/<int:pk>/', cache_page(60)(ViewNews.as_view()), name='view_news'),
    # path('news/<int:news_id>/', view_news,  name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    # path('news/add_news/', add_news, name='add_news'),
]

