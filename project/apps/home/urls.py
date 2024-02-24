from django.urls import path
from django.views.generic import TemplateView

from .views import LoginView, RegisterView, LogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #urls ubi provisoria
    path('dashboard', TemplateView.as_view(template_name='home/dashboard.html'), name='dashboard'),
    path('examenes', TemplateView.as_view(template_name='examenes/index.html'), name='examenes'),
    path('perfiles_lipidicos', TemplateView.as_view(template_name='examenes/perfiles_lipidicos.html'), name='perfiles_lipidicos'),
    path('perfil_lipidico', TemplateView.as_view(template_name='examenes/perfil_lipidico.html'), name='perfil_lipidico'),
    path('hormonas_tiroideas', TemplateView.as_view(template_name='examenes/hormonas_tiroideas.html'), name='hormonas_tiroideas'),
    path('hormonas_tiroideas_all', TemplateView.as_view(template_name='examenes/hormonas_tiroideas_all.html'), name='hormonas_tiroideas_all'),
]