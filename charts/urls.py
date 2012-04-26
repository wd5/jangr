# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('charts.views',
	#url(r'^news/(?P<year>.+)/(?P<month>.+)/(?P<day>.+)/(?P<slug>.+)/$', 'view_news_item'),
	#url(r'^news/(?P<page>.+)/$', 'news_index'),
	url(r'^chart/$', 'chart_index'),
	#url(r'^news/(?P<date>.+)/(?P<article>.+)/$', 'news_index'),
)