#import users.views
from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('users.views',
	url(r'^login/$', 'login', {'template_name': 'users/login.html'}),
	url(r'^logout/$', 'logout', kwargs={'next_page':'/',}),
	url(r'^register/$', 'register', kwargs={'next_page':'/',}),
	url(r'^me/$', TemplateView.as_view(template_name='users/profile.html')),
)