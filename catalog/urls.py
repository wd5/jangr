# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('catalog.views',
	url(r'(?P<item_slug>.+)$', 'view_item'),
	url(r'$', 'index'),
)