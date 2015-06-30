# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.loading import get_model


class BaseLink(object):
    model = None
    skip_instance_rule = None

    def get_queryset(self):
        '''
            If the "model" has a classmethod called "get_link_queryset" it will
            be used here instead the default one.
        '''
        model_cls_method = getattr(self.model, 'get_link_queryset', None)
        if model_cls_method:
            return model_cls_method()
        return self.model.objects.all()

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
        model_method = getattr(instance, 'get_link_url', None)
        if model_method:
            return model_method()
        return instance.get_absolute_url()

    def get_name(self, instance):
        '''
            If the "model" has a method called "get_link_name" it will
            be used here instead the default one.
        '''
        model_method = getattr(instance, 'get_link_name', None)
        if model_method:
            return model_method()
        return instance.__unicode__()

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


def link_builder(link_config):
    full_link = link_config.get('full_reverse_link')
    if full_link:
        link_attr = {'name': full_link['name'],
                     'url': reverse(full_link['url'])}
        return [link_attr]

    app_label, model_name = link_config['model'].split('.')

    class ModelLink(BaseLink):
        model = get_model(app_label, model_name)
        skip_instance_rule = link_config.get('skip_instance_rule', None)

    return ModelLink().generate()


def generate_links():
    registered_models = getattr(
        settings, 'REGISTER_LINKS', None)
    if not registered_models:
        return []

    links_list = []
    for link_config in registered_models:
        links_list.extend(link_builder(link_config))

    return links_list


SITE_LINKS = generate_links()
