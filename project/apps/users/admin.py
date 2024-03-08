from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustomUserCreationAdminForm, CustomUserChangeAdminForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeAdminForm
    fieldsets = (
        (None, {'fields': ('email', 'dni', 'name', 'last_name', 'age', 'sex', 'groups', 'is_staff', 'is_superuser', 'password')}),
    )
    
    add_form = CustomUserCreationAdminForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'dni', 'name', 'last_name', 'age', 'sex', 'is_staff', 'is_superuser', 'groups' ,'password1', 'password2'),
        }),
    )
    
    list_display = ('email', 'name', 'last_name', 'is_staff') 
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',) 

admin.site.register(User, CustomUserAdmin)

