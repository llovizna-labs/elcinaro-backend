# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-10 19:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0012_auto_20170110_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubro',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 10, 19, 50, 17, 808545, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rubro',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 1, 10, 19, 50, 21, 247938, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
