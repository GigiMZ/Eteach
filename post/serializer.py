from rest_framework import serializers
from .models import Comment, Post, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'image', 'tags', 'comment', 'vote_up', 'vote_down', 'views']
        read_only_fields  = ['date']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'parent', 'vote_up', 'vote_down', 'views']
        read_only_fields = ['date']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'