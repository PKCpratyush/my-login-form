from os import name
from django.contrib import admin
from django.urls import path,include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index,name="index"),
    path('show_data', views.show_data,name="data page")
]