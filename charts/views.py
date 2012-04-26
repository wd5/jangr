# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext

from datetime import datetime
import re


def chart_index(request,page=1):
	
	return render_to_response(
		'charts/chart-index.html',
		{
			'nav_category':'chart',
		},
		context_instance=RequestContext(request)
	)