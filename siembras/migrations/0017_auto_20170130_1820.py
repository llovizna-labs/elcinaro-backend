# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-30 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0016_auto_20170130_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semillalote',
            name='fecha_enviado',
        ),
        migrations.AddField(
            model_name='lotesiembra',
            name='fecha_enviado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
