# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.db import models

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField

from multisitesutils.models import SiteModel
from magicgallery.models import GalleryItem

from .behaviours import Permalinkable
from .managers import WidgetManager, AreaManager, BaseContentManager


class Area(SiteModel):
    name = models.CharField(
        _('name'), max_length=64)
    widget = models.ForeignKey('Widget', verbose_name=_('widget'), null=True)
    is_visible = models.BooleanField('visible', default=True)
    is_always_visible = models.BooleanField('Always visible', default=False)

    objects = models.Manager()
    site_objects = AreaManager()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return "%s -> %s" % (self.site, self.name)


# TODO: technical debt - make this items dynamic
WIDGET_TYPES = (
    ('simplecontent', 'Simple Content'),
    ('iconcontent', 'Icon Content'),
    ('longcontent', 'Long Content'),
    ('background', 'Background'),
    ('pagelink', 'PageLink'),
    ('imagecontent', 'ImageContent'),
    ('newsfeedcontent', 'Newsfeed Content'),
    ('menuitem', 'MenuItem'),
    ('faq', 'Faq'),
    ('gallerycontent', 'Gallery Content'),
)

# TODO: technical debt - make this items dynamic
TEMPLATE_STYLES = (
    ('default', 'SimpleContent - List 1 (default)'),
    ('list2', 'SimpleContent - List 2'),
    ('list3', 'SimpleContent - List 3'),
    ('list4', 'SimpleContent - List 4'),
    ('slide_by_1', 'SimpleContent - Slide by 1'),
    ('slide_by_2', 'SimpleContent - Slide by 2'),
    ('slide_by_3', 'SimpleContent - Slide by 3'),
    ('slide_by_4', 'SimpleContent - Slide by 4'),
    ('imageleft', 'SimpleContent - Image Left'),
    ('imageright', 'SimpleContent - Image Right'),
    ('imagebottom', 'SimpleContent - Image Bottom'),
    ('default', 'LongContent - List 1 (default)'),
    ('list2', 'LongContent - List 2'),
    ('list3', 'LongContent - List 3'),
    ('default', 'Background - Style 1 (default)'),
    ('style2', 'Background - Style 2 - long'),
    ('style3', 'Background - Style 3 - small'),
    ('bg-slider1', 'Background - Slider 1'),
    ('style4', 'Background - Style 4 - half'),
    ('default', 'PageLink - Style 1 (default)'),
    ('button', 'PageLink - Button'),
    ('default', 'IconContent - Small Icons (default)'),
    ('bigicons', 'IconContent - Big Icons'),
    ('circledicons', 'IconContent - Circled Icons'),
    ('default', 'ImageContent - List'),
    ('caption1', 'ImageContent - Caption 1'),
    ('caption2', 'ImageContent - Caption 2'),
    ('caption3', 'ImageContent - Caption 3'),
    ('caption4', 'ImageContent - Caption 4'),
    ('caption5', 'ImageContent - Caption 5'),
    ('default', 'NewsfeedContent - List'),
    ('timeline', 'NewsfeedContent - Timeline'),
    ('default', 'Faq - general'),
    ('default', 'GalleryContent - general'),
    ('default', 'MenuItem - default'),
    ('hidemenu', 'MenuItem - hidemenu'),
)


