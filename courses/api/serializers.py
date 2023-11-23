#Serializer created by: Antonio González, antonioglez1801@gmail.com

from rest_framework import serializers
from teachers.api.serializers import PopulateTeacherSerializer
from students.api.serializers import PopulateStudentSerializer
from courses.models import Course


class CourseSerializer( serializers.ModelSerializer ):
    #Meta class
    class Meta:
        model = Course
        fields = [ 'title', 'start_date', 'end_date', 'teacher', 'students' ]


class PopulateCourseSerializer( serializers.ModelSerializer ):
    teacher  = PopulateTeacherSerializer()
    students = PopulateStudentSerializer( many=True )
    #Meta class
    class Meta:
        model = Course
        fields = [ 'id', 'title', 'start_date', 'end_date', 'teacher', 'students' ]