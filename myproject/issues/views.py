from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import IssueSerializer
from myapp.permissions import IsAuthorOrReadOnly, IsContributor, IsProjectAuthor
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Issue, Project
from users.models import User
from rest_framework.permissions import IsAuthenticated


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AssignIssueView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsContributor]

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, id=kwargs["issue_id"])
        project = issue.project
        assignee = get_object_or_404(User, id=request.data["user_id"])

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
    permission_classes = [IsAuthenticated, IsContributor]

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, id=kwargs["issue_id"])
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