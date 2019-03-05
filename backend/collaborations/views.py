from .models import Post, DetailMember 
from .serializers import PostSerializer, MemberSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(writter=self.request.user)
# Create your views here.

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MemberListCreate(generics.ListCreateAPIView):
    queryset = DetailMember.objects.all()
    serializer_class = MemberSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer