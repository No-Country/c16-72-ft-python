from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

from medical_history.models import MedicalHistory

# Create your models here.

class TypeStudieMedical(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class StudiesMedicals(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, )
    medical = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='estudios_solicitados', on_delete=models.CASCADE)
    tipy = models.ForeignKey(TypeStudieMedical, on_delete=models.CASCADE)
    result = models.FileField(upload_to='estudios_resultados/', null=True, blank=True)
    report = models.TextField(null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if not self.medical.groups.filter(name='Medicals').exists():
            raise ValidationError("El médico emisor debe ser parte del grupo 'Médicos'.")
        super().clean()