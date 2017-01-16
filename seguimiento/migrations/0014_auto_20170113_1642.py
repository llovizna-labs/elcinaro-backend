# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-13 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0013_auto_20170111_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlagaImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.URLField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='actividadescultivo',
            name='cosecha',
        ),
        migrations.RemoveField(
            model_name='actividadescultivo',
            name='crecimiento',
        ),
        migrations.RemoveField(
            model_name='actividadescultivo',
            name='insumo',
        ),
        migrations.RemoveField(
            model_name='plaga',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='actividadescultivo',
            name='actividad',
            field=models.IntegerField(choices=[(1, 'Desmalezamiento'), (2, 'Riego'), (3, 'Observaciones'), (4, 'Limpieza')], default=1),
        ),
        migrations.AlterField(
            model_name='actividadescultivo',
            name='fecha_realizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insumocultivo',
            name='fecha_aplicacion',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='plagaimagen',
            name='plaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plaga_media', to='seguimiento.Plaga'),
        ),
    ]
