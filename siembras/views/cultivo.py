from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_extensions.mixins import NestedViewSetMixin
from siembras.serializers.cultivo import CultivoSerializer, ParcelaSerializer, InvernaderoSerializer, \
	LoteSiembraSerializer
from siembras.models import Cultivo, Parcela, Invernadero, LoteSiembra


@permission_classes((IsAuthenticatedOrReadOnly, ))
class CultivoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	queryset = Cultivo.objects.all()
	serializer_class = CultivoSerializer
	model = Cultivo


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
	model = Parcela
