from rest_framework import serializers
from .models import User
# TODO create serializer class for DetailUser


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


    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
