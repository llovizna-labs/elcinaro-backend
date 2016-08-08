from rest_framework import serializers
from seguimiento.models import CultivoMuestra


class CultivoMuestraSerializer(serializers.ModelSerializer):
	class Meta:
		model = CultivoMuestra
		fields = ('id', 'codigo', 'ubicacion', 'cultivo', 'fecha_registro')

