# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TopArticle'
        db.create_table('archive_toparticle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Article'])),
        ))
        db.send_create_signal('archive', ['TopArticle'])

        # Adding model 'Article'
        db.create_table('archive_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('archive', ['Article'])

        # Adding model 'Person'
        db.create_table('archive_person', (
            ('article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['archive.Article'], unique=True, primary_key=True)),
            ('alive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('born', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('died', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Person'])

        # Adding model 'Artist'
        db.create_table('archive_artist', (
            ('article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['archive.Article'], unique=True, primary_key=True)),
            ('years_active', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Artist'])

        # Adding model 'Membership'
        db.create_table('archive_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Person'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Artist'])),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('years', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('now', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('archive', ['Membership'])

        # Adding model 'Song'
        db.create_table('archive_song', (
            ('article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['archive.Article'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('archive', ['Song'])

        # Adding M2M table for field original_artists on 'Song'
        db.create_table('archive_song_original_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['archive.song'], null=False)),
            ('artist', models.ForeignKey(orm['archive.artist'], null=False))
        ))
        db.create_unique('archive_song_original_artists', ['song_id', 'artist_id'])

        # Adding model 'Album'
        db.create_table('archive_album', (
            ('article_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['archive.Article'], unique=True, primary_key=True)),
            ('released', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('archive', ['Album'])

        # Adding M2M table for field artists on 'Album'
        db.create_table('archive_album_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm['archive.album'], null=False)),
            ('artist', models.ForeignKey(orm['archive.artist'], null=False))
        ))
        db.create_unique('archive_album_artists', ['album_id', 'artist_id'])

        # Adding model 'AlbumTrack'
        db.create_table('archive_albumtrack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Song'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['archive.Album'])),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('archive', ['AlbumTrack'])


    def backwards(self, orm):
        
        # Deleting model 'TopArticle'
        db.delete_table('archive_toparticle')

        # Deleting model 'Article'
        db.delete_table('archive_article')

        # Deleting model 'Person'
        db.delete_table('archive_person')

        # Deleting model 'Artist'
        db.delete_table('archive_artist')

        # Deleting model 'Membership'
        db.delete_table('archive_membership')

        # Deleting model 'Song'
        db.delete_table('archive_song')

        # Removing M2M table for field original_artists on 'Song'
        db.delete_table('archive_song_original_artists')

        # Deleting model 'Album'
        db.delete_table('archive_album')

        # Removing M2M table for field artists on 'Album'
        db.delete_table('archive_album_artists')

        # Deleting model 'AlbumTrack'
        db.delete_table('archive_albumtrack')


    models = {
        'archive.album': {
            'Meta': {'object_name': 'Album', '_ormbases': ['archive.Article']},
            'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['archive.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Artist']", 'symmetrical': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'released': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Song']", 'symmetrical': 'False', 'through': "orm['archive.AlbumTrack']", 'blank': 'True'})
        },
        'archive.albumtrack': {
            'Meta': {'object_name': 'AlbumTrack'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Song']"})
        },
        'archive.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'archive.artist': {
            'Meta': {'object_name': 'Artist', '_ormbases': ['archive.Article']},
            'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['archive.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Person']", 'null': 'True', 'through': "orm['archive.Membership']", 'symmetrical': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Person', '_ormbases': ['archive.Article']},
            'alive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['archive.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'born': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'died': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'archive.song': {
            'Meta': {'object_name': 'Song', '_ormbases': ['archive.Article']},
            'article_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['archive.Article']", 'unique': 'True', 'primary_key': 'True'}),
            'original_artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['archive.Artist']", 'symmetrical': 'False'})
        },
        'archive.toparticle': {
            'Meta': {'object_name': 'TopArticle'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['archive.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['archive']
