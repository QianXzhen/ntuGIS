# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0010_auto_20180817_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='', upload_to='static/image/news/%Y/%m'),
        ),
    ]
