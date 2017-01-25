from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone



class Job(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    submitInfo = models.TextField()
    tags = TaggableManager()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



# Create your models here.
