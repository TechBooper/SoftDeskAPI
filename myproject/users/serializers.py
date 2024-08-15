from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'can_be_contacted', 'can_data_be_shared', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("Users must be at least 15 years old.")
        return value

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        validated_data['password'] = self.validate_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = self.validate_password(validated_data['password'])
        return super().update(instance, validated_data)
