from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, HomePageView, \
    LocalNewsView, SportNewsPage, XorijNewsView, TechNewsPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),

    path('news/', news_list, name='all_news_list'),

    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),

    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport/', SportNewsPage.as_view(), name='sport_news_page'),
    path('xorij/', XorijNewsView.as_view(), name='xorij_news_page'),
    path('techno/', TechNewsPage.as_view(), name='techno_news_page'),

]