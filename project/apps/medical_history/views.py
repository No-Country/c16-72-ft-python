from . import models, forms 
from django.urls import reverse_lazy

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from django.db.models import Q

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect

 
class MedicalHistoryDetail(LoginRequiredMixin, DetailView):
    model = models.MedicalHistory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['is_medical'] = is_medical(user)
        return context

    def test_func(self):
        return is_medical(self.request.user)
        
from django.db.models import Q

class MedicalHistoryList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.MedicalHistory

    def get_queryset(self):
        """Filtra todas las historias medicas que contengan el texto ingresado en DNI o apellido."""
        query = self.request.GET.get("consult")
        
        if query:
            object_list = models.MedicalHistory.objects.filter(
                Q(patient__dni__icontains=query) | Q(patient__name__icontains=query) | Q(patient__last_name__icontains=query) 
            )
        else:
            object_list = models.MedicalHistory.objects.all()
        return object_list
    
    def test_func(self):
        return is_medical(self.request.user)
    
class MedicalHistoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.MedicalHistory
    form_class = forms.MedicalHistoryForm
    success_url = reverse_lazy("medical_history:medicalhistory_list")

    def form_valid(self, form):
        form.instance.medical = self.request.user
        messages.success(self.request, "Historial creado correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        return is_medical(self.request.user)
"""
class MedicalHistoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.MedicalHistory
    template_name = "medical_history/confirm_delete.html"
    success_url = reverse_lazy("medical_history:medicalhistory_list")

    def get_success_url(self):
            messages.success(self.request, "Historial eliminado correctamente.", extra_tags="alert alert-success")
            return super().get_success_url()
     
    def test_func(self):
        return is_medical(self.request.user)
"""
    
    
class MedicalHistoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.MedicalHistory
    success_url = reverse_lazy("medical_history:medicalhistory_list")
    form_class = forms.MedicalHistoryForm

    def form_valid(self, form):
        messages.success(self.request, "Historial actualizado correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def test_func(self):
        return is_medical(self.request.user)
    

# _______________ Funciones auxiliares _______________
    
def is_medical(user):
    """Devuelve True si el usuario pertenece al grupo Medicos o es un superusuario."""
    return user.groups.filter(name='Medicals').exists() or user.is_staff

def is_patient(user):
    """Devuelve True si el usuario pertenece al grupo Pacientes."""
    return user.groups.filter(name="Patients").exists()




@login_required
@user_passes_test(is_medical)
def delete_history_view(request, pk):

    studie_medical = get_object_or_404(models.MedicalHistory, pk=pk)
    studie_medical.delete()
    messages.success(request, "Historial eliminado correctamente.", extra_tags="alert alert-success")
    return redirect('studies_medicals:studiesmedicals_list')