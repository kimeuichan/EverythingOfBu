from .models import Post, DetailMember
from .serializers import PostSerializer, MemberSerializer
from rest_framework import generics

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.

class MemberListCreate(generics.ListCreateAPIView):
    queryset = DetailMember.objects.all()
    serializer_class = MemberSerializer
