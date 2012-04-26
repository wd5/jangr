from django.db import models
from django.contrib.comments.models import Comment

class NestedComment(Comment):
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)