"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework.authtoken import views
from siembras.views import cultivo
from seguimiento.views import muestra, seguimiento_cultivos
from pedidos.views import clientes

router = ExtendedSimpleRouter()

# User Routes
# user_routes = router.register(
#     r'users', user.UserViewSet,
#     base_name='user')
# (
#   user_routes.register(r'groups',
#                     user.GroupViewSet,
#                     base_name='users-group',
#                     parents_query_lookups=['user'])
#             .register(r'permissions',
#                     user.PermissionViewSet,
#                     base_name='users-groups-permission',
#                     parents_query_lookups=['group__user', 'group'])
# )

# Siembras module Routes

rubro_routes = router.register(
    r'rubros',
    cultivo.RubroViewSet,
    base_name='rubro'
)

semilla_routes = router.register(
    r'semillas',
    cultivo.SemillaViewSet,
    base_name='semilla'
)

rubro_meta = rubro_routes.register(
	r'media',
	cultivo.RubroMediaViewSet,
	base_name='rubro-media',
	parents_query_lookups=['rubro']
)

actividades = router.register(
	r'actividades',
	seguimiento_cultivos.ActividadesViewSet,
	base_name='actividades'
)

cultivo_routes = router.register(
    r'cultivos',
    cultivo.CultivoViewSet,
    base_name='cultivo')

parcela_routes = router.register(
    r'parcelas',
    cultivo.ParcelaViewSet,
    base_name='parcela')


invernadero_routes = router.register(
    r'invernaderos',
    cultivo.InvernaderoViewSet,
    base_name='invernadero')


lote_routes = router.register(
    r'lotes',
    cultivo.LoteSiembraViewSet,
    base_name='lote')

# Seguimiento Module
muestras_routes = router.register(
	r'muestras',
    muestra.MuestraCultivoViewSet,
    base_name='muestras'
)


actividades_cultivo = cultivo_routes.register(
	r'actividades',
    seguimiento_cultivos.ActividadesCultivoViewSet,
    base_name='cultivo-actividades',
	parents_query_lookups=['cultivo']
)


insumos = router.register(
	r'insumos',
    seguimiento_cultivos.InsumoViewSet,
    base_name='insumo'
)

muestras_cultivo = cultivo_routes.register(
	r'muestras',
	muestra.MuestraCultivoViewSet,
	base_name='cultivo-muestras',
	parents_query_lookups=['cultivo']
)


# Pedidos Module

cliente_routes = router.register(
    r'clientes',
    clientes.ClienteViewSet,
    base_name='cliente'
)

cliente_routes = router.register(
    r'proovedores',
    cultivo.ProovedorViewSet,
    base_name='proovedor'
)


cliente_routes = router.register(
    r'categorias',
    cultivo.CategoriaViewSet,
    base_name='categoria'
)
urlpatterns = [
	url(r'^auth/', views.obtain_auth_token),
	url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls'))
]

urlpatterns += router.urls
