# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_student_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(default='Hello', max_length=500, upload_to='pictures/'),
            preserve_default=False,
        ),
    ]