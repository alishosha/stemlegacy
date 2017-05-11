# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-19 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('place', models.CharField(default='', max_length=250)),
                ('eventt', models.CharField(default='', max_length=250)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.row')),
            ],
        ),
    ]
