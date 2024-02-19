from django.contrib import admin
from .models import HistoriaClinica, TipoDeEstudio, Estudios
from .forms import HistoriaClinicaAdminForm

@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('paciente__username', 'antecedentes', 'alergias')
    form = HistoriaClinicaAdminForm


@admin.register(TipoDeEstudio)
class TipoDeEstudioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Estudios)
class EstudiosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'paciente', 'medico_solicitante', 'tipo', 'fecha_realización')
    list_filter = ('fecha_realización', 'tipo')
    search_fields = ('nombre',)
