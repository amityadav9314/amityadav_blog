# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from posts.dto import PostDTO
from sql_services import get_one_db_object, get_many_db_object


def test(request):
    return render(
        request,
        'blog/posts/test.html',
    )


class OnePostView(View):
    def get(self, request, **kwargs):
        year = kwargs.get('year', '')
        day = kwargs.get('day', '')
        month = kwargs.get('month', '')
        slug = kwargs.get('slug')

        requested_url = "/" + str(year) + "/" + str(month) + "/" + str(day) + "/" + slug + "/"

        # TODO Get Post from NoSQL
        # If Post not found in NoSQl, then find it in SQL
        post_db_obj = get_one_db_object(
            'posts.models',
            'Posts',
            _prefetch_related="authors, categories",
            **{
                'slug': slug,
            }
        )

        if str(post_db_obj.get_absolute_url()) != requested_url:
            return HttpResponseRedirect(post_db_obj.get_absolute_url())
        post_dto = PostDTO(post_db_obj)
        return render(
            request,
            'blog/posts/show_one_post.html',
            {
                'post_dto': post_dto
            }
        )


class ListPostsView(View):
    def get(self, request, **kwargs):
        page_no = kwargs.get('page_no', 0)
        limit = kwargs.get('limit', settings.LIST_POSTS_LIMIT)
        start_publication_date = kwargs.get('start_publication_date')
        end_publication_date = kwargs.get('end_publication_date')
        start = page_no * limit
        end = start + limit
        if start_publication_date and not end_publication_date:
            fields = {
                'publication_date__gte': start_publication_date
            }
        elif not start_publication_date and end_publication_date:
            fields = {
                'publication_date__lte': start_publication_date
            }
        elif not start_publication_date and not end_publication_date:
            fields = {}
        else:
            fields = {
                'publication_date__range': (start_publication_date, end_publication_date),
            }
        posts_db_obj = get_many_db_object(
            'posts.models',
            'Posts',
            _prefetch_related="authors, categories",
            **fields
        )[start:end]

        posts_dto = []
        for post_obj in posts_db_obj:
            posts_dto.append(PostDTO(post_obj, exclude=['content']))
        return render(
            request,
            'blog/posts/show_list_of_posts.html',
            {
                'posts_dto': posts_dto
            }
        )

