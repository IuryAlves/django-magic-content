# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns

from magiccontent.dynamic_content_urls import get_content_urls_for
from .models import GalleryContent

urlpatterns = patterns("",)
urlpatterns += get_content_urls_for(GalleryContent)
