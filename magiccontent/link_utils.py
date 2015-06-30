# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re


class BaseLink(object):
    model = None
    skip_instance_rule = None

    def get_queryset(self):
        '''
            If the "model" has a classmethod called "get_link_queryset" it will
            be used here instead the default one.
        '''
        model_cls_method = getattr(
            self.model, 'get_link_queryset', self.model.objects.all)
        return model_cls_method()

    def _skip_instance(self, instance):
        ''' Try to find a pattern on instance's name, if so, it will be skipped
            on links generator's method '''

        if self.skip_instance_rule is None:
            return False

        name = self.get_name(instance)
        rule = re.compile(self.skip_instance_rule)
        if re.search(rule, name):
            return True
        return False

    def get_url(self, instance):
        '''
            If the "model" has a method called "get_link_url" it will
            be used here instead the default one.
        '''
        model_method = getattr(
            instance, 'get_link_url', instance.get_absolute_url)
        return model_method()

    def get_name(self, instance):
        '''
            If the "model" has a method called "get_link_name" it will
            be used here instead the default one.
        '''
        model_method = getattr(
            instance, 'get_link_name', instance.__unicode__)
        return model_method()

    def generate(self):
        ''' must return a list of a dict like that:
            [
                {'url': 'some_url', 'name': 'some name'},
            ]

            If the "model" has a classmethod called "generate_link" it will
            be used here instead the default one.
        '''
        model_cls_method = getattr(self.model, 'generate_link', None)
        if model_cls_method:
            return model_cls_method()

        queryset = self.get_queryset()
        links_list = []

        for instance in queryset:
            if self._skip_instance(instance):
                continue

            data = {'url': self.get_url(instance),
                    'name': self.get_name(instance)
                    }
            links_list.append(data)

        return links_list


class AnchorLink(BaseLink):
    model = Area
    skip_instance_rule = r'_\d+'  # skip strange link's name

    def get_name(self, instance):
        return instance.widget.name

    def get_url(self, instance):
        return "#" + instance.name


class ContactusLink(BaseLink):

    def generate(self):
        link = reverse('contacts.topic.create')
        return [
            {'name': 'Contact Us', 'url': link}
        ]


class GalleryListLink(BaseLink):

    def generate(self):
        link = reverse('galleries.gallery.list')
        return [
            {'name': 'Galleries', 'url': link}
        ]


class GalleryLink(BaseLink):
    model = Gallery

    def get_name(self, instance):
        return 'Gallery: ' + instance.name


def links_builder(builder_list):
    links_list = []

    for BuilderClass in builder_list:
        builder_links_list = BuilderClass().generate()
        links_list.extend(builder_links_list)

    return links_list


SITE_LINKS = links_builder([
    AnchorLink,
    ContactusLink,
    GalleryListLink,
    GalleryLink,
])
