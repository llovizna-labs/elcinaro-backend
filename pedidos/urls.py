__author__ = 'ronsuez'


from django.conf.urls import patterns, include, url
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework.authtoken import views
from pedidos.views import clientes
# from .views import schema_view


router = ExtendedSimpleRouter()

cliente_routes = router.register(
    r'clientes',
    clientes.ClienteViewSet,
    base_name='cliente'
)


