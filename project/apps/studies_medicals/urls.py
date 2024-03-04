from django.urls import path

from .views import (
    ListTypeStudieMedical,
    ListStudiesMedicalsView,
    ListStudiesMedicalsInTypesView,
    StudieMedicalPatientPDF,
    DetailStudieMedicalView,
    CreateStudieMedical, 
    UpdateStudieMedical, 
    delete_studieMedical_view
)

urlpatterns = [
    path('', ListStudiesMedicalsView.as_view(), name='studiesmedicals_list'),
    path('type/', ListTypeStudieMedical.as_view(), name='studiesmedicals_type'),
    path('type/<int:pk>', ListTypeStudieMedical.as_view(), name='studiesmedicals_type'),
    path('type/studies/<int:pk_type>', ListStudiesMedicalsInTypesView.as_view(), name='studiesmedicals_studies'),
    path('type/studies/<int:pk_patient>/<int:pk_type>', ListStudiesMedicalsInTypesView.as_view(), name='studiesmedicals_studies'),
    path('create', CreateStudieMedical.as_view(), name='studiesmedicals_create'),
    path('detail/<int:pk>', DetailStudieMedicalView.as_view(), name='studiesmedicals_detail'),
    path('pdf/<int:pk>', StudieMedicalPatientPDF.as_view(), name='studiesmedicals_pdf_patient'),
    path('update/<int:pk>', UpdateStudieMedical.as_view(), name='studiesmedicals_update'),
    path('delete/<int:pk>', delete_studieMedical_view, name='studiesmedicals_delete'),
]
