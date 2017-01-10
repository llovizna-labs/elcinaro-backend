from siembras.models import Cultivo

__author__ = 'ronsuez'
from rest_framework import serializers
from seguimiento.models import ActividadesCultivo, Insumo, MEDIDAS, ACTIVIDADES, InsumoCultivo, \
	PlagasCultivo, CosechaCultivo
from siembras.serializers.cultivo import CultivoSerializer as SiembrasCultivoSerializer

class CultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cultivo
		fields = ('id', 'lote')


class PlagasCultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlagasCultivo
		fields = ('cultivo', 'plaga')


class InsumoCultivoSerializer(serializers.ModelSerializer):
	medida = serializers.ChoiceField(choices=MEDIDAS, default='l')

	class Meta:
		model = InsumoCultivo
		fields = ('cultivo', 'insumo', 'fecha_aplicacion', 'cantidad', 'medida')


class CosechaCultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = CosechaCultivo
		fields = ('cultivo', 'fecha_cosecha', 'cantidad', 'medida')

class InsumoSerializer(serializers.ModelSerializer):
	medida = serializers.ChoiceField(choices=MEDIDAS, default='l')
	class Meta:
		model = Insumo
		fields = ('id', 'nombre', 'cantidad', 'medida', 'proovedor', 'updated')


class ActividadesSerializer(serializers.ModelSerializer):
	cosecha = CosechaCultivoSerializer(allow_null=True)
	insumo = InsumoCultivoSerializer(allow_null=True)
	cultivo = CultivoSerializer()

	class Meta:
		model = ActividadesCultivo
		fields = ('id', 'cultivo', 'actividad', 'observaciones', 'fecha_realizacion', 'cosecha', 'insumo', 'crecimiento')

	# def create(self, validated_data):
	# 	insumo = validated_data.pop('insumo')
	#
	# 	actividad =


class ActividadesCultivoSerializer(serializers.ModelSerializer):
	cultivo = SiembrasCultivoSerializer()
	class Meta:
		model = ActividadesCultivo
		fields = ('id', 'cultivo', 'actividad', 'observaciones', 'fecha_realizacion', 'cosecha', 'insumo', 'crecimiento')

