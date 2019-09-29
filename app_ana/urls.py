# from django.urls import path
from . import views, views_export
from django.conf.urls import url

app_name = 'login'
urlpatterns = [
    url(r'login_2/', views.spider_category, name='lg'),
    url(r'xing2/', views.spider_xing_2),
    url(r'detail/', views.spider_detail),
    url(r'shop/', views.spider_shop),
    url(r'keywords/', views.spider_keywords),

    url(r'login/', views.Login.as_view()),
    url(r'index/', views.Index.as_view()),
    url(r'menu/', views.Menu.as_view()),
    url(r'goods/', views.Goods.as_view()),
    # url(r'spider/', views.Spider.as_view()),


    url(r'export_xing', views_export.ExportXing),
    url(r'export_detail', views_export.ExportDetail),
]