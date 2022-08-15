from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'get_absolute_url', 'tags']