from __future__ import unicode_literals

from django.db import models
from siembras.models import Cultivo, Proovedor
# Create your models here.


class SeguimientoCultivo(models.Model):
	cultivo = models.ForeignKey(Cultivo)
	observaciones = models.TextField()
	fecha_registro = models.DateField(auto_now_add=True)

	def __str__(self):
			return '%s ' % self.cultivo.codigo

	def __unicode__(self):
			return '%s ' % self.cultivo.codigo


class ActividadesCultivo(models.Model):
	ACTIVIDADES = (
        (1, 'Desmalezamiento'),
        (2, 'Riego'),
        (3, 'Fertilizacion'),
	    (4, 'Plaguicida'),
	    (5, 'Limpieza'),
	)

	fecha_realizacion = models.DateTimeField()
	actividad = models.IntegerField(default=1, choices=ACTIVIDADES)
	observacion = models.TextField(blank=True)
	cultivo = models.ForeignKey(Cultivo)

	def __str__(self):
			return '%s ' % self.cultivo.codigo

	def __unicode__(self):
			return '%s ' % self.cultivo.codigo


class CultivoMuestra(models.Model):
	codigo = models.CharField(max_length=255)
	ubicacion = models.CharField(max_length=255)
	cultivo = models.ForeignKey(Cultivo)
	fecha_registro = models.DateField(auto_now_add=True)

	def __str__(self):
			return '%s - %s ' % (self.codigo, self.cultivo.codigo)

	def __unicode__(self):
			return '%s - %s ' % (self.codigo, self.cultivo.codigo)


class CrecimientoCultivo(models.Model):
	MEDIDAS = (
        (1, 'cm'),
        (2, 'mm'),
	)

	muestra_cultivo = models.ForeignKey(CultivoMuestra)
	medida = models.FloatField(default=0.0)
	unidad = models.IntegerField(default=1, choices=MEDIDAS)
	fecha_registro = models.DateField(auto_now=True)
	observaciones = models.TextField(max_length=255)


class Plaga(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(max_length=255)
	imagen = models.CharField(max_length=255)


class PlagasCultivo(models.Model):
	fecha_aparacion = models.DateField()
	plaga = models.ForeignKey(Plaga)
	imagen = models.CharField(max_length=255)


class Fertilizante(models.Model):
	nombre = models.CharField(max_length=255)
	codigo = models.CharField(max_length=255, blank=True)
	proovedor = models.ForeignKey(Proovedor)

	def __str__(self):
			return '%s' % self.nombre

	def __unicode__(self):
			return '%s' % self.nombre


class FertilizanteCultivo(models.Model):
	fecha_aplicacion = models.DateField()
	fertilizante = models.ForeignKey(Fertilizante)
	observaciones = models.TextField()
	cultivo = models.ForeignKey(Cultivo)

	def __str__(self):
			return '%s - %s' % (self.fertilizante.nombre,self.cultivo.__str__())

	def __unicode__(self):
			return '%s - %s' % (self.fertilizante.nombre, self.cultivo.__unicode__())
