from . import models, forms 
from django.urls import reverse_lazy

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

class IndexView(TemplateView):
    template_name = 'historias_clinicas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        try:
            historia_clinica = models.HistoriaClinica.objects.get(paciente=user)
            context['historia_clinica'] = historia_clinica
        except models.HistoriaClinica.DoesNotExist:
            context['historia_clinica'] = None

        context['es_paciente'] = user.groups.filter(name='Pacientes').exists()

        context['es_medico'] = user.groups.filter(name='Medicos').exists()
        
        return context

    
    
class HistoriaClinicaDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.HistoriaClinica
    def test_func(self):
        """ Devuelve True si el usuario pertenece al grupo Medicos."""
        return self.request.user.groups.filter(name='Medicos').exists()
        
class HistoriaClinicaList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = models.HistoriaClinica
  
    def test_func(self):
        """ Devuelve True si el usuario pertenece al grupo Medicos."""
        return self.request.user.groups.filter(name='Medicos').exists()
    
class HistoriaClinicaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.HistoriaClinica
    form_class = forms.HistoriaClinicaForm
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")

    def form_valid(self, form):
        messages.success(self.request, "Historia Clinica creada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        """ Devuelve True si el usuario pertenece al grupo Medicos."""
        return self.request.user.groups.filter(name='Medicos').exists()
    
class HistoriaClinicaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.HistoriaClinica
    template_name = "historias_clinicas/confirm_delete.html"
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")

    def get_success_url(self):
            messages.success(self.request, "Historia Clinica eliminada correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    
    def test_func(self):
        """ Devuelve True si el usuario pertenece al grupo Medicos."""
        return self.request.user.groups.filter(name='Medicos').exists()
    
    
class HistoriaClinicaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.HistoriaClinica
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")
    form_class = forms.HistoriaClinicaForm

    def form_valid(self, form):
        messages.success(self.request, "Historia Clinica actualizada correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def test_func(self):
        """ Devuelve True si el usuario pertenece al grupo Medicos."""
        return self.request.user.groups.filter(name='Medicos').exists()
    