# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse

from rest_framework.views import APIView
from rest_framework.response import Response

from .mixins import EditableMixin
from .models import Area, Widget
from .forms import ContentFormBuilder, AreaForm, WidgetForm, NewWidgetForm
from .serializers import AreaVisibleSerializer, ContentFieldUpdateSerializer


class MagicDeleteView(DeleteView):

    def get(self, request, *args, **kws):
        # allows delete through GET requests
        return self.delete(request, *args, **kws)

    def delete(self, request, *args, **kws):
        instance = self.get_object()
        widget = instance.widget
        model_qs = self.model.site_objects.filter(
            widget=widget, is_active=True)
        is_the_last = model_qs.count() == 1

        # creates a blank content if that one is the last
        if is_the_last:
            self.model.site_objects.create(
                title='add a content here', widget=widget)

        return super(MagicDeleteView, self).delete(request, *args, **kws)


class PictureUpdateView(UpdateView):
    ''' An UpdateView with only picture's field '''

    def get_form_class(self):
        fields = ['picture', 'picture_cropping', 'picture_filter']
        return ContentFormBuilder(self.form_class, fields).build()


# Base views

class AreaUpdateView(EditableMixin, UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'magiccontent/area_form.html'


class AreaVisibleUpdateView(ListView):
    model = Area
    template_name = 'magiccontent/area_visible_form.html'
    paginate_by = '100'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Area.site_objects.actives()


class StyleWidgetUpdateView(EditableMixin, UpdateView):
    model = Widget
    form_class = WidgetForm
    template_name = 'magiccontent/stylewidget_form.html'


class WidgetCreateView(EditableMixin, CreateView):
    model = Widget
    form_class = NewWidgetForm
    template_name = 'magiccontent/newwidget_form.html'

    def form_valid(self, form):
        area_pk = self.kwargs['area_pk']
        self.object = form.save(commit=False)
        Widget.site_objects.create(
            widget_type=self.object.widget_type,
            style_template=self.object.style_template,
            name=self.object.name)
        area_url = reverse("magiccontent.area.update",
                           kwargs={'pk': area_pk})
        return redirect(area_url)


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
