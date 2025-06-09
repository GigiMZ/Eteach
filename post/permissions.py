from rest_framework import permissions


# Client can only use SAFE_METHODS while logged out and only the creator can modify the post
class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated


class EditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj.author or request.method in permissions.SAFE_METHODS
