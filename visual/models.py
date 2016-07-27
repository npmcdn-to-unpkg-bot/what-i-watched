from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Visual(models.Model):
    title = models.CharField(max_length=60, blank=True)
    watched = models.BooleanField(default=True)
    douban_id = models.CharField(max_length=60, unique=True)
    imdb_id = models.CharField(max_length=60, blank=True)
    date_watched = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    original_title = models.CharField(max_length=60, blank=True)
    year = models.IntegerField(blank=True, default=0)
    rating = models.FloatField(blank=True, default=0.0)
    images = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)
    
    visual_type = models.ManyToManyField(Type, blank=True)
    favorite = models.ManyToManyField(User, blank=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-rating']

class Review(models.Model):
    content = models.TextField()
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visual = models.ForeignKey(Visual, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.content
    
    class Meta:
        ordering = ['-updated_at']