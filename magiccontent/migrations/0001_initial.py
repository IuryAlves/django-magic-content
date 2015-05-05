# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'magiccontent_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'], null=True)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_always_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'magiccontent', ['Area'])

        # Adding model 'Widget'
        db.create_table(u'magiccontent_widget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(default=u'6yBZ68SvXBdz', max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, db_index=True)),
            ('widget_type', self.gf('django.db.models.fields.CharField')(default=u'simplecontent', max_length=32)),
            ('style_template', self.gf('django.db.models.fields.CharField')(default=u'default', max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('is_content_data', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'magiccontent', ['Widget'])

        # Adding model 'SimpleContent'
        db.create_table(u'magiccontent_simplecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['SimpleContent'])

        # Adding model 'LongContent'
        db.create_table(u'magiccontent_longcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['LongContent'])

        # Adding model 'IconContent'
        db.create_table(u'magiccontent_iconcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(default=u'fa-check', max_length=64)),
        ))
        db.send_create_signal(u'magiccontent', ['IconContent'])

        # Adding model 'BackgroundArea'
        db.create_table(u'magiccontent_backgroundarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('link1_url', self.gf('django.db.models.fields.CharField')(default=u'#intro', max_length=255, null=True, blank=True)),
            ('link1_label', self.gf('django.db.models.fields.CharField')(default=u'link1', max_length=64, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['BackgroundArea'])

        # Adding model 'PageLink'
        db.create_table(u'magiccontent_pagelink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('link1_url', self.gf('django.db.models.fields.CharField')(default=u'#intro', max_length=255, blank=True)),
            ('link1_label', self.gf('django.db.models.fields.CharField')(default=u'link1', max_length=64, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['PageLink'])

        # Adding model 'ImageContent'
        db.create_table(u'magiccontent_imagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['ImageContent'])

        # Adding model 'GalleryContent'
        db.create_table(u'magiccontent_gallerycontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Lorem ipsum dolor sit amet', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(default=u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \n                  pri argumentum constituam ad. Per sapientem constituam id. \n                  Veniam officiis constituto vis ex, debet persequeris cum te. \n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \n                  vero aliquip splendide eam te, fugit error paulo per no.', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('link_url', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'magiccontent', ['GalleryContent'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'magiccontent_area')

        # Deleting model 'Widget'
        db.delete_table(u'magiccontent_widget')

        # Deleting model 'SimpleContent'
        db.delete_table(u'magiccontent_simplecontent')

        # Deleting model 'LongContent'
        db.delete_table(u'magiccontent_longcontent')

        # Deleting model 'IconContent'
        db.delete_table(u'magiccontent_iconcontent')

        # Deleting model 'BackgroundArea'
        db.delete_table(u'magiccontent_backgroundarea')

        # Deleting model 'PageLink'
        db.delete_table(u'magiccontent_pagelink')

        # Deleting model 'ImageContent'
        db.delete_table(u'magiccontent_imagecontent')

        # Deleting model 'GalleryContent'
        db.delete_table(u'magiccontent_gallerycontent')


    models = {
        u'magiccontent.area': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_always_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']", 'null': 'True'})
        },
        u'magiccontent.backgroundarea': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'BackgroundArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link1_label': ('django.db.models.fields.CharField', [], {'default': "u'link1'", 'max_length': '64', 'blank': 'True'}),
            'link1_url': ('django.db.models.fields.CharField', [], {'default': "u'#intro'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sub_title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.gallerycontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'GalleryContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.iconcontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'IconContent'},
            'icon': ('django.db.models.fields.CharField', [], {'default': "u'fa-check'", 'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.imagecontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'ImageContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.longcontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'LongContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.pagelink': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'PageLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link1_label': ('django.db.models.fields.CharField', [], {'default': "u'link1'", 'max_length': '64', 'blank': 'True'}),
            'link1_url': ('django.db.models.fields.CharField', [], {'default': "u'#intro'", 'max_length': '255', 'blank': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sub_title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.simplecontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'SimpleContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u'Lorem ipsum dolor sit amet, cu regione reformidans qui, \\n                  pri argumentum constituam ad. Per sapientem constituam id. \\n                  Veniam officiis constituto vis ex, debet persequeris cum te. \\n                  Est autem fuisset quaerendum eu. His at lobortis gubergren posidonium, \\n                  vero aliquip splendide eam te, fugit error paulo per no.'", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'default': "u'Per sapientem constituam id. Veniam officiis constituto vis ex, debet persequeris cum te.'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'sub_title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Lorem ipsum dolor sit amet'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'TSpYj84A8Pnq'", 'max_length': '50'}),
            'style_template': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '128'}),
            'widget_type': ('django.db.models.fields.CharField', [], {'default': "u'simplecontent'", 'max_length': '32'})
        },
        u'magicgallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'magicgallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['magiccontent']