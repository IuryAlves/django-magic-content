# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from magiccontent.models import Widget
from .factories import AreaFactory, WidgetFactory
from .helpers import AuthTestCase


class AreaUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(AreaUpdateViewTest, self).setUp()

        self.area = AreaFactory(site=self.site)
        self.url = reverse('magiccontent.area.update', args=[self.area.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magiccontent/area_form.html')

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

    def test_post_response_with_permission(self):
        self.login_user()
        response = self.client.post(
            self.url, data={'widget': self.area.widget.pk})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

    def test_post_response_without_permission(self):
        response = self.client.post(
            self.url, data={'widget': self.area.widget.pk})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


class AreaVisibleUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(AreaVisibleUpdateViewTest, self).setUp()

        self.areas = []
        for i in range(3):
            self.areas.append(AreaFactory(site=self.site))

        self.url = reverse('magiccontent.area.visible.update')
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'magiccontent/area_visible_form.html')
        context = response.context

        self.assertTrue(context['object_list'])
        for item in context['object_list']:
            self.assertTrue(item in self.areas)

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'magiccontent/area_visible_form.html')
        context = response.context

        self.assertTrue(context['object_list'])
        for item in context['object_list']:
            self.assertTrue(item in self.areas)


class StyleWidgetUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(StyleWidgetUpdateViewTest, self).setUp()

        self.widget = WidgetFactory(site=self.site, description='bla')
        self.url = reverse('magiccontent.widget.update', args=[self.widget.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magiccontent/stylewidget_form.html')

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

    def test_post_response_with_permission(self):
        self.login_user()
        old_description = self.widget.description
        new_description = 'nice description'
        self.assertFalse(old_description == new_description)

        response = self.client.post(
            self.url, data={'description': new_description,
                            'style_template': self.widget.style_template})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

        widget = Widget.objects.get(pk=self.widget.pk)
        self.assertEqual(widget.description, new_description)

    def test_post_response_without_permission(self):
        response = self.client.post(
            self.url, data={'description': 'new bla'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


# TODO: Test API views:
#       AreaUpdateVisibilityViewDetail
#       ContentOrderUpdate
#       ContentIsActiveUpdate
