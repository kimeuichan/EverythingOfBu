from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room
from django.contrib.gis.geos import fromstr

class RoomListCreate(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query is not None:
            return Room.objects.filter(name__icontains=query)
        return Room.objects.all()

    def perform_create(self, serializer):
        lon = self.request.data.get('longitude')
        lat = self.request.data.get('latitude')
        lastId = Room.objects.last()
        print(lastId)
        location = fromstr(f'POINT({lon} {lat})', srid=lastId)
        serializer.save(location=location, writter=self.request.user)
    