from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from users.models import User

from medical_history.models import MedicalHistory

# Create your models here.

class TypeStudieMedical(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class StudiesMedicals(models.Model):
    name = models.CharField(max_length=50, default="Examen")
    patient = models.ForeignKey(MedicalHistory, related_name='patient_history', on_delete=models.CASCADE, )
    medical = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='estudios_solicitados', on_delete=models.CASCADE)
    type_studie = models.ForeignKey(TypeStudieMedical, on_delete=models.CASCADE)
    result = models.FileField(upload_to='estudios_resultados/', null=True, blank=True)
    report = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    observations = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.name
