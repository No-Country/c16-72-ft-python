from django.contrib import admin

from .models import TypeStudieMedical, StudiesMedicals
from .forms import StudiesMedicalAdminForm

# Register your models here.

admin.site.register(TypeStudieMedical)

@admin.register(StudiesMedicals)
class StudiesMedicalAdmin(admin.ModelAdmin):
    form = StudiesMedicalAdminForm