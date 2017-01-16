__author__ = 'ronsuez'

from rest_framework.response import Response
from rest_framework_extensions.decorators import action
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.filters import DjangoFilterBackend, OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from seguimiento.serializers.seguimiento_cultivos import ActividadesCultivoSerializer, \
	InsumoSerializer, InsumoCultivoSerializer, ActividadesSerializer, PlagaSerializer, CosechaCultivoSerializer

from seguimiento.models import ActividadesCultivo, Insumo, InsumoCultivo, Plaga, CosechaCultivo


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 100
	page_size_query_param = 'page_size'
	max_page_size = 1000


@permission_classes((IsAuthenticatedOrReadOnly,))
class ActividadesCultivoViewSet(viewsets.ModelViewSet):
	queryset = ActividadesCultivo.objects.all()
	serializer_class = ActividadesCultivoSerializer
	model = ActividadesCultivo
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('fecha_realizacion', 'actividad')


# class ActividadesViewSet(viewsets.ModelViewSet):
# 	queryset = ActividadesCultivo.objects.all()
# 	serializer_class = ActividadesCultivoSerializer
# 	model = ActividadesCultivo
# 	pagination_class = StandardResultsSetPagination
# 	filter_backends = (OrderingFilter, SearchFilter)
# 	ordering_fields = ('fecha_realizacion', 'actividad')


class InsumoViewSet(viewsets.ModelViewSet):
	queryset = Insumo.objects.all()
	serializer_class = InsumoSerializer
	model = Insumo
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('id', 'nombre', 'cantidad', 'proovedor')


class CosechaViewSet(viewsets.ModelViewSet):
	queryset = CosechaCultivo.objects.all()
	serializer_class = CosechaCultivoSerializer
	model = CosechaCultivo
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('id', 'nombre', 'cantidad',)


class PlagaViewSet(viewsets.ModelViewSet):
	queryset = Plaga.objects.all()
	serializer_class = PlagaSerializer
	model = Plaga
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('id', 'nombre', 'created', 'updated')


class ActividadesViewSet(generics.ListCreateAPIView):
	def create(self, request, *args, **kwargs):
		actividades = ['riego', 'desmalezamiento', 'limpieza', 'observaciones']
		insumos = ['fertilizacion', 'plaguicida']

		for selector, cultivos in request.data.iteritems():
			if selector in actividades:
				actividad_serializer = ActividadesCultivoSerializer(data=cultivos, many=True)
			if selector in insumos:
				insumos_serializer = InsumoCultivoSerializer(data=cultivos, many=True)
			else:
				print(cultivos)

		if not actividad_serializer.is_valid():
			return Response(actividad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		if not insumos_serializer.is_valid():
			return Response(insumos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		response = {
			'data': request.data,
			'actividades': actividad_serializer.data,
			'insumos': insumos_serializer.data
		}

		return Response(response, status=status.HTTP_200_OK)

# class ActividadesViewSet(generics.ListCreateAPIView):
# 	serializer_class = ActividadesSerializer
# 	pagination_class = StandardResultsSetPagination
#
# 	def create(self, request):
#
# 		resource = self.serializer_class(data=request.data)
#
# 		if resource.is_valid():
# 			data = [{'created': 1}, resource.data]
# 			return Response(data, status=status.HTTP_201_CREATED)
#
# 		elif not resource.is_valid():
# 			data = [{'created': 0}, resource.errors]
# 			return Response(data, status=status.HTTP_400_BAD_REQUEST)
#
# 	def list(self, request):
# 		# Note the use of `get_queryset()` instead of `self.queryset`
# 		insumos = InsumoCultivoSerializer(InsumoCultivo.objects.order_by('-fecha_aplicacion'), many=True)
# 		actividades = ActividadesCultivoSerializer(ActividadesCultivo.objects.order_by('-fecha_realizacion'), many=True)
#
# 		response = {
# 			'insumos': insumos.data,
# 		    'actividades': actividades.data
# 		}
#
# 		page = self.get_paginated_response(response)
#
# 		return Response(page, status.HTTP_200_OK)
