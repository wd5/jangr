# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('forum.views',
	url(r'(?P<section_id>.+)$', 'section_index'),
	url(r'$', 'index'),
)