# Model registered by: Antonio González, antonioglez1801@gmail.com

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register( User )
class AdminUser( BaseUserAdmin ):
    pass