# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-26 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0014_auto_20170113_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotesiembra',
            name='codigo',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