class Widget(Permalinkable, SiteModel):

    """ Dynamic Widget """
    name = models.CharField(
        _('name'), max_length=64, db_index=True)
    widget_type = models.CharField(
        _('widget type'), max_length=32, default='simplecontent', choices=WIDGET_TYPES)
    style_template = models.CharField(
        _('Template Style'), max_length=128, default='default', choices=TEMPLATE_STYLES)
    description = models.CharField(
        _('description'), max_length=128, default='', blank=True)
    is_content_data = models.BooleanField('Content Data', default=True)

    objects = models.Manager()
    site_objects = WidgetManager()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.style_template)

    @property
    def content_list(self):
        """ List of all contents """
        data_type = self.get_widget_type
        return data_type.site_objects.filter(widget=self)

    @property
    def first_content(self, content_type):
        """ Show first content (order equals 0) """
        contents = content_type.site_objects.filter(widget=self)
        return contents[0]

    @property
    def get_widget_type(self):
        if self.widget_type == 'background':
            return BackgroundArea
        elif self.widget_type == 'iconcontent':
            return IconContent
        elif self.widget_type == 'longcontent':
            return LongContent
        elif self.widget_type == 'pagelink':
            return PageLink
        elif self.widget_type == 'imagecontent':
            return ImageContent
        elif self.widget_type == 'newsfeedcontent':
            ## TODO: not good parent app depend no child apps!!!
            NewsfeedContent = models.get_model('newsfeeds', 'NewsfeedContent')
            return NewsfeedContent
        elif self.widget_type == 'menuitem':
            MenuItem = models.get_model('navigation', 'MenuItem')
            return MenuItem
        elif self.widget_type == 'faq':
            Faq = models.get_model('faqs', 'Faq')
            return Faq
        elif self.widget_type == 'gallerycontent':
            return GalleryContent
        else:
            return SimpleContent

    def widget_types_list(self):
        #TODO: workaround!!!!!
        #      we do need to decide if we are moving the TEMPLATE_STYLES to the Database or not...
        result_list = [(id,label) for id,label in TEMPLATE_STYLES if self.widget_type in label.lower()]
        return result_list

LOREM_LIPSUM = """Lorem ipsum dolor sit amet, cu regione reformidans qui, 
                  pri argumentum constituam ad. Per sapientem constituam id. 
                  Veniam officiis constituto vis ex, debet persequeris cum te. 
                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, 
                  vero aliquip splendide eam te, fugit error paulo per no."""


class BaseContent(SiteModel):
    PICTURE_FILTERS = (
        ('', 'Original'),
        ('image-xpro2', 'XPro2'),
        ('image-willow', 'Willow'),
        ('image-inkwell', 'Inkwell'),
        ('image-walden', 'Walden'),
        ('image-toaster', 'Toaster'),
        ('image-sierra', 'Sierra'),
        ('image-nashville', 'Nashville'),
        ('image-mayfair', 'Mayfair'),
        ('image-kelvin', 'Kelvin'),
        ('image-hudson', 'Hudson'),
        ('image-brannan', 'Brannan'),
        ('image-1977', '1977'),
        ('image-blur', 'Blur'),
    )

    widget = models.ForeignKey('Widget', verbose_name=_('widget'))
    title = models.CharField(
        _('title'), max_length=128, default='Lorem ipsum dolor sit amet', blank=True)
    short_content = models.TextField(
        _('short content'), max_length=512, default='Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', blank=True)
    long_content = RichTextField(
        _('long content'), default=LOREM_LIPSUM, blank=True)
    picture = models.ForeignKey(GalleryItem, null=True, blank=True)
    picture_filter = models.CharField(
        _('Image Filter'), max_length=32, default='',
        choices=PICTURE_FILTERS, blank=True)
    order = models.PositiveIntegerField(_('order'), default=99)
    is_active = models.BooleanField(_('active'), default=True)
    link_url = models.CharField(
        _('link url'), max_length=255, default='', blank=True)
    link_label = models.CharField(
        _('link label'), max_length=64, default='', blank=True)

    objects = models.Manager()
    site_objects = BaseContentManager()

    class Meta:
        abstract = True
        ordering = ['order']

    def __unicode__(self):
        return "%s - %s" % (self.is_active, self.title)

    def _content(self):
        pass

    @property
    def content(self):
        return self._content()

    @property
    def model_name(self):
        return self._meta.model_name


class SimpleContent(BaseContent):

    """ title, subtitle, shorttext """
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    picture_cropping = ImageRatioField('picture__picture', '960x593')

    def _content(self):
        return self.short_content


class LongContent(BaseContent):

    """ title, longtext """
    picture_cropping = ImageRatioField('picture__picture', '960x480')

    def _content(self):
        return self.long_content


