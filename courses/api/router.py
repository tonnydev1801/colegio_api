from rest_framework.routers import DefaultRouter
from courses.api.views import CoursesApiModelViewSet

router = DefaultRouter()
router.register( prefix='courses', viewset=CoursesApiModelViewSet, basename='courses' )