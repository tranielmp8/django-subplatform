from django.db import models
from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your CUSTOM USER models and other models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
  
  username = None # tell django this field is not needed
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=80)
  last_name = models.CharField(max_length=135)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(default=timezone.now)
  
  is_writer = models.BooleanField(default=False, verbose_name="Are you a writer?")
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  objects = CustomUserManager()
  
  def __str__(self):
    return self.email 





