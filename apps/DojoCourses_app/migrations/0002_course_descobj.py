# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DojoCourses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='DescObj',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='courseObj', to='DojoCourses_app.CourseDescription'),
            preserve_default=False,
        ),
    ]
