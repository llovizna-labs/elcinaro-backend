from django.contrib import admin
from .models import Cliente, Factura, DetalleFactura

# Register your models here.

class ClienteAdmin (admin.ModelAdmin):
	model = Cliente


class DetalleFacturaAdmin(admin.TabularInline):
	model = DetalleFactura


class FacturaAdmin(admin.ModelAdmin):
	model = Factura
	inlines = [DetalleFacturaAdmin]
	extra = 5

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Factura, FacturaAdmin)
