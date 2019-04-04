from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Video
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import VideoForm

# Create your views here.
# CRUD
class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    #queryset = Video.objects.all()
    model = Video
    form_class = VideoForm


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()

    # def get_object_or_404(Video, slug=self.kwargs.get("abc"))

    def get_context_data(self,*args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        print(context)
        return context


class VideoListView(StaffMemberRequiredMixin, ListView):
    # queryset = Video.objects.all()

    def get_queryset(self):
        request = self.request
        qs = Video.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs
    

    # def get_context_data(self,*args, **kwargs):
    #     context = super(VideoListView, self).get_context_data(**kwargs)
    #     return context
    

class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'