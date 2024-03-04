from django.urls import path
from django.views.generic import TemplateView
from . import views

from .utils import check_and_create_groups_and_models 

check_and_create_groups_and_models()


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]