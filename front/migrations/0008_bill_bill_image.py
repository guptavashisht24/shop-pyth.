# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0007_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_image',
            field=models.ImageField(default='/media/2016.jpg', upload_to='/media/'),
        ),
    ]