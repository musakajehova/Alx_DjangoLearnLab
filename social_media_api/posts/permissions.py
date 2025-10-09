from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners can edit/delete; read-only for others.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise only owner (author) can edit/delete
        return getattr(obj, 'author', None) == request.user
