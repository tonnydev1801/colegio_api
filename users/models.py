#Model created by: Antonio González, antonioglez1801@gmail.com

from django.db import models
from django.contrib.auth.models import AbstractUser

#User model
class User( AbstractUser ):
    #We replace the username by email for make login
    email = models.EmailField( unique=True, error_messages={ 'unique': 'Ya existe un usuario con este email.' } )
    is_teacher = models.BooleanField( default=False )
    is_student = models.BooleanField( default=False )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #Override __str__ method
    def __str__( self ):
        return self.first_name + ' ' + self.last_name + ' - ' + self.email