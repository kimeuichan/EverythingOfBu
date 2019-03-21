from .models import Room, RoomScore
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    writter = serializers.ReadOnlyField(source='writter.username')
    class Meta:
        model = Room
        fields = '__all__'

class RoomScoreSerializer(serializers.ModelSerializer):
    reviewer = serializers.ReadOnlyField(source='reviewer.username')
    room_no = serializers.ReadOnlyField(source='room_no.id')
    class Meta:
        model = RoomScore
        fields = '__all__'