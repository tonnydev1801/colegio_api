#Serializer created by: Antonio González, antonioglez1801@gmail.com

from rest_framework import serializers
from users.api.serializers import UserSerializerStaffAuth
from students.models import Student


class StudentSerializer( serializers.ModelSerializer ):
    #Meta class
    class Meta:
        model = Student
        fields = [ 'genre', 'age', 'user' ]


class PopulateStudentSerializer( serializers.ModelSerializer ):
    user = UserSerializerStaffAuth()
    #Meta class
    class Meta:
        model = Student
        fields = [ 'id', 'genre', 'age', 'user' ]