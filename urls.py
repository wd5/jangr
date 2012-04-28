# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'D:/Web/Projects/jangr/jangr/_media/'}),
	url(r'^comments/', include('mycomments.urls')),
	url(r'^', include('samodei.urls')),
	url(r'^', include('archive.urls')),
	url(r'^catalog/', include('catalog.urls')),
	url(r'^', include('newsevents.urls')),
	url(r'^', include('users.urls')),
	url(r'^', include('charts.urls')),
	url(r'^red/', include('editor.urls')),
	url(r'^forum/', include('forum.urls')),
	url(r'^upload-test/', include('upload.urls')),

	
	url(r'^admin/', include(admin.site.urls)),
	
    #('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
)


handler500 = 'djangotoolbox.errorviews.server_error'