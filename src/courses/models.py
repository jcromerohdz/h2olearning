from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from videos.models import Video

from .fields import PositionField
from .utils import create_slug, make_display_price


class MyCourses(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    courses         = models.ManyToManyField('Course', blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.courses.all().count())

    class Meta:
        verbose_name = 'My Courses'
        verbose_name_plural = 'My courses'

def post_save_user_create(sender, instance, created, *args, **kwargs):
    if created:
        MyCourses.objects.get_or_create(user=instance)

post_save.connect(post_save_user_create, sender=settings.AUTH_USER_MODEL)



POS_CHOICES = (
    ('main', 'Main'),
    ('secondary', 'Secondary'),
)

class Course(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True)
    category        = models.CharField(max_length=120, choices=POS_CHOICES, default='main')
    order           = PositionField(collection='category')
    description     = models.TextField()
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return "/videos/{slug_arg}".format(slug_arg=self.slug)
        return reverse('courses:detail', kwargs={'slug':self.slug})

    def display_price(self):
        return make_display_price(self.price)

class Lecture(models.Model):   
    course          = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video           = models.ForeignKey(Video,  on_delete=models.SET_NULL, null=True)
    title           = models.CharField(max_length=120)
    order           = PositionField()
    slug            = models.SlugField(blank=True)
    description     = models.TextField(blank=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (('slug', 'course'),)
        ordering = ['order', 'title']
    
    def get_absolute_url(self):
        # return "/videos/{slug_arg}".format(slug_arg=self.slug)
        return reverse('courses:detail', kwargs={'slug':course.slug})

def pre_save_course_receiver(sender , instance, *args, **kwargs): 
    if not instance.slug:
        # instance.slug = slugify(instance.title) 
        instance.slug = create_slug(instance) 
      

pre_save.connect(pre_save_course_receiver, sender=Course)
pre_save.connect(pre_save_course_receiver, sender=Lecture)
