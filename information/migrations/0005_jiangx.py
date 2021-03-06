# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 15:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='JiangX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='static/image/JiangX/%Y/%m', verbose_name='轮播图')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '奖项',
                'verbose_name_plural': '奖项',
            },
        ),
    ]
