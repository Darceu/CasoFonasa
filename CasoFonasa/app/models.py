from django.db import models

# modelo de CONSULTAS
class Consulta(models.Model):
    def liberar_consulta(self):
        self.estado = 'desocupada'
        self.save()
    ESTADO_CHOICES = [
        ('desocupada', 'Desocupada'),
        ('ocupada', 'Ocupada'),
        
    ]

    TIPO_CONSULTA_CHOICES = [
        ('Pediatría', 'Pediatría'),
        ('Urgencia', 'Urgencia'),
        ('CGI', 'Consulta General Integral'),
    ]
    def atender_paciente(self, paciente):
        paciente.consulta_asignada = self
        paciente.estado = 'Atendido'
        paciente.save()

        self.pacientes_atendidos += 1
        self.estado = 'Ocupada'
        self.save()
    id_consulta = models.AutoField(primary_key=True)
    pacientes_atendidos = models.IntegerField(default=0)
    especialista = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='desocupada')
    tipo_consulta = models.CharField(max_length=20, choices=TIPO_CONSULTA_CHOICES)

    def __str__(self):
        return f"Consulta {self.id_consulta}"

# modelo de PACIENTES
class Paciente(models.Model):
    ESTADO_CHOICES = [
        ('sala_espera', 'Sala de Espera'),
        ('pendiente', 'Pendiente'),
        ('pendiente_atendido','Pendiente Atendido')
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='sala_espera')
    historia_clinica = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    peso = models.FloatField(null=True, blank=True)
    estatura = models.FloatField(null=True, blank=True)
    fumador = models.BooleanField(default=False)
    anos_fumador = models.IntegerField(default=0)
    dieta_asignada = models.BooleanField(default=False)
    prioridad = models.FloatField(null=True, blank=True)
    grupo_edad = models.CharField(max_length=10, blank=True)

    def calcular_grupo_edad(self):
        if 1 <= self.edad <= 15:
            self.grupo_edad = 'niño'
        elif 16 <= self.edad <= 40:
            self.grupo_edad = 'joven'
        else:
            self.grupo_edad = 'anciano'

    def calcular_prioridad(self):
        if self.grupo_edad == 'niño':
            if 1 <= self.edad <= 5:
                self.prioridad = self.peso - self.estatura - 3
            elif 6 <= self.edad <= 12:
                self.prioridad = self.peso - self.estatura - 2
            elif 13 <= self.edad <= 15:
                self.prioridad = self.peso - self.estatura - 1

        elif self.grupo_edad == 'joven':
            if self.fumador:
                self.prioridad = self.anos_fumador / 4 + 2
            else:
                self.prioridad = 2

        elif self.grupo_edad == 'anciano':
            if self.dieta_asignada and 60 <= self.edad <= 100:
                self.prioridad = self.edad / 20 + 4
            else:
                self.prioridad = self.edad / 30 + 3

        if self.grupo_edad == 'anciano':
            self.prioridad = (self.edad * self.prioridad) / 100 + 5.3
        else:
            self.prioridad = (self.edad * self.prioridad) / 100

    def save(self, *args, **kwargs):
        if not self.grupo_edad:
            self.calcular_grupo_edad()
        if not self.prioridad:
            self.calcular_prioridad()
        super().save(*args, **kwargs)