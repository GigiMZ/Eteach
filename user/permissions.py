from rest_framework import permissions


class UserEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['PUT', 'PATCH', 'GET'] and obj.username == request.user.username


class UserCreatePermission(permissions.BasePermission):
    message = "You are logged in."
    def has_permission(self, request, view):
        return not (request.method == 'POST' and request.user.is_authenticated)


class PostCreateEditPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated
