from rest_framework import generics
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer
# from .serializers import TopicSerializer, TopicCreateSerializer

class TopicListView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    # def create(self, request, *args,**kwargs):
    #     serializer = TopicSerializer(data=request.data)
    #     # serializer.create(validated_data=request.data)
    #     if serializer.is_valid():
    #         print(request.data)
    #         serializer.create(validated_data=request.data)
    #     print(serializer.errors)
    #     return Response(serializer.data)
