from django.contrib import admin

# Register your models here.
from visual.models import Visual, Type, Review

admin.site.register(Visual)
admin.site.register(Type)
admin.site.register(Review)