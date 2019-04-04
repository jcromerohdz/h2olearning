from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Course 
from video.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
# from .forms import VideoForm

# Create your views here.
# CRUD
# class VideoCreateView(StaffMemberRequiredMixin, CreateView):
#     #queryset = Video.objects.all()
#     model = Video
#     form_class = VideoForm


class CourseDetailView(MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()

    # def get_object_or_404(Course, slug=self.kwargs.get("abc"))

    def get_context_data(self,*args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        print(context)
        return context


class CourseListView(StaffMemberRequiredMixin, ListView):
    # queryset = Course.objects.all()

    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs
    

    # def get_context_data(self,*args, **kwargs):
    #     context = super(CourseListView, self).get_context_data(**kwargs)
    #     return context
    

class CourseUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/courses/'
