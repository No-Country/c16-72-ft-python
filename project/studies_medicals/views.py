from django.shortcuts import render
from django.views import View

from .models import StudiesMedicals
from medical_history.models import MedicalHistory

# Create your views here.

class ListStudiesMedicalsView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            studies_medicals = StudiesMedicals.objects.filter(medical=request.user)
            context = {
                'studies_medicals' : studies_medicals
            }
            return render(request, 'studies_medicals/medical/list.html', context)
        
        if not request.user.is_staff:
            try:
                medical_history = MedicalHistory.objects.get(patient=request.user)
                studies_patients = StudiesMedicals.objects.filter(patient=medical_history)
                context = {
                    'studies_patients' : studies_patients
                }
                return render(request, 'studies_medicals/patient/list.html', context)
            except:
                return render(request, 'studies_medicals/patient/error.html')
