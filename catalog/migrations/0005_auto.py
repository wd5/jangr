# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field related_artists on 'CatalogEntry'
        db.create_table('catalog_catalogentry_related_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('catalogentry', models.ForeignKey(orm['catalog.catalogentry'], null=False)),
            ('artist', models.ForeignKey(orm['archive.artist'], null=False))
        ))
        db.create_unique('catalog_catalogentry_related_artists', ['catalogentry_id', 'artist_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field related_artists on 'CatalogEntry'
        db.delete_table('catalog_catalogentry_related_artists')


    models = {
        'archive.artist': {
            'Meta': {'object_name': 'Artist'},
            'city': ('django.db.models.fields.CharField', [], {'default': "'\\xd0\\xa1\\xd0\\xbe\\xd1\\x84\\xd0\\xb8\\xd1\\x8f'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Person']", 'null': 'True', 'through': "orm['archive.Membership']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'years_active': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'})
        },
        'archive.membership': {
            'Meta': {'object_name': 'Membership'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'now': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Person']"}),
            'years': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'archive.person': {
            'Meta': {'object_name': 'Person'},
            'alive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'born': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'died': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'})
        },
        'catalog.catalogentry': {
            'Meta': {'object_name': 'CatalogEntry'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['samodei.City']", 'null': 'True', 'blank': 'True'}),
            'contact_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related_artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Artist']", 'symmetrical': 'False'}),
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
