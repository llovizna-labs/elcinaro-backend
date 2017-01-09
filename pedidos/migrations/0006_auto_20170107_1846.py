# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-07 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20160802_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 7, 18, 46, 7, 815898, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 1, 7, 18, 46, 16, 17399, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
