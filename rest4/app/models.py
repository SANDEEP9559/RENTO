from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
#Create your CustomUserMnager here.
class CustomUserManager(BaseUserManager):


#Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField()

