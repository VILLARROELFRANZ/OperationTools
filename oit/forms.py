from django import forms
from .models import OIT

class OITForm(forms.ModelForm):
    class Meta:
        model = OIT
        fields = [
            'numero_oit', 'tipo_oit', 'equipo', 'serial', 'descripcion_eq',
            'fecha_emision', 'fecha_inicio_ejecucion', 'hora_inicio',
            'dato_actual_frecuencia', 'fecha_final_ejecucion', 'hora_fin',
            'reporte_tecnico', 'actividad_realizada', 'actividades_pendientes',
            'completado',  # Asegúrate de agregar el campo 'completado' aquí
        ]
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
            'fecha_inicio_ejecucion': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'dato_actual_frecuencia': forms.DateInput(attrs={'type': 'date'}),
            'fecha_final_ejecucion': forms.DateInput(attrs={'type': 'date'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
            # Puedes agregar widgets adicionales si es necesario
        }
        labels = {
            'completado': 'Completado',  # Agrega un label si es necesario
        }





