from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.TextField(blank=True)
    signatrue = models.TextField(blank=True)
    datebirth = models.DateField(blank=True)