from rest_framework import serializers
from .models import Post, DetailMember

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailMember
        fields = '__all__'