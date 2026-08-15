from django.urls import path
from .views import RegistrationApiView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('registration/', RegistrationApiView.as_view(), name='registration'),
    path('login/', obtain_auth_token, name='login'),
    path('jwt/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
]