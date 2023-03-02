from __future__ import unicode_literals

from django.contrib import admin

from .models import Revise


class ReviseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Revise._meta.get_fields()]


admin.site.register(Revise, ReviseAdmin)
