from datetime import datetime

from django.db.models import Q
from rest_framework.generics import ListAPIView

from posts.models import Posts
from posts.serializers import PostSerializer
from .models import Revise


class RevisePostViewSet(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        today = datetime.today().strftime("%Y-%m-%d")
        post_ids = Revise.objects.filter(
            Q(first_revision_date=today)
            | Q(second_revision_date=today)
            | Q(third_revision_date=today)
            | Q(seventh_revision_date=today)
            | Q(fifteenth_revision_date=today)
            | Q(last_revision_date=today)
        ).values_list('post_id', flat=True)
        posts = Posts.objects.filter(id__in=post_ids)
        return posts
