# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import factory

from magiccontent.models import Widget, Area, WIDGET_TYPES
from magiccontent.contrib.textimagecontent.models import TextImageContent
from magiccontent.contrib.background.models import BackgroundArea
from magiccontent.contrib.iconcontent.models import IconContent
from magiccontent.contrib.imagecontent.models import ImageContent
from magiccontent.contrib.formattedtextimagecontent.models import FormattedTextImageContent
from magiccontent.contrib.dividertextcontent.models import DividerTextContent


class WidgetFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Widget

    name = factory.Sequence(lambda n: 'Widget Name {0}'.format(n))
    widget_type = WIDGET_TYPES[0][0]  # textimagecontent
    style_template = 'default'


class AreaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Area

    name = factory.Sequence(lambda n: 'Area Name {0}'.format(n))
    widget = factory.SubFactory(WidgetFactory)
    is_visible = True


class TextImageContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TextImageContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))
    long_content = factory.Sequence(lambda n: 'Long content {0}'.format(n))
    sub_title = factory.Sequence(lambda n: 'Subtitle {0}'.format(n))


class BackgroundAreaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = BackgroundArea

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))
    sub_title = factory.Sequence(lambda n: 'Subtitle {0}'.format(n))


class IconContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = IconContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))


class ImageContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ImageContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))


class FormattedTextImageContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FormattedTextImageContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))
    long_content = factory.Sequence(lambda n: 'Long content {0}'.format(n))


class DividerTextContentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DividerTextContent

    widget = factory.SubFactory(WidgetFactory)
    title = factory.Sequence(lambda n: 'Title {0}'.format(n))
    short_content = factory.Sequence(lambda n: 'Short content {0}'.format(n))
