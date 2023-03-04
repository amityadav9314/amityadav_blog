from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from .models import Posts
from .serializers import PostSerializer


class PostViewSet(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email', None)
        if email:
            try:
                user = User.objects.get(email=email)
                queryset = Posts.objects.filter(authors=user).order_by('-publication_date')
            except User.DoesNotExist:
                queryset = Posts.objects.none()
        else:
            queryset = Posts.objects.all().order_by('-publication_date')
        return queryset
