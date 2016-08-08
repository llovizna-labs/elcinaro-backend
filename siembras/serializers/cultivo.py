from rest_framework import serializers
from siembras.models import Cultivo
from seguimiento.serializers.muestra import CultivoMuestraSerializer


class CultivoSerializer(serializers.ModelSerializer):
	muestras = CultivoMuestraSerializer(many=True, read_only=True)

	class Meta:
		model = Cultivo
		fields = ('id', 'codigo', 'fecha_siembra', 'lote', 'invernadero', 'parcela', 'posicion_inicial', 'posicion_final', 'densidad_siembra', 'muestras')
