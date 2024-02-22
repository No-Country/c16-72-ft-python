from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # HISTORIAS CLINICAS
    path("history/detail/<int:pk>", views.MedicalHistoryDetail.as_view(), name="medicalhistory_detail"),
    path("history/list/", views.MedicalHistoryList.as_view(), name="medicalhistory_list"),
    path("history/create/", views.MedicalHistoryCreateView.as_view(), name="medicalhistory_create"),
    path("history/delete/<int:pk>", views.MedicalHistoryDelete.as_view(), name="medicalhistory_delete"),
    path("history/update/<int:pk>", views.MedicalHistoryUpdate.as_view(), name="medicalhistory_update"),
    # ESTUDIOS
]