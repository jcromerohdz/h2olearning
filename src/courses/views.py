import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Prefetch
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView
)

from .models import Course, Lecture 
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


class LectureDetailView(MemberRequiredMixin, DetailView):
    def get_object(self):
        course_slug = self.kwargs.get("cslug")
        lecture_slug = self.kwargs.get("lslug")
        obj = get_object_or_404(Lecture, course__slug=course_slug, slug=lecture_slug)
        return obj


class CourseDetailView(MemberRequiredMixin, DetailView):
    # queryset = Course.objects.all()

    def get_object(self):
        slug = self.kwargs.get("slug")
        qs = Course.objects.filter(slug=slug).owned(self.request.user)
        if qs.exists():
            return qs.first()
        raise Http404


class CoursePurchaseView(LoginRequiredMixin, RedirectView):
    # queryset = Course.objects.all()
    permanet = False

    def get_redirect_url(self, slug=None):
        # slug = self.kwargs.get("slug")
        qs = Course.objects.filter(slug=slug).owned(self.request.user)
        if qs.exists():
            user = self.request.user
            if user.is_authenticated:
                my_courses = user.mycourses
                # If transacction is successful:
                my_courses.courses.add(qs.first())
                return (qs.first().get_absolute_url())
            return (qs.first().get_absolute_url())
        return "/courses/"


class CourseListView(ListView):
    # queryset = Course.objects.all()

    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        user = self.request.user
        if query:
            qs = qs.filter(title__icontains=query)

        if user.is_authenticated:
            qs = qs.owned(user)
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
            obj.user = self.request.user
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
