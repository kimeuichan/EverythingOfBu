from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer