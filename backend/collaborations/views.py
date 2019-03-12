from .models import Post, NeedMember 
from .serializers import PostSerializer, UserSerializer, MemberSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('uesr-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        'members': reverse('member-list', request=request, format=format),
    })

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        print("here")
        serializer.save(writter=self.request.user)

# Create your views here.

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MemberList(generics.ListCreateAPIView):
    queryset = NeedMember.objects.all()
    serializer_class = MemberSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer