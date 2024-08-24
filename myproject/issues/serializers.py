from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'project', 'author', 'assignee', 'priority', 'tag', 'status', 'created_time']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
