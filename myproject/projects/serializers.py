from rest_framework import serializers
from .models import Project
from .models import Contributor

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'author', 'created_time']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'project', 'created_time']  # Adjust fields as necessary