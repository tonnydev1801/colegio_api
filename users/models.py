#Model created by: Antonio González, antonioglez1801@gmail.com

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


#Model User
class User( AbstractBaseUser ):
    # Replace the username field with email for authentication 
    email = models.EmailField( unique=True, error_messages={'unique': 'This email has been registered.'} )
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []