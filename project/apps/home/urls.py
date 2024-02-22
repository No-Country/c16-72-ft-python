from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('', HomeView.as_view(), name='home'),
]