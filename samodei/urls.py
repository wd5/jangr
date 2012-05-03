from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('samodei.views',
	url(r'^$', 'homepage'),
	#url(r'^image/(?P<path>.*)/(?P<width>\d*)/(?P<height>\d*)$', 'view_image'),
	#url(r'^image/(?P<path>.*)/$', 'view_image'),
	url(r'^file/(?P<filename>.*)$', 'download_handler', {}, 'serve-file'),
	url(r'^image/(?P<blobkey>.*)$', 'redirect_to_serving_url', {}, 'serve-image'),
)