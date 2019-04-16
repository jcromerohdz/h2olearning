from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Course 
from courses.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import CourseForm

# CRUD
class CourseCreateView(StaffMemberRequiredMixin, CreateView):
    #queryset = Video.objects.all()
    model = Course
    form_class = CourseForm
    success_url = '/courses/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CourseCreateView, self).form_valid(form)


class CourseDetailView(MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()

    # def get_object_or_404(Course, slug=self.kwargs.get("abc"))

    # def get_context_data(self,*args, **kwargs):
    #     context = super(CourseDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_object(self):
        slug = self.kwargs.get("slug")
        obj = Course.objects.filter(slug=slug)
        if obj.exists():
            return obj.first()
        raise Http404


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

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_staff:
            obj.user = self.reques.user
        obj.save()
        return super(CourseUpdateView, self).form_valid(form)

    def get_object(self):
        slug = self.kwargs.get("slug")
        obj = Course.objects.filter(slug=slug)
        if obj.exists():
            return obj.first()
        raise Http404


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/courses/'

    def get_object(self):
        slug = self.kwargs.get("slug")
        obj = Course.objects.filter(slug=slug)
        if obj.exists():
            return obj.first()
        raise Http404
