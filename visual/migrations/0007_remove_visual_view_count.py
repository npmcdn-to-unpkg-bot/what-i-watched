# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 03:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0006_visual_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visual',
            name='view_count',
        ),
    ]
