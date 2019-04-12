from rest_framework import generics
from .models import Topic
from .serializers import TopicSerializer

class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    # def perform_create(self, serializer):