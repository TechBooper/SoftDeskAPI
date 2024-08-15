from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a project to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
