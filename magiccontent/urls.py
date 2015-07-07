# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from .helpers import CONTENT_MODEL_NAMES
from .views import (AreaUpdateView, StyleWidgetUpdateView,
                    WidgetCreateView, AreaVisibleUpdateView,
                    AreaUpdateVisibilityViewDetail,
                    ContentOrderUpdate, ContentIsActiveUpdate)


# This will output something like (?P<content>(simplecontent|longcontent...))
content_regex = r'(?P<content>({0}))'.format(r'|'.join(CONTENT_MODEL_NAMES))

urlpatterns = patterns('',  # noqa
    # API
    url(r'^api/area/(?P<pk>[0-9]+)/$',
        AreaUpdateVisibilityViewDetail.as_view()),
    url(r'^api/{0}/order/(?P<widget_pk>\d+)/(?P<pk>\d+)/$'.format(
        content_regex), ContentOrderUpdate.as_view(),
        name='magiccontent.api.content_order.update'),
    url(r'^api/{0}/is_active/(?P<widget_pk>\d+)/(?P<pk>\d+)/$'.format(
        content_regex), ContentIsActiveUpdate.as_view(),
        name='magiccontent.api.content_isactive.update'),

    # Area
    url(r'^magiccontent/area/update/(?P<pk>\d+)/$', AreaUpdateView.as_view(),
        name='magiccontent.area.update'),
    url(r'^magiccontent/area/visible/update/$',
        AreaVisibleUpdateView.as_view(),
        name='magiccontent.area.visible.update'),

    # Widget
    url(r'^magiccontent/widget/update/(?P<pk>\d+)/$',
        StyleWidgetUpdateView.as_view(), name='magiccontent.widget.update'),

    url(r'^magiccontent/widget/create/(?P<area_pk>\d+)/$',
        WidgetCreateView.as_view(),
        name='magiccontent.widget.create'),

    url(r'^magiccontent/windows_close/$', TemplateView.as_view(
        template_name="magiccontent/windows_close.html"),
        name='magiccontent.windows_close'),

)
