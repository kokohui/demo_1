from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import url, include


urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', include('app_ana.urls', namespace='login')),
]
