from rest_framework import permissions
from .methods import get_posts


# Client can only use SAFE_METHODS while logged out
class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_authenticated


# Only the creator and superuser can use non SAFE_METHODS
class EditPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj.author or request.method in permissions.SAFE_METHODS


# Only non-private users posts comments and viewers followers posts comments are visible to viewer
class ListCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.kwargs.get('pos_pk') in get_posts(request.user)



class DetailCommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.post)
        print(get_posts(request.user))
        return obj.post in get_posts(request.user)