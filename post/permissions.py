from rest_framework import permissions


# Client can only use SAFE_METHODS while logged out and only the creator can modify the post
class CreateEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated or request.user == obj.author
