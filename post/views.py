from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializer import PostSerializer, DetailPostSerializer, CommentSerializer, DetailCommentSerializer, TagSerializer
from .models import Post, Comment, Tag
from user.models import User
from .permissions import CreatePermission, EditPermission, ListCommentPermission, DetailCommentPermission
from .methods import get_posts

from django.db.models import F


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreatePermission]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return get_posts(self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [EditPermission]

    serializer_class = DetailPostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return get_posts(self.request.user)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = self.get_object()
            post.views = F('views') + 1
            post.save()
        return super().get(request, *args, **kwargs)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_up_vote(request, pk, *args, **kwargs):
    undo = request.data.get('undo')
    post = Post.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)

    if undo:
        if post not in request.user.up_voted_posts.all():  return Response({'message': 'Invalid Operation.'}, status=400)
        post.vote_up = F('vote_up') - 1
        post.save()
        user.up_voted_posts.remove(post)
        user.save()
        return Response({'message': 'success'}, status=200)

    if post in request.user.up_voted_posts.all() or post in request.user.down_voted_posts.all():
        return Response({'message': 'Already voted.'}, status=400)

    post.vote_up = F('vote_up') + 1
    post.save()
    user.up_voted_posts.add(post)
    user.save()
    return Response({'message': 'success'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_down_vote(request, pk, *args, **kwargs):
    undo = request.data.get('undo')
    post = Post.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.id)

    if undo:
        if post not in request.user.down_voted_posts.all():  return Response({'message': 'Invalid Operation.'}, status=400)
        post.vote_down = F('vote_down') - 1
        post.save()
        user.down_voted_posts.remove(post)
        user.save()
        return Response({'message': 'success'}, status=200)

    if post in request.user.down_voted_posts.all() or post in request.user.up_voted_posts.all():
        return Response({'message': 'Already voted.'}, status=400)

    post.vote_down = F('vote_down') + 1
    post.save()
    user.down_voted_posts.add(post)
    user.save()
    return Response({'message': 'success'}, status=200)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreatePermission, ListCommentPermission]

    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pos_pk')
        return Comment.objects.filter(post_id=post_id, comment=None)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pos_pk')
        serializer.save(post_id=post_id)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [EditPermission, DetailCommentPermission]

    serializer_class = DetailCommentSerializer
    queryset = Comment.objects.all()

@api_view(['POST'])
@permission_classes([IsAuthenticated, DetailCommentPermission])
def comment_up_vote(request, com_pk, *args, **kwargs):
    undo = request.data.get('undo')
    comment = Comment.objects.get(pk=com_pk)
    user = User.objects.get(pk=request.user.id)

    if undo:
        if comment not in request.user.up_voted_comments.all():  return Response({'message': 'Invalid Operation.'}, status=400)
        comment.vote_up = F('vote_up') - 1
        comment.save()
        user.up_voted_comments.remove(comment)
        user.save()
        return Response({'message': 'success'}, status=200)

    if comment in request.user.up_voted_comments.all() or comment in request.user.down_voted_comments.all():
        return Response({'message': 'Already voted.'}, status=400)

    comment.vote_up = F('vote_up') + 1
    comment.save()
    user.up_voted_comments.add(comment)
    user.save()
    return Response({'message': 'success'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated, DetailCommentPermission])
def comment_down_vote(request, com_pk, *args, **kwargs):
    undo = request.data.get('undo')
    comment = Comment.objects.get(pk=com_pk)
    user = User.objects.get(pk=request.user.id)

    if undo:
        if comment not in request.user.down_voted_comments.all():  return Response({'message': 'Invalid Operation.'}, status=400)
        comment.vote_down = F('vote_down') - 1
        comment.save()
        user.down_voted_comments.remove(comment)
        user.save()
        return Response({'message': 'success'}, status=200)

    if comment in request.user.up_voted_comments.all() or comment in request.user.down_voted_comments.all():
        return Response({'message': 'Already voted.'}, status=400)

    comment.vote_down = F('vote_down') + 1
    comment.save()
    user.down_voted_comments.add(comment)
    user.save()
    return Response({'message': 'success'}, status=200)


class TagListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CreatePermission]

    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
