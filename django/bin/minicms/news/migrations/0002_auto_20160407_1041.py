# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 02:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 7, 2, 41, 38, 220135, tzinfo=utc), verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]