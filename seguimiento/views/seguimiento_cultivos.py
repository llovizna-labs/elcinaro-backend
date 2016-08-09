__author__ = 'ronsuez'
__author__ = 'ronsuez'

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin

from seguimiento.serializers.seguimiento_cultivos import SeguimientoCultivoSerializer, ActividadesCultivoSerializer

from seguimiento.models import SeguimientoCultivo, ActividadesCultivo

@permission_classes((IsAuthenticatedOrReadOnly, ))
class SeguimientoCultivoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = SeguimientoCultivo.objects.all()
	serializer_class = SeguimientoCultivoSerializer
	model = SeguimientoCultivo


@permission_classes((IsAuthenticatedOrReadOnly, ))
class ActividadesCultivoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = ActividadesCultivo.objects.all()
	serializer_class = ActividadesCultivoSerializer
	model = ActividadesCultivo