from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('samodei.views',
	url(r'^$', 'homepage'),
	url(r'^image/(?P<path>.*)/(?P<width>\d*)/(?P<height>\d*)$', 'view_image'),
	url(r'^image/(?P<path>.*)/$', 'view_image'),
)