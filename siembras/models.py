from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import qrcode
import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.


class Categoria(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return '%s ' % self.nombre

	def __unicode__(self):
		return '%s ' % self.nombre


class Rubro(models.Model):
	nombre = models.CharField(max_length=255, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s ' % self.nombre

	def __unicode__(self):
		return '%s ' % self.nombre


class RubroImagen(models.Model):
	rubro = models.ForeignKey(Rubro, related_name='rubro_media')
	imagen = models.URLField(max_length=2000)


class Proovedor(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255, blank=True)
	telefono = models.CharField(max_length=255, blank=True)
	direccion = models.CharField(max_length=255, blank=True)
	categoria = models.ForeignKey(Categoria, related_name='proovedor_categoria')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s ' % self.nombre

	def __unicode__(self):
		return '%s ' % self.nombre

	class Meta:
		verbose_name_plural = "Proovedores"


class Semilla(models.Model):
	MEDIDAS = (
		(1, 'grs'),
		(2, 'unidad'),
	)

	familia = models.ForeignKey(Rubro)
	proovedor = models.ForeignKey(Proovedor)
	descripcion = models.CharField(max_length=255, default='nombre comercial semilla')
	fecha_compra = models.DateField()
	precio_compra = models.FloatField(default=0.0)
	cantidad = models.FloatField(default=0.0)
	unidad = models.IntegerField(default=1, choices=MEDIDAS)
	codigo = models.CharField(max_length=255, blank=True)
	nivel_germinacion = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1)])
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s - %s - %s' % (self.familia.nombre, self.proovedor.nombre, self.descripcion)

	def __unicode__(self):
		return '%s - %s - %s' % (self.familia.nombre, self.proovedor.nombre, self.descripcion)


class TipoParcela(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)

	def __str__(self):
		return '%s ' % self.nombre

	def __unicode__(self):
		return '%s ' % self.nombre


class Parcela(models.Model):
	ubicacion = models.CharField(max_length=255)
	codigo = models.CharField(max_length=255)
	tipo = models.ForeignKey(TipoParcela)
	largo_medida = models.FloatField(default=1.0)
	ancho_medida = models.FloatField(default=2.0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s ' % self.codigo

	def __unicode__(self):
		return '%s ' % self.codigo

	def _get_name(self):
		return '%s %s' % (self.codigo, self.ubicacion)


class Invernadero(models.Model):
	nombre = models.CharField(max_length=255)
	ubicacion = models.CharField(max_length=255, blank=True)
	codigo = models.CharField(max_length=255, unique=True)
	capacidad = models.IntegerField(default=500)

	def __str__(self):
		return '%s ' % self.codigo

	def __unicode__(self):
		return '%s ' % self.codigo

	def _get_name(self):
		return '%s - %s' % (self.codigo, self.ubicacion)


class LoteSiembra(models.Model):
	semilla_utilizada = models.ForeignKey(Semilla)
	cantidad_semillas_enviadas = models.FloatField(default=0.0)
	cantidad_semillas_recibidas = models.FloatField(default=0.0)
	fecha_enviado = models.DateField(blank=True, null=True)
	fecha_recibido = models.DateField(blank=True, null=True)
	proovedor = models.ForeignKey(Proovedor, blank=True, null=True)
	germinado = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.semilla_utilizada.descripcion)

	def __unicode__(self):
		return '%s' % (self.semilla_utilizada.descripcion)

	class Meta:
		verbose_name_plural = "Lotes de Siembra"


class Cultivo(models.Model):
	codigo = models.CharField(max_length=255)
	lote = models.ForeignKey(LoteSiembra)
	invernadero = models.ForeignKey(Invernadero, blank=True, null=True, related_name='cultivos_invernadero')
	parcela = models.ForeignKey(Parcela, blank=True, null=True, related_name='cultivos_parcela')
	fecha_siembra = models.DateField(blank=True, null=True)
	posicion_inicial = models.IntegerField()
	posicion_final = models.IntegerField()
	densidad_siembra = models.FloatField()
	qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def plantas_sembradas(self):
		count = self.posicion_final - self.posicion_inicial
		return count

	def __str__(self):
		return '%s - %s' % (self.lote.__str__(), self.codigo)

	def __unicode__(self):
		return '%s - %s' % (self.lote.__unicode__(), self.codigo)

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
		filename = 'cultivo-%s.png' % (self.id)
		filebuffer = InMemoryUploadedFile(
			buffer, None, filename, 'image/png', buffer.len, None)
		self.qrcode.save(filename, filebuffer)
