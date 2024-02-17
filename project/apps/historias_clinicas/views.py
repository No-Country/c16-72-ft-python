from . import models, forms
from django.urls import reverse_lazy

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'historias_clinicas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        try:
            historia_clinica = models.HistoriaClinica.objects.get(paciente=user)
            context['historia_clinica'] = historia_clinica
            estudios = models.Estudios.objects.filter(paciente=historia_clinica)
            if estudios:
                context['estudios'] = True
        except models.HistoriaClinica.DoesNotExist:
            context['historia_clinica'] = None
        except models.Estudios.DoesNotExist:
            context['estudios'] = False

        context['es_paciente'] = user.groups.filter(name='Pacientes').exists()

        context['es_medico'] = user.groups.filter(name='Medicos').exists()
        
        return context


# _______________ Historias clinicas Views _______________

class HistoriaClinicaDetail(LoginRequiredMixin, DetailView):
    """Vista de detalle de Historia Clinica para usuario medico o superusuario."""

    model = models.HistoriaClinica

    def test_func(self):
        return medico_o_superuser(self.request.user)


from django.shortcuts import get_object_or_404

class HistoriaPacienteDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Vista de detalle de Historia Clinica para usuario paciente."""

    model = models.HistoriaClinica
    template_name = "historias_clinicas/historiaclinica_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(models.HistoriaClinica, paciente=self.request.user)

    def test_func(self):
        return paciente(self.request.user)


class HistoriaClinicaList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Vista de listado de Historia Clinica para usuario medico o superusuario."""
    
    model = models.HistoriaClinica

    def test_func(self):
        return medico_o_superuser(self.request.user)


class HistoriaClinicaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Vista de creacion de Historia Clinica para usuario medico o superusuario."""
    
    model = models.HistoriaClinica
    form_class = forms.HistoriaClinicaForm
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")

    def form_valid(self, form):
        form.instance.medico_tratante = self.request.user
        messages.success(
            self.request,
            "Historia Clinica creada correctamente.",
            extra_tags="alert alert-success",
        )
        return super().form_valid(form)

    def test_func(self):
        return medico_o_superuser(self.request.user)


class HistoriaClinicaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Vista de eliminacion de Historia Clinica para usuario medico o superusuario."""
    
    model = models.HistoriaClinica
    template_name = "historias_clinicas/confirm_delete.html"
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")

    def get_success_url(self):
        messages.success(
            self.request,
            "Historia Clinica eliminada correctamente.",
            extra_tags="alert alert-danger",
        )
        return super().get_success_url()

    def test_func(self):
        return medico_o_superuser(self.request.user)


class HistoriaClinicaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Vista de actualizacion de Historia Clinica para usuario medico o superusuario."""
    
    model = models.HistoriaClinica
    success_url = reverse_lazy("historias_clinicas:historiaclinica_list")
    form_class = forms.HistoriaClinicaForm

    def form_valid(self, form):
        messages.success(
            self.request,
            "Historia Clinica actualizada correctamente.",
            extra_tags="alert alert-success",
        )
        return super().form_valid(form)

    def test_func(self):
        return medico_o_superuser(self.request.user)


# Estudios views

class EstudioList(LoginRequiredMixin, ListView):
    """Vista de listado de estudios para usuario medico o paciente."""
    
    model = models.Estudios

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.groups.filter(name="Medicos").exists():
            return queryset
        else:
            return queryset.filter(paciente__paciente=user)


# _______________ Funciones auxiliares _______________

def medico_o_superuser(user):
    """Devuelve True si el usuario pertenece al grupo Medicos o es un superusuario."""
    return user.groups.filter(name="Medicos").exists() or user.is_superuser

def paciente(user):
    """Devuelve True si el usuario pertenece al grupo Pacientes."""
    return user.groups.filter(name="Pacientes").exists()
