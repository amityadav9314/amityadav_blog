from rest_framework import serializers

from posts.models import Posts
from revision.models import Revise


class PostReviseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        post_id = validated_data.get("post_id")
        post = Posts.objects.get(id=post_id)
        r = Revise(post=post)
        r.save()
        return post
