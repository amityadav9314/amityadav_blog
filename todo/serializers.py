from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Todo


class TodoGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']


class TodoAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title']

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        email = self.context.get('email')
        user = User.objects.get(email=email)
        r = Todo(user=user, title=validated_data.get('title'))
        r.save()
        return r


class TodoDeleteSerializer(serializers.Serializer):
    todo_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        todo_id = validated_data.get("todo_id")
        todo = Todo.objects.get(id=todo_id).delete()
        return todo
