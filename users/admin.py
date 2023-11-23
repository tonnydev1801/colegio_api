# Model registered by: Antonio González, antonioglez1801@gmail.com

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register( User )
class UserAdmin( BaseUserAdmin ):
    #List display
    list_display = [ 'email', 'is_teacher', 'is_student', 'is_staff' ]
    #Set fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        ( 'User type', 
            {
                'fields': ( 'is_teacher', 'is_student' )
            } 
        ),
    )