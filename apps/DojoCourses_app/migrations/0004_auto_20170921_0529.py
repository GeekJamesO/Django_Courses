# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DojoCourses_app', '0003_auto_20170921_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='DescObj',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseObj', to='DojoCourses_app.CourseDescription'),
        ),
    ]
