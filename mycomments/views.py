from django import http
from django.conf import settings
from django.contrib.comments.views.utils import next_redirect, confirmation_view
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import escape
from django.views.decorators.http import require_POST
from django.contrib import comments
from django.contrib.comments import signals
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):

	# Fill out some initial data fields from an authenticated user, if present
	data = request.POST.copy()
	if request.user.is_authenticated():
		data["name"] = request.user.get_full_name() or request.user.username
		data["email"] = request.user.email
	else:
		return CommentPostBadRequest("Tried to comment while not logged in.")

	# Check to see if the POST data overrides the view's next argument.
	next = data.get("next", next)

	# Look up the object we're trying to comment about
	ctype = data.get("content_type")
	object_pk = data.get("object_pk")
	if ctype is None or object_pk is None:
		return CommentPostBadRequest("Missing content_type or object_pk field.")
	try:
		model = models.get_model(*ctype.split(".", 1))
		target = model._default_manager.using(using).get(pk=object_pk)
	except TypeError:
		return CommentPostBadRequest(
			"Invalid content_type value: %r" % escape(ctype))
	except AttributeError:
		return CommentPostBadRequest(
			"The given content-type %r does not resolve to a valid model." % \
				escape(ctype))
	except ObjectDoesNotExist:
		return CommentPostBadRequest(
			"No object matching content-type %r and object PK %r exists." % \
				(escape(ctype), escape(object_pk)))
	except (ValueError, ValidationError), e:
		return CommentPostBadRequest(
			"Attempting go get content-type %r and object PK %r exists raised %s" % \
				(escape(ctype), escape(object_pk), e.__class__.__name__))

	# Construct the comment form
	form = comments.get_form()(target, data=data)

	# Check security information
	if form.security_errors():
		return CommentPostBadRequest(
			"The comment form failed security verification: %s" % \
				escape(str(form.security_errors())))

	# Create the comment
	comment = form.get_comment_object()
	comment.ip_address = request.META.get("REMOTE_ADDR", None)
	if request.user.is_authenticated():
		comment.user = request.user

	# Signal that the comment is about to be saved
	responses = signals.comment_will_be_posted.send(
		sender  = comment.__class__,
		comment = comment,
		request = request
	)

	for (receiver, response) in responses:
		if response == False:
			return CommentPostBadRequest(
				"comment_will_be_posted receiver %r killed the comment" % receiver.__name__)

	# Save the comment and signal that it was saved
	comment.save()
	signals.comment_was_posted.send(
		sender  = comment.__class__,
		comment = comment,
		request = request
	)

	return next_redirect(data, next, comment_done, c=comment._get_pk_val())

comment_done = confirmation_view(
	template = "comments/posted.html",
	doc = """Display a "comment was posted" success page."""
)