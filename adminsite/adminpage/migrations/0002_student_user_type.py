# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('prof', 'Professor'), ('fac', 'Faculty')], default='student', max_length=100),
        ),
    ]
