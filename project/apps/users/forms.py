from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

class UserRegisterForm(CustomUserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'dni', 'email', 'sex', 'age', 'password1', 'password2']
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'DNI',
            'email': 'Correo electrónico',
            'sex': 'Género',
            'age': 'Edad',
        }

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Correo electrónico'
        self.fields['password'].label = 'Contraseña'

class LoginForm(CustomAuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']