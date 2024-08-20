from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View to retrieve and update the authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)
