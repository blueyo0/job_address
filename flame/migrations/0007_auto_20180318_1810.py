# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-18 18:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flame', '0006_auto_20180318_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpositionssearchweb',
            name='search_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='search time'),
        ),
    ]