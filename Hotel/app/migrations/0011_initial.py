# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]