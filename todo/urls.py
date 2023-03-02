from django.urls import re_path

from . import rest_views

urlpatterns = [
    re_path('^rest/todo/$', rest_views.TodoAddViewSet.as_view()),
]
