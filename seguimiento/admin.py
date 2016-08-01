from django.contrib import admin

from .models import SeguimientoCultivo, ActividadesCultivo, PlagasCultivo, Plaga, CultivoMuestra, FertilizanteCultivo, Fertilizante, CrecimientoCultivo
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


class FertilizanteAdmin(admin.ModelAdmin):
	model = Fertilizante


class FertilizanteCultivoAdmin(admin.ModelAdmin):
	model = FertilizanteCultivo


admin.site.register(CultivoMuestra, CultivoMuestraAdmin)

admin.site.register(CrecimientoCultivo, CrecimientoCultivoAdmin)

admin.site.register(SeguimientoCultivo, SeguimientoCultivoAdmin)

admin.site.register(ActividadesCultivo, ActividadesCultivoAdmin)

admin.site.register(Fertilizante, FertilizanteAdmin)

admin.site.register(FertilizanteCultivo, FertilizanteCultivoAdmin)

admin.site.register(Plaga, PlagaAdmin)
