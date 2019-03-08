from rest_framework import serializers
from .models import Post, NeedMember
from django.contrib.auth.models import User
from rest_framework import permissions


class MemberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = NeedMember
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    writter = serializers.ReadOnlyField(source='writter.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'writter', 'created_time', 'isAlive', 'members')

    def create(self, validated_data):
        membersData = validated_data.pop('members')
        post = Post.objects.create(**validated_data)
        for member in membersData:
            NeedMember.objects.create(post=post, **member)
        return post

    def update(self, instance, validated_data):
        members = validated_data.pop('members')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.isAlive = validated_data.get('isAlive', instance.isAlive)

        newMemberList = []
        for patchMember in members:
            member, created = NeedMember.objects.get_or_create(id=patchMember.get('id'), post_id=instance.id)
            member.memberType = patchMember.get('memberType', member.memberType)
            member.isRecruit = patchMember.get('isRecruit', member.isRecruit)
            member.save()
            newMemberList.append(member)

        instance.members.set(newMemberList)
        instance.save()
        return instance

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', queryset=NeedMember.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'posts')