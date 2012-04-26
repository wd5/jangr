# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CatalogEntry'
        db.create_table('catalog_catalogentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('catalog', ['CatalogEntry'])

        # Adding model 'CatalogReview'
        db.create_table('catalog_catalogreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('for_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.CatalogEntry'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('helpful', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('unhelpful', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('catalog', ['CatalogReview'])

        # Adding model 'Classified'
        db.create_table('catalog_classified', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('catalog', ['Classified'])


    def backwards(self, orm):
        
        # Deleting model 'CatalogEntry'
        db.delete_table('catalog_catalogentry')

        # Deleting model 'CatalogReview'
        db.delete_table('catalog_catalogreview')

        # Deleting model 'Classified'
        db.delete_table('catalog_classified')


    models = {
        'catalog.catalogentry': {
            'Meta': {'object_name': 'CatalogEntry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'catalog.catalogreview': {
            'Meta': {'object_name': 'CatalogReview'},
            'for_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.CatalogEntry']"}),
            'helpful': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unhelpful': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'catalog.classified': {
            'Meta': {'object_name': 'Classified'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalog']
