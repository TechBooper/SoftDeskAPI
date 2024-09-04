from rest_framework import viewsets
from .serializers import IssueSerializer
from myapp.permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Issue, Project
from users.models import User
from rest_framework.permissions import IsAuthenticated


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user  # Custom User
        serializer.save(author=user)


class AssignIssueView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs["issue_id"])
        project = issue.project
        assignee = User.objects.get(id=request.data["user_id"])

        # Check if the user is a contributor to the project
        if not project.contributors.filter(id=assignee.id).exists():
            return Response(
                {"detail": "User is not a contributor to this project."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        issue.assignee = assignee
        issue.save()

        return Response(
            {"detail": "Issue assigned successfully."}, status=status.HTTP_200_OK
        )


class UpdateIssueStatusView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        issue = Issue.objects.get(id=kwargs["issue_id"])
        status_value = request.data.get("status")

        if status_value not in ["To Do", "In Progress", "Finished"]:
            return Response(
                {"detail": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST
            )

        issue.status = status_value
        issue.save()

        return Response(
            {"detail": "Issue status updated successfully."}, status=status.HTTP_200_OK
        )
