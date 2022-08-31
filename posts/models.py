from django.db import models
from django.urls import reverse

from django.utils import timezone
from emtex_common_utils.models import BaseModel

from tagging.fields import TagField

from posts.managers import PostPublishedManager


class Posts(BaseModel):
    DRAFT = "draft"
    HIDDEN = "hidden"
    PUBLISHED = "published"
    STATUS_CHOICES = ((DRAFT, DRAFT),
                      (HIDDEN, HIDDEN),
                      (PUBLISHED, PUBLISHED))

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=255,
        unique_for_date='publication_date',
        help_text="Used to build the entry's URL.")

    content = models.TextField()

    status = models.CharField(
        max_length=10,
        db_index=True,
        choices=STATUS_CHOICES,
        default=DRAFT
    )

    publication_date = models.DateTimeField(
        db_index=True, default=timezone.now,
    )

    comment_enabled = models.BooleanField(
        default=True,
    )

    authors = models.ManyToManyField(
        'auth.User',
        blank=True,
        related_name='posts',
    )

    categories = models.ManyToManyField(
        'categories.Category',
        blank=True,
        related_name='posts',
    )

    tags = TagField('tags')

    objects = models.Manager()
    published = PostPublishedManager()

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        publication_date = self.publication_date
        if timezone.is_aware(publication_date):
            publication_date = timezone.localtime(publication_date)
        return reverse('show_one_post', kwargs={
            'year': publication_date.strftime('%Y'),
            'month': publication_date.strftime('%m'),
            'day': publication_date.strftime('%d'),
            'slug': self.slug})

    @property
    def is_published(self):
        """
        Checks if an entry is visible and published.
        """
        return self.is_active and self.status == self.PUBLISHED

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']
        get_latest_by = 'publication_date'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        index_together = [['slug', 'publication_date'],
                          ['status', 'publication_date']]
        permissions = (('can_view_all', 'Can view all entries'),
                       ('can_change_status', 'Can change status'),
                       ('can_change_author', 'Can change author(s)'),)
