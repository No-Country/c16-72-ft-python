from django.urls import path
from django.views.generic import TemplateView

from .views import LoginView, RegisterView, LogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]