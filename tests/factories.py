# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import factory

from magiccontent.models import Widget, Area, WIDGET_TYPES
from magiccontent.contrib.simplecontent.models import SimpleContent


class WidgetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Widget

    name = factory.Sequence(lambda n: 'Widget Name {0}'.format(n))
    widget_type = WIDGET_TYPES[0][0]  # simplecontent
    style_template = 'default'


class AreaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Area

    name = factory.Sequence(lambda n: 'Area Name {0}'.format(n))
    widget = factory.SubFactory(WidgetFactory)
    is_visible = True


class SimpleContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SimpleContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))
    long_content = factory.Sequence(lambda n: 'Long content {0}'.format(n))
    sub_title = factory.Sequence(lambda n: 'Subtitle {0}'.format(n))
