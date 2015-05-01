# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.sites.models import Site

from rest_framework.views import APIView
from rest_framework.response import Response
from fabric.colors import red

from accounts.mixins import AdministratorRequiredMixin
from gallery.models import Gallery, GalleryItem
from .models import (Area, Widget, SimpleContent, LongContent, IconContent,
                     PageLink, BackgroundArea, ImageContent, GalleryContent)
from .forms import (AreaForm, WidgetForm, NewWidgetForm, SimpleContentForm,
                    LongContentForm, PageLinkForm, IconContentForm,
                    BackgroundAreaForm, ImageContentForm, GalleryContentForm)
from .serializers import AreaVisibleSerializer, ContentFieldUpdateSerializer


# HELPERS

def can_edit_flatpages(request):
    """ Used by the djenie-flatpages to define who can add/update pages
        content
    """
    print(red(
        'flexcontent.can_edit is unsafe, use accounts.mixins.CanEdit instead'))
    return request.user.is_authenticated() and request.user.is_staff


def get_access_denied_redirect_url():
    # TODO: this function is invoked over this module, however is not defined
    #       check the right origin
    return '/'


# MIXINS

class EditableMixin(AdministratorRequiredMixin):

    success_url = reverse_lazy('flexcontent.windows_close')

    def get_context_data(self, *args, **kws):
        ''' provides the default_gallery to upload files '''
        gallery = Gallery.site_objects.default_gallery()
        context = super(EditableMixin, self).get_context_data(*args, **kws)
        context['default_gallery'] = gallery
        context['all_images'] = GalleryItem.site_objects.all().order_by(
            'gallery')
        return context

    def get_success_url(self):
        ''' if user clicked on "save and edit", send him to same url '''
        if self.request.POST.get('edit'):
            return self.request.path
        return self.success_url


class CreateContentMixin(object):

    def form_valid(self, form):
        widget = Widget.site_objects.get(pk=self.kwargs['widget_pk'])
        self.object = form.save(commit=False)
        self.object.widget = widget
        # TODO: remove it from here
        self.object.site = Site.objects.get_current()
        self.object.save()
        return redirect(self.get_success_url())


class ListContentMixin(object):
    template_name = 'flexcontent/widget_element_order.html'
    paginate_by = '100'
    context_object_name = 'content_list'

    def get_queryset(self):
        widget = Widget.site_objects.get(pk=self.kwargs.get('widget_pk'))
        return self.model.objects.filter(widget=widget)


class SimpleContentMixin(object):
    model = SimpleContent
    form_class = SimpleContentForm
    template_name = 'flexcontent/simplecontent_form.html'


class LongContentMixin(object):
    model = LongContent
    form_class = LongContentForm
    template_name = 'flexcontent/simplecontent_form.html'


class PageLinkMixin(object):
    model = PageLink
    form_class = PageLinkForm
    template_name = 'flexcontent/simplecontent_form.html'


class IconContentMixin(object):
    model = IconContent
    form_class = IconContentForm
    template_name = 'flexcontent/simplecontent_form.html'


class BackgroundAreaMixin(object):
    model = BackgroundArea
    form_class = BackgroundAreaForm
    template_name = 'flexcontent/simplecontent_form.html'


# VIEWS

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
