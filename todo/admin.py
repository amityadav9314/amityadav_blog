from __future__ import unicode_literals

from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Todo._meta.get_fields()]


admin.site.register(Todo, TodoAdmin)
