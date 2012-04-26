# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import admin_views

urlpatterns = patterns('newsevents.views',
	url(r'admin/newsevents/article/add_from_feed_post', admin_views.create_article_from_feed_post),
	url(r'admin/newsevents/event/add_from_feed_post', admin_views.create_event_from_feed_post),
	
	url(r'^news/(?P<year>.+)/(?P<month>.+)/(?P<day>.+)/(?P<slug>.+)/$', 'view_news_item'),
	url(r'^news/(?P<page>.+)/$', 'news_index'),
	url(r'^news/$', 'news_index'),
	#url(r'^news/(?P<date>.+)/(?P<article>.+)/$', 'news_index'),
	
	url(r'^events/(?P<date>.+)/(?P<slug>.+)/$', 'view_event'),
	url(r'^events/$', 'events_index'),
)