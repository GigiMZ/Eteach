from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from . import methods

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    age = serializers.IntegerField(write_only=True)

    date_joined = serializers.CharField(read_only=True)
    last_login = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'age', 'profile_pic', 'date_joined', 'last_login']


class DetailUserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'followers', 'following', 'first_name', 'last_name',
                  'email', 'age', 'profile_pic', 'date_joined']
        read_only_fields  = ['id', 'username', 'followers', 'following', 'first_name', 'last_name',
                             'email', 'age', 'profile_pic', 'date_joined'] # TODO add last_login for followers

    def get_followers(self, obj) -> int:
        return len(methods.get_followers_id(obj))

    def get_following(self, obj) -> int:
        return len(obj.following.all())

    def get_email(self, obj) -> str:
        viewer = self.context.get('request').user
        if viewer in obj.following.all() or viewer == obj: return obj.email
        return ""


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    repeat_password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'repeat_password', 'age', 'profile_pic',]

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('repeat_password'):
            raise ValidationError('Password mismatch.')
        validated_data.pop('repeat_password')
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
