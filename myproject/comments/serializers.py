from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue', 'author', 'created_time']
        read_only_fields = ['author']

    def create(self, validated_data):
        # Automatically set the author to the current authenticated user
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)