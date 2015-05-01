# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.colors import yellow

from django.conf.urls import url

from .helpers import content_url_generator, ALLOWED_VIEWS


def get_content_urls_for(model_content):
    urls = []
    views_list = content_url_generator(model_content)

    if len(views_list) < len(ALLOWED_VIEWS):
        expected_labels = [i['url_label'] for i in ALLOWED_VIEWS]
        found_labels = [i['view_type'] for i in views_list]
        for label in expected_labels:
            if label not in found_labels:
                msg = '{0} has no "{1}" view'.format(model_content, label)
                print(yellow(msg))

    for view_row in views_list:

        if view_row['view_type'] in ['create', 'order']:

            row = url(r'flexcontent/{0}/(?P<widget_pk>\d+)/{1}/$'.format(
                view_row['model_name'], view_row['view_type']),
                view_row['view_class'].as_view(),
                name='flexcontent.{0}.{1}'.format(
                    view_row['model_name'], view_row['view_type'])
            )

        elif view_row['view_type'] in ['update', 'delete']:

            row = url(
                r'flexcontent/{0}/(?P<widget_pk>\d+)/{1}/(?P<pk>\d+)/$'.
                format(view_row['model_name'], view_row['view_type']),
                view_row['view_class'].as_view(),
                name='flexcontent.{0}.{1}'.format(
                    view_row['model_name'], view_row['view_type'])
            )

        else:
            continue

        urls.append(row)

    return tuple(urls)
