from rest_framework import serializers
from .models import Comment, Post, Tag


class PostSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    views = serializers.IntegerField(read_only=True)

    image = serializers.ImageField(write_only=True, allow_null=True)

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'image', 'tags',
                  'date', 'vote_up', 'vote_down', 'views']


class DetailPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()

    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    views = serializers.IntegerField(read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'author','title', 'content', 'image', 'tags',
                  'comments', 'date', 'vote_up', 'vote_down', 'views']
        read_only_fields  = ['date', 'author']

    def get_comments(self, obj):
        # comments: list = list(obj.comments.all())
        # ordered_comments = {}
        # for comment in comments:
        #     if not comment.comment:
        #         ordered_comments[comment.id] = {}
        #         comments.remove(comment)
        # for comment in comments:
        #     if comment.comment.id in ordered_comments.keys():
        #         ordered_comments[comment.comment.id][comment.id] = {}
        #
        #
        # print(ordered_comments)
        return [comment.content for comment in obj.comments.all()]


class CommentSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'comment', 'vote_up', 'vote_down', 'post', 'date']

    def get_comment(self, obj):
        return CommentSerializer(obj.comment).data

class TagSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Tag
        fields = ['id', 'name', 'posts']
