__author__ = 'ronsuez'
from rest_framework import serializers
from seguimiento.models import SeguimientoCultivo, ActividadesCultivo


class SeguimientoCultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SeguimientoCultivo
		fields = ('id', 'cultivo', 'observaciones', 'fecha_registro')


class ActividadesCultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActividadesCultivo
		fields = ('id', 'fecha_realizacion', 'actividad', 'observacion', 'cultivo')



