from django import forms
from .models import MedicalHistory
from users.models import User
from django.contrib import admin


class MedicalHistoryForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Patients'))
    
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'history', 'allergies', 'observations']

class MedicalHistoryAdminForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MedicalHistoryAdminForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(groups__name='Patients')
        self.fields['medical'].queryset = User.objects.filter(groups__name='Medicals')