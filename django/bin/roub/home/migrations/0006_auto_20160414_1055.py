# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-14 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160414_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gcontent',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gdprice',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gimg',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='goprice',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gorder',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gstatus',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gstock',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gtype',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='gvrebate',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='isboutique',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='pictureset',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='printid',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='sid',
        ),
    ]
