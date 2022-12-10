
from django.contrib import admin
from django.urls import path
from cms.views import *

urlpatterns = [
    path("",home,name="home"),
    path("insert/",insert,name="insert"),
    path('admin/', admin.site.urls),
]
