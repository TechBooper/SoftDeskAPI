from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import ProjectSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .serializers import ContributorSerializer
from users.models import User
from rest_framework.exceptions import ValidationError


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
    permission_classes = [IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise ValidationError("User must be authenticated to create a project.")
        # Save the project with the current user as the author
        project = serializer.save(author=self.request.user)
        # Optionally add the author as a contributor as well
        project.contributors.add(self.request.user)


class AddContributorView(generics.CreateAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Retrieve the project and user based on the provided IDs
        project = Project.objects.get(id=kwargs['project_id'])
        user = User.objects.get(id=request.data['user_id'])
        
        # Debug print to check request user and project author
        print(f"Request user: {request.user}, Project author: {project.author}")
        print(f"Project ID: {project.id}, User ID: {request.user.id}")

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
        user_id = kwargs.get('user_id')
        
        if not user_id:
            return Response({"detail": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id=user_id)

        if project.author != request.user:
            return Response({"detail": "You do not have permission to remove contributors from this project."},
                            status=status.HTTP_403_FORBIDDEN)

        project.contributors.remove(user)
        return Response({"detail": "Contributor removed successfully."}, status=status.HTTP_204_NO_CONTENT)