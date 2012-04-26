from django.contrib.comments.models import BaseCommentAbstractModel, Comment

FIELD_INDEXES = {
    BaseCommentAbstractModel: {'indexed': ['object_pk'],},
    Comment: {'indexed': ['object_pk']},
}