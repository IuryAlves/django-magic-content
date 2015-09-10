# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
try:
    settings.configure()
except RuntimeError:
    pass

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import SiteLink


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
    link_cfg = get_model_link_config(instance)
    link_cfg = link_cfg and link_cfg.copy() or None

    if link_cfg:
        # avoid circular importing (import only when the right model is found)
        from .link_utils import link_builder

        model_str = link_cfg['model']
        links_for_model = link_builder(link_cfg)

        for link_item in links_for_model:
            url = link_item['url']
            if url.startswith('#'):
                referer = 'landingpage'
            elif url.startswith('/'):
                referer = 'internalpage'
            else:
                referer = 'externalpage'

            link_item['referer'] = referer

            site_link, _ = SiteLink.site_objects.get_or_create(
                origin_model=model_str,
                origin_model_pk=instance.pk,
                defaults=link_item)


@receiver(pre_delete)
def content_pre_delete_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    link_config = get_model_link_config(instance)

    if link_config:
        links = SiteLink.site_objects.filter(origin_model=link_config['model'],
                                             origin_model_pk=instance.pk)
        if links:
            links.delete()
