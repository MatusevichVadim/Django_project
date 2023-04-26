from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin


class HomeNews(ListView, MyMixin):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    mixin_properties = 'hello'
    paginate_by = 5

    # queryset = News.objects.select_related('category') для жадной выборки

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_properties'] = self.get_properties()
        return context

    def get_queryset(self):
        # select_related делает жадный запрос к бд, чтобы не стучаться каждый раз за категорией
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#     }
#     return render(request, template_name='news/index.html', context=context)


class NewsByCategory(ListView, MyMixin):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    # queryset = News.objects.select_related('category') для жадной выборки

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        # not_empty_fields = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)
        # for i in not_empty_fields:
        #     print(i.title, i.cnt)
        return News.objects.filter(
            category_id=self.kwargs['category_id'], is_published=True
        ).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context=context)


class ViewNews(DeleteView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news'


# def view_news(request, news_id):
#     news = get_object_or_404(News, pk=news_id)
#     context = {
#         'news': news,
#     }
#     return render(request, template_name='news/view_news.html', context=context)


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')  # redirect to home page
    login_url = '/admin/'

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # new_news = News.objects.create(**form.cleaned_data)
#             new_news = form.save()
#             return redirect(new_news)
#     else:
#         form = NewsForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name='news/add_news.html', context=context)
