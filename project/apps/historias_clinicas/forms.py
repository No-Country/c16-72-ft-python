from django import forms
from . import models
from home.models import User

class HistoriaClinicaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Pacientes'))
    
    class Meta:
        model = models.HistoriaClinica
        fields = ['paciente', 'antecedentes', 'alergias', 'observaciones']
        
class EstudiosForm(forms.ModelForm):
    class Meta:
        model = models.Estudios
        fields = '__all__'