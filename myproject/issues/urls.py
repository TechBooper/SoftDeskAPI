from django.urls import path
from .views import IssueViewSet, UpdateIssueStatusView, AssignIssueView

urlpatterns = [
    path('', IssueViewSet.as_view({'get': 'list', 'post': 'create'})),  # List all issues, create a new issue
    path('<int:pk>/', IssueViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/issues/<int:issue_id>/assign/', AssignIssueView.as_view(), name='assign-issue'),
    path('issues/<int:issue_id>/status/', UpdateIssueStatusView.as_view(), name='update-issue-status'),  # Issue detail, update, delete
]