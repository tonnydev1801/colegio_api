#Model created by: Antonio González, antonioglez1801@gmail.com

from django.db import models
from users.models import User


#Student model
class Student( models.Model ):
    #fields
    genre      = models.CharField( max_length = 10 )
    age        = models.IntegerField()
    user       = models.ForeignKey( User, on_delete=models.CASCADE, related_name='students', blank=True, null=True )

    #Override __str__ method
    def __str__( self ):
        return self.user.first_name + ' ' + self.user.last_name + ' - ' + self.user.email