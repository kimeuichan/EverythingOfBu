from rest_framework import serializers
from .models import Post, DetailMember
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
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