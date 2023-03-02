from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Todo(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified']
        get_latest_by = 'modified'
        verbose_name = 'TODO'
        verbose_name_plural = 'TODO'
