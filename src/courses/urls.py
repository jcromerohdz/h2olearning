
from django.contrib import admin
from django.urls import path, re_path

from courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/purches/$', views.CoursePurchaseView.as_view(), name='purchase'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.CourseUpdateView.as_view(), name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.CourseDeleteView.as_view(), name='delete'),
]
