# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0004_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
