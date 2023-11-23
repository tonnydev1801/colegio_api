# Model registered by: Antonio González, antonioglez1801@gmail.com

from django.contrib import admin
from users.models import User
from students.models import Student

@admin.register( Student )
class StudentAdmin( admin.ModelAdmin ):

    #Show in the admin only when is_student is True
    def formfield_for_foreignkey( self, db_field, request, **kwargs ):
        if db_field.name == 'user':
            kwargs[ "queryset" ] = User.objects.filter( is_student=True )
        return super().formfield_for_foreignkey( db_field, request, **kwargs )

    #Get first name from user
    def get_user_first_name( obj ):
        return obj.user.first_name
    get_user_first_name.short_description = 'First name'  # Sets column header in admin panel

    #Get last name from user
    def get_user_last_name( obj ):
        return obj.user.last_name
    get_user_last_name.short_description = 'Last name'  # Sets column header in admin panel

    list_display = [ get_user_first_name, get_user_last_name ]

    #Override __str__ method
    def __str__( self ):
        return self.user.email