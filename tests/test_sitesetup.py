from django.test import TestCase

from ..models import Area, Widget


class SiteSetupTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def get_or_create_widget_area(self, area, widget_type, style):
        area, created = Area.site_objects.get_or_create(name=area)
        if created:
            widget = Widget.site_objects.create(widget_type=widget_type, style_template=style)
            area.widget = widget
            area.save()
        return area.widget

    def test_should_create_the_landingpage(self):

        widget1 = self.get_or_create_widget_area('top-menu', 'menuitem', 'default')
        widget1_list = Widget.site_objects.list_content_from_type(widget1)
        self.assertEqual(len(widget1_list), 3)

        widget2 = self.get_or_create_widget_area('main-background', 'background', 'default')
        widget2_list = Widget.site_objects.list_content_from_type(widget2)
        self.assertEqual(len(widget2_list), 3)

        widget3 = self.get_or_create_widget_area('intro', 'simplecontent', 'default')
        widget3_list = Widget.site_objects.list_content_from_type(widget3)
        self.assertEqual(len(widget3_list), 3)