from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from siembras.serializers.cultivo import CultivoSerializer
from siembras.models import Cultivo

@permission_classes((IsAuthenticatedOrReadOnly, ))
class CultivoViewSet(viewsets.ModelViewSet):
	queryset = Cultivo.objects.all()
	serializer_class = CultivoSerializer
	model = Cultivo



