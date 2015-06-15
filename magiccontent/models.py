# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.db import models

from multisitesutils.models import SiteModel

from .behaviours import Permalinkable
from .managers import WidgetManager, AreaManager


class Area(SiteModel):
    name = models.CharField(
        _('name'), max_length=64)
    widget = models.ForeignKey('Widget', verbose_name=_('widget'), null=True)
    is_visible = models.BooleanField('visible', default=True)
    is_always_visible = models.BooleanField('Always visible', default=False)

    objects = models.Manager()
    site_objects = AreaManager()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "{0} -> {1}".format(self.site, self.name)

# TODO: the magiccontent shouldn't know its children
WIDGET_TYPES = (
    ('simplecontent', 'Simple Content'),
    ('iconcontent', 'Icon Content'),
    ('longcontent', 'Long Content'),
    ('background', 'Background'),
    ('pagelink', 'PageLink'),
    ('imagecontent', 'Image Content'),
    ('menuitem', 'MenuItem'),
    ('timelineeventcontent', 'Timeline Events'),
    ('faq', 'Faq'),
    ('calendareventcontent', 'Calendar Events'),
)

TEMPLATE_STYLES = (
    ('must', 'be'),
    ('implemented', 'by the child'),
)


class Widget(Permalinkable, SiteModel):

    """ Dynamic Widget """
    name = models.CharField(
        _('name'), max_length=64, db_index=True)
    widget_type = models.CharField(
        _('widget type'), max_length=32, default='simplecontent',
        choices=WIDGET_TYPES)
    style_template = models.CharField(
        _('Template Style'), max_length=128, default='default',
        choices=TEMPLATE_STYLES)
    description = models.CharField(
        _('description'), max_length=128, default='', blank=True)
    is_content_data = models.BooleanField('Content Data', default=True)

    objects = models.Manager()
    site_objects = WidgetManager()

    def __unicode__(self):
        return "%s, %s" % (self.name, self.widget_type, )

    @property
    def content_list(self):
        """ List of all contents """
        data_type = self.get_widget_type
        return data_type.site_objects.filter(widget=self)

    @property
    def first_content(self, content_type):
        """ Show first content (order equals 0) """
        contents = content_type.site_objects.filter(widget=self)
        return contents[0]

    def _get_content_model(self, modelname):
        meta = self._meta
        field = meta.get_field_by_name(modelname)[0]
        return field.model

    @property
    def get_widget_type(self):
        _type = self.widget_type
        if _type == 'simplecontent':
            return self._get_content_model('simplecontent')
        elif _type == 'longcontent':
            return self._get_content_model('longcontent')
        elif _type == 'iconcontent':
            return self._get_content_model('iconcontent')
        elif _type == 'background':
            return self._get_content_model('backgroundarea')
        elif _type == 'pagelink':
            return self._get_content_model('pagelink')
        elif _type == 'imagecontent':
            return self._get_content_model('imagecontent')
        elif _type == 'menuitem':
            return self._get_content_model('menuitem')
        elif _type == 'timelineeventcontent':
            return self._get_content_model('timelineeventcontent')
        elif _type == 'calendareventcontent':
            return self._get_content_model('calendareventcontent')
        else:
            return self._get_content_model('simplecontent')

    def widget_types_list(self):
        """ returns the styles available for the given content """
        return self.get_widget_type.style_list()
