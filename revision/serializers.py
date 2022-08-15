from rest_framework import serializers

from revision.models import Revise


class PostReviseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        Revise.objects.create(post_id=validated_data)
