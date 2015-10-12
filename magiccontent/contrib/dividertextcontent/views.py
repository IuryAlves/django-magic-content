# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView

from magiccontent.mixins import EditableMixin, CreateContentMixin
from magiccontent.views import MagicDeleteView, PictureUpdateView

from .models import DividerTextContent
from .forms import DividerTextContentForm, DividerTextContentCreateForm


class DividerTextContentMixin(object):
    model = DividerTextContent
    form_class = DividerTextContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class DividerTextContentCreateView(CreateContentMixin, DividerTextContentMixin, EditableMixin,
                         CreateView):
    form_class = DividerTextContentCreateForm


class DividerTextContentUpdateView(DividerTextContentMixin, EditableMixin, UpdateView):
    pass


class DividerTextContentPictureUpdateView(DividerTextContentMixin, EditableMixin,
                                PictureUpdateView):
    template_name = 'magiccontent/defaultcontent_image_form.html'


class DividerTextContentDeleteView(DividerTextContentMixin, EditableMixin, MagicDeleteView):
    pass
