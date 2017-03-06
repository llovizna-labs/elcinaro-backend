from django.contrib import admin

# Register your models here.
from .models import Categoria, Rubro, Semilla, Proovedor, LoteSiembra, TipoParcela, Parcela, Invernadero, Cultivo, \
	SemillaLote
from seguimiento.models import CultivoMuestra

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RubroResource(resources.ModelResource):
	class Meta:
		model = Rubro
		skip_unchanged = True
		report_skipped = False
		fields = ('id', 'nombre',)


class SemillaResource(resources.ModelResource):
	class Meta:
		model = Semilla
		skip_unchanged = True
		report_skipped = False
		fields = ("id", "descripcion", "familia__nombre", "proovedor__nombre", "cantidad", "unidad",)


class CultivoInlineAdmin(admin.TabularInline):
	model = Cultivo


class SemillaLoteInline(admin.StackedInline):
	model = SemillaLote


class SemillaLoteAdmin(admin.ModelAdmin):
	model = SemillaLote
	list_display = (
		"__unicode__", "proovedor", "cantidad_semillas_enviadas", "cantidad_semillas_recibidas")


class LoteSiembraAdmin(admin.ModelAdmin):
	model = LoteSiembra
	inlines = [SemillaLoteInline, ]


class CategoriaAdmin(admin.ModelAdmin):
	model = Categoria


class RubroAdmin(ImportExportModelAdmin):
	resource_class = RubroResource


class ProovedorAdmin(admin.ModelAdmin):
	model = Proovedor
	list_display = ("nombre", "categoria")


class SemillaAdmin(ImportExportModelAdmin):
	resource_class = SemillaResource


class TipoParcelaAdmin(admin.ModelAdmin):
	model = TipoParcela


class ParcelaAdmin(admin.ModelAdmin):
	model = Parcela
	inlines = [CultivoInlineAdmin]


class InvernaderoAdmin(admin.ModelAdmin):
	model = Invernadero
	list_display = ("nombre", "codigo", "ubicacion")
	inlines = [CultivoInlineAdmin]


class CultivoMuestraAdmin(admin.TabularInline):
	model = CultivoMuestra


class CultivoAdmin(admin.ModelAdmin):
	model = Cultivo
	list_display = ("__unicode__", "codigo", "fecha_siembra")
	inlines = [CultivoMuestraAdmin]


admin.site.register(Cultivo, CultivoAdmin)

admin.site.register(Parcela, ParcelaAdmin)

admin.site.register(Invernadero, InvernaderoAdmin)

admin.site.register(TipoParcela, TipoParcelaAdmin)

admin.site.register(LoteSiembra, LoteSiembraAdmin)

admin.site.register(SemillaLote, SemillaLoteAdmin)

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Rubro, RubroAdmin)

admin.site.register(Proovedor, ProovedorAdmin)

admin.site.register(Semilla, SemillaAdmin)
