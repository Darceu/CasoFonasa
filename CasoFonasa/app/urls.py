from django.urls import path
from .views import home, listar_pacientes_mayor_riesgo, atender_paciente, lista_pacientes, liberar_consultas, listar_pacientes_fumadores_urgentes, consulta_mas_pacientes_atendidos, paciente_mas_anciano, formulario_add_paciente, formulario_add_consulta, lista_consultas

urlpatterns = [
    path('home/', home, name='home'),
    path('listar_pacientes_mayor_riesgo/', listar_pacientes_mayor_riesgo, name='listar_pacientes_mayor_riesgo'),
    path('atender_paciente/', atender_paciente, name='atender_paciente'),
    path('liberar_consultas/', liberar_consultas, name='liberar_consultas'),
    path('listar_pacientes_fumadores_urgentes/', listar_pacientes_fumadores_urgentes, name='listar_pacientes_fumadores_urgentes'),
    path('consulta_mas_pacientes_atendidos/', consulta_mas_pacientes_atendidos, name='consulta_mas_pacientes_atendidos'),
    path('paciente_mas_anciano/', paciente_mas_anciano, name='paciente_mas_anciano'),
    path('formulario_add_paciente/', formulario_add_paciente, name='formulario_add_paciente'),
    path('formulario_add_consulta/', formulario_add_consulta, name='formulario_add_consulta'),
    path('lista_pacientes/', lista_pacientes, name='lista_pacientes'),
    path('lista_consultas/', lista_consultas, name='lista_consultas'),
]
