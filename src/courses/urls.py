
from django.contrib import admin
from django.urls import path, re_path

from courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    # path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    # re_path(r'^courses/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course-detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(), name='detail'),
    # re_path(r'^courses/(?P<slug>[\w-]+)/edit/$', views.CourseUpdateView.as_view(), name='course-update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.CourseDeleteView.as_view(), name='delete'),
]
