# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-09-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_auto_20160927_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hornet',
            name='name',
            field=models.CharField(default='New test post Individual', max_length=200),
        ),
        migrations.AlterField(
            model_name='hornetnode',
            name='name',
            field=models.CharField(default='New test post NODE', max_length=200),
        ),
    ]
