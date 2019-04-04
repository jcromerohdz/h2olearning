"""learningplat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from videos import views


urlpatterns = [
    path('videos/', views.VideoListView.as_view(), name='videoslist'),
    path('videos/create/', views.VideoCreateView.as_view(), name='videos-create'),
    re_path(r'^videos/(?P<pk>\d+)/$', views.VideoDetailView.as_view(), name='video-detail'),
    re_path(r'^videos/(?P<slug>[\w-]+)/$', views.VideoDetailView.as_view(), name='video-detail-slug'),
    re_path(r'^videos/(?P<slug>[\w-]+)/edit/$', views.VideoUpdateView.as_view(), name='video-update'),
    re_path(r'^videos/(?P<slug>[\w-]+)/delete/$', views.VideoDeleteView.as_view(), name='video-delete'),
    path('admin/', admin.site.urls),
]
