from django.urls import path
from .views import IssueViewSet

urlpatterns = [
    path('', IssueViewSet.as_view({'get': 'list', 'post': 'create'})),  # List all issues, create a new issue
    path('<int:pk>/', IssueViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # Issue detail, update, delete
]