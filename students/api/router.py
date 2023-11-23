from rest_framework.routers import DefaultRouter
from students.api.views import StudentApiModelViewSet

router = DefaultRouter()
router.register( prefix='students', viewset=StudentApiModelViewSet, basename='students' )