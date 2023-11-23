#View created by: Antonio González, antonioglez1801@gmail.com

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from teachers.models import Teacher
from teachers.api.serializers import TeacherSerializer, PopulateTeacherSerializer
from teachers.api.permissions import IsStaffOrReadOnly

class TeacherApiModelViewSet( ModelViewSet ):
    #Set permission classes
    permission_classes = [ IsStaffOrReadOnly ]
    #Set serializer class
    serializer_class = PopulateTeacherSerializer
    #Set queryset
    queryset = Teacher.objects.all()
    #Override the get_serializer_class method to return a different serializer
    def get_serializer_class( self ):
        if self.action == 'list' or self.action == 'retrieve':
            return PopulateTeacherSerializer
        else:
            return TeacherSerializer





