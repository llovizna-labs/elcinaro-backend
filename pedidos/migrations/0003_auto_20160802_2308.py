# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-02 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20160802_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='anulado',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='unidad',
            field=models.IntegerField(choices=[(1, 'gr'), (2, 'Kg'), (3, 'L'), (4, 'mg'), (5, 'ml'), (6, 'unidades')], default=2),
        ),
    ]
