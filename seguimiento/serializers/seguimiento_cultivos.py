from siembras.models import Cultivo
from rest_framework import serializers
from seguimiento.models import ActividadesCultivo, Insumo, MEDIDAS, ACTIVIDADES, InsumoCultivo, \
	PlagasCultivo, CosechaCultivo, Plaga, CrecimientoCultivo
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


class CosechaCultivoSerializer(serializers.ModelSerializer):
	cultivo_cosecha = serializers.SerializerMethodField('_get_cosecha')
	observaciones = serializers.SerializerMethodField('_get_observacion')
	cultivo_name = serializers.SerializerMethodField('_get_cultivo')

	class Meta:
		model = CosechaCultivo
		fields = ('id', 'cultivo', 'cantidad', 'medida', 'fecha_cosecha', 'cultivo_cosecha','observaciones', 'cultivo_name')

	def _get_cosecha(self, obj):
		serializer = CultivoSerializer(obj.cultivo)
		return serializer.data

	def _get_observacion(self, obj):
		return 'Se Cosecharon  %d' % (obj.cantidad,)

	def _get_cultivo(self, obj):
		return '%s (%s)' % (obj.cultivo.lote.semilla_utilizada.descripcion, obj.cultivo.get_ubicacion())


class PlagasCultivoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlagasCultivo
		fields = ('cultivo', 'plaga')


class InsumoCultivoSerializer(serializers.ModelSerializer):
	medida = serializers.ChoiceField(choices=MEDIDAS, default='l')
	observaciones = serializers.SerializerMethodField('_get_observacion')
	cultivo_name = serializers.SerializerMethodField('_get_cultivo')

	class Meta:
		model = InsumoCultivo
		fields = ('cultivo_name', 'cultivo', 'insumo', 'fecha_aplicacion', 'cantidad', 'medida', 'observaciones')

	def _get_observacion(self, obj):
		return 'Se aplico el Insumo %s' % (obj.insumo.nombre,)

	def _get_cultivo(self, obj):
		return '%s (%s)' % (obj.cultivo.lote.semilla_utilizada.descripcion, obj.cultivo.get_ubicacion())


class CrecimientoCultivoSerializer(serializers.ModelSerializer):
	# observaciones = serializers.SerializerMethodField('_get_observacion')
	cultivo_name = serializers.SerializerMethodField('_get_cultivo')

	class Meta:
		model = CrecimientoCultivo
		fields = ('__all__')

	def _get_cultivo(self, obj):
		return '%s (%s) (Muestra %s)' % (obj.muestra_cultivo.cultivo.lote.semilla_utilizada.descripcion, obj.muestra_cultivo.cultivo.get_ubicacion(), obj.muestra_cultivo.codigo)


class ActividadesCultivoSerializer(serializers.ModelSerializer):
	cultivo_name = serializers.SerializerMethodField('_get_cultivo')

	class Meta:
		model = ActividadesCultivo
		fields = (
			'id', 'cultivo', 'actividad', 'observaciones', 'fecha_realizacion', 'cultivo_name')

	def _get_cultivo(self, obj):
		return '%s (%s)' % (obj.cultivo.lote.semilla_utilizada.descripcion, obj.cultivo.get_ubicacion())
