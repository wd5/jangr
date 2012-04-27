from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from google.appengine.api import images

# Django's built-in ImageField doesn't work on AppEngine because
# it relies on unavailable PIL APIs. Here's my own version that works.

def image_bytes_are_valid(image_bytes):
	try:
		test_image = images.Image(image_bytes)
		# Unfortunately the only way to validate image bytes on AppEngine is to
		# perform a transform. Lame.
		ignored_output = test_image.execute_transforms(images.PNG)
	except images.Error:
		return False
	return True


class AppEngineImageFormField(forms.FileField):
	default_error_messages = {
		'invalid_image': _(u"Upload a valid image. The file you uploaded was either not an image or was a corrupted image."),
	}
	
	def clean(self, data, initial=None):
		raw_file = super(AppEngineImageField, self).clean(data, initial)
		if raw_file is None:
			return None
		elif not data and initial:
			return initial
			
		if hasattr(data, 'read'):
			bytes = data.read()
		else:
			try:
				bytes = data['content']
			except:
				bytes = None
		
		if bytes is None:
			raise forms.ValidationError(self.error_messages['invalid_image'])
		
		if (len(bytes) > 0) and (not image_bytes_are_valid(bytes)):
			raise forms.ValidationError(self.error_messages['invalid_image'])
		
		if hasattr(raw_file, 'seek') and callable(raw_file.seek):
			raw_file.seek(0)
			
		return raw_file
		

class ImageField(models.FileField):

	def formfield(self, **kwargs):
		defaults = {'form_class': AppEngineImageFormField}
		defaults.update(kwargs)
		return super(HandField, self).formfield(**defaults)