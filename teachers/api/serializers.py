#Serializer created by: Antonio González, antonioglez1801@gmail.com

from rest_framework import serializers
from users.api.serializers import UserSerializerStaffAuth
from teachers.models import Teacher


class TeacherSerializer( serializers.ModelSerializer ):
    #Meta class
    class Meta:
        model = Teacher
        fields = [ 'genre', 'age', 'user' ]


class PopulateTeacherSerializer( serializers.ModelSerializer ):
    user = UserSerializerStaffAuth()
    #Meta class
    class Meta:
        model = Teacher
        fields = [ 'id', 'genre', 'age', 'user' ]