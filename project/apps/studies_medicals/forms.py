from django import forms
from django.contrib import admin
from users.models import User

from .models import StudiesMedicals

class StudieMedicalForm(forms.ModelForm):
    dni_patient = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':''}),
        required=True
    )
    
    class Meta:
        model = StudiesMedicals
        fields = ['name','dni_patient', 'type_studie', 'result', 'report']
        exclude = ['medical']

class StudiesMedicalAdminForm(forms.ModelForm):
    class Meta:
        model = StudiesMedicals
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudiesMedicalAdminForm, self).__init__(*args, **kwargs)
        self.fields['medical'].queryset = User.objects.filter(groups__name='Medicals')