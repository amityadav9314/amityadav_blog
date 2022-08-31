from rest_framework import serializers

from revision.models import Revise
from .models import Posts


class PostSerializer(serializers.HyperlinkedModelSerializer):
    do_revise = serializers.SerializerMethodField(read_only=True)

    def get_do_revise(self, obj):
        r = Revise.objects.filter(post=obj)
        if r.exists():
            return True
        return False

    class Meta:
        model = Posts
        fields = ['id', 'title', 'get_absolute_url', 'tags', 'do_revise']
