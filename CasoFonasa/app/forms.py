from django import forms
from .models import Paciente, Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['historia_clinica', 'nombre', 'edad', 'peso', 'estatura', 'fumador', 'anos_fumador', 'dieta_asignada']
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['especialista', 'estado', 'tipo_consulta', 'pacientes_atendidos']