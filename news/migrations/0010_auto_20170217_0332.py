# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-17 01:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170217_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
    ]