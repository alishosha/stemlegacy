# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-19 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20170413_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='place',
            field=models.CharField(default='', max_length=500),
        ),
    ]
