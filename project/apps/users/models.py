from django.db import models
from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Debes tener un correo electronico")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    #modificacion funcion model User create de usuario comun => paciente
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        return self._create_user(email, password, **extra_fields)
    
    #modificacion del comando createsuperuser consola del modelo User
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        #Pedir por consola dni
        dni = input("DNI: ")
        extra_fields['dni'] = dni
        
        if not dni:
            raise ValueError("Debes tener un numero de identificacion")
        
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    
    SEX_USER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    email = models.CharField(max_length=100, unique=True)
    dni = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    sex = models.CharField(max_length=10, choices=SEX_USER, default='Male')
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    class Meta:
        ordering = ["-date_joined"]
        
    def __str__(self):        
        return f'{self.dni}'
    

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
     if created and not instance.is_superuser:
        try:
            group = Group.objects.get(name="Patients")
        except Group.DoesNotExist:
            group = Group.objects.create(name="Patients")
        group.user_set.add(instance)

