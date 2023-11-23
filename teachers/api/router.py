from rest_framework.routers import DefaultRouter
from teachers.api.views import TeacherApiModelViewSet

router = DefaultRouter()
router.register( prefix='teachers', viewset=TeacherApiModelViewSet, basename='teachers' )