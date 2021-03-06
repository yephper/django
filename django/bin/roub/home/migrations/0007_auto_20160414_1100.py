# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-14 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160414_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=100, unique=True, verbose_name='商品名称')),
                ('gdescription', models.CharField(max_length=200, unique=True, verbose_name='商品描述')),
                ('gcontent', models.TextField(verbose_name='商品详情')),
                ('cid', models.IntegerField(verbose_name='商品分类id')),
                ('sid', models.IntegerField(verbose_name='分店ID')),
                ('goprice', models.FloatField(max_length=10, unique=True, verbose_name='原价')),
                ('gdprice', models.FloatField(max_length=10, unique=True, verbose_name='折扣价')),
                ('gstock', models.IntegerField(max_length=10, unique=True, verbose_name='库存')),
                ('gimg', models.CharField(max_length=200, unique=True, verbose_name='商品图片')),
                ('pictureset', models.TextField(verbose_name='商品图片集')),
                ('gorder', models.IntegerField(max_length=5, unique=True, verbose_name='商品排序')),
                ('gtype', models.IntegerField(max_length=1, unique=True, verbose_name='消费类型')),
                ('gstatus', models.IntegerField(max_length=1, unique=True, verbose_name='商品状态')),
                ('gvrebate', models.FloatField(max_length=10, verbose_name='VIP会员返现金额')),
                ('printid', models.CharField(max_length=32, unique=True, verbose_name='打印机ID')),
                ('isboutique', models.IntegerField(max_length=1, unique=True, verbose_name='是否精品')),
            ],
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]
