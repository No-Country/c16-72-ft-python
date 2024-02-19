from django import forms
from . import models
from home.models import User


class HistoriaClinicaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Pacientes'))
    
    class Meta:
        model = models.HistoriaClinica
        fields = ['paciente', 'antecedentes', 'alergias', 'observaciones']


        from django.contrib import admin

class HistoriaClinicaAdminForm(forms.ModelForm):
    class Meta:
        model = models.HistoriaClinica
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaAdminForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].queryset = User.objects.filter(groups__name='Pacientes')
        self.fields['medico_tratante'].queryset = User.objects.filter(groups__name='Medicos')



        
class EstudiosForm(forms.ModelForm):
    class Meta:
        model = models.Estudios
        fields = '__all__'