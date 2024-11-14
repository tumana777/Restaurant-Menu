from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer