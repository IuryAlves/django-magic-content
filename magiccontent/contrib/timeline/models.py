# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from image_cropping import ImageRatioField
from taggit.managers import TaggableManager

from magiccontent.abstract_models import BaseContent


ENTRY_TYPES = (('news', _('News')),
               ('event', _('Event')))

ENTRY_ACCESS = (('private', _('Private')),
                ('public', _('Public')))


class EntryAuthor(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.get_full_name()


class EntryContent(BaseContent):

    _widget_type = 'entrycontent'

    entry_author = models.ForeignKey(EntryAuthor)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    entry_type = models.CharField(
        _('entry type'), max_length=30, choices=ENTRY_TYPES)
    # default entry access: public
    entry_access = models.CharField(
        _('entry access'), max_length=30, choices=ENTRY_ACCESS,
        default=ENTRY_ACCESS[1][0])
    slug = models.SlugField(editable=False)
    picture_cropping = ImageRatioField('picture__picture', '960x960')

    tags = TaggableManager()

    def _content(self):
        return self.long_content

    def save(self, *args, **kws):
        # the slug should never change after being set
        # that is to avoid to break shared links
        if not self.pk:
            self.slug = slugify(self.title)

        super(EntryContent, self).save(*args, **kws)

    @property
    def get_entry_url(self):
        return reverse(
            'timeline.entrycontent.detail',
            kwargs={'entry_type': self.entry_type,
                    'entry_slug': self.slug,
                    'pk': self.pk})

    @property
    def tags_list(self):
        return self.tags.all()
