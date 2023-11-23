# Model registered by: Antonio González, antonioglez1801@gmail.com

from django.contrib import admin
from courses.models import Course
from teachers.models import Teacher

@admin.register( Course )
class CourseAdmin( admin.ModelAdmin ):

    #Get first name from user
    def get_teacher_name( obj ):
        return obj.teacher.user.first_name + ' ' + obj.teacher.user.last_name
    get_teacher_name.short_description = 'Teacher'  # Sets column header in admin panel

    #Display fields
    list_display = [ 'title', 'start_date', 'end_date', get_teacher_name ]

    #Override __str__ method
    def __str__( self ):
        return self.title