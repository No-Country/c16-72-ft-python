from django import forms
from .models import MedicalHistory
from users.models import User

class MedicalHistoryForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Patients'))
    
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'history', 'allergies', 'observations']