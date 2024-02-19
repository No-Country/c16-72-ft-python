from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medico_tratante = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='historias_clinicas_tratadas', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    antecedentes = models.TextField(null=True, blank=True)
    alergias = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.paciente.name} - {self.paciente.last_name}"

    def clean(self):
        if not self.paciente.groups.filter(name='Pacientes').exists():
            raise ValidationError("El paciente debe ser parte del grupo 'Pacientes'.")
       
        super().clean()



class TipoDeEstudio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    
class Estudios(models.Model):
    nombre = models.CharField(max_length=100)
    paciente = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, )
    medico_solicitante = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='estudios_solicitados', on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoDeEstudio, on_delete=models.CASCADE)
    resultado = models.FileField(upload_to='estudios_resultados/', null=True, blank=True)
    informe = models.TextField(null=True, blank=True)
    fecha_realización = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    