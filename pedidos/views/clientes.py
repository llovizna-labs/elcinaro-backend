__author__ = 'ronsuez'

from rest_framework.response import Response
from rest_framework_extensions.decorators import action
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.filters import DjangoFilterBackend, OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from pedidos.models import Cliente
from pedidos.serializers.clientes import ClienteSerializer


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 100
	page_size_query_param = 'page_size'
	max_page_size = 1000


class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	model = Cliente
	pagination_class = StandardResultsSetPagination
	filter_backends = (OrderingFilter, SearchFilter)
	ordering_fields = ('identificacion', 'telefono', 'email', 'created', 'updated')