
from django.db import models


class PostPublishedManager(models.Manager):

    def get_queryset(self):
        """
        Return published entries.
        """
        return super(PostPublishedManager, self).get_queryset(
            status=self.model.PUBLISHED
        )
