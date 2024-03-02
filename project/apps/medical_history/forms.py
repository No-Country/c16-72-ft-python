from django import forms
from .models import MedicalHistory
from users.models import User
from django.contrib import admin


class MedicalHistoryForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Patients'), label='Paciente')
    chronic_diseases = forms.CharField(label='Enfermedades Crónicas', required=False, widget=forms.Textarea)
    family_history = forms.CharField(label='Antecedentes Familiares', required=False, widget=forms.Textarea)
    surgeries = forms.CharField(label='Cirugías', required=False, widget=forms.Textarea)
    allergies = forms.CharField(label='Alergias', required=False, widget=forms.Textarea)
    medications = forms.CharField(label='Medicamentos', required=False, widget=forms.Textarea)
    vaccines = forms.CharField(label='Vacunas', required=False, widget=forms.Textarea)
    habits = forms.CharField(label='Hábitos', required=False, widget=forms.Textarea)
    observations = forms.CharField(label='Observaciones', required=False, widget=forms.Textarea)
    
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'chronic_diseases', 'family_history', 'surgeries', 'allergies', 'medications', 'vaccines', 'habits', 'observations']


class MedicalHistoryAdminForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MedicalHistoryAdminForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(groups__name='Patients')
        self.fields['medical'].queryset = User.objects.filter(groups__name='Medicals')