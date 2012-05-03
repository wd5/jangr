# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('archive.views',
	url(r'^$', 'index'),
	url(r'^artists/$', 'artist_list', {}, 'artist-list'),

	url(r'^songs/(?P<artist>.+)/(?P<song>.+)/$', 'song', {}, 'view-song'),
	url(r'^albums/(?P<artist>.+)/(?P<album>.+)/$', 'album', {}, 'view-album'),
	url(r'^artists/(?P<artist>.+)/$', 'artist', {}, 'view-artist'),
	url(r'^people/(?P<name>.+)/$', 'person', {}, 'view-person'),
)