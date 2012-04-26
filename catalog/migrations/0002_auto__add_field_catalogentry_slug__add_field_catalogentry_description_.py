# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CatalogEntry.slug'
        db.add_column('catalog_catalogentry', 'slug', self.gf('autoslug.fields.AutoSlugField')(default='', unique_with=(), max_length=50, populate_from=None, db_index=True), keep_default=False)

        # Adding field 'CatalogEntry.description'
        db.add_column('catalog_catalogentry', 'description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'CatalogEntry.contact_data'
        db.add_column('catalog_catalogentry', 'contact_data', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CatalogEntry.slug'
        db.delete_column('catalog_catalogentry', 'slug')

        # Deleting field 'CatalogEntry.description'
        db.delete_column('catalog_catalogentry', 'description')

        # Deleting field 'CatalogEntry.contact_data'
        db.delete_column('catalog_catalogentry', 'contact_data')


    models = {
        'catalog.catalogentry': {
            'Meta': {'object_name': 'CatalogEntry'},
            'contact_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
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
