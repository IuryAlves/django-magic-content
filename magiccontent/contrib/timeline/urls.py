# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, patterns

from magiccontent.dynamic_content_urls import get_content_urls_for
from .models import EntryContent
from .views import EntryDetailView, ShowEntryContentPageView

urlpatterns = patterns("",  # noqa
    url(r'^(?P<entry_type>[-\w]+)/(?P<pk>\d+)/$',
        ShowEntryContentPageView.as_view(),
        name='timeline.entrycontent.showpage'),
    url(r'^(?P<entry_type>[-\w]+)/(?P<entry_slug>[-\w]+)/(?P<pk>\d+)/$',
        EntryDetailView.as_view(), name='timeline.entrycontent.detail'),
)
urlpatterns += get_content_urls_for(EntryContent)
