# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import os
import urllib
from hashlib import sha1

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings

from magicgallery.models import item_upload_to, Gallery, GalleryItem

from rest_framework.views import APIView
from rest_framework.response import Response
import floppyforms.__future__ as forms

from .mixins import EditableMixin
from .models import Area, Widget
from .widgets import CustomCropImageWidget, RadioImageFilterSelect
from .forms import PictureForm, AreaForm, WidgetForm, NewWidgetForm
from .serializers import AreaVisibleSerializer, ContentFieldUpdateSerializer


# helpers (this code can't live in helpers by recursive importing)
def download_picture(external_url):

    default_gallery = Gallery.site_objects.default_gallery()

    class FakeGalleryItem(object):
        gallery = default_gallery

    filename = '{0}.{1}'.format(sha1(external_url).hexdigest()[:8],
                                external_url.split('.')[-1][:4])
    relative_path = item_upload_to(FakeGalleryItem, filename)
    abs_path = os.path.join(settings.MEDIA_ROOT, relative_path)

    urllib.urlretrieve(external_url, abs_path)

    picture = GalleryItem.objects.create(
        gallery=default_gallery, picture=relative_path)

    return picture


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
    show_picture_fields = True

    def get_form_class(self):
        _model = self.model

        class PictureContentForm(PictureForm):

            external_url = forms.URLField(
                widget=forms.HiddenInput, required=False)

            class Meta:
                model = _model
                fields = ('picture', 'picture_cropping', 'picture_filter')
                widgets = {
                    'picture': CustomCropImageWidget(_model, 'picture'),
                    'picture_filter': RadioImageFilterSelect,
                }

            def clean(form_self):
                data = form_self.cleaned_data

                external_url = data.get('external_url')
                self.picture = None

                if external_url:
                    try:
                        self.picture = download_picture(external_url)
                    except:
                        raise forms.ValidationError(
                            "the image source from web is not avaiable.")

                return data

        return PictureContentForm

    def form_valid(self, form, *args, **kws):
        instance = form.save(commit=False)
        instance.picture = self.picture
        instance.save()

        return redirect(self.get_success_url())


# Base views

class AreaUpdateView(EditableMixin, UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'magiccontent/area_form.html'


# TODO: This is a ListView, should have a better name
class AreaVisibleUpdateView(ListView):
    model = Area
    template_name = 'magiccontent/area_visible_form.html'
    paginate_by = '100'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Area.site_objects.filter(
            is_landingpage_area=True)


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
