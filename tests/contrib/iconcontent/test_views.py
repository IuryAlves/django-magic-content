# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from magiccontent.contrib.iconcontent.models import IconContent

from ...helpers import AuthTestCase
from ...factories import WidgetFactory, IconContentFactory


class IconContentCreateViewTest(AuthTestCase):

    def setUp(self):
        super(IconContentCreateViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)

        self.url = reverse(
            'magiccontent.iconcontent.create', args=[self.widget.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'magiccontent/defaultcontent_form.html')

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

        self.assertFalse(IconContent.site_objects.all())

    def test_post_response_with_permission(self):
        self.login_user()
        data = {'title': 'nice title'}

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        qs = IconContent.site_objects.all()
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs[0].title, data['title'])

        self.assertRedirects(response, qs[0].update_url)

    def test_post_response_without_permission(self):
        data = {'title': 'nice title'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


class IconContentUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(IconContentUpdateViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)
        self.content = IconContentFactory(site=self.site, widget=self.widget)

        self.url = reverse(
            'magiccontent.iconcontent.update',
            args=[self.widget.pk, self.content.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'magiccontent/defaultcontent_form.html')

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

    def test_post_response_with_permission(self):
        self.login_user()
        old_title = self.content.title
        new_title = 'hey im a new title'
        self.assertFalse(old_title == new_title)

        response = self.client.post(
            self.url, {'title': new_title, 'icon': self.content.icon})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

        content = IconContent.objects.get(pk=self.content.pk)
        self.assertEqual(content.title, new_title)

    def test_post_response_without_permission(self):
        data = {'title': 'hey im a nice title'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


class IconContentDeleteViewTest(AuthTestCase):

    def setUp(self):
        super(IconContentDeleteViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)
        self.content = IconContentFactory(site=self.site, widget=self.widget)

        self.url = reverse(
            'magiccontent.iconcontent.delete',
            args=[self.widget.pk, self.content.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

        self.assertFalse(IconContent.objects.filter(pk=self.content.pk))
        # when the last content is deleted (above behaviour) it creates a
        # default one to replace it
        self.assertEqual(IconContent.objects.all().count(), 1)

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

        self.assertTrue(IconContent.objects.filter(pk=self.content.pk))


# TODO: missing tests for:
#        IconContentPicUpdateView
#        IconContentOrderListView
