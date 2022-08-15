from django.urls import re_path

from . import rest_views

urlpatterns = [
    re_path('^rest/revise/$', rest_views.RevisePostViewSet.as_view()),
]
