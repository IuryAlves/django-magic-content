# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView
from .models import ImageContent
from .forms import ImageContentForm, ImageContentCreateForm


class ImageContentMixin(object):
    model = ImageContent
    form_class = ImageContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class ImageContentCreateView(CreateContentMixin, ImageContentMixin,
                             EditableMixin, CreateView):
    form_class = ImageContentCreateForm


class ImageContentUpdateView(ImageContentMixin, EditableMixin, UpdateView):
    pass


class ImageContentDeleteView(ImageContentMixin, EditableMixin,
                             MagicDeleteView):
    pass


class ImageContentOrderListView(ListContentMixin, ImageContentMixin, ListView):
    pass
