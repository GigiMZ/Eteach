from rest_framework import serializers
from .models import Comment, Post, Tag

# TODO fix serializer
class PostSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.username')
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'image', 'tags', 'comment', 'vote_up', 'vote_down', 'views']
        read_only_fields  = ['date', 'author']

    def get_comment(self, obj):
        return CommentSerializer(obj.comment).data

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.CharField(source='author.username', read_only=True)
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'comment', 'vote_up', 'vote_down']
        read_only_fields = ['date']

    def get_comment(self, obj):
        return CommentSerializer(obj.comment).data

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
