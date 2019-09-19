from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('login', views.spider_category, name='lg'),
    path('index', views.spider_keyword, name='lr'),
]