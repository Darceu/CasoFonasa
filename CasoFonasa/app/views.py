from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Paciente, Consulta
from django.shortcuts import get_object_or_404
from .forms import PacienteForm, ConsultaForm
def home(request):
    historia_clinica_default = 1

    return render(request, 'fonasa_app/home.html', {'historia_clinica_default': historia_clinica_default})

def listar_pacientes_mayor_riesgo(request):
    historia_clinica = request.GET.get('historia_clinica', None)

    # validar historia clinica
    if historia_clinica is not None:
        paciente_base = get_object_or_404(Paciente, historia_clinica=historia_clinica)

        pacientes_mayor_riesgo = Paciente.objects.filter(
            prioridad__gt=paciente_base.prioridad
        ).exclude(historia_clinica=paciente_base.historia_clinica)

        context = {'pacientes_mayor_riesgo': pacientes_mayor_riesgo, 'paciente_base': paciente_base}
        return render(request, 'fonasa_app/listar_pacientes_mayor_riesgo.html', context)

    else:
        # numero de clinica no valido
        return HttpResponse("Por favor, proporcione un numero de historia clinica valido.")
def atender_paciente(request):
    # obtener todas las consultas desocupadas
    consultas_disponibles = Consulta.objects.filter(estado='Desocupada')

    # atender pacientes en la sala de espera
    for consulta in consultas_disponibles:
        pacientes_en_sala_espera = Paciente.objects.filter(estado='Sala de Espera', consulta_asignada=None)
        pacientes_en_sala_espera = sorted(pacientes_en_sala_espera, key=lambda x: x.prioridad, reverse=True)

        for paciente in pacientes_en_sala_espera:
            if consulta.estado == 'Desocupada':
                consulta.atender_paciente(paciente)

    # obtener pacientes pendientes
    pacientes_pendientes = Paciente.objects.filter(estado='Pendiente')
    pacientes_pendientes = sorted(pacientes_pendientes, key=lambda x: x.prioridad, reverse=True)

    # tender pacientes pendientes segun su prioridad
    for paciente_pendiente in pacientes_pendientes:
        consulta_disponible = Consulta.objects.filter(estado='Desocupada').first()
        if consulta_disponible:
            consulta_disponible.atender_paciente(paciente_pendiente)
        else:
            # mover al paciente de pendientes a la sala de espera
            paciente_pendiente.estado = 'Sala de Espera'
            paciente_pendiente.save()

    return redirect('home')

def liberar_consultas(request):
    consultas_ocupadas = Consulta.objects.filter(estado='ocupada')

    for consulta in consultas_ocupadas:
        consulta.liberar_consulta()

    # atender a los pacientes y liberar consultas
    return atender_paciente(request)

def listar_pacientes_fumadores_urgentes(request):
    # filtrar pacientes fumadores que necesitan ser atendidos con urgencia
    pacientes_fumadores_urgentes = Paciente.objects.filter(fumador=True)

    context = {'pacientes_fumadores_urgentes': pacientes_fumadores_urgentes}
    return render(request, 'fonasa_app/listar_pacientes_fumadores_urgentes.html', context)

def consulta_mas_pacientes_atendidos(request):
    # obtener todas las consultas ordenadas de mayor a menor segun la cantidad de pacientes atendidos
    consultas = Consulta.objects.all().order_by('-pacientes_atendidos')

    context = {'consultas': consultas}
    return render(request, 'fonasa_app/consulta_mas_pacientes_atendidos.html', context)

def paciente_mas_anciano(request):
    # obtener todos los pacientes en la sala de espera
    pacientes_en_sala_espera = Paciente.objects.filter(estado='sala_espera')

    # verificar si hay pacientes en la sala de espera
    if pacientes_en_sala_espera.exists():
        # filtrar al paciente mas anciano
        paciente_mas_anciano = max(pacientes_en_sala_espera, key=lambda x: x.edad)

        context = {'paciente_mas_anciano': paciente_mas_anciano}
        return render(request, 'fonasa_app/paciente_mas_anciano.html', context)
    else:
        # si no hay pacientes
        return render(request, 'fonasa_app/paciente_mas_anciano.html', {'sin_pacientes': True})

def formulario_add_paciente(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = PacienteForm()

    return render(request, 'fonasa_app/formulario_add_paciente.html', {'form': form})

def formulario_add_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultaForm()

    return render(request, 'fonasa_app/formulario_add_consulta.html', {'form': form})

def lista_pacientes(request):
    
    pacientes = Paciente.objects.all()
    return render(request, 'fonasa_app/lista_paciente.html', {'pacientes': pacientes})

def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'fonasa_app/lista_consultas.html', {'consultas': consultas})