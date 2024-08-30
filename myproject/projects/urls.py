from django.urls import path
from .views import ProjectViewSet
from .views import AddContributorView, RemoveContributorView

urlpatterns = [
    path('', ProjectViewSet.as_view({'get': 'list', 'post': 'create'})),  # List all projects, create a new project
    path('<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:project_id>/contributors/', AddContributorView.as_view(), name='add-contributor'), # Project detail, update, delete
    path('<int:project_id>/contributors/<int:user_id>/', RemoveContributorView.as_view(), name='remove-contributor'),  # Project detail, update, delete
]