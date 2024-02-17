from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # HISTORIAS CLINICAS
    path("historia/detail/<int:pk>", views.HistoriaClinicaDetail.as_view(), name="historiaclinica_detail"),
    path("historia/list/", views.HistoriaClinicaList.as_view(), name="historiaclinica_list"),
    path("historia/create/", views.HistoriaClinicaCreateView.as_view(), name="historiaclinica_create"),
    path("historia/delete/<int:pk>", views.HistoriaClinicaDelete.as_view(), name="historiaclinica_delete"),
    path("historia/update/<int:pk>", views.HistoriaClinicaUpdate.as_view(), name="historiaclinica_update"),
    # ESTUDIOS
    path("historia/study/list/", views.EstudioList.as_view(), name="estudio_list"),
]