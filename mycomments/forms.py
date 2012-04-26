# -*- coding: utf-8 -*-

import time
import datetime

from django import forms
from django.conf import settings
from django.contrib.comments.forms import CommentSecurityForm
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.utils.translation import ungettext, ugettext_lazy as _
from mycomments.models import NestedComment

COMMENT_MAX_LENGTH = getattr(settings,'COMMENT_MAX_LENGTH', 3000)

class NestedCommentForm(CommentSecurityForm):

	comment		= forms.CharField(label=_(u'Коментар'), widget=forms.Textarea(attrs={'rows':'','cols':'','class':'comment-textarea box-sized'}), max_length=COMMENT_MAX_LENGTH)
	honeypot	= forms.CharField(required=False,label=_(u'В това поле не въвеждай нищо'))

	def get_comment_object(self):
		if not self.is_valid():
			raise ValueError("get_comment_object may only be called on valid forms")

		CommentModel = self.get_comment_model()
		new = CommentModel(**self.get_comment_create_data())
		new = self.check_for_duplicate_comment(new)

		return new

	def get_comment_model(self):
		return NestedComment

	def get_comment_create_data(self):
		return dict(
			content_type = ContentType.objects.get_for_model(self.target_object),
			object_pk	= force_unicode(self.target_object._get_pk_val()),
			#user_name	= self.cleaned_data["name"],
			#user_email   = self.cleaned_data["email"],
			#user_url	 = self.cleaned_data["url"],
			comment	  = self.cleaned_data["comment"],
			submit_date  = datetime.datetime.now(),
			site_id	  = settings.SITE_ID,
			is_public	= True,
			is_removed   = False,
		)

	def check_for_duplicate_comment(self, new):
		possible_duplicates = self.get_comment_model()._default_manager.using(
			self.target_object._state.db
		).filter(
			content_type = new.content_type,
			object_pk = new.object_pk,
			user_name = new.user_name,
			user_email = new.user_email,
			user_url = new.user_url,
		)
		for old in possible_duplicates:
			if old.submit_date.date() == new.submit_date.date() and old.comment == new.comment:
				return old

		return new

	def clean_comment(self):
		comment = self.cleaned_data["comment"]
		if settings.COMMENTS_ALLOW_PROFANITIES == False:
			bad_words = [w for w in settings.PROFANITIES_LIST if w in comment.lower()]
			if bad_words:
				plural = len(bad_words) > 1
				raise forms.ValidationError(ungettext(
					"Watch your mouth! The word %s is not allowed here.",
					"Watch your mouth! The words %s are not allowed here.", plural) % \
					get_text_list(['"%s%s%s"' % (i[0], '-'*(len(i)-2), i[-1]) for i in bad_words], 'and'))
		return comment
	
	def clean_honeypot(self):
		"""Check that nothing's been entered into the honeypot."""
		value = self.cleaned_data["honeypot"]
		if value:
			raise forms.ValidationError(self.fields["honeypot"].label)
		return value