from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import DjangoFilterBackend, OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin
from siembras.serializers.cultivo import CultivoSerializer, ParcelaSerializer, InvernaderoSerializer, \
	LoteSiembraSerializer, RubroSerializer, RubroImagenSerializer, SemillaSerializer, ProovedorSerializer, \
	CategoriaSerializer, TipoParcelaSerializer
from siembras.models import Cultivo, Parcela, Invernadero, LoteSiembra, Rubro, RubroImagen, Semilla, Proovedor, \
	Categoria, TipoParcela


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 100
	page_size_query_param = 'page_size'
	max_page_size = 1000


class RubroViewSet(viewsets.ModelViewSet):
	queryset = Rubro.objects.all()
	serializer_class = RubroSerializer
	model = Rubro
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	search_fields = ('nombre',)


class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer
	model = Categoria


class SemillaViewSet(viewsets.ModelViewSet):
	queryset = Semilla.objects.all()
	serializer_class = SemillaSerializer
	model = Semilla
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('familia__nombre', 'proovedor__nombre', 'nivel_germinacion', 'cantidad', 'created', 'updated',)
	search_fields = ('descripcion', 'familia__nombre', 'proovedor__nombre', 'nivel_germinacion', 'cantidad')


class RubroMediaViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = RubroImagen.objects.all()
	serializer_class = RubroImagenSerializer
	model = RubroImagen
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('name', 'created', 'updated',)


@permission_classes((IsAuthenticatedOrReadOnly,))
class CultivoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = Cultivo.objects.all()
	serializer_class = CultivoSerializer
	model = Cultivo
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	search_fields = ('lote__semilla_utilizada__familia__nombre',)
	ordering_fields = (
		'lote__id', 'lote__semilla_utilizada__familia__nombre', 'lote__semilla_utilizada__descripcion', 'fecha_siembra')


class TipoParcelaViewSet(generics.ListAPIView):
	queryset = TipoParcela.objects.all()
	serializer_class = TipoParcelaSerializer
	pagination_class = StandardResultsSetPagination
	model = TipoParcela


class ParcelaViewSet(viewsets.ModelViewSet):
	queryset = Parcela.objects.all()
	serializer_class = ParcelaSerializer
	model = Parcela


class InvernaderoViewSet(viewsets.ModelViewSet):
	queryset = Invernadero.objects.all()
	serializer_class = InvernaderoSerializer
	model = Parcela


class LoteSiembraViewSet(viewsets.ModelViewSet):
	queryset = LoteSiembra.objects.all()
	serializer_class = LoteSiembraSerializer
	model = LoteSiembra
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('familia__nombre', 'proovedor__nombre', 'nivel_germinacion', 'cantidad')
	search_fields = ('descripcion', 'familia__nombre', 'proovedor__nombre', 'nivel_germinacion', 'cantidad')




class ProovedorViewSet(viewsets.ModelViewSet):
	queryset = Proovedor.objects.all()
	serializer_class = ProovedorSerializer
	model = Proovedor
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('nombre', 'created', 'updated', 'categoria__nombre')
	search_fields = ('nombre',)
