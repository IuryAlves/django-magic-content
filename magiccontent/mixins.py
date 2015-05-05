# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib

from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse_lazy
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from braces.views._access import AccessMixin

from magicgallery.models import Gallery, GalleryItem

from .models import (Widget, SimpleContent, LongContent, IconContent,
                     PageLink, BackgroundArea)
from .forms import (SimpleContentForm, LongContentForm, PageLinkForm,
                    IconContentForm, BackgroundAreaForm)


class CanEditMixin(object):

    '''
        This mixin exposes a variable "can_edit" to template in order to
        display the admin controls.
        WARNING: This mixin doesn't protect the view against non-admins,
        you should use AdministratorRequiredMixin if you want a full protection
    '''

    def get_context_data(self, *args, **kws):
        context = super(CanEditMixin, self).get_context_data(*args, **kws)
        context['can_edit'] = get_is_content_owner(self.request)
        return context


class OwnerRequiredMixin(AccessMixin):

    ''' only site's administrators can access the view that uses this mixin '''

    def dispatch(self, request, *args, **kwargs):
        login_redirect = redirect_to_login(request.get_full_path(),
                                           self.get_login_url(),
                                           self.get_redirect_field_name())

        if not get_is_content_owner(request):
            return login_redirect

        return super(OwnerRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class EditableMixin(OwnerRequiredMixin):

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


def _load_permission_module(settings_name):
    permission_settings = getattr(settings, settings_name, None)

    if not permission_settings:
        raise ImproperlyConfigured(
            'The settings.{0} param is not defined.'.format(settings_name))
    module_name, method_name = permission_settings.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, method_name)


def get_is_content_owner(request):
    is_admin = _load_permission_module(
        'CONTENT_PAGE_IS_OWNER_METHOD')(request)

    return is_admin
