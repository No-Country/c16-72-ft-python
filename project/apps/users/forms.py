from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={'class':''}),
        required=True
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={'class':''}),
        required=True
    )
    class Meta:
        model = User
        fields = ['name', 'last_name', 'dni', 'email', 'sex', 'age', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password1']