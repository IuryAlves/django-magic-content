# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from magiccontent.abstract_models import BaseContent


ENTRY_ACCESS = (('private', _('Private (only for logged users)')),
                ('public', _('Public')))


class EntryAuthor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.get_full_name()


class TimelineEventContent(BaseContent):

    _widget_type = 'timelineeventcontent'

    entry_author = models.ForeignKey(EntryAuthor, blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    # default entry access: public
    entry_access = models.CharField(
        _('entry access'), max_length=30, choices=ENTRY_ACCESS,
        default=ENTRY_ACCESS[1][0])
    slug = models.SlugField(editable=False)

    tags = TaggableManager(blank=True)

    def _content(self):
        return self.long_content

    def save(self, *args, **kws):
        # the slug should never change after being set
        # that is to avoid to break shared links
        if not self.pk:
            self.slug = slugify(self.title)

        super(TimelineEventContent, self).save(*args, **kws)

    @property
    def private(self):
        return self.entry_access == 'private'

    @property
    def get_entry_url(self):
        return reverse(
            'timeline.entrycontent.detail',
            kwargs={'entry_slug': self.slug,
                    'pk': self.pk})

    @property
    def tags_list(self):
        return self.tags.all()

    @property
    def enable_picture(self):
        return False

    @classmethod
    def style_list(cls_obj):
        style_list = (
            ('default', 'TimelineEventContent - default'), )
        return style_list
