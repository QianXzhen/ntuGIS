# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180816_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='index',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='url',
        ),
    ]