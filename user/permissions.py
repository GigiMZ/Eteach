from rest_framework import permissions


# Clients can only edit their own profile
class UserEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in ['PUT', 'PATCH', 'GET'] and obj.username == request.user.username


# Clients can only create account while being logged out
class UserCreatePermission(permissions.BasePermission):
    message = "You are logged in."
    def has_permission(self, request, view):
        return not (request.method == 'POST' and request.user.is_authenticated)
