from rest_framework import serializers
from siembras.models import RubroImagen, Rubro, Cultivo, Parcela, Invernadero, LoteSiembra, Semilla, Proovedor, \
	Categoria, TipoParcela
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

	cultivos_count = serializers.SerializerMethodField()
	semillas_count = serializers.SerializerMethodField()
	lotes_count = serializers.SerializerMethodField()

	class Meta:
		fields = ('id', 'nombre', 'rubro_media', 'updated', 'cultivos_count', 'semillas_count', 'lotes_count')
		model = Rubro
		read_only_fields = ('rubro_media',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(lote__semilla_utilizada__familia_id=obj.pk).count()

	def get_semillas_count(self, obj):
		return Semilla.objects.filter(familia_id=obj.pk).count()

	def get_lotes_count(self, obj):
		return LoteSiembra.objects.filter(semilla_utilizada__familia_id=obj.pk).count()


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
	cultivos_count = serializers.SerializerMethodField()
	semilla_proovedor = serializers.SerializerMethodField('_get_proovedor')
	semilla_familia = serializers.SerializerMethodField('_get_rubro')

	class Meta:
		fields = ('id', 'familia', 'proovedor', 'descripcion', 'cantidad', 'unidad', 'codigo', 'fecha_compra',
		          'nivel_germinacion', 'created', 'updated', 'cultivos_count', 'semilla_proovedor', 'semilla_familia')
		model = Semilla
		read_only_fields = ('cultivos_count',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(lote__semilla_utilizada=obj.pk).count()

	def _get_proovedor(self, obj):
		serializer = ProovedorSerializer(obj.proovedor)
		return serializer.data

	def _get_rubro(self, obj):
		serializer = RubroSerializer(obj.familia)
		return serializer.data


class LoteSiembraSerializer(serializers.ModelSerializer):
	semilla_utilizada = SemillaSerializer(read_only=True)

	class Meta:
		model = LoteSiembra
		fields = (
			'id', 'semilla_utilizada', 'cantidad_semillas_enviadas', 'cantidad_semillas_recibidas', 'fecha_enviado',
			'fecha_recibido', 'germinado', 'proovedor')


class CultivoSerializer(serializers.ModelSerializer):
	muestras = CultivoMuestraSerializer(many=True, read_only=True)
	cultivo_lote = serializers.SerializerMethodField('_get_lote')
	area_siembra = serializers.SerializerMethodField('_get_area_siembra')

	class Meta:
		model = Cultivo
		fields = (
			'id', 'codigo', 'fecha_siembra', 'lote', 'area_siembra', 'posicion_inicial', 'posicion_final',
			'densidad_siembra', 'muestras', 'cultivo_lote')

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

	class Meta:
		model = Parcela
		fields = ('id', 'codigo', 'tipo', 'ubicacion', 'largo_medida', 'ancho_medida', 'cultivos_count')
		read_only_fields = ('cultivos_count',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(parcela=obj.pk).count()


class InvernaderoSerializer(serializers.ModelSerializer):
	# cultivos_invernadero = CultivoSerializer(many=True, read_only=True)

	cultivos_count = serializers.SerializerMethodField()

	class Meta:
		model = Invernadero
		fields = ('id', 'nombre', 'codigo', 'ubicacion', 'capacidad', 'cultivos_count')
		read_only_fields = ('cultivos_count',)

	def get_cultivos_count(self, obj):
		return Cultivo.objects.filter(invernadero=obj.pk).count()
