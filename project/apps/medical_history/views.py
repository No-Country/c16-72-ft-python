from . import models, forms 
from django.urls import reverse_lazy

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages



class IndexView(TemplateView):
    template_name = 'medical_history/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        try:
            medical_history = models.MedicalHistory.objects.get(patient=user)
            context['medical_history'] = medical_history
        except models.MedicalHistory.DoesNotExist:
            context['medical_history'] = None

        context['is_patient'] = user.groups.filter(name='Patients').exists()

        context['is_medical'] = user.groups.filter(name='Medicals').exists()
        
        return context
 
class MedicalHistoryDetail(LoginRequiredMixin, DetailView):
    model = models.MedicalHistory
    def test_func(self):
        return medico_or_superuser(self.request.user)
        
class MedicalHistoryList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.MedicalHistory
  
    def test_func(self):
        return medico_or_superuser(self.request.user)
    
class MedicalHistoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.MedicalHistory
    form_class = forms.MedicalHistoryForm
    success_url = reverse_lazy("medical_history:medicalhistory_list")

    def form_valid(self, form):
        form.instance.medical = self.request.user
        messages.success(self.request, "Historia Clinica creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        return medico_or_superuser(self.request.user)
    
class MedicalHistoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.MedicalHistory
    template_name = "medical_history/confirm_delete.html"
    success_url = reverse_lazy("medical_history:medicalhistory_list")

    def get_success_url(self):
            messages.success(self.request, "Historia Clinica eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    
    def test_func(self):
        return medico_or_superuser(self.request.user)
    
    
class MedicalHistoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.MedicalHistory
    success_url = reverse_lazy("medical_history:medicalhistory_list")
    form_class = forms.MedicalHistoryForm

    def form_valid(self, form):
        messages.success(self.request, "Historia Clinica actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def test_func(self):
        return medico_or_superuser(self.request.user)


def medico_or_superuser(user):
    """Devuelve True si el usuario pertenece al grupo Medicos o es un superusuario."""
    return user.groups.filter(name='Medicals').exists() or user.is_staff