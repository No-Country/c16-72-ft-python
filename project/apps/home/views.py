from django.views.generic import TemplateView
from medical_history.models import MedicalHistory
from studies_medicals.models import StudiesMedicals



class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            try:
                medical_history = MedicalHistory.objects.get(patient=user)
                context['medical_history'] = medical_history
                studies_medicals = StudiesMedicals.objects.filter(patient=medical_history)
                if studies_medicals:
                    context['studies_medicals'] = True
            except MedicalHistory.DoesNotExist:
                context['medical_history'] = None
            except StudiesMedicals.DoesNotExist:
                context['studies_medicals'] = False
        
            return context