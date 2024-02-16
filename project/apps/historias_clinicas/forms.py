from django import forms
from . import models


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = models.HistoriaClinica
        fields = ['paciente', 'antecedentes', 'alergias', 'observaciones']
        
class EstudiosForm(forms.ModelForm):
    class Meta:
        model = models.Estudios
        fields = '__all__'