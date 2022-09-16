import traceback
from datetime import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from posts.models import Posts
from posts.serializers import PostSerializer
from .models import Revise
from .serializers import PostReviseSerializer, PostDeleteSerializer


class RevisePostViewSet(ListCreateAPIView):
    default_serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostReviseSerializer
        elif self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'DELETE':
            return PostDeleteSerializer

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

    def post(self, request, *args, **kwargs):
        serializer = PostReviseSerializer(data=request.data)
        my_dict = {'status': 'success'}
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(my_dict, status=status.HTTP_201_CREATED, content_type='application/json')
        except Exception as e:
            print(traceback.format_exc())
            my_dict['status'] = 'failed'
            my_dict['error'] = str(e)
            return Response(my_dict, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        serializer = PostDeleteSerializer(data=request.data)
        my_dict = {'status': 'success'}
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(my_dict, status=status.HTTP_201_CREATED, content_type='application/json')
        except Exception as e:
            print(traceback.format_exc())
            my_dict['status'] = 'failed'
            my_dict['error'] = str(e)
            return Response(my_dict, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
