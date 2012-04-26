from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F

from forum.models import ForumSection

def index(request):
	sections = ForumSection.objects.filter(parent=None)
	return render_to_response(
		'forum/index.html',
		{
			'sections':sections,
		},
		context_instance=RequestContext(request)
	)
	
def section_index(request,section_id):
	
	pass
	