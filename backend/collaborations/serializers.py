from rest_framework import serializers
from .models import Post, DetailMember
from django.contrib.auth.models import User
from rest_framework import permissions

class PostSerializer(serializers.ModelSerializer):
    writter = serializers.ReadOnlyField(source='writter.username')
    # writter = serializers.CharField(read_only=True, source='writter.username')
    class Meta:
        model = Post
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailMember
        fields = '__all__'

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'posts')