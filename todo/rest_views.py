import traceback

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoDeleteSerializer, TodoAddSerializer, TodoGetSerializer


class TodoAddViewSet(ListCreateAPIView):
    default_serializer_class = TodoAddSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TodoAddSerializer
        elif self.request.method == 'GET':
            return TodoGetSerializer
        elif self.request.method == 'DELETE':
            return TodoDeleteSerializer

    def get_queryset(self):
        queryset = Todo.objects.none()
        email = self.request.query_params.get('email', None)
        if email:
            try:
                user = User.objects.get(email=email)
                queryset = Todo.objects.filter(user=user)
            except User.DoesNotExist:
                pass
        return queryset

    def post(self, request, *args, **kwargs):
        serializer = TodoAddSerializer(data=request.data, context={'email': self.request.query_params.get('email')})
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
        serializer = TodoDeleteSerializer(data=request.data)
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
