from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class MedicalHistory(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medical = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='medic_historys', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    chronic_diseases = models.TextField(null=True, blank=True)
    family_history = models.TextField(null=True, blank=True)
    surgeries = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medications = models.TextField(null=True, blank=True)
    vaccines = models.TextField(null=True, blank=True)
    habits = models.TextField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.patient.name} {self.patient.last_name}'

    def clean(self):
        if not self.patient.groups.filter(name='Patients').exists():
            raise ValidationError("The patient must be part of the 'Patients' group.")
        
        super().clean()