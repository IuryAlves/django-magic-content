# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from .models import GalleryContent
from .forms import GalleryContentForm


class GalleryContentMixin(object):
    model = GalleryContent
    form_class = GalleryContentForm
    template_name = 'magiccontent/simplecontent_form.html'


class GalleryContentCreateView(CreateContentMixin, GalleryContentMixin,
                               EditableMixin, CreateView):
    pass


class GalleryContentUpdateView(GalleryContentMixin, EditableMixin, UpdateView):
    pass


class GalleryContentDeleteView(GalleryContentMixin, EditableMixin, DeleteView):
    pass


class GalleryContentOrderListView(ListContentMixin, GalleryContentMixin,
                                  ListView):
    pass
