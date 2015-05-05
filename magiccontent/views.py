# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse

from rest_framework.views import APIView
from rest_framework.response import Response

from .mixins import (EditableMixin, CreateContentMixin,
                     ListContentMixin, SimpleContentMixin, LongContentMixin,
                     PageLinkMixin, IconContentMixin, BackgroundAreaMixin)
from .models import Area, Widget, ImageContent, GalleryContent
from .forms import (AreaForm, WidgetForm, NewWidgetForm, GalleryContentForm,
                    ImageContentForm)
from .serializers import AreaVisibleSerializer, ContentFieldUpdateSerializer


class AreaUpdateView(EditableMixin, UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'flexcontent/area_form.html'


class AreaVisibleUpdateView(ListView):
    model = Area
    template_name = 'flexcontent/area_visible_form.html'
    paginate_by = '100'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Area.site_objects.actives()


class StyleWidgetUpdateView(EditableMixin, UpdateView):
    model = Widget
    form_class = WidgetForm
    template_name = 'flexcontent/stylewidget_form.html'


class WidgetCreateView(EditableMixin, CreateView):
    model = Widget
    form_class = NewWidgetForm
    template_name = 'flexcontent/newwidget_form.html'

    def form_valid(self, form):
        area_pk = self.kwargs['area_pk']
        self.object = form.save(commit=False)
        Widget.site_objects.create(
            widget_type=self.object.widget_type,
            style_template=self.object.style_template,
            name=self.object.name)
        area_url = reverse("flexcontent.area.update",
                           kwargs={'pk': area_pk})
        return redirect(area_url)


class SimpleContentCreateView(CreateContentMixin, SimpleContentMixin,
                              EditableMixin, CreateView):
    pass


class SimplecontentUpdateView(SimpleContentMixin, EditableMixin, UpdateView):
    pass


class SimplecontentDeleteView(SimpleContentMixin, EditableMixin, DeleteView):
    pass


class SimpleContentOrderListView(ListContentMixin, SimpleContentMixin,
                                 ListView):
    pass


class LongContentCreateView(CreateContentMixin, LongContentMixin,
                            EditableMixin, CreateView):
    pass


class LongContentUpdateView(LongContentMixin, EditableMixin, UpdateView):
    pass


class LongContentDeleteView(LongContentMixin, EditableMixin, DeleteView):
    pass


class LongContentOrderListView(ListContentMixin, LongContentMixin, ListView):
    pass


class PageLinkCreateView(CreateContentMixin, PageLinkMixin, EditableMixin,
                         CreateView):
    pass


class PageLinkUpdateView(PageLinkMixin, EditableMixin, UpdateView):
    pass


class PageLinkDeleteView(PageLinkMixin, EditableMixin, DeleteView):
    pass


class IconContentCreateView(CreateContentMixin, IconContentMixin,
                            EditableMixin, CreateView):
    pass


class IconContentUpdateView(IconContentMixin, EditableMixin, UpdateView):
    pass


class IconContentDeleteView(IconContentMixin, EditableMixin, DeleteView):
    pass


class IconContentOrderListView(ListContentMixin, IconContentMixin, ListView):
    pass


class BackgroundAreaUpdateView(BackgroundAreaMixin, EditableMixin, UpdateView):
    pass


class ImageContentMixin(object):
    model = ImageContent
    form_class = ImageContentForm
    template_name = 'flexcontent/simplecontent_form.html'


class ImageContentCreateView(CreateContentMixin, ImageContentMixin,
                             EditableMixin, CreateView):
    pass


class ImageContentUpdateView(ImageContentMixin, EditableMixin, UpdateView):
    pass


class ImageContentDeleteView(ImageContentMixin, EditableMixin, DeleteView):
    pass


class ImageContentOrderListView(ListContentMixin, ImageContentMixin, ListView):
    pass


class AreaUpdateVisibilityViewDetail(APIView):
    """
    Retrieve Area instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Area, pk=pk)

    def post(self, request, pk, format=None):
        area = self.get_object(pk)
        serializer = AreaVisibleSerializer(area, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ContentOrderUpdate(APIView):

    def get_object(self, model_class, pk):
        return get_object_or_404(model_class, pk=pk)

    def post(self, request, **kwargs):
        widget = Widget.site_objects.get(pk=self.kwargs.get('widget_pk'))
        model_class = widget.get_widget_type
        instance = self.get_object(model_class, kwargs['pk'])
        serializer = ContentFieldUpdateSerializer(
            model_class, instance, request.DATA, _fields=['order'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ContentIsActiveUpdate(APIView):

    def get_object(self, model_class, pk):
        return get_object_or_404(model_class, pk=pk)

    def post(self, request, **kwargs):
        widget = Widget.site_objects.get(pk=self.kwargs.get('widget_pk'))
        model_class = widget.get_widget_type
        instance = self.get_object(model_class, kwargs['pk'])
        serializer = ContentFieldUpdateSerializer(
            model_class, instance, request.DATA, _fields=['is_active'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class GalleryContentMixin(object):
    model = GalleryContent
    form_class = GalleryContentForm
    template_name = 'flexcontent/simplecontent_form.html'


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
