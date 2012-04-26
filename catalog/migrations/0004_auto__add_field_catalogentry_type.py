# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CatalogEntry.type'
        db.add_column('catalog_catalogentry', 'type', self.gf('django.db.models.fields.CharField')(default='nil', max_length=3), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CatalogEntry.type'
        db.delete_column('catalog_catalogentry', 'type')


    models = {
        'catalog.catalogentry': {
            'Meta': {'object_name': 'CatalogEntry'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samodei.City']", 'null': 'True', 'blank': 'True'}),
            'contact_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'nil'", 'max_length': '3'})
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
        },
        'samodei.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'})
        }
    }

    complete_apps = ['catalog']
