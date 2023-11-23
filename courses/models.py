#Model created by: Antonio González, antonioglez1801@gmail.com

from django.db import models
from teachers.models import Teacher
from students.models import Student


#teacher model
class Course( models.Model ):
    #fields
    title       = models.CharField( max_length = 255 )
    description = models.TextField()
    area        = models.CharField( max_length = 255 )
    start_date  = models.DateField()
    end_date    = models.DateField()
    teacher     = models.ForeignKey( Teacher, on_delete=models.SET_NULL, related_name='teachers', blank=True, null=True )
    students    = models.ManyToManyField( Student, related_name='students' )
    #Override __str__ method
    def __str__( self ):
        return self.title