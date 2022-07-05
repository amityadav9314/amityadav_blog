from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path(r'^test/$', test, name='test'),

    re_path(
        r'^$',
        ListPostsView.as_view(),
        name='show_list_of_posts'
    ),
    # re_path(
    #     r'^(?P<slug>[A-Za-z0-9._-]+)/$',
    #     OnePostView.as_view(),
    #     name='show_one_post'
    # ),
    re_path(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[A-Za-z0-9._-]+)/$',
        OnePostView.as_view(),
        name='show_one_post'
    ),
]
