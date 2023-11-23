#View created by: Antonio González, antonioglez1801@gmail.com

from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from courses.api.serializers import CourseSerializer,PopulateCourseSerializer
from users.api.permissions import IsStaffAuthenticated

class CoursesApiModelViewSet( ModelViewSet ):
    #Set permission classes
    permission_classes = [ IsStaffAuthenticated ]
    #Set serializer class
    serializer_class = PopulateCourseSerializer
    #Set queryset
    queryset = Course.objects.all()

    #Override the get_serializer_class method to return a different serializer
    def get_serializer_class( self ):
        if self.action == 'list' or self.action == 'retrieve':
            return PopulateCourseSerializer
        else:
            return CourseSerializer