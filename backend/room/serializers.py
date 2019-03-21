from .models import Room, RoomScore
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    writter = serializers.ReadOnlyField(source='writter.username')
    location = serializers.CharField()
    longitude = serializers.FloatField(write_only=True)
    latitude = serializers.FloatField(write_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'writter', 'location', 'description', 'photo', 'created_time', 'longitude', 'latitude')

    def create(self, validated_data):
        room = Room(**validated_data)
        room.location = location
        room.save()
        return room

class RoomScoreSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.username')
    room_no = serializers.ReadOnlyField(source='room_no.id')
    class Meta:
        model = RoomScore
        fields = '__all__'