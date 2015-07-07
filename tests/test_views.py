# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from accounts.tests.factories import UserFactory, DEFAULT_USER_PASSWORD
from accounts.models import SiteOwner
from magiccontent.models import Area
from magiccontent.factories import AreaFactory, WidgetFactory


# WARNING: DRY principle should not be used in tests, copy and paste is better

class AreaUpdateViewTest(TestCase):

    def setUp(self):
        self.user = UserFactory()
        site = Site.objects.get_current()
        SiteOwner.objects.create(user=self.user, site=site)
        self.instance = AreaFactory()
        self.url = reverse('magiccontent.area.update', args=[self.instance.pk])

        self.client.login(
            username=self.user.username, password=DEFAULT_USER_PASSWORD)

    @property
    def login_url(self):
        base_url = reverse('url_login_auth')
        return '{0}?next={1}'.format(base_url, self.url)

    def test_get_response(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magiccontent/area_form.html')

    def test_change_widget(self):
        new_widget = WidgetFactory()
        data = {'widget': new_widget.pk}
        response = self.client.post(self.url, data=data)
        success_url = reverse('magiccontent.windows_close')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, success_url)

        area = Area.site_objects.get(name=self.instance.name)
        self.assertEqual(area.widget.pk, new_widget.pk)

    def test_no_auth_get_response(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

    def test_no_auth_post_response(self):
        self.client.logout()
        new_widget = WidgetFactory()
        data = {'widget': new_widget.id}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

        area = Area.site_objects.get(name=self.instance.name)
        self.assertFalse(area.widget.pk == new_widget.pk)


class AreaVisibleUpdateViewTest(TestCase):
    pass


class StyleWidgetUpdateViewTest(TestCase):
    pass


class WidgetCreateViewTest(TestCase):
    pass


class SimpleContentCreateViewTest(TestCase):
    pass


class SimpleContentUpdateViewTest(TestCase):
    pass


class SimpleContentDeleteViewTest(TestCase):
    pass


class LongContentCreateViewTest(TestCase):
    pass


class LongContentUpdateViewTest(TestCase):
    pass


class LongContentOrderListViewTest(TestCase):
    pass


class PageLinkCreateViewTest(TestCase):
    pass


class PageLinkUpdateViewTest(TestCase):
    pass


class PageLinkDeleteViewTest(TestCase):
    pass


class IconContentCreateViewTest(TestCase):
    pass


class IconContentUpdateViewTest(TestCase):
    pass


class IconContentDeleteViewTest(TestCase):
    pass


class IconContentOrderListViewTest(TestCase):
    pass


class BackgroundAreaUpdateViewTest(TestCase):
    pass


class AreaUpdateVisibilityViewDetail(TestCase):
    pass
