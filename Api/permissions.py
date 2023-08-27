from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # authenticated user only can see the list
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # read permission are always allowd
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

        
