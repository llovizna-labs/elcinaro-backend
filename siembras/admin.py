from django.contrib import admin

# Register your models here.
from .models import Categoria, Rubro, Semilla, Proovedor, LoteSiembra, TipoParcela, Parcela, Invernadero, Cultivo


class LoteSiembraAdmin(admin.ModelAdmin):
	model = LoteSiembra
	list_display = ("__unicode__", "proovedor", "fecha_enviado", "cantidad")


class CategoriaAdmin(admin.ModelAdmin):
	model = Categoria


class RubroAdmin(admin.ModelAdmin):
	model = Rubro


class ProovedorAdmin(admin.ModelAdmin):
	model = Proovedor
	list_display = ("nombre", "categoria")


class SemillaAdmin(admin.ModelAdmin):
	model = Semilla
	list_display = ("familia", "proovedor", "descripcion", "cantidad", "unidad")


class TipoParcelaAdmin(admin.ModelAdmin):
	model = TipoParcela


class ParcelAdmin(admin.ModelAdmin):
	model = Parcela


class InvernaderoAdmin (admin.ModelAdmin):
	model = Invernadero
	list_display = ("nombre", "codigo", "ubicacion")


class CultivoAdmin(admin.ModelAdmin):
	model = Cultivo
	list_display = ("__unicode__", "codigo", "fecha_siembra")




admin.site.register(Cultivo, CultivoAdmin)

admin.site.register(Parcela, ParcelAdmin)

admin.site.register(Invernadero, InvernaderoAdmin)

admin.site.register(TipoParcela, TipoParcelaAdmin)

admin.site.register(LoteSiembra, LoteSiembraAdmin)

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Rubro, RubroAdmin)

admin.site.register(Proovedor, ProovedorAdmin)

admin.site.register(Semilla, SemillaAdmin)
