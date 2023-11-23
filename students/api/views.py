#View created by: Antonio González, antonioglez1801@gmail.com

from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.api.serializers import StudentSerializer, PopulateStudentSerializer
from teachers.api.permissions import IsStaffOrReadOnly

class StudentApiModelViewSet( ModelViewSet ):
    #Set permission classes
    permission_classes = [ IsStaffOrReadOnly ]
    #Set serializer class
    serializer_class = PopulateStudentSerializer
    #Set queryset
    queryset = Student.objects.all()

    #Override the get_serializer_class method to return a different serializer
    def get_serializer_class( self ):
        if self.action == 'list' or self.action == 'retrieve':
            return PopulateStudentSerializer
        else:
            return StudentSerializer