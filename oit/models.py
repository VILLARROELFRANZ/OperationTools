from django.db import models

class OIT(models.Model):
    TIPO_OIT_CHOICES = [
        ('preventivo', 'Mantenimiento Preventivo'),
        ('correctivo', 'Mantenimiento Correctivo'),
    ]

    # Campos existentes de OIT
    numero_oit = models.IntegerField(verbose_name="Numero de OIT", default=0)
    tipo_oit = models.CharField(max_length=20, choices=TIPO_OIT_CHOICES, verbose_name="Tipo de OIT")
    equipo = models.CharField(max_length=255, verbose_name="Equipo")
    serial = models.CharField(max_length=255, verbose_name="Serial")
    descripcion_eq = models.TextField(verbose_name="Descripción del Equipo")
    fecha_emision = models.DateField(verbose_name="Fecha de Emisión")
    fecha_inicio_ejecucion = models.DateField(verbose_name="Fecha de Inicio de Ejecución")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    dato_actual_frecuencia = models.DateField(verbose_name="Dato Actual Frecuencia")
    fecha_final_ejecucion = models.DateField(verbose_name="Fecha Final de Ejecución")
    hora_fin = models.TimeField(verbose_name="Hora Fin")
    reporte_tecnico = models.TextField(verbose_name="Reporte Técnico")
    actividad_realizada = models.TextField(verbose_name="Actividad Realizada")
    actividades_pendientes = models.TextField(blank=True, null=True, verbose_name="Actividades Pendientes")

    # Campos adicionales para Repuesto
    nombre_repuesto = models.CharField(max_length=255, verbose_name="Nombre del Repuesto", blank=True, null=True)
    referencia_repuesto = models.CharField(max_length=255, verbose_name="Referencia del Repuesto", blank=True, null=True)
    unidad_medida = models.CharField(max_length=100, verbose_name="Unidad de Medida", blank=True, null=True)
    descripcion_repuesto = models.TextField(verbose_name="Descripción del Repuesto", blank=True, null=True)
    cantidad_usada = models.PositiveIntegerField(verbose_name="Cantidad Usada", blank=True, null=True)

    # Campos adicionales para Falla
    parte_que_fallo = models.CharField(max_length=255, verbose_name="Parte que Falló", blank=True, null=True)
    causa_del_fallo = models.CharField(max_length=255, verbose_name="Causa del Fallo", blank=True, null=True)
    medida_correctiva = models.TextField(verbose_name="Medida Correctiva", blank=True, null=True)

    completado = models.BooleanField(default=False, verbose_name="Completado")


    class Meta:
        verbose_name = "Orden Interna de Trabajo"
        verbose_name_plural = "Ordenes Internas de Trabajo"

    def __str__(self):
        return f"OIT {self.clase_oit} - {self.equipo}"

