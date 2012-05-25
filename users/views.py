from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import django.contrib.auth.views

from users.forms import LoginForm, RegistrationForm

def login(request, *args, **kwargs):
	if request.method == 'POST':
		if not request.POST.get('remember_me', None):
			request.session.set_expiry(0)
		return django.contrib.auth.views.login(request, *args, **kwargs)
		
	else:
		form_login = LoginForm()
		form_register = RegistrationForm()
			
		return render_to_response(
			'users/login.html',
			{
				'login_form':form_login,
				'register_form':form_register,
			},
			context_instance=RequestContext(request)
		)

		
def logout(request, *args, **kwargs):
	django.contrib.auth.views.logout(request)
	return HttpResponseRedirect(reverse('home.views.homepage'))
	
	
def register(request, *args, **kwargs):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
		else:
			return HttpResponseRedirect('/login/')

	else:
		return login(request, *args, **kwargs)