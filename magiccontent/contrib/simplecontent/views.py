# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from magiccontent.mixins import (EditableMixin, CreateContentMixin,
                                 ListContentMixin)
from magiccontent.views import MagicDeleteView, PictureUpdateView
from .models import SimpleContent
from .forms import SimpleContentForm, SimpleContentCreateForm


class SimpleContentMixin(object):
    model = SimpleContent
    form_class = SimpleContentForm
    template_name = 'magiccontent/defaultcontent_form.html'


class SimpleContentCreateView(CreateContentMixin, SimpleContentMixin,
                              EditableMixin, CreateView):
    form_class = SimpleContentCreateForm


class SimpleContentUpdateView(SimpleContentMixin, EditableMixin, UpdateView):
    pass


class SimpleContentPicUpdateView(SimpleContentMixin, EditableMixin,
                                 PictureUpdateView):
    pass


class SimpleContentDeleteView(SimpleContentMixin, EditableMixin,
                              MagicDeleteView):
    pass


class SimpleContentOrderListView(ListContentMixin, SimpleContentMixin,
                                 ListView):
    pass
