# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('archive.views',
	url(r'^archive/$', 'index'),
	url(r'^artists/$', 'artist_list'),

	url(r'^songs/(?P<artist>.+)/(?P<song>.+)/$', 'view_song'),
	url(r'^albums/(?P<artist>.+)/(?P<album>.+)/$', 'view_album'),
	url(r'^artists/(?P<artist>.+)/$', 'view_artist'),	
)