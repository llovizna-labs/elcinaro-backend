from siembras.models import Cultivo
from rest_framework import serializers
from seguimiento.models import ActividadesCultivo, Insumo, MEDIDAS, ACTIVIDADES, InsumoCultivo, \
	PlagasCultivo, CosechaCultivo, Plaga
from siembras.serializers.cultivo import CultivoSerializer as SiembrasCultivoSerializer, ProovedorSerializer, \
	LoteSiembraSerializer


class CultivoSerializer(serializers.ModelSerializer):
	cultivo_lote = serializers.SerializerMethodField('_get_lote')

	cosecha_cultivo = serializers.StringRelatedField(many=True)

	class Meta:
		model = Cultivo
		fields = ('id', 'lote', 'cultivo_lote', 'cosecha_cultivo')

	def _get_lote(self, obj):
		serializer = LoteSiembraSerializer(obj.lote)
		return serializer.data


class PlagaSerializer(serializers.ModelSerializer):
	plaga_media = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Plaga
		fields = ('id', 'nombre', 'descripcion', 'created', 'updated', 'plaga_media')


class CosechaCultivoSerializer(serializers.ModelSerializer):
	cultivo_cosecha = serializers.SerializerMethodField('_get_cosecha')

	class Meta:
		model = CosechaCultivo
		fields = ('id', 'cultivo', 'cantidad', 'medida', 'fecha_cosecha', 'cultivo_cosecha',)

	def _get_cosecha(self, obj):
		serializer = CultivoSerializer(obj.cultivo)
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


class InsumoSerializer(serializers.ModelSerializer):
	medida = serializers.ChoiceField(choices=MEDIDAS, default='l')
	insumo_proovedor = serializers.SerializerMethodField('_get_proovedor')

	class Meta:
		model = Insumo
		read_only_fields = ('updated',)
		fields = ('id', 'nombre', 'codigo', 'cantidad', 'medida', 'proovedor', 'insumo_proovedor', 'updated')

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
