from rest_framework import generics
from .serializers import RegistrationSerializer


class RegistrationApiView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
