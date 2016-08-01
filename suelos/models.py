from __future__ import unicode_literals

from django.db import models
from siembras.models import Invernadero, Parcela
# Create your models here.


class MuestraSuelo(models.Model):
	codigo = models.CharField(max_length=255)
	ubicacion = models.CharField(max_length=255)
	fecha_registro = models.DateField(auto_now_add=True)
	parcela = models.ForeignKey(Parcela, null=True, blank=True)
	invernadero = models.ForeignKey(Invernadero, null=True, blank=True)

	def __str__(self):
			return 'Muestra %s' % self.ubicacion

	def __unicode__(self):
			return 'Muestra %s' % self.ubicacion

	class Meta:
		verbose_name_plural = "Muestras"


class AnalisisSuelo(models.Model):
	codigo = models.CharField(max_length=255)
	muestra = models.ForeignKey(MuestraSuelo)
	fecha_registro = models.DateField(auto_now_add=True)
	fecha_aplicacion = models.DateField()

	def __str__(self):
			return '%s - %s' % (self.codigo, self.muestra.ubicacion)

	def __unicode__(self):
			return '%s - %s' % (self.codigo, self.muestra.ubicacion)

	class Meta:
		verbose_name_plural = "Analisis"