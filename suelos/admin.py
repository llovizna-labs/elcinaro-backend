from django.contrib import admin

from .models import MuestraSuelo, AnalisisSuelo

# Register your models here.


class MuestraSueloAdmin(admin.ModelAdmin):
	model = MuestraSuelo


class AnalisisSueloAdmin(admin.ModelAdmin):
	model = AnalisisSuelo




admin.site.register(MuestraSuelo, MuestraSueloAdmin)

admin.site.register(AnalisisSuelo, AnalisisSueloAdmin)