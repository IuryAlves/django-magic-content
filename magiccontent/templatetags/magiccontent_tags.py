# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django import template
from django.db import models
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.core.urlresolvers import NoReverseMatch

Widget = models.get_model('magiccontent', 'Widget')
Area = models.get_model('magiccontent', 'Area')

register = template.Library()


def get_first_content(content_list, widget):
    if not content_list:
        first_item = widget.get_widget_type.site_objects.create(widget=widget)
        first_item.save()
    else:
        first_item = content_list[0]
    return first_item


@register.simple_tag(takes_context=True)
def show_widget_area_tag(context, area_name, can_edit=False,
                         widget_type='textimagecontent', style='default',
                         *args, **kwargs):
    """
    Template Tag for generating a custom HTML for the given 'area_name' which
    will have a correspondent Widget.
    When the Area does not exist, it will be generated an Area, Widget and its
    BaseContent register.
    """

    request = context['request']

    div = kwargs.get('div', None)
    page_url = kwargs.get('page_url', None)

    area, created = Area.site_objects.get_or_create(name=area_name)
    if created:
        widget = Widget.site_objects.create(
            widget_type=widget_type, style_template=style)
        area.widget = widget
        area.save()

    content_list = Widget.site_objects.list_content_from_type(area.widget)
    first_item = get_first_content(content_list, area.widget)

    # TODO: find a better place to add those CSS style classes names
    editable = 'darkBorder edit-block' if can_edit else ''
    template_name = 'magiccontent/{0}/{1}.html'.format(
        area.widget.widget_type, area.widget.style_template)

    context.update({'widget': area.widget, 'area': area, 'div': div,
                    'object_list': content_list, 'object': first_item,
                    'can_edit': can_edit, 'editable': editable,
                    'page_url': page_url, 'user': request.user})
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


@register.simple_tag(takes_context=True)
def show_widget_page_tag(context, widget=None, content_list=[],
                         can_edit=False, show_page=False, style=None):
    """
    Template Tag for generating a custom HTML for the given Widget Page
    """
    page = "_page" if show_page else ''
    style_template = style if style else widget.style_template
    template_name = 'magiccontent/{0}/{1}{2}.html'.format(
        widget.widget_type, style_template, page)
    first_item = get_first_content(content_list, widget)

    context.update({'widget': widget, 'object_list': content_list,
                    'can_edit': can_edit, 'object': first_item, })

    return render_to_string(template_name, context)


@register.inclusion_tag('magiccontent/show_editable_area_tag.html')
def show_editable_area_tag(area_id='', widget_id='', can_edit=False,
                           area_name='area'):
    return {'area_id': area_id,
            'widget_id': widget_id,
            'area_name': area_name,
            'can_edit': can_edit,
            'widget': Widget.site_objects.get(pk=int(widget_id))}


@register.inclusion_tag('magiccontent/show_editable_widget_tag.html',
                        takes_context=True)
def show_editable_widget_tag(context, widget_type='', widget_id='',
                             content_id='', can_edit=False, show_add_btn=True,
                             show_order_btn=True, show_sytle_btn=True):
    content_create_url = 'magiccontent.%s.create' % widget_type
    content_update_url = 'magiccontent.%s.update' % widget_type
    picture_update_url = 'magiccontent.%s.updatepicture' % widget_type
    content_order_url = 'magiccontent.%s.order' % widget_type

    create_url = reverse(
        content_create_url,
        kwargs={'widget_pk': widget_id}) if show_add_btn else ''
    update_url = reverse(
        content_update_url,
        kwargs={'widget_pk': widget_id, 'pk': content_id})
    try:
        updatepicture_url = reverse(
            picture_update_url,
            kwargs={'widget_pk': widget_id, 'pk': content_id})
    except NoReverseMatch:
        updatepicture_url = None
    order_url = reverse(
        content_order_url,
        kwargs={'widget_pk': widget_id}) if show_order_btn else ''
    widget_update_url = reverse(
        'magiccontent.widget.update', kwargs={'pk': widget_id})

    _help_ctx = {
        'help_edit_url': context.get('help_page_edit_content'),
        'help_edit_show': context.get('show_help_page_edit_content'),
        'help_edit_description': 'Learn how to edit contents',
        'help_edit_flag': 'help_page_edit_content',
        'help_add_url': context.get('help_page_add_content'),
        'help_add_show': context.get('show_help_page_add_content'),
        'help_add_description': 'Learn how to add new contents',
        'help_add_flag': 'help_page_add_content',
    }
    ctx = {'create_url': create_url,
           'update_url': update_url,
           'updatepicture_url': updatepicture_url,
           'order_url': order_url,
           'style_url': widget_update_url if show_sytle_btn else '',
           'can_edit': can_edit}
    ctx.update(_help_ctx)

    return ctx


@register.filter(name='show_help_text', is_safe=True)
def show_help_text(value):
    """
    Returns a standard help file path
    """
    return "magiccontent/help_text_{0}.html".format(slugify(value))
