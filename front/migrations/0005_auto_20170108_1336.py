# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-08 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20170108_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='bill',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='description',
            name='length',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='description',
            name='quality',
            field=models.CharField(default='custom', max_length=200),
        ),
        migrations.AlterField(
            model_name='description',
            name='rate',
            field=models.CharField(max_length=200),
        ),
    ]
