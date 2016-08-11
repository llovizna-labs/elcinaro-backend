from django.contrib import admin

from .models import SeguimientoCultivo, ActividadesCultivo, PlagasCultivo, Plaga, CultivoMuestra, InsumoCultivo, Insumo, CrecimientoCultivo
# Register your models here.


class CultivoMuestraAdmin(admin.ModelAdmin):
	model = CultivoMuestra


class CrecimientoCultivoAdmin(admin.ModelAdmin):
	model = CrecimientoCultivo


class SeguimientoCultivoAdmin(admin.ModelAdmin):
	model = SeguimientoCultivo


class ActividadesCultivoAdmin(admin.ModelAdmin):
	model = ActividadesCultivo


class PlagasCultivoAdmin(admin.ModelAdmin):
	model = PlagasCultivo


class PlagaAdmin(admin.ModelAdmin):
	model = Plaga


class InsumoAdmin(admin.ModelAdmin):
	model = Insumo


class InsumoCultivoAdmin(admin.ModelAdmin):
	model = InsumoCultivo


admin.site.register(CultivoMuestra, CultivoMuestraAdmin)

admin.site.register(CrecimientoCultivo, CrecimientoCultivoAdmin)

admin.site.register(SeguimientoCultivo, SeguimientoCultivoAdmin)

admin.site.register(ActividadesCultivo, ActividadesCultivoAdmin)

admin.site.register(Insumo, InsumoAdmin)

admin.site.register(InsumoCultivo, InsumoCultivoAdmin)

admin.site.register(Plaga, PlagaAdmin)
