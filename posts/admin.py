from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse, NoReverseMatch
from django.utils.html import conditional_escape
from django.utils.html import format_html_join
from django.utils.translation import gettext_lazy as _

from .models import Posts


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    fieldsets = (
        (_('Content'), {
            'fields': (('title', 'status'), 'content',)}),

        (_('Publication'), {
            'fields': ('publication_date',),
            'classes': ('collapse', 'collapse-closed')}),

        (_('Discussions'), {
            'fields': ('comment_enabled',),
            'classes': ('collapse', 'collapse-closed')}),

        (_('Metadatas'), {
            'fields': ('authors',),
            'classes': ('collapse', 'collapse-closed')}),

        (None, {'fields': ('categories', 'tags', 'slug')}))

    filter_horizontal = ('categories',)

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ('title', 'content', 'tags')

    actions = ['make_published', 'close_comments', ]
    actions_on_top = True
    actions_on_bottom = True

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(PostAdmin, self).__init__(model, admin_site)

    def get_categories(self, post):
        """
        Return the categories linked in HTML.
        """
        try:
            return format_html_join(
                ', ', '<a href="{}" target="blank">{}</a>',
                [(category.get_absolute_url(), category.title)
                 for category in post.categories.all()])
        except NoReverseMatch:
            return ', '.join([conditional_escape(category.title)
                              for category in post.categories.all()])

    get_categories.short_description = _('category(s)')

    def get_tags(self, post):
        """
        Return the tags linked in HTML.
        """
        try:
            return format_html_join(
                ', ', '<a href="{}" target="blank">{}</a>',
                [(reverse('zinnia:tag_detail', args=[tag]), tag)
                 for tag in post.tags_list])
        except NoReverseMatch:
            return conditional_escape(post.tags)

    get_tags.short_description = _('tag(s)')

    def get_is_visible(self, post):
        """
        Admin wrapper for post.is_visible.
        """
        return post.is_visible

    get_is_visible.boolean = True
    get_is_visible.short_description = _('is visible')


admin.site.register(Posts, PostAdmin)
