# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-13 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20170413_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Speaker',
            new_name='event',
        ),
    ]