from django.contrib import admin

from .models import MedicalHistory
from .forms import MedicalHistoryAdminForm

@admin.register(MedicalHistory)
class HistoryMedicalAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('patient__username', 'history', 'allergies')
    form = MedicalHistoryAdminForm
