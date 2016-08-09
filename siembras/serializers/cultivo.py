from rest_framework import serializers
from siembras.models import Cultivo, Parcela, Invernadero, LoteSiembra
from seguimiento.serializers.muestra import CultivoMuestraSerializer


class CultivoSerializer(serializers.ModelSerializer):
	muestras = CultivoMuestraSerializer(many=True, read_only=True)

	class Meta:
		model = Cultivo
		fields = ('id', 'codigo', 'fecha_siembra', 'lote', 'invernadero', 'parcela', 'posicion_inicial', 'posicion_final', 'densidad_siembra', 'muestras')


class ParcelaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Parcela
		fields = ('id', 'tipo', 'ubicacion')


class InvernaderoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Invernadero
		fields = ('id', 'ubicacion', 'capacidad')


class LoteSiembraSerializer(serializers.ModelSerializer):

	class Meta:
		model = LoteSiembra
		fields = ('id', 'semilla_utilizada', 'cantidad', 'fecha_enviado', 'fecha_recibido', 'germinado', 'proovedor')