from rest_framework import serializers
from .models import Project
from .models import Contributor

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'author', 'created_time']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def get_queryset(self):
        return Project.objects.all().order_by('id') 
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'project', 'created_time']