from rest_framework import generics
from .models import User
from .serializer import UserSerializer
from .permissions import UserEditPermission, UserCreatePermission



class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [UserCreatePermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UserEditPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()
