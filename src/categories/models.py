from django.db import models
from django.urls import reverse
from django.db.models import Count
from django.db.models.signals import pre_save

from courses.utils import create_slug
from courses.fields import PositionField

from videos.models import Video

class CategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all(
        ).active().annotate(
            courses_lenght=Count('primary_category')+Count('secondary_category')
            ).prefetch_related('primary_category', 'secondary_category')

        # qs = Category.objects.all()
        # obj = qs.first()
        # courses = obj.course_set.all()


class Category(models.Model):
    title           = models.CharField(max_length=120)
    video           = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    slug            = models.SlugField(blank=True)
    order           = PositionField(blank=True)
    description     = models.TextField()
    active          = models.BooleanField(default=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects         = CategoryManager()

    def  __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/videos/{slug_arg}".format(slug_arg=self.slug)
        return reverse('categories:detail', kwargs={'slug':self.slug})

def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_category_receiver, sender=Category)