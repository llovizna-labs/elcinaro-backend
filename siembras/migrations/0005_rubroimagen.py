# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-03 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0004_auto_20160827_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='RubroImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.URLField(max_length=2000)),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siembras.Rubro')),
            ],
        ),
    ]
