from __future__ import unicode_literals

from django.db import models

from django.core.validators import RegexValidator

from django.utils import timezone

from siembras.models import Rubro
# Create your models here.
#
class Cliente(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	direccion = models.TextField(default='Merida')
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
	                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	telefono = models.CharField(validators=[phone_regex], blank=True, max_length=16)  # validators should be a list
	email = models.EmailField(blank=True)
	identification = models.CharField(max_length=100, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.apellido)


class Factura(models.Model):
	nro_factura = models.IntegerField(help_text='Numero de Factura')
	fecha = models.DateField(help_text='Format YYYY-mm-dd', blank=True)
	cliente = models.ForeignKey(Cliente, null=True, blank=True)
	anulado = models.BooleanField(default=0)

	def __str__(self):
		return 'Factura %s' % (self.nro_factura)

	def __unicode__(self):
		return 'Factura %s' % (self.nro_factura)


class DetalleFactura(models.Model):
	MEDIDAS = (
		(1, 'gr'),
		(2, 'Kg'),
		(3, 'L'),
		(4, 'mg'),
		(5, 'ml'),
	    (6, 'unidades'),
	)
	rubro = models.ForeignKey(Rubro)
	cantidad = models.FloatField()
	unidad = models.IntegerField(default=2, choices=MEDIDAS)
	precio_unitario = models.FloatField(default=0.0)
	factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
