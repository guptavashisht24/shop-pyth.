# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('party', models.CharField(default='none', max_length=200)),
                ('invoice', models.FloatField(max_length=200)),
                ('amount', models.FloatField(max_length=200)),
                ('bill_name', models.CharField(default='none', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(default='none', max_length=200)),
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(default='Suits', max_length=200)),
                ('bill', models.FloatField(max_length=200)),
                ('length', models.FloatField(max_length=200)),
                ('quality', models.CharField(default='custom', max_length=200)),
                ('rate', models.FloatField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=1000)),
                ('length', models.CharField(max_length=1000)),
                ('cust_id', models.BigIntegerField()),
            ],
        ),
    ]
