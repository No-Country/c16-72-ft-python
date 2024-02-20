from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages

from .forms import LoginForm, UserRegisterForm
from .models import User


# Create your views here.

class RegisterView(View):
     def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'users/register.html', context)
    
     def post(self, request, *args, **kwargs):
         form = UserRegisterForm()
         
         if request.method == "POST":
            form = UserRegisterForm(request.POST)
            
            if request.POST['password1'] == request.POST['password2']:
            
                try:
                    user = User.objects.create_user(
                        email=request.POST['email'], 
                        dni=request.POST['dni'], 
                        name=request.POST['name'], 
                        last_name=request.POST['last_name'], 
                        password=request.POST['password1']
                    )
                    
                    user.save()
                    login(request, user)
                    return redirect('medical_history:index')
                
                except IntegrityError:
                    messages.warning(request, 'El DNI o el Email ya exiten', extra_tags="alert alert-danger")
                    return render(request, 'users/register.html', context={
                        'form' : UserRegisterForm,
                    })
            else:
                messages.warning(request, 'Las contrasenias no coinciden', extra_tags="alert alert-danger")
                return render(request, 'users/register.html', context={
                    'form' : UserRegisterForm,
                })

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'users/login.html', context)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm()
        
        if request.method == "POST":
            form = LoginForm(request.POST)
            
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            
            if user is None:
                messages.warning(request, 'Email o contrasenia incorrectos', extra_tags="alert alert-danger")
                return render(request, 'users/login.html', context={
                        'form' : form,
                    })
            else:
                login(request, user)
                return redirect('medical_history:index')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('users:login')