from rest_framework import viewsets
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.permissions import IsAuthenticated

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]