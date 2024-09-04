from rest_framework import serializers
from .models import Issue
from rest_framework.exceptions import PermissionDenied
from users.models import User


class IssueSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    assignee = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "project",
            "author",
            "assignee",
            "priority",
            "label",
            "status",
            "created_time",
        ]
