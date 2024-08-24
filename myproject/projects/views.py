from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import ProjectSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .serializers import ContributorSerializer
from users.models import User


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a project to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class AddContributorView(generics.CreateAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['project_id'])
        user = User.objects.get(id=request.data['user_id'])
        
        # Check if the request user is the author of the project
        if project.author != request.user:
            return Response({"detail": "You do not have permission to add contributors to this project."},
                            status=status.HTTP_403_FORBIDDEN)

        # Add the contributor
        Contributor.objects.create(project=project, user=user)
        return Response({"detail": "Contributor added successfully."}, status=status.HTTP_201_CREATED)

class RemoveContributorView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['project_id'])
        user = User.objects.get(id=kwargs['user_id'])
        
        # Check if the request user is the author of the project
        if project.author != request.user:
            return Response({"detail": "You do not have permission to remove contributors from this project."},
                            status=status.HTTP_403_FORBIDDEN)

        # Remove the contributor
        Contributor.objects.filter(project=project, user=user).delete()
        return Response({"detail": "Contributor removed successfully."}, status=status.HTTP_204_NO_CONTENT)