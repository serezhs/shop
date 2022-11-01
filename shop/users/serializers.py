from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "adress",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "adress")
