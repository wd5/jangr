# -*- coding: utf-8 -*-
from django.contrib.comments.urls import urlpatterns
from django.conf.urls.defaults import patterns, include, url

urlpatterns += patterns('mycomments.views',
	url(r'^post/$', 'post_comment'),
)