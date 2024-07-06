from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        'news_list': news_list
    }
    return render(request,'news/news_list.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]

    local_one = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[0]
    local_news = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]

    sport_news = News.published.all().filter(category__name='Sport')[1:6]

    technology_one = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[0]
    technology_news = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]
    context = {
        'categories': categories,
        'news_list': news_list,

        'local_news': local_news,
        'local_one': local_one,

        'technology_one': technology_one,
        'technology_news': technology_news,

        'sport_news': sport_news,
    }
    return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time')[:6]

        context['maxalliy_news'] = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[:6]

        context['technology_news'] = News.objects.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]

        context['xorij_news'] = News.objects.all().filter(category__name='Xorij').order_by('-publish_time')[1:6]

        context['sport_news'] = News.objects.all().filter(category__name='Sport').order_by('-publish_time')[1:6]

        return context


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request,  *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Thanks for contacting with us</h2>")
        context = {
            'form': form,
        }
        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news


class XorijNewsView(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news


class TechNewsPage(ListView):
    model = News
    template_name = 'news/texno.html'
    context_object_name = 'texno_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news


class SportNewsPage(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news
