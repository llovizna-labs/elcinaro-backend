# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-01 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0007_auto_20160801_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotesiembra',
            name='proovedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siembras.Proovedor'),
        ),
    ]
