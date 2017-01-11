from siembras.models import Cultivo
from rest_framework import serializers
from seguimiento.models import ActividadesCultivo, Insumo, MEDIDAS, ACTIVIDADES, InsumoCultivo, \
	PlagasCultivo, CosechaCultivo
from siembras.serializers.cultivo import CultivoSerializer as SiembrasCultivoSerializer, ProovedorSerializer, \
	LoteSiembraSerializer


class CultivoSerializer(serializers.ModelSerializer):

	cultivo_lote = serializers.SerializerMethodField('_get_lote')

	class Meta:
		model = Cultivo
		fields = ('id', 'lote', 'cultivo_lote')

	def _get_lote(self, obj):
		serializer = LoteSiembraSerializer(obj.lote)
		return serializer.data

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
	insumo_proovedor = serializers.SerializerMethodField('_get_proovedor')

	class Meta:
		model = Insumo
		read_only_fields = ('updated',)
		fields = ('id', 'nombre', 'codigo', 'cantidad', 'medida', 'proovedor',  'insumo_proovedor', 'updated')

	def _get_proovedor(self, obj):
		serializer = ProovedorSerializer(obj.proovedor)
		return serializer.data


class ActividadesSerializer(serializers.ModelSerializer):
	cosecha = CosechaCultivoSerializer(allow_null=True)
	insumo = InsumoCultivoSerializer(allow_null=True)
	cultivo = CultivoSerializer()

	class Meta:
		model = ActividadesCultivo
		fields = (
			'id', 'cultivo', 'actividad', 'observaciones', 'fecha_realizacion', 'cosecha', 'insumo', 'crecimiento')




class ActividadesCultivoSerializer(serializers.ModelSerializer):
	# cultivo = SiembrasCultivoSerializer()
	# cosecha = CosechaCultivoSerializer(allow_null=True)
	# insumo = InsumoCultivoSerializer(allow_null=True)

	class Meta:
		model = ActividadesCultivo
		fields = (
			'id', 'cultivo', 'actividad', 'observaciones', 'fecha_realizacion')
