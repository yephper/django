# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-14 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160414_1100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commodity',
            new_name='Goods',
        ),
    ]
