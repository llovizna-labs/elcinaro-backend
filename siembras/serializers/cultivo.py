from rest_framework import serializers
from siembras.models import RubroImagen, Rubro, Cultivo, Parcela, Invernadero, LoteSiembra, Semilla, Proovedor, \
	Categoria, TipoParcela, SemillaLote
from seguimiento.serializers.muestra import CultivoMuestraSerializer


class TipoParcelaSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'nombre', 'descripcion')
		model = TipoParcela


class RubroImagenSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'imagen', 'rubro')
		model = RubroImagen


class RubroSerializer(serializers.ModelSerializer):
	rubro_media = RubroImagenSerializer(many=True, read_only=True)

	#cultivos_count = serializers.SerializerMethodField()
	#semillas_count = serializers.SerializerMethodField()
	#lotes_count = serializers.SerializerMethodField()

	class Meta:
		fields = ('id', 'nombre', 'rubro_media', 'updated')
		model = Rubro
		read_only_fields = ('rubro_media',)

	def get_semillas_count(self, obj):
		return Semilla.objects.filter(familia_id=obj.pk).count()



class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'nombre', 'descripcion')
		model = Categoria


class ProovedorSerializer(serializers.ModelSerializer):
	proovedor_categoria = serializers.SerializerMethodField('_get_categoria')

	class Meta:
		fields = ('id', 'nombre', 'descripcion', 'telefono', 'direccion', 'categoria', 'created', 'updated',
		          'proovedor_categoria')
		model = Proovedor

	def _get_categoria(self, obj):
		serializer = CategoriaSerializer(obj.categoria)
		return serializer.data


class SemillaSerializer(serializers.ModelSerializer):
	#cultivos_count = serializers.SerializerMethodField()
	semilla_proovedor = serializers.SerializerMethodField('_get_proovedor')
	semilla_familia = serializers.SerializerMethodField('_get_rubro')
	nombre = serializers.SerializerMethodField('_get_semilla')

	class Meta:
		fields = ('id', 'nombre', 'familia', 'proovedor', 'descripcion', 'cantidad', 'unidad', 'codigo', 'fecha_compra',
		          'nivel_germinacion', 'created', 'updated', 'semilla_proovedor', 'semilla_familia',
		          'created', 'updated')
		model = Semilla
		read_only_fields = ()


	def _get_proovedor(self, obj):
		serializer = ProovedorSerializer(obj.proovedor)
		return serializer.data

	def _get_rubro(self, obj):
		serializer = RubroSerializer(obj.familia)
		return serializer.data

	def _get_semilla(self, obj):
		return '%s' % (obj.descripcion)


class SemillaLoteSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = SemillaLote

class LoteSiembraSerializer(serializers.ModelSerializer):
	rubro_lote = serializers.SerializerMethodField('_get_rubro')
	semilla_lote = SemillaLoteSerializer(many=True, read_only=True)
	class Meta:
		model = LoteSiembra
		fields = ('id', 'codigo',  'rubro', 'rubro_lote', 'fecha_enviado', 'created', 'updated', 'semilla_lote')

	def _get_cultivos_count(self, obj):
		return Cultivo.objects.filter(lote=obj.pk).count()

	def _get_proovedor(self, obj):
		return ProovedorSerializer(obj.proovedor).data

	def _get_rubro(self, obj):
		return obj.rubro.__unicode__()


class CultivoSerializer(serializers.ModelSerializer):
	muestras = CultivoMuestraSerializer(many=True, read_only=True)
	cultivo_lote = serializers.SerializerMethodField('_get_lote')
	area_siembra = serializers.SerializerMethodField('_get_area_siembra')
	cosecha_cultivo = serializers.StringRelatedField(many=True, read_only=True)
	nombre = serializers.SerializerMethodField('_get_name')

	class Meta:
		model = Cultivo
		fields = (
			'id', 'nombre', 'codigo', 'fecha_siembra', 'lote', 'parcela', 'invernadero', 'area_siembra',
			'posicion_inicial', 'posicion_final',
			'densidad_siembra', 'muestras', 'cultivo_lote', 'cosecha_cultivo', 'created', 'updated')

	def _get_name(self, obj):
		return '(%s) %s -  %s' % (
			obj.codigo, obj.lote.semilla_utilizada.descripcion, self._get_area_siembra(obj)['codigo'])

	def _get_lote(self, obj):
		serializer = LoteSiembraSerializer(obj.lote)
		return serializer.data

	def _get_area_siembra(self, obj):
		if obj.parcela is not None:
			serializer = ParcelaSerializer(obj.parcela)
		else:
			serializer = InvernaderoSerializer(obj.invernadero)
		return serializer.data


class ParcelaSerializer(serializers.ModelSerializer):
	# cultivos= CultivoSerializer(many=True, read_only=True)
	# tipo = TipoParcelaSerializer(read_only=True)
	cultivos_count = serializers.SerializerMethodField()
	nombre = serializers.ReadOnlyField(source='_get_name')
	type = serializers.SerializerMethodField('_get_type')

	class Meta:
		model = Parcela
		fields = (
			'id', 'nombre', 'type', 'codigo', 'tipo', 'ubicacion', 'largo_medida', 'ancho_medida', 'cultivos_count')
		read_only_fields = ('cultivos_count',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(parcela=obj.pk).count()

	def _get_type(self, obj):
		return 'parcela'


class InvernaderoSerializer(serializers.ModelSerializer):
	# cultivos_invernadero = CultivoSerializer(many=True, read_only=True)
	cultivos_count = serializers.SerializerMethodField()
	nombre = serializers.ReadOnlyField(source='_get_name')
	type = serializers.SerializerMethodField('_get_type')

	class Meta:
		model = Invernadero
		fields = ('id', 'nombre', 'type', 'codigo', 'ubicacion', 'capacidad', 'cultivos_count')
		read_only_fields = ('cultivos_count',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(invernadero=obj.pk).count()

	def _get_type(self, obj):
		return 'invernadero'
