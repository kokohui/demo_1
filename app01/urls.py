from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('login', views.spider_post, name='lg')
]