# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured
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

    def get_link_name(self):
        return self.widget and self.widget.name or self.name

    def get_link_url(self):
        return "#" + self.name

# TODO: the magiccontent shouldn't know its children
# This types should be registed based on the installed content apps
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
    ('default', 'styles must be'),
    ('default', 'implement by the child contents'),
)


class Widget(Permalinkable, SiteModel):

    """ Dynamic Widget """
    name = models.CharField(
        _('name'), max_length=64, db_index=True)
    widget_type = models.CharField(
        _('widget type'), max_length=32, default='simplecontent',
        choices=WIDGET_TYPES)
    style_template = models.CharField(max_length=128, default='default')
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
    def can_edit_description(self):
        return self.get_widget_type.can_edit_description

    @property
    def get_widget_type(self):
        _type = self.widget_type
        if _type == 'background':
            return self._get_content_model('backgroundarea')
        elif _type == 'pagelink':
            return self._get_content_model('pagelink')
        elif _type == 'menuitem':
            return self._get_content_model('menuitem')
        else:
            try:
                return self._get_content_model(_type)
            except:
                raise ImproperlyConfigured(
                    'Could find a model for the widget type: {0}'
                    .format(_type))

    def widget_types_list(self):
        """ returns the styles available for the given content """
        return self.get_widget_type.style_list()


class SiteLink(SiteModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    origin_model = models.CharField(max_length=255, null=True, blank=True)
    origin_model_pk = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
