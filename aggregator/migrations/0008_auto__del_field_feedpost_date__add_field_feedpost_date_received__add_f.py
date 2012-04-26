# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FeedPost.date'
        db.delete_column('aggregator_feedpost', 'date')

        # Adding field 'FeedPost.date_received'
        db.add_column('aggregator_feedpost', 'date_received', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'FeedPost.date_published'
        db.add_column('aggregator_feedpost', 'date_published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'FeedPost.date'
        db.add_column('aggregator_feedpost', 'date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Deleting field 'FeedPost.date_received'
        db.delete_column('aggregator_feedpost', 'date_received')

        # Deleting field 'FeedPost.date_published'
        db.delete_column('aggregator_feedpost', 'date_published')


    models = {
        'aggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'feed_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_parsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'moderate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'aggregator.feedpost': {
            'Meta': {'object_name': 'FeedPost'},
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'from_feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Feed']"}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'relevance': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['aggregator']
