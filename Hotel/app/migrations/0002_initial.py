# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_info_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
