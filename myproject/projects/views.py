from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Project, Contributor
from .serializers import ProjectSerializer
from myapp.permissions import IsAuthorOrReadOnly, IsContributor, IsProjectAuthor
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .serializers import ContributorSerializer
from users.models import User
from rest_framework.exceptions import ValidationError


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AddContributorView(generics.CreateAPIView):
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

    def post(self, request, *args, **kwargs):

        project = Project.objects.get(id=kwargs["project_id"])
        user = User.objects.get(id=request.data["user_id"])

        Contributor.objects.create(project=project, user=user)
        return Response(
            {"detail": "Contributor added successfully."},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, *args, **kwargs):
        project = self.get_object()
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RemoveContributorView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

    def delete(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs["project_id"])
        user_id = kwargs.get("user_id")

        if not user_id:
            return Response(
                {"detail": "user_id is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(id=user_id)

        project.contributors.remove(user)
        return Response(
            {"detail": "Contributor removed successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
