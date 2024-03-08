from django.urls import path

from .views import (
    ListTypeStudieMedicalView,
    ListStudiesMedicalsView,
    ListStudiesMedicalsInTypesView,
    StudieMedicalFileDownload,
    DetailStudieMedicalView,
    CreateStudieMedicalView, 
    UpdateStudieMedicalView, 
    delete_studieMedical_view
)

urlpatterns = [
    
    #urls paciente y medico
    path('', ListStudiesMedicalsView.as_view(), name='studiesmedicals_list'),
    path('file/<int:pk>', StudieMedicalFileDownload.as_view(), name='studiesmedicals_download'),
    
    
    #urls paciente
    path('type/', ListTypeStudieMedicalView.as_view(), name='studiesmedicals_type'),
    path('type/studies/<int:pk_type>', ListStudiesMedicalsInTypesView.as_view(), name='studiesmedicals_studies'),

    #urls medico
    path('type/<int:pk>', ListTypeStudieMedicalView.as_view(), name='studiesmedicals_type'),
    path('type/studies/<int:pk_patient>/<int:pk_type>', ListStudiesMedicalsInTypesView.as_view(), name='studiesmedicals_studies'),
    path('create', CreateStudieMedicalView.as_view(), name='studiesmedicals_create'),
    path('detail/<int:pk>', DetailStudieMedicalView.as_view(), name='studiesmedicals_detail'),
    path('update/<int:pk>', UpdateStudieMedicalView.as_view(), name='studiesmedicals_update'),
    path('delete/<int:pk>', delete_studieMedical_view, name='studiesmedicals_delete'),
]
