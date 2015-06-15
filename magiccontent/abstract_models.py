# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from multisitesutils.models import SiteModel
from magicgallery.models import GalleryItem

from .models import Widget
from .managers import BaseContentManager


class BaseContent(SiteModel):

    # must be defined at children models, this is the value used by
    # get_widget_type method
    _widget_type = None

    PICTURE_FILTERS = (
        ('', 'Original'),
        ('image-xpro2', 'XPro2'),
        ('image-willow', 'Willow'),
        ('image-inkwell', 'Inkwell'),
        ('image-walden', 'Walden'),
        ('image-toaster', 'Toaster'),
        ('image-sierra', 'Sierra'),
        ('image-nashville', 'Nashville'),
        ('image-mayfair', 'Mayfair'),
        ('image-kelvin', 'Kelvin'),
        ('image-hudson', 'Hudson'),
        ('image-brannan', 'Brannan'),
        ('image-1977', '1977'),
        ('image-blur', 'Blur'),
    )

    widget = models.ForeignKey(Widget, verbose_name=_('widget'))
    title = models.CharField(
        _('title'), max_length=128, default='Edit title',
        blank=True)
    short_content = models.TextField(
        _('short content'), max_length=512,
        default='Edit content',
        blank=True)
    long_content = RichTextField(
        _('long content'), default='', blank=True)
    picture = models.ForeignKey(GalleryItem, null=True, blank=True)
    picture_filter = models.CharField(
        _('Image Filter'), max_length=32, default='',
        choices=PICTURE_FILTERS, blank=True)
    order = models.PositiveIntegerField(_('order'), default=99)
    is_active = models.BooleanField(_('active'), default=True)
    link_url = models.CharField(
        _('link url'), max_length=255, default='', blank=True)
    link_label = models.CharField(
        _('link label'), max_length=64, default='', blank=True)

    objects = models.Manager()
    site_objects = BaseContentManager()

    class Meta:
        abstract = True
        ordering = ['order']

    def __unicode__(self):
        return '{0}.{1}'.format(self.is_active, self.title)

    def _content(self):
        pass

    @property
    def content(self):
        return self._content()

    @property
    def model_name(self):
        return self._meta.model_name

    @property
    def enable_picture(self):
        """
        make contents have images manipulation, for contents such as Icon
        this method must be overwritten as False
        """
        return True
