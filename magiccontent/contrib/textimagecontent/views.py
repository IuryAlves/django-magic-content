# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView, PictureUpdateView

from .models import TextImageContent
from .forms import TextImageContentForm, TextImageContentCreateForm


class TextImageContentMixin(object):
    model = TextImageContent
    form_class = TextImageContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class TextImageContentCreateView(CreateContentMixin, TextImageContentMixin,
                              EditableMixin, CreateView):
    form_class = TextImageContentCreateForm


class TextImageContentUpdateView(TextImageContentMixin, EditableMixin, UpdateView):
    pass


class TextImageContentPicUpdateView(TextImageContentMixin, EditableMixin,
                                 PictureUpdateView):
    template_name = 'magiccontent/defaultcontent_image_form.html'


class TextImageContentDeleteView(TextImageContentMixin, EditableMixin,
                              MagicDeleteView):
    pass


class TextImageContentOrderListView(ListContentMixin, TextImageContentMixin,
                                 ListView):
    pass
