from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Course(models.Model):
        
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=5, decimal_places=2)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def pre_save_course_receiver(sender , instance, *args, **kwargs): 
    if not instance.slug:
        instance.slug = slugify(instance.title) 
      

pre_save.connect(pre_save_course_receiver, sender=Course)
