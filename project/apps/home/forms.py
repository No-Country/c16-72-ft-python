from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password1']