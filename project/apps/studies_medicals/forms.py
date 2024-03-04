from django import forms
from django.contrib import admin
from users.models import User

from .models import StudiesMedicals

class StudieMedicalForm(forms.ModelForm):
    dni_patient = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':''}),
        required=True,
        label='DNI del paciente'  # Label en español
    )
    
    class Meta:
        model = StudiesMedicals
        fields = ['dni_patient', 'type_studie','studie_name', 'result', 'report', 'observations']
        exclude = ['medical']
        labels = {
            'dni_patient': 'DNI del paciente',
            'type_studie': 'Tipo de estudio',
            'studie_name': 'Nombre del estudio',
            'result': 'Resultado',
            'report': 'Informe',
            'observations': 'Observaciones'
        }



class StudiesMedicalAdminForm(forms.ModelForm):
    class Meta:
        model = StudiesMedicals
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudiesMedicalAdminForm, self).__init__(*args, **kwargs)
        self.fields['medical'].queryset = User.objects.filter(groups__name='Medicals')