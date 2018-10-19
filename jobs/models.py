from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


class Job(models.Model):
    STATUS_CHOICES = (('pendente', 'Pendente'), ('publicado', 'Publicado'), ('expirado','Expirado'))

    title = models.CharField(max_length=512)
    description = models.TextField()
    submitInfo = models.TextField()
    tags = TaggableManager()
    slug = AutoSlugField(populate_from='title', unique=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=0)
    image = models.CharField(null=True,blank=True, max_length=512)
    tipo = models.CharField(null=True, blank=True, max_length=50)
    company = models.CharField(null=True, blank=True, max_length=256)
    salary = models.DecimalField(null=True, blank=True,max_digits=8, decimal_places=2)

    def get_absolute_url(self):
        return reverse('job:job_detail', args=[self.slug])

    def __str__(self):
        return self.title



# Create your models here.
