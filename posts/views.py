# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def test(request):
    return render(
        request,
        'blog/posts/test.html',
    )
