# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from datetime import datetime
from random import randint

from django.contrib.sites.models import Site

from multisitesutils.managers import SiteManager


class AreaManager(SiteManager):

    def get_or_create(self, name):
        return super(AreaManager, self).get_query_set().get_or_create(
            name=name, site=Site.objects.get_current())

    def get(self, name):
        return super(AreaManager, self).get_query_set().get(
            name=name, site=Site.objects.get_current())

    def actives(self):
        return self.get_query_set()


class WidgetManager(SiteManager):

    def list_content_from_type(self, widget):
        content_type_class = widget.get_widget_type
        return content_type_class.site_objects.filter(
            widget=widget, is_active=True)

    def list_content_widgets(self):
        """
        Returns widgets for contents (not pagelinks, menus or backgrounds)
        """
        return self.get_query_set().filter(is_content_data=True)

    def create(self, widget_type, style_template, name=''):
        if not name:
            current_time = datetime.now()
            name = "{0}_{1}_{2}".format(widget_type,
                                        current_time.strftime("%d%H%M%S%f"),
                                        randint(128, 1024))

        new_widget, _ = super(WidgetManager, self).get_query_set() \
            .get_or_create(name=name, widget_type=widget_type,
                           style_template=style_template)
        new_widget.description = new_widget.name
        new_widget.save()
        new_content = new_widget.get_widget_type.site_objects.create(
            widget=new_widget)
        new_content.save()
        return new_widget


class BaseContentManager(SiteManager):

    def actives(self):
        return self.get_query_set().filter(is_active=True)
