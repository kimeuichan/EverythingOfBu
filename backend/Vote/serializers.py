from .models import Topic, Choice, Ballot
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        # fields = ('content', )

class BallotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballot
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'content', 'start_date', 'end_date', 'writter', 'choices')

    def create(self, validated_data):
        print("HERE")
        choicesData = validated_data.pop('choices')
        topic = Topic.objects.create(**validated_data)
        for choice in choicesData:
            Choice.objects.create(topic_id=topic, **choice)
        return topic

# class TopicCreateSerializer(serializers.ModelSerializer):
#     Choice = ChoiceSerializer(write_only=True)
#     class Meta:
#         model = Topic
#         fields = '__all__'
