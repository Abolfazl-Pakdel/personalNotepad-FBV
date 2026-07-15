from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', loginPage, name='login' ),
    path("logout/", logoutUser, name="logout"),
    path("register/", register_view, name="register"),
]