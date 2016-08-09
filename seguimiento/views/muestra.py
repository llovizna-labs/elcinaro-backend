__author__ = 'ronsuez'

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin

from seguimiento.serializers.muestra import CultivoMuestraSerializer

from seguimiento.models import CultivoMuestra

@permission_classes((IsAuthenticatedOrReadOnly, ))
class MuestraCultivoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = CultivoMuestra.objects.all()
	serializer_class = CultivoMuestraSerializer
	model = CultivoMuestra
