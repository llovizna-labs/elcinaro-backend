from rest_framework.decorators import renderer_classes, api_view
from rest_framework.response import Response
from rest_framework_csv import renderers as r

from siembras.models import Cultivo
# Create your views here.


class CultivosRenderer(r.CSVRenderer):
	header = ['rubro', 'semilla', 'fecha_siembra', 'plantas_sembradas',
	          'lote_siembra', 'fecha_enviado', 'fecha_recibido', 'germinado',
	          'semillas_enviadas', 'plantulas_recibidas']


@api_view(['GET'])
@renderer_classes((CultivosRenderer,))
def cultivo_csv(request):
	cultivos = Cultivo.objects.all().order_by('lote.germinado')
	content = [{
		'rubro': cultivo.lote.semilla_utilizada.familia.nombre,
		'semilla': cultivo.lote.semilla_utilizada.descripcion,
		'fecha_siembra': cultivo.fecha_siembra,
		'plantas_sembradas': cultivo.plantas_sembradas(),
		'lote_siembra': cultivo.lote.id,
	    'germinado': cultivo.lote.germinado,
		'fecha_enviado': cultivo.lote.fecha_enviado,
		'fecha_recibido': cultivo.lote.fecha_recibido,
		'semillas_enviadas': cultivo.lote.cantidad_semillas_enviadas,
		'plantulas_recibidas': cultivo.lote.cantidad_semillas_recibidas} for cultivo in cultivos]

	return Response(content)