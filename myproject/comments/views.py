from rest_framework import viewsets
from .serializers import CommentSerializer
from myapp.permissions import IsContributor, IsAuthorOrReadOnly
from comments.models import Comment
import uuid


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsContributor, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def check_uuid_validity():
        comments = Comment.objects.all()
        for comment in comments:
            try:
                uuid_obj = uuid.UUID(str(comment.id))
                print(f"Comment ID {comment.id} is a valid UUID.")
            except ValueError:
                print(f"Comment ID {comment.id} is not a valid UUID!")

    if __name__ == "__main__":
        check_uuid_validity()
