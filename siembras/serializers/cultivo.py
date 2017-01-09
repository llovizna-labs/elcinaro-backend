from rest_framework import serializers
from siembras.models import RubroImagen, Rubro, Cultivo, Parcela, Invernadero, LoteSiembra, Semilla, Proovedor, \
	Categoria
from seguimiento.serializers.muestra import CultivoMuestraSerializer

import moment

class RubroImagenSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'imagen', 'rubro')
		model = RubroImagen

class RubroSerializer(serializers.ModelSerializer):
	rubro_media = RubroImagenSerializer(many=True, read_only=True)
	class Meta:
		fields = ('id', 'nombre', 'rubro_media')
		model = Rubro


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'nombre', 'descripcion')
		model = Categoria


class ProovedorSerializer(serializers.ModelSerializer):
	#categoria = CategoriaSerializer()
	class Meta:
		fields = ('id', 'nombre', 'descripcion', 'telefono', 'direccion', 'categoria', 'created', 'updated')
		model = Proovedor


class SemillaSerializer(serializers.ModelSerializer):
	#familia = RubroSerializer()
	#proovedor = ProovedorSerializer()

	class Meta:
		fields = ('id', 'familia', 'proovedor', 'descripcion', 'cantidad', 'unidad', 'codigo', 'fecha_compra', 'nivel_germinacion', 'created', 'updated')
		model = Semilla
	
class LoteSiembraSerializer(serializers.ModelSerializer):
	semilla_utilizada = SemillaSerializer(read_only=True)
	class Meta:
		model = LoteSiembra
		fields = ('id', 'semilla_utilizada', 'cantidad_semillas_enviadas', 'cantidad_semillas_recibidas', 'fecha_enviado', 'fecha_recibido', 'germinado', 'proovedor')


class CultivoSerializer(serializers.ModelSerializer):
	muestras = CultivoMuestraSerializer(many=True, read_only=True)
	lote = LoteSiembraSerializer(read_only=True)
	class Meta:
		model = Cultivo
		fields = ('id', 'codigo', 'fecha_siembra', 'lote', 'invernadero', 'parcela', 'posicion_inicial', 'posicion_final', 'densidad_siembra', 'muestras')


class ParcelaSerializer(serializers.ModelSerializer):
	cultivos= CultivoSerializer(many=True, read_only=True)
	class Meta:
		model = Parcela
		fields = ('id', 'tipo', 'ubicacion', 'cultivos')


class InvernaderoSerializer(serializers.ModelSerializer):
	cultivos_invernadero = CultivoSerializer(many=True, read_only=True)
	class Meta:
		model = Invernadero
		fields = ('id', 'ubicacion', 'capacidad', 'cultivos_invernadero')
