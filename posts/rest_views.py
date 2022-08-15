from rest_framework.generics import ListAPIView

from .models import Posts
from .serializers import PostSerializer


class PostViewSet(ListAPIView):
    queryset = Posts.objects.all().order_by('-publication_date')
    serializer_class = PostSerializer
