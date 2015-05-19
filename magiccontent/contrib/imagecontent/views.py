# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import ImageContent
from .forms import ImageContentForm


class ImageContentMixin(object):
    model = ImageContent
    form_class = ImageContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class ImageContentCreateView(CreateContentMixin, ImageContentMixin,
                             EditableMixin, CreateView):
    pass


class ImageContentUpdateView(ImageContentMixin, EditableMixin, UpdateView):
    pass


class ImageContentDeleteView(ImageContentMixin, EditableMixin, DeleteView):
    pass


class ImageContentOrderListView(ListContentMixin, ImageContentMixin, ListView):
    pass
