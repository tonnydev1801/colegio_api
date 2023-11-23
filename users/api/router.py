#Router created by: Antonio González, antonioglez1801@gmail.com

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import RegisterUser, AuthUser


urlpatterns = [

    path( 'auth/staff/register', RegisterUser.as_view(), name='staff-register' ),
    path( 'auth/staff/token/', TokenObtainPairView.as_view(), name='staff-login'),
    path( 'auth/staff/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path( 'auth/staff/user', AuthUser.as_view(), name='user_data' )

]