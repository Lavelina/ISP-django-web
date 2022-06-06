from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Section(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Continent")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'sect_slug': self.slug})

    class Meta:
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    body = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    publish = models.DateTimeField(default=timezone.now)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    sect = models.ForeignKey(Section, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ('publish', 'title')
