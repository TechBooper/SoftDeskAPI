from rest_framework import viewsets, generics, permissions
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View to retrieve and update the authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # This method retrieves the current authenticated user
        return self.request.user
