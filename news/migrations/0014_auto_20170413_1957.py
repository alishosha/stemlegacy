# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-13 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_remove_images_eventt'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='Speaker',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='images',
            name='place',
            field=models.CharField(default='', max_length=150),
        ),
    ]
