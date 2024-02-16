from django import forms
from . import models

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = models.HistoriaClinica
        fields = '__all__'
        
class EstudiosForm(forms.ModelForm):
    class Meta:
        model = models.Estudios
        fields = '__all__'