class IconContent(BaseContent):
    FONTAWESOME_ICONS = (
        ('fa-adjust', 'adjust'), ('fa-arrows', 'arrows'),
        ('fa-barcode', 'barcode'), ('fa-bars', 'bars'),
        ('fa-beer', 'beer'), ('fa-bell', 'bell'), ('fa-bolt', 'bolt'),
        ('fa-bomb', 'bomb'), ('fa-book', 'book'), ('fa-bookmark', 'bookmark'),
        ('fa-briefcase', 'briefcase'), ('fa-bug', 'bug'),
        ('fa-building', 'building'), ('fa-bullhorn', 'bullhorn'),
        ('fa-bullseye', 'bullseye'), ('fa-calendar', 'calendar'),
        ('fa-camera', 'camera'), ('fa-car', 'car'),
        ('fa-caret-square-o-down', 'caret-square-o-down'),
        ('fa-caret-square-o-left', 'caret-square-o-left'),
        ('fa-caret-square-o-right', 'caret-square-o-right'),
        ('fa-caret-square-o-up', 'caret-square-o-up'),
        ('fa-certificate', 'certificate'), ('fa-check', 'check'),
        ('fa-child', 'child'), ('fa-circle', 'circle'),
        ('fa-clock-o', 'clock-o'), ('fa-sort-desc', 'sort-desc'),
        ('fa-space-shuttle', 'space-shuttle'), ('fa-spinner', 'spinner'),
        ('fa-spoon', 'spoon'), ('fa-square', 'square'),
        ('fa-star', 'star'), ('fa-star-half', 'star-half'),
        ('fa-suitcase', 'suitcase'), ('fa-sun-o', 'sun-o'),
        ('fa-tablet', 'tablet'), ('fa-tachometer', 'tachometer'),
        ('fa-tag', 'tag'), ('fa-tags', 'tags'),
        ('fa-tasks', 'tasks'), ('fa-taxi', 'taxi'),
        ('fa-terminal', 'terminal'), ('fa-thumb-tack', 'thumb-tack'),
        ('fa-thumbs-down', 'thumbs-down'),
        ('fa-thumbs-o-down', 'thumbs-o-down'),
        ('fa-thumbs-o-up', 'thumbs-o-up'), ('fa-thumbs-up', 'thumbs-up'),
        ('fa-ticket', 'ticket'), ('fa-times', 'times'),
        ('fa-times-circle', 'times-circle'), ('fa-tint', 'tint'),
        ('fa-tree', 'tree'), ('fa-trophy', 'trophy'), ('fa-truck', 'truck'),
        ('fa-umbrella', 'umbrella'), ('fa-university', 'university'),
        ('fa-unlock', 'unlock'), ('fa-upload', 'upload'),
        ('fa-user', 'user'), ('fa-users', 'users'),
        ('fa-video-camera', 'video-camera'), ('fa-volume-down', 'volume-down'),
        ('fa-wheelchair', 'wheelchair'),
    )
    """ title, shorttext and icon """
    icon = models.CharField(_('icon'), max_length=64, default='fa-check',
                            choices=FONTAWESOME_ICONS)

    def _content(self):
        return self.short_content


class BackgroundArea(BaseContent):

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '1600x952')
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    link1_url = models.CharField(
        _('link1 url'), max_length=255, null=True, blank=True, default='#intro')
    link1_label = models.CharField(
        _('link1 label'), max_length=64, default='link1', blank=True)

    def _content(self):
        return self.short_content


class PageLink(BaseContent):

    """ title, subtitle, link1 and picture background """
    picture_cropping = ImageRatioField('picture__picture', '1600x989')
    sub_title = models.CharField(
        _('sub title'), max_length=128, default='', blank=True)
    link1_url = models.CharField(
        _('link1 url'), max_length=255, default='#intro', blank=True)
    link1_label = models.CharField(
        _('link1 label'), max_length=64, default='link1', blank=True)


class ImageContent(BaseContent):

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '960x960')

    def _content(self):
        return self.short_content


# It might be better change this to the gallery app and it shouldnt be a content...(disquis)
class GalleryContent(BaseContent):

    """ title, subtitle"""
    picture_cropping = ImageRatioField('picture__picture', '960x960')

    def _content(self):
        return self.short_content
