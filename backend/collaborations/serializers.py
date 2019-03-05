from rest_framework import serializers
from .models import Post, DetailMember
from django.contrib.auth.models import User
from rest_framework import permissions

class PostSerializer(serializers.ModelSerializer):
    writter = serializers.ReadOnlyField(source='writter.username')
    permission_classes = (permissions.IsAdminUser,)
    class Meta:
        model = Post
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailMember
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'posts')