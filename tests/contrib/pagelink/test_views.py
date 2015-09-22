# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from magiccontent.contrib.pagelink.models import PageLink

from ...helpers import AuthTestCase
from ...factories import WidgetFactory, PageLinkFactory


class PageLinkCreateViewTest(AuthTestCase):

    def setUp(self):
        super(PageLinkCreateViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)

        self.url = reverse(
            'magiccontent.pagelink.create', args=[self.widget.pk])
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

        self.assertFalse(PageLink.site_objects.all())

    def test_post_response_with_permission(self):
        self.login_user()
        data = {'title': 'nice title'}

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        qs = PageLink.site_objects.all()
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs[0].title, data['title'])

        self.assertRedirects(response, qs[0].update_url)

    def test_post_response_without_permission(self):
        data = {'title': 'nice title'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


class PageLinkUpdateViewTest(AuthTestCase):

    def setUp(self):
        super(PageLinkUpdateViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)
        self.content = PageLinkFactory(site=self.site, widget=self.widget)

        self.url = reverse(
            'magiccontent.pagelink.update',
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

        response = self.client.post(self.url, {'title': new_title})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

        content = PageLink.objects.get(pk=self.content.pk)
        self.assertEqual(content.title, new_title)

    def test_post_response_without_permission(self):
        data = {'title': 'hey im a nice title'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)


class PageLinkDeleteViewTest(AuthTestCase):

    def setUp(self):
        super(PageLinkDeleteViewTest, self).setUp()
        self.widget = WidgetFactory(site=self.site)
        self.content = PageLinkFactory(site=self.site, widget=self.widget)

        self.url = reverse(
            'magiccontent.pagelink.delete',
            args=[self.widget.pk, self.content.pk])
        self.no_perm_url = '/accounts/login/?next={0}'.format(self.url)

    def test_get_response_with_permission(self):
        self.login_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('magiccontent.windows_close'))

        self.assertFalse(PageLink.objects.filter(pk=self.content.pk))
        # when the last content is deleted (above behaviour) it creates a
        # default one to replace it
        self.assertEqual(PageLink.objects.all().count(), 1)

    def test_get_response_without_permission(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.no_perm_url)

        self.assertTrue(PageLink.objects.filter(pk=self.content.pk))


# TODO: missing tests for:
#        PageLinkPicUpdateView
#        PageLinkOrderListView
