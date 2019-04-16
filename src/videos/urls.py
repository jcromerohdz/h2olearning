from django.contrib import admin
from django.urls import path, re_path

from videos import views

app_name = 'videos'
urlpatterns = [
    path('', views.VideoListView.as_view(), name='list'),
    path('create/', views.VideoCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', views.VideoDetailView.as_view(), name='video-detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.VideoDetailView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.VideoUpdateView.as_view(), name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.VideoDeleteView.as_view(), name='delete'),
]