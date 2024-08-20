from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from myapp.views import RegisterView, LoginView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from projects.views import ProjectViewSet, AddContributorView, RemoveContributorView
from issues.views import IssueViewSet
from comments.views import CommentViewSet


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
    path("admin/", admin.site.urls),
    path('projects/<int:project_id>/contributors/', AddContributorView.as_view(), name='add-contributor'),
    path('api/projects/<int:project_id>/contributors/<int:user_id>/', RemoveContributorView.as_view(), name='remove-contributor'),
]        
