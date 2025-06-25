from rest_framework import serializers

from .models import Comment, Post, Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    post_author = serializers.SerializerMethodField()
    date = serializers.DateTimeField(read_only=True)
    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, slug_field='name')

    image = serializers.ImageField(write_only=True, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'post_author', 'title', 'content', 'image', 'tags',
                  'date', 'vote_up', 'vote_down', 'views']

    def get_post_author(self, obj):
        return obj.author.username


class DetailPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()
    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    views = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, slug_field='name')

    class Meta:
        model = Post
        fields = ['id', 'author','title', 'content', 'image', 'tags',
                  'comments', 'date', 'vote_up', 'vote_down', 'views']

    def get_comments(self, obj):
        return CommentSerializer(instance=obj.comments.filter(comment_id=None), many=True).data


class CommentSerializer(serializers.ModelSerializer):

    class PostsComments(serializers.PrimaryKeyRelatedField):
        def get_queryset(self):
            return Comment.objects.filter(post_id=self.context.get('view').kwargs['pos_pk'])

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    parrent_comment = PostsComments(source='comment', write_only=True, allow_null=True)
    replies = serializers.SerializerMethodField(source='comment')

    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'parrent_comment', 'content', 'vote_up', 'vote_down', 'date', 'replies']

    def get_replies(self, obj):
        return CommentSerializer(instance=obj.replies, many=True).data


class DetailCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    replies = serializers.SerializerMethodField(source='comment')

    vote_up = serializers.IntegerField(read_only=True)
    vote_down = serializers.IntegerField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'replies', 'vote_up', 'vote_down', 'date']

    def get_replies(self, obj):
        return CommentSerializer(instance=obj.replies, many=True).data


class TagSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Tag
        fields = ['id', 'name', 'posts']
