from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Visual(models.Model):
    title = models.CharField(max_length=60, blank=True)
    watched = models.BooleanField(default=True)
    douban_id = models.CharField(max_length=60)
    imdb_id = models.CharField(max_length=60, blank=True)
    visual_type = models.ManyToManyField(Type, blank=True)
    date_watched = models.DateTimeField(auto_now_add = True)
    original_title = models.CharField(max_length=60, blank=True)
    year = models.IntegerField(blank=True, default=0)
    rating = models.FloatField(blank=True, default=0.0)
    images = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_watched']