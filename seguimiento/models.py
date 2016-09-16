from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey

from django.db import models
from siembras.models import Cultivo, Proovedor

import qrcode
import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.


MEDIDAS = (
    (1, 'cm'),
    (2, 'mm'),
    (3, 'ml'),
    (4, 'l'),
    (5, 'Kg'),
    (6, 'mg'),
)

ACTIVIDADES = (
    (1, 'Desmalezamiento'),
    (2, 'Riego'),
    (3, 'Fertilizacion'),
    (4, 'Plaguicida'),
    (5, 'Limpieza'),
)


class Insumo(models.Model):
	nombre = models.CharField(max_length=255)
	codigo = models.CharField(max_length=255, blank=True)
	proovedor = models.ForeignKey(Proovedor)
	cantidad = models.FloatField(default=0.0)
	medida = models.IntegerField(choices=MEDIDAS, default=5)
	def __str__(self):
			return '%s' % self.nombre

	def __unicode__(self):
			return '%s' % self.nombre

class Plaga(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField(max_length=255)
	imagen = models.CharField(max_length=255)



class PlagasCultivo(models.Model):
	fecha_aparacion = models.DateField()
	plaga = models.ForeignKey(Plaga)
	imagen = models.CharField(max_length=255)
	cultivo = models.ForeignKey(Cultivo)



class CosechaCultivo(models.Model):
	cultivo = models.ForeignKey(Cultivo)
	fecha_cosecha = models.DateField(blank=True)
	cantidad = models.FloatField(default=0.0)
	medida = models.IntegerField(choices=MEDIDAS, default=5)



class InsumoCultivo(models.Model):
	MEDIDAS = (
        (1, 'cm'),
        (2, 'mm'),
	    (3, 'ml'),
	    (4, 'l'),
	    (5, 'Kg'),
	    (6, 'mg'),
	)

	fecha_aplicacion = models.DateField()
	insumo = models.ForeignKey(Insumo)
	observaciones = models.TextField()
	cultivo = models.ForeignKey(Cultivo)
	cantidad = models.FloatField(default=0.0)
	medida = models.IntegerField(choices=MEDIDAS, default=5)

	def __str__(self):
			return '%s - %s' % (self.insumo.nombre,self.cultivo.__str__())

	def __unicode__(self):
			return '%s - %s' % (self.insumo.nombre, self.cultivo.__unicode__())


class ActividadesCultivo(models.Model):
	ACTIVIDADES = (
        (1, 'Desmalezamiento'),
        (2, 'Riego'),
        (3, 'Fertilizacion'),
	    (4, 'Plaguicida'),
	    (5, 'Limpieza'),
	)

	cultivo = models.ForeignKey(Cultivo, related_name='actividades')
	fecha_realizacion = models.DateTimeField()
	actividad = models.IntegerField(default=1, choices=ACTIVIDADES)
	observaciones = models.TextField(blank=True)
	crecimiento = models.ForeignKey(CrecimientoCultivo, null=True, blank=True)
	cosecha = models.ForeignKey(CosechaCultivo, null=True, blank=True)
	insumo = models.ForeignKey(InsumoCultivo, null=True, blank=True)


	def __str__(self):
			return '%s ' % self.cultivo.codigo

	def __unicode__(self):
			return '%s ' % self.cultivo.codigo





class CultivoMuestra(models.Model):
	codigo = models.CharField(max_length=255)
	ubicacion = models.CharField(max_length=255)
	cultivo = models.ForeignKey(Cultivo, related_name='muestras')
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

	muestra_cultivo = models.ForeignKey(CultivoMuestra, related_name='crecimiento_muestra')
	medida = models.FloatField(default=0.0)
	unidad = models.IntegerField(default=1, choices=MEDIDAS)
	fecha_registro = models.DateField(auto_now=True)
	observaciones = models.TextField(max_length=255)
	qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

	def generate_qrcode(self):

		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=6,
			border=0,
		)
		qr.add_data(self.pk)
		qr.make(fit=True)

		img = qr.make_image()

		buffer = StringIO.StringIO()
		img.save(buffer)
		filename = 'cultivo-muestra-%s.png' % (self.id)
		filebuffer = InMemoryUploadedFile(
			buffer, None, filename, 'image/png', buffer.len, None)
		self.qrcode.save(filename, filebuffer)

