from django.contrib import admin
from .models import Consulta, Paciente
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_consulta', 'pacientes_atendidos', 'especialista', 'estado', 'tipo_consulta')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('historia_clinica', 'nombre', 'edad', 'peso', 'grupo_edad', 'prioridad', 'estado', 'dieta_asignada', 'fumador', 'anos_fumador')
    search_fields = ('historia_clinica', 'nombre')
    list_filter = ('estado', 'grupo_edad')
