from rest_framework.serializers import ModelSerializer
from .models import User


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user