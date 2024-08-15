from django.urls import path
from .views import CommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),  # List all comments, create a new comment
    path('<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # Comment detail, update, delete
]