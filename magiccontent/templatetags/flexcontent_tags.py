# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django import template
from django.db import models
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

Widget = models.get_model('flexcontent', 'Widget')
Area = models.get_model('flexcontent', 'Area')

register = template.Library()


@register.simple_tag
def show_widget_area_tag(area_name, can_edit=False,
                         widget_type='simplecontent', style='default',
                         *args, **kwargs):
    """
    Template Tag for generating a custom HTML for the given 'area_name' which
    will have a correspondent Widget.
    When the Area does not exist, it will be generated an Area, Widget and its
    BaseContent register.
    """
    div = kwargs.get('div', None)
    page_url = kwargs.get('page_url', None)

    area, created = Area.site_objects.get_or_create(name=area_name)
    if created:
        widget = Widget.site_objects.create(
            widget_type=widget_type, style_template=style)
        area.widget = widget
        area.save()

    content_list = Widget.site_objects.list_content_from_type(area.widget)

    first_item = content_list[0]

    # TODO: find a better place to add those CSS style classes names
    editable = 'darkBorder edit-block' if can_edit else ''
    template_name = 'flexcontent/{0}/{1}.html'.format(
        area.widget.widget_type, area.widget.style_template)

    context = {'widget': area.widget, 'area': area, 'div': div,
               'object_list': content_list, 'object': first_item,
               'can_edit': can_edit, 'editable': editable,
               'page_url': page_url}
    return render_to_string(template_name, context)


@register.filter(name='is_an_area_visible_tag')
def is_an_area_visible_tag(area_name):
    try:
        area = Area.site_objects.get(name=area_name)
    except Area.DoesNotExist:
        area = None

    if not area:
        return True
    return area.is_visible


@register.simple_tag
def show_widget_page_tag(widget=None, content_list=[], can_edit=False):
    """
    Template Tag for generating a custom HTML for the given Widget Page
    """
    template_name = 'flexcontent/{0}/{1}.html'.format(
        widget.widget_type, widget.style_template)

    context = {'widget': widget, 'object_list': content_list,
               'can_edit': can_edit}
    return render_to_string(template_name, context)


@register.inclusion_tag('flexcontent/show_editable_area_tag.html')
def show_editable_area_tag(area_id='', widget_id='', can_edit=False, area_name='area'):
    return {'area_id': area_id,
            'widget_id': widget_id,
            'area_name': area_name,
            'can_edit': can_edit}


@register.inclusion_tag('flexcontent/show_editable_widget_tag.html')
def show_editable_widget_tag(widget_type='', widget_id='', content_id='',
                             can_edit=False):
    content_create_url = 'flexcontent.%s.create' % widget_type
    content_update_url = 'flexcontent.%s.update' % widget_type
    content_order_url = 'flexcontent.%s.order' % widget_type

    create_url = reverse(content_create_url, kwargs={'widget_pk': widget_id})
    update_url = reverse(content_update_url, kwargs={'widget_pk': widget_id,
                         'pk': content_id})
    order_url = reverse(content_order_url, kwargs={'widget_pk': widget_id})
    return {'create_url': create_url, 'update_url': update_url,
            'order_url': order_url, 'can_edit': can_edit}
