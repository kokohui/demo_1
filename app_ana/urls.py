from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path(r'login_2', views.spider_category, name='lg'),
    path(r'index_2', views.spider_keyword, name='lr'),
    path(r'detail', views.spider_detail),

    path(r'login', views.Login.as_view()),
    path(r'index', views.Index.as_view()),
    path(r'menu', views.Menu.as_view()),
    path(r'goods', views.Goods.as_view()),
    path(r'spider', views.Spider.as_view())
]