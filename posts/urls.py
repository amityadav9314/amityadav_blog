from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^test/$', test, name='test'),

    url(
        r'^$',
        ListPostsView.as_view(),
        name='show_list_of_posts'
    ),
    url(
        r'^(?P<slug>[A-Za-z0-9._-]+)/$',
        OnePostView.as_view(),
        name='show_one_post'
    ),
    url(
        r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[A-Za-z0-9._-]+)/$',
        OnePostView.as_view(),
        name='show_one_post'
    ),
]
