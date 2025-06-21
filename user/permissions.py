from rest_framework import permissions
from .models import User


# Clients can only edit their own profile
class UserEditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj == request.user


# Clients can only create account while being logged out
class UserCreatePermission(permissions.BasePermission):
    message = "You are logged in."
    def has_permission(self, request, view):
        return not (request.method == 'POST' and request.user.is_authenticated)


# private accounts can be seen if the viewer is in their following list
class PrivateUserPermission(permissions.BasePermission):
    message = 'This account is private.'
    def has_object_permission(self, request, view, obj):
        print("usrr")
        if request.method in permissions.SAFE_METHODS:
            print("usr23r")
            return not obj.private or request.user in obj.following.all() or request.user.is_superuser
        return True


# private accounts posts can be seen if the viewer is in their following list
class UserPostPermission(permissions.BasePermission):
    message = 'This account is private.'
    def has_permission(self, request, view):
        user = User.objects.get(pk=view.kwargs.get('pk'))
        return not user.private or request.user in user.following.all() or request.user.is_superuser
