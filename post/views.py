from rest_framework import generics
from .serializer import PostSerializer, CommentSerializer, TagSerializer
from .models import Post, Comment, Tag
from .permissions import CreateEditPermission

from django.db.models import F


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = self.get_object()
            post.views = F('views') + 1
            post.save()
        return super().get(request, *args, **kwargs)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class TagListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CreateEditPermission]

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
