from django.contrib import admin
from .models import OIT

class OITAdmin(admin.ModelAdmin):
    list_display = ('numero_oit', 'equipo', 'tipo_oit', 'fecha_emision', 'fecha_inicio_ejecucion')
    list_filter = ('tipo_oit', 'fecha_emision')
    search_fields = ('equipo', 'serial', 'nombre_repuesto', 'parte_que_fallo')
    ordering = ('fecha_emision', 'numero_oit')

admin.site.register(OIT, OITAdmin)


