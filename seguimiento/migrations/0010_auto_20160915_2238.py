# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-15 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siembras', '0006_auto_20160915_2238'),
        ('seguimiento', '0009_auto_20160827_1441'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cosecha',
            new_name='CosechaCultivo',
        ),
        migrations.RenameField(
            model_name='actividadescultivo',
            old_name='observacion',
            new_name='observaciones',
        ),
        migrations.AddField(
            model_name='actividadescultivo',
            name='cosecha',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seguimiento.CosechaCultivo'),
        ),
        migrations.AddField(
            model_name='actividadescultivo',
            name='crecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siembras.Cultivo'),
        ),
        migrations.AddField(
            model_name='actividadescultivo',
            name='insumo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seguimiento.InsumoCultivo'),
        ),
        migrations.AddField(
            model_name='plagascultivo',
            name='cultivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='siembras.Cultivo'),
            preserve_default=False,
        ),
    ]
