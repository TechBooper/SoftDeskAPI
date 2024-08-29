from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from myapp.views import RegisterView, LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from projects.views import ProjectViewSet, AddContributorView, RemoveContributorView
from issues.views import IssueViewSet, AssignIssueView, UpdateIssueStatusView
from comments.views import CommentViewSet
from django.urls import path


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/projects/', include('projects.urls')),  
    path('api/comments/', include('comments.urls')),  
    path('api/issues/', include('issues.urls')),      
    path('api/users/', include('users.urls')),
    path('api/projects/<int:project_id>/contributors/add/', AddContributorView.as_view(), name='add-contributor'),
    path('api/projects/<int:project_id>/contributors/remove/<int:user_id>/', RemoveContributorView.as_view(), name='remove-contributor'),
    path('api/issues/<uuid:issue_id>/assign/', AssignIssueView.as_view(), name='assign_issue'),
    path('api/issues/<uuid:issue_id>/status/', UpdateIssueStatusView.as_view(), name='update-issue-status'),
    path('api/comments/<uuid:pk>/', CommentViewSet.as_view({'get': 'retrieve'}), name='comment-detail'),
]        
