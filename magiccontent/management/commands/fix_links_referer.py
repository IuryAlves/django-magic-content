# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.core.management.base import BaseCommand

from ...models import SiteLink


class Command(BaseCommand):

    def handle(self, **options):
        for link in SiteLink.objects.all():
            url = link.url
            if url.startswith('#'):
                referer = 'landingpage'
            elif url.startswith('/'):
                referer = 'internalpage'
            else:
                referer = 'externalpage'

            link.referer = referer
            link.save()
