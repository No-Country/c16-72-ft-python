from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .forms import LoginForm, UserRegisterForm
from .models import User

# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'home/login.html', context)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm()
        
        if request.method == "POST":
            form = LoginForm(request.POST)
            
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            
            if user is None:
                return render(request, 'pages/login.html', context={
                        'form' : form,
                    })
            else:
                login(request, user)
                return redirect('/')
        
class RegisterView(View):
     def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'home/register.html', context)
    
     def post(self, request, *args, **kwargs):
         form = UserRegisterForm()
         
         if request.method == "POST":
            form = UserRegisterForm(request.POST)
            
            if request.POST['password1'] == request.POST['password2']:
            
                try:
                    user = User.objects.create_user(email=request.POST['email'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('/')
                
                except IntegrityError:
                    return render(request, 'home/register.html', context={
                        'form' : UserRegisterFrom,
                    })

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home:login')