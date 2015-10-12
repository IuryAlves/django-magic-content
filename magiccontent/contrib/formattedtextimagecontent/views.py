# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView, PictureUpdateView
from .models import FormattedTextImageContent
from .forms import FormattedTextImageContentForm, FormattedTextImageContentCreateForm


class FormattedTextImageContentMixin(object):
    model = FormattedTextImageContent
    form_class = FormattedTextImageContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class FormattedTextImageContentCreateView(CreateContentMixin, FormattedTextImageContentMixin,
                            EditableMixin, CreateView):
    form_class = FormattedTextImageContentCreateForm


class FormattedTextImageContentUpdateView(FormattedTextImageContentMixin, EditableMixin, UpdateView):
    pass


class FormattedTextImageContentPictureUpdateView(FormattedTextImageContentMixin, EditableMixin,
                                   PictureUpdateView):
    template_name = 'magiccontent/defaultcontent_image_form.html'


class FormattedTextImageContentDeleteView(FormattedTextImageContentMixin, EditableMixin, MagicDeleteView):
    pass


class FormattedTextImageContentOrderListView(ListContentMixin, FormattedTextImageContentMixin, ListView):
    pass
