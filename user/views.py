from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User
from post.models import Post
from .serializer import UserSerializer, RegisterSerializer
from post.serializer import PostSerializer
from .permissions import (UserEditPermission, UserCreatePermission, PrivateUserPermission, UserPostPermission,
                          RegisterPermission)


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [UserCreatePermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UserEditPermission, PrivateUserPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, pk, *args, **kwargs):
    undo = request.data.get('undo')
    user = request.user
    selected_user = User.objects.get(pk=pk)

    if selected_user.id == user.id:
        return Response({'message': 'Can\'t unfollow yourself.' if undo else 'Can\'t follow yourself.'}, status=400)
    if (selected_user in user.following.all() and not undo) or (undo and selected_user not in user.following.all()):
        return Response({'message': 'Not following user.' if undo else 'Already following user.'}, status=400)

    if undo:
        user.following.remove(selected_user)
        return Response({'message': 'success'}, status=200)

    user.following.add(selected_user)
    return Response({'message': 'success'}, status=200)


class UserPostListAPIView(generics.ListAPIView):
    permission_classes = [UserPostPermission]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.filter(author_id=self.kwargs.get('pk'))


class Register(generics.CreateAPIView):
    permission_classes = [RegisterPermission]

    serializer_class = RegisterSerializer
    queryset = User.objects.all()
