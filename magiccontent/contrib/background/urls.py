# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, patterns

from .views import BackgroundAreaUpdateView, BackgroundAreaPictureUpdateView


urlpatterns = patterns("",  # noqa
    url(r'^magiccontent/backgroundarea/(?P<widget_pk>\d+)/update/(?P<pk>\d+)/$',
        BackgroundAreaUpdateView.as_view(),
        name='magiccontent.background.update'),
    url(r'^magiccontent/backgroundarea/(?P<widget_pk>\d+)/updatepicture/(?P<pk>\d+)/$',
        BackgroundAreaPictureUpdateView.as_view(),
        name='magiccontent.background.updatepicture'),
)
