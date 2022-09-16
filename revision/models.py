from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel

from posts.models import Posts


class Revise(TimeStampedModel):
    post = models.OneToOneField(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    first_revision_date = models.DateField(default=timezone.now() + timedelta(days=1))
    second_revision_date = models.DateField(default=timezone.now() + timedelta(days=2))
    third_revision_date = models.DateField(default=timezone.now() + timedelta(days=3))
    seventh_revision_date = models.DateField(default=timezone.now() + timedelta(days=7))
    fifteenth_revision_date = models.DateField(default=timezone.now() + timedelta(days=14))
    last_revision_date = models.DateField(default=timezone.now() + timedelta(days=30))

    def __str__(self):
        return self.post.title

    class Meta:
        ordering = ['-modified']
        get_latest_by = 'modified'
        verbose_name = 'Revision'
        verbose_name_plural = 'Revisions'
        index_together = [['post', 'user'],]

