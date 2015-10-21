# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .helpers import content_url_generator


def get_content_urls_for(model_content):
    urls = []
    views_list = content_url_generator(model_content)

    for view_row in views_list:

        if view_row['view_type'] in ['create', 'order']:

            row = url(r'magiccontent/{0}/(?P<widget_pk>\d+)/{1}/$'.format(
                view_row['model_name'], view_row['view_type']),
                view_row['view_class'].as_view(),
                name='magiccontent.{0}.{1}'.format(
                    view_row['model_name'], view_row['view_type'])
            )

        elif view_row['view_type'] in ['update', 'updatepicture', 'delete']:

            row = url(
                r'magiccontent/{0}/(?P<widget_pk>\d+)/{1}/(?P<pk>\d+)/$'.
                format(view_row['model_name'], view_row['view_type']),
                view_row['view_class'].as_view(),
                name='magiccontent.{0}.{1}'.format(
                    view_row['model_name'], view_row['view_type'])
            )

        else:
            continue

        urls.append(row)

    return tuple(urls)
