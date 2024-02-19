from django.urls import path

from .views import ListStudiesMedicalsView, DetailStudieMedicalView, CreateStudieMedical, UpdateStudieMedical, delete_studieMedical_view

urlpatterns = [
    path('', ListStudiesMedicalsView.as_view(), name='studiesmedicals_list'),
    path('create', CreateStudieMedical.as_view(), name='studiesmedicals_create'),
    path('detail/<int:pk>', DetailStudieMedicalView.as_view(), name='studiesmedicals_detail'),
    path('update/<int:pk>', UpdateStudieMedical.as_view(), name='studiesmedicals_update'),
    path('delete/<int:pk>', delete_studieMedical_view, name='studiesmedicals_delete'),
]
