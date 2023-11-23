"""colegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from teachers.api.router import router as teachers_router
from courses.api.router import router as courses_router
from students.api.router import router as students_router

schema_view = get_schema_view(

    openapi.Info(

        title="Colegio API",
        default_version='v1',
        description="This is the API documentation.",
        terms_of_service="",
        contact=openapi.Contact( email="antonioglez1801@gmail.com" ),
        license=openapi.License( name="BSD License" )

   ),
   public=True,
   #permission_classes=( permissions.AllowAny, )

)

urlpatterns = [

    path( 'admin/', admin.site.urls ),
    path( 'api/docs/', schema_view.with_ui( 'redoc', cache_timeout=0), name='schema-redoc' ),
    path( 'api/', include( 'users.api.router' ) ),
    path( 'api/', include( teachers_router.urls ) ),
    path( 'api/', include( courses_router.urls ) ),
    path( 'api/', include( students_router.urls ) )

]