from django.core.urlresolvers import reverse

from mycomments.models import NestedComment
from mycomments.forms import NestedCommentForm
from mycomments.views import post_comment

def get_model():
    return NestedComment

def get_form():
    return NestedCommentForm
	
def get_form_target():
	return reverse(post_comment)