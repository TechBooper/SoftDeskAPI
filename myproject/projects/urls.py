from django.urls import path
from .views import ProjectViewSet

urlpatterns = [
    path('', ProjectViewSet.as_view({'get': 'list', 'post': 'create'})),  # List all projects, create a new project
    path('<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # Project detail, update, delete
]