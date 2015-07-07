from django.test import TestCase
from django.core.urlresolvers import resolve


class MagicContent_urls_generationTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_resolve_home_page(self):
        found = resolve('/')
        self.assertNotEqual(found.func, None)

    def test_should_resolve_magiccontent_simplecontent_urls(self):
        found = resolve('/magiccontent/magiccontent/simplecontent/1/create/')
        self.assertEqual(found.func.func_name, 'SimpleContentCreateView')

        found = resolve('/magiccontent/magiccontent/simplecontent/1/update/1/')
        self.assertEqual(found.func.func_name, 'SimpleContentUpdateView')

        found = resolve('/magiccontent/magiccontent/simplecontent/1/delete/1/')
        self.assertEqual(found.func.func_name, 'SimpleContentDeleteView')

        found = resolve('/magiccontent/magiccontent/simplecontent/1/order/')
        self.assertEqual(found.func.func_name, 'SimpleContentOrderListView')

    def test_should_resolve_magiccontent_imagecontent_urls(self):
        found = resolve('/magiccontent/magiccontent/imagecontent/1/create/')
        self.assertEqual(found.func.func_name, 'ImageContentCreateView')

        found = resolve('/magiccontent/magiccontent/imagecontent/1/update/1/')
        self.assertEqual(found.func.func_name, 'ImageContentUpdateView')

        found = resolve('/magiccontent/magiccontent/imagecontent/1/delete/1/')
        self.assertEqual(found.func.func_name, 'ImageContentDeleteView')

        found = resolve('/magiccontent/magiccontent/imagecontent/1/order/')
        self.assertEqual(found.func.func_name, 'ImageContentOrderListView')
