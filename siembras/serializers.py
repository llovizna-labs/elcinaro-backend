from rest_framework import  serializers
from .models import Rubro

# Serializers define the API representation.
class RubroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rubro
        fields = ('id', 'nombre')

