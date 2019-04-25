
from django.contrib import admin
from django.urls import path, re_path

from categories import views

app_name = 'categories'
urlpatterns = [
    path('', views.CategoryListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name='detail'),
]
