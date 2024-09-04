from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("Users must be at least 15 years old.")
        return value

    def update(self, instance, validated_data):
        # If password is in the validated_data, hash it before saving
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            validated_data.pop(
                "password", None
            )  # Remove password from validated_data to avoid double processing
        return super().update(instance, validated_data)
