# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FormattedTextImageContent'
        db.create_table(u'formattedtextimagecontent_formattedtextimagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('widget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.Widget'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Edit title', max_length=128, blank=True)),
            ('short_content', self.gf('django.db.models.fields.CharField')(default=u'Edit content', max_length=512, blank=True)),
            ('long_content', self.gf('ckeditor.fields.RichTextField')(default=u'', blank=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magicgallery.GalleryItem'], null=True, blank=True)),
            ('picture_filter', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=99)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('site_link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magiccontent.SiteLink'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('link_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('picture_cropping', self.gf(u'django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'formattedtextimagecontent', ['FormattedTextImageContent'])


    def backwards(self, orm):
        # Deleting model 'FormattedTextImageContent'
        db.delete_table(u'formattedtextimagecontent_formattedtextimagecontent')


    models = {
        u'formattedtextimagecontent.formattedtextimagecontent': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'FormattedTextImageContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'long_content': ('ckeditor.fields.RichTextField', [], {'default': "u''", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magicgallery.GalleryItem']", 'null': 'True', 'blank': 'True'}),
            'picture_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'picture_filter': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'short_content': ('django.db.models.fields.CharField', [], {'default': "u'Edit content'", 'max_length': '512', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'site_link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.SiteLink']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Edit title'", 'max_length': '128', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magiccontent.Widget']"})
        },
        u'magiccontent.sitelink': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'SiteLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'origin_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'origin_model_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'default': "u'landingpage'", 'max_length': '20', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magiccontent.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_content_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'qXo6LGgGN7Ft'", 'max_length': '50'}),
            'style_template': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '128'}),
            'widget_type': ('django.db.models.fields.CharField', [], {'default': "u'textimagecontent'", 'max_length': '32'})
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

    complete_apps = ['formattedtextimagecontent']