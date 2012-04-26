#import users.views
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('users.views',
	url(r'^login/$', 'login', {'template_name': 'users/login.html'}),
	url(r'^logout/$', 'logout', kwargs={'next_page':'/',}),
	url(r'^register/$', 'register', kwargs={'next_page':'/',}),
)