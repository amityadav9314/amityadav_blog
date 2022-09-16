from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Posts
from revision.models import Revise


class PostReviseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        post_id = validated_data.get("post_id")
        user = User.objects.get(id=1)
        post = Posts.objects.get(id=post_id)
        r = Revise(post=post, user=user)
        r.save()
        return post


class PostDeleteSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        post_id = validated_data.get("post_id")
        user = User.objects.get(id=1)
        post = Posts.objects.get(id=post_id)
        Revise.objects.filter(post=post, user=user).delete()
        return post
