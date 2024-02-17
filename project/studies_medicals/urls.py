from django.urls import path

from .views import ListStudiesMedicalsView

urlpatterns = [
    path('', ListStudiesMedicalsView.as_view(), name='studiesmedicals_list'),
]
