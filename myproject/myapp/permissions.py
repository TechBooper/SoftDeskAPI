from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsContributor(BasePermission):
    """
    Custom permission to check if the user is a contributor to the project.
    """

    def has_object_permission(self, request, view, obj):
        project = obj.project if hasattr(obj, "project") else obj
        return request.user in project.contributors.all()


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a resource to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
