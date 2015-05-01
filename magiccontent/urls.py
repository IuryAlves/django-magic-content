# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, url

from django.views.generic import TemplateView

from .helpers import CONTENT_MODEL_NAMES
from .views import (AreaUpdateView, StyleWidgetUpdateView,
                    BackgroundAreaUpdateView,
                    WidgetCreateView, AreaVisibleUpdateView,
                    AreaUpdateVisibilityViewDetail,
                    ContentOrderUpdate, ContentIsActiveUpdate)
from .models import (SimpleContent, LongContent, IconContent, PageLink,
                     ImageContent, GalleryContent)
from .dynamic_content_urls import get_content_urls_for


# This will output something like (?P<content>(simplecontent|longcontent...))
content_regex = r'(?P<content>({0}))'.format(r'|'.join(CONTENT_MODEL_NAMES))

urlpatterns = patterns('',  # noqa
    # API
    url(r'^api/area/(?P<pk>[0-9]+)/$',
        AreaUpdateVisibilityViewDetail.as_view()),
    url(r'^api/{0}/order/(?P<widget_pk>\d+)/(?P<pk>\d+)/$'.format(
        content_regex), ContentOrderUpdate.as_view(),
        name='flexcontent.api.content_order.update'),
    url(r'^api/{0}/is_active/(?P<widget_pk>\d+)/(?P<pk>\d+)/$'.format(
        content_regex), ContentIsActiveUpdate.as_view(),
        name='flexcontent.api.content_isactive.update'),

    # Area
    url(r'^flexcontent/area/update/(?P<pk>\d+)/$', AreaUpdateView.as_view(),
        name='flexcontent.area.update'),
    url(r'^flexcontent/area/visible/update/$', AreaVisibleUpdateView.as_view(),
        name='flexcontent.area.visible.update'),

    # Widget
    url(r'^flexcontent/widget/update/(?P<pk>\d+)/$',
        StyleWidgetUpdateView.as_view(), name='flexcontent.widget.update'),

    url(r'^flexcontent/widget/create/(?P<area_pk>\d+)/$',
        WidgetCreateView.as_view(),
        name='flexcontent.widget.create'),

    # BackgroundArea
    url(r'^flexcontent/backgroundarea/(?P<widget_pk>\d+)/update/(?P<pk>\d+)/$',
        BackgroundAreaUpdateView.as_view(),
        name='flexcontent.backgroundarea.update'),

    url(r'^flexcontent/windows_close/$', TemplateView.as_view(
        template_name="flexcontent/windows_close.html"),
        name='flexcontent.windows_close'),

)

simplecontent_urls = get_content_urls_for(SimpleContent)
longcontent_urls = get_content_urls_for(LongContent)
iconcontent_urls = get_content_urls_for(IconContent)
pagelink_urls = get_content_urls_for(PageLink)
imagecontent_urls = get_content_urls_for(ImageContent)
gallerycontent_urls = get_content_urls_for(GalleryContent)

urlpatterns += simplecontent_urls + longcontent_urls + iconcontent_urls +\
               pagelink_urls + imagecontent_urls + gallerycontent_urls
