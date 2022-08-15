from __future__ import unicode_literals

from django.contrib import admin

from .models import Revise


class ReviseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Revise, ReviseAdmin)
