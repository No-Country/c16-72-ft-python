from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class MedicalHistory(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medical = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='historias_clinicas_tratadas', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    history = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.patient.name} {self.patient.last_name}'

    def clean(self):
        if not self.patient.groups.filter(name='Patients').exists():
            raise ValidationError("El paciente debe ser parte del grupo 'Pacientes'.")
       
        super().clean()
