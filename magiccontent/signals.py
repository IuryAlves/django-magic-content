# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings

from .models import SiteLink
from .link_utils import link_builder


def get_model_link_config(instance):
    ''' avoid overhead, just allow models listed on settings.REGISTER_LINKS '''

    _meta = instance._meta
    app = _meta.app_label
    model_name = _meta.object_name
    links = getattr(settings, 'REGISTER_LINKS', None)
    if links is None:
        return False

    model_list = filter(lambda k: 'model' in k.keys(), links)
    model_list_name = map(lambda k: k['model'], model_list)

    model_name_str = '{0}.{1}'.format(app, model_name)
    if model_name_str in model_list_name:
        return filter(lambda k: model_name_str in k.values(), model_list)[0]

    return None


@receiver(post_save)
def content_post_save_handler(sender, **kwargs):

    instance = kwargs.get('instance')
    link_config = get_model_link_config(instance)

    if link_config:
        links_for_model = link_builder(link_config)

        for link_item in links_for_model:
            site_link, _ = SiteLink.site_objects.get_or_create(
                origin_model=link_config['model'],
                origin_model_pk=instance.pk,
                defaults=link_item)


@receiver(pre_delete)
def content_pre_delete_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    link_config = get_model_link_config(instance)

    if link_config:
        try:
            link = SiteLink.site_objects.get(origin_model=link_config['model'],
                                             origin_model_pk=instance.pk)
        except SiteLink.DoesNotExist:
            link = None

        if link:
            link.delete()